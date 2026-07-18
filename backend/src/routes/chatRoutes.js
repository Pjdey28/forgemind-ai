import express from "express";
import { verifyJWT } from "../middlewares/authMiddleware.js";
import { askQuestion } from "../controllers/chatController.js";

const router = express.Router();

router.use(verifyJWT);

router.post("/", askQuestion);

export default router;
