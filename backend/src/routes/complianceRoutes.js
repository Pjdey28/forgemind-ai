import express from "express";
import { verifyJWT } from "../middlewares/authMiddleware.js";
import { getComplianceAlerts, generateReport } from "../controllers/complianceController.js";

const router = express.Router();

router.use(verifyJWT);

router.get("/", getComplianceAlerts);
router.post("/report", generateReport);

export default router;
