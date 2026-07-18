import mongoose from "mongoose";

const documentSchema = new mongoose.Schema(
  {
    doc_id: {
      type: String,
      required: true,
      unique: true,
      trim: true,
    },
    name: {
      type: String,
      required: true,
      trim: true,
    },
    size: {
      type: String,
      required: true,
    },
    format: {
      type: String,
      required: true,
      uppercase: true,
    },
    status: {
      type: String,
      enum: ["PENDING", "INDEXING", "OCR_DONE", "FAILED"],
      default: "PENDING",
    },
    chunksCount: {
      type: Number,
      default: 0,
    },
    owner: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
  },
  {
    timestamps: true,
  }
);

const Document = mongoose.model("Document", documentSchema);

export default Document;
