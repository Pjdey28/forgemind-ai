import mongoose from "mongoose";

const equipmentSchema = new mongoose.Schema(
  {
    name: { type: String, required: true },
    type: { type: String, required: true },
    plant: { type: String, required: true },
    status: { type: String, enum: ["ONLINE", "WARNING", "OFFLINE"], default: "ONLINE" },
    load: { type: Number, default: 50 },
    owner: { type: mongoose.Schema.Types.ObjectId, ref: "User", required: true }
  },
  { timestamps: true }
);

export default mongoose.model("Equipment", equipmentSchema);
