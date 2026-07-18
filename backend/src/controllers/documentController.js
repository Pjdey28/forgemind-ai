import Document from "../models/Document.model.js";
import asyncHandler from "../utils/AsyncHandler.js";
import { ApiError } from "../utils/ApiError.js";
import { ApiResponse } from "../utils/Apiresponse.js";
import axios from "axios";

export const uploadDocument = asyncHandler(async (req, res) => {
  if (!req.file) {
    throw new ApiError(400, "Please upload a file");
  }

  // Create a pending document in MongoDB
  const sizeMB = `${(req.file.size / (1024 * 1024)).toFixed(1)} MB`;
  const format = req.file.originalname.split(".").pop().toUpperCase();

  const tempDocId = `temp_${Date.now()}`;
  const document = await Document.create({
    doc_id: tempDocId,
    name: req.file.originalname,
    size: sizeMB,
    format: format,
    status: "INDEXING",
    owner: req.user._id,
  });

  try {
    // Construct Form-Data to forward file to FastAPI AI service
    const formData = new FormData();
    const fileBlob = new Blob([req.file.buffer], { type: req.file.mimetype });
    formData.append("file", fileBlob, req.file.originalname);

    const aiResponse = await axios.post(
      `${process.env.AI_SERVICE_URL}/upload`,
      formData
    );

    if (aiResponse.data && aiResponse.data.status === "success") {
      document.doc_id = aiResponse.data.doc_id;
      document.status = "OCR_DONE";
      document.chunksCount = aiResponse.data.chunks_count || 0;
      await document.save();
    } else {
      document.status = "FAILED";
      await document.save();
    }
  } catch (error) {
    console.error("AI service upload error:", error.message);
    document.status = "FAILED";
    await document.save();
  }

  return res
    .status(201)
    .json(new ApiResponse(201, document, "Document uploaded and indexed successfully"));
});

export const getDocuments = asyncHandler(async (req, res) => {
  const documents = await Document.find({ owner: req.user._id }).sort({
    createdAt: -1,
  });

  return res
    .status(200)
    .json(new ApiResponse(200, documents, "Documents retrieved successfully"));
});

export const deleteDocument = asyncHandler(async (req, res) => {
  const { id } = req.params;

  const document = await Document.findById(id);
  if (!document) {
    throw new ApiError(404, "Document not found");
  }

  // Ensure owner is the one deleting
  if (document.owner.toString() !== req.user._id.toString()) {
    throw new ApiError(403, "Unauthorized to delete this document");
  }

  try {
    // Notify FastAPI to delete vectors and graph nodes/edges
    if (!document.doc_id.startsWith("temp_")) {
      await axios.delete(
        `${process.env.AI_SERVICE_URL}/upload/${document.doc_id}`
      );
    }
  } catch (error) {
    console.error("AI service document deletion error:", error.message);
  }

  await Document.findByIdAndDelete(id);

  return res
    .status(200)
    .json(new ApiResponse(200, null, "Document deleted successfully"));
});
