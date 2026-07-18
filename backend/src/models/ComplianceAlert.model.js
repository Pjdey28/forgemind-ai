import mongoose from "mongoose";

const complianceAlertSchema = new mongoose.Schema(
  {
    equipmentId: { type: String, required: true },
    equipmentName: { type: String, required: true },
    severity: { type: String, enum: ["HIGH", "MEDIUM", "LOW"], default: "MEDIUM" },
    description: { type: String, required: true },
    timestamp: { type: String, required: true },
    rca: { type: String, required: true },
    recommendation: { type: String, required: true },
    owner: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }
  },
  { timestamps: true }
);

export default mongoose.model("ComplianceAlert", complianceAlertSchema);
