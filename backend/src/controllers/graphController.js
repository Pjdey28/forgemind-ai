import asyncHandler from "../utils/AsyncHandler.js";
import { ApiResponse } from "../utils/Apiresponse.js";
import axios from "axios";

export const getGraphNetwork = asyncHandler(async (req, res) => {
  try {
    const aiResponse = await axios.get(
      `${process.env.AI_SERVICE_URL}/graph/all`
    );
    return res
      .status(200)
      .json(
        new ApiResponse(
          200,
          aiResponse.data,
          "Knowledge network retrieved successfully"
        )
      );
  } catch (error) {
    console.error("AI service get graph network error:", error.message);
    // Return empty nodes/edges structure rather than crashing, for smooth UI fallback
    return res
      .status(200)
      .json(
        new ApiResponse(
          200,
          { nodes: [], edges: [] },
          "AI service graph network offline. Returned empty network."
        )
      );
  }
});
