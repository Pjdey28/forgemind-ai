import asyncHandler from "../utils/AsyncHandler.js";
import { ApiResponse } from "../utils/Apiresponse.js";
import { ApiError } from "../utils/ApiError.js";
import axios from "axios";

export const askQuestion = asyncHandler(async (req, res) => {
  const { question } = req.body;

  if (!question) {
    throw new ApiError(400, "Question is required");
  }

  try {
    const aiResponse = await axios.post(`${process.env.AI_SERVICE_URL}/query`, {
      question,
    });

    return res
      .status(200)
      .json(
        new ApiResponse(
          200,
          aiResponse.data,
          "Question answered successfully"
        )
      );
  } catch (error) {
    console.error("AI service query error:", error.message);
    throw new ApiError(500, "AI Service failed to answer question");
  }
});
