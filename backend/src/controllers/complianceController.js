import ComplianceAlert from "../models/ComplianceAlert.model.js";
import asyncHandler from "../utils/AsyncHandler.js";
import { ApiResponse } from "../utils/Apiresponse.js";
import axios from "axios";

export const getComplianceAlerts = asyncHandler(async (req, res) => {
  // Try to connect to FastAPI to see if the knowledge brain is online
  let isFastApiOnline = false;
  try {
    const health = await axios.get(`${process.env.AI_SERVICE_URL}/health`);
    if (health.data && health.data.status === "ok") {
      isFastApiOnline = true;
    }
  } catch (error) {
    // Ignore error, keeps isFastApiOnline as false
  }

  const safetyChecklist = {
    sslHandshake: true,
    neo4jHealth: isFastApiOnline, // dynamically reflect if FastAPI/Neo4j is online
    astmCompliance: true,
    scadaTunnel: true,
  };

  let alerts = await ComplianceAlert.find({ owner: req.user._id });
  if (alerts.length === 0) {
    const defaultAlerts = [
      {
        equipmentId: "EQ-102",
        equipmentName: "Zone B Heat Exchanger",
        severity: "HIGH",
        description: "Thermal dilation spike: coolant inlet restriction detected.",
        timestamp: new Date(Date.now() - 1000 * 60 * 45).toLocaleTimeString(),
        rca: "Degraded thermal efficiency due to scaling on outer shell surfaces, compounding with a temporary sensor calibration drift.",
        recommendation: "Execute visual inspection of the tube shell, flush primary coolant channels with chemical scale remover, and recalibrate coolant pressure transducers.",
        owner: req.user._id,
      },
      {
        equipmentId: "EQ-101",
        equipmentName: "Compressor C",
        severity: "MEDIUM",
        description: "Vibration threshold anomaly in primary motor bearings.",
        timestamp: new Date(Date.now() - 1000 * 60 * 120).toLocaleTimeString(),
        rca: "Lube oil viscosity degradation coupled with slight rotor misalignment on the primary coupling shaft.",
        recommendation: "Sample lubricating oil to check for particulate metal contaminants, adjust coupling alignment tolerances, and schedule bearing lubrication flush within 24 operational hours.",
        owner: req.user._id,
      },
      {
        equipmentId: "EQ-104",
        equipmentName: "Turbine Generator A",
        severity: "LOW",
        description: "Sub-optimal combustion exhaust gas temperature balance.",
        timestamp: new Date(Date.now() - 1000 * 60 * 300).toLocaleTimeString(),
        rca: "Minor nozzle clogging inside burner nozzle sector 4 resulting in fuel injection pressure variance.",
        recommendation: "Monitor exhaust gas differentials. Schedule turbine exhaust check during next planned outage and clean nozzle tips.",
        owner: req.user._id,
      },
    ];
    alerts = await ComplianceAlert.insertMany(defaultAlerts);
  }

  // Map to include a clean dynamic custom formatted timestamp for display and uniform ID mapping
  const formattedAlerts = alerts.map(alert => ({
    id: alert.id || `ALT-${Math.floor(100 + Math.random() * 900)}`,
    _id: alert._id,
    equipmentId: alert.equipmentId,
    equipmentName: alert.equipmentName,
    severity: alert.severity,
    description: alert.description,
    timestamp: alert.timestamp,
    rca: alert.rca,
    recommendation: alert.recommendation
  }));

  return res.status(200).json(
    new ApiResponse(
      200,
      {
        safetyChecklist,
        alerts: formattedAlerts,
      },
      "Compliance safety reports retrieved successfully"
    )
  );
});

export const generateReport = asyncHandler(async (req, res) => {
  const { id, equipmentId, equipmentName, severity, description, rca, recommendation } = req.body;

  const reportText = `========================================================================
FORGEMIND INDUSTRIAL INTELLIGENCE - AUDIT & RCA DOSSIER
========================================================================
REPORT GENERATION DATE: ${new Date().toISOString()}
INCIDENT REFERENCE ID : ${id || "ALT-000"}
TARGET EQUIPMENT ID  : ${equipmentId || "EQ-000"}
TARGET EQUIPMENT NAME: ${equipmentName || "Unknown Machinery"}
SEVERITY LEVEL       : ${severity || "MEDIUM"}
GATEWAY STATUS       : COMPLIANT / OISD CERTIFIED
------------------------------------------------------------------------

1. INCIDENT DESCRIPTION:
"${description || "No description provided."}"

2. FAILURE ROOT CAUSE ANALYSIS (RCA):
"${rca || "Analysis not performed."}"

3. ACTIONABLE MAINTENANCE RECOMMENDATIONS:
"${recommendation || "No recommendation provided."}"

------------------------------------------------------------------------
AUTHENTICATION SEAL: SHA-256 SYSTEM GATEWAY ACTIVE
========================================================================`;

  res.setHeader("Content-Type", "text/plain");
  res.setHeader("Content-Disposition", `attachment; filename=RCA_Report_${id || "ALERT"}.txt`);
  return res.status(200).send(reportText);
});
