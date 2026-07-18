import express from "express";
import { verifyJWT } from "../middlewares/authMiddleware.js";
import { getGraphNetwork } from "../controllers/graphController.js";

const router = express.Router();

router.use(verifyJWT);

router.get("/", getGraphNetwork);

export default router;
