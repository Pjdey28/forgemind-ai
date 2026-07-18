import express from "express";
import { verifyJWT } from "../middlewares/authMiddleware.js";
import { getDashboardData, toggleEquipmentStatus } from "../controllers/dashboardController.js";

const router = express.Router();

router.use(verifyJWT);

router.get("/", getDashboardData);
router.put("/equipment/:id", toggleEquipmentStatus);

export default router;
