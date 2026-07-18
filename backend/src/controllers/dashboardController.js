import Document from "../models/Document.model.js";
import Equipment from "../models/Equipment.model.js";
import asyncHandler from "../utils/AsyncHandler.js";
import { ApiResponse } from "../utils/Apiresponse.js";
import axios from "axios";

export const getDashboardData = asyncHandler(async (req, res) => {
  // 1. Fetch document count & recent uploads from MongoDB
  const totalDocuments = await Document.countDocuments({ owner: req.user._id });
  const recentUploads = await Document.find({ owner: req.user._id })
    .sort({ createdAt: -1 })
    .limit(5);

  // 2. Fetch or seed equipment list
  let equipmentList = await Equipment.find({ owner: req.user._id });
  if (equipmentList.length === 0) {
    const defaultEquipment = [
      { name: "Compressor C", type: "Rotary Screw", plant: "Sector A", status: "ONLINE", load: 68, owner: req.user._id },
      { name: "Zone B Heat Exchanger", type: "Shell & Tube", plant: "Sector B", status: "WARNING", load: 82, owner: req.user._id },
      { name: "Valve 04 Controller", type: "Flow Regulation", plant: "Sector B", status: "ONLINE", load: 45, owner: req.user._id },
      { name: "Turbine Generator A", type: "Gas Turbine", plant: "Sector C", status: "OFFLINE", load: 0, owner: req.user._id },
    ];
    equipmentList = await Equipment.insertMany(defaultEquipment);
  }

  let graphNodesCount = 0;
  let graphEdgesCount = 0;
  let aiServiceStatus = "OFFLINE";

  // 3. Fetch stats from FastAPI graph stats router
  try {
    const statsResponse = await axios.get(
      `${process.env.AI_SERVICE_URL}/graph/stats`
    );
    if (statsResponse.data) {
      graphNodesCount = statsResponse.data.nodes_count || 0;
      graphEdgesCount = statsResponse.data.edges_count || 0;
      aiServiceStatus = "ONLINE";
    }
  } catch (error) {
    console.error("AI service dashboard stats fetch error:", error.message);
  }

  // 4. Compile telemetry payload
  const dashboardStats = {
    totalDocuments,
    recentUploads,
    graphNodesCount,
    graphEdgesCount,
    aiServiceStatus,
    equipmentList,
    neuralCoreLoad: totalDocuments > 0 ? 45 + totalDocuments * 5 : 45,
    bufferMem: 61,
    cpuTemp: 42,
  };

  return res
    .status(200)
    .json(
      new ApiResponse(
        200,
        dashboardStats,
        "Dashboard statistics retrieved successfully"
      )
    );
});

export const toggleEquipmentStatus = asyncHandler(async (req, res) => {
  const { id } = req.params;
  const equipment = await Equipment.findOne({ _id: id, owner: req.user._id });
  if (!equipment) {
    return res.status(404).json(new ApiResponse(404, null, "Equipment not found"));
  }
  const nextStatus = equipment.status === "OFFLINE" ? "ONLINE" : "OFFLINE";
  equipment.status = nextStatus;
  equipment.load = nextStatus === "OFFLINE" ? 0 : Math.round(40 + Math.random() * 30);
  await equipment.save();

  return res.status(200).json(
    new ApiResponse(200, equipment, "Equipment status updated successfully")
  );
});
