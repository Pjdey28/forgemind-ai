import express from "express";
import { upload } from "../middlewares/multer.middleware.js";
import { verifyJWT } from "../middlewares/authMiddleware.js";
import {
  uploadDocument,
  getDocuments,
  deleteDocument,
} from "../controllers/documentController.js";

const router = express.Router();

router.use(verifyJWT);

router.get("/", getDocuments);
router.post("/upload", upload.single("file"), uploadDocument);
router.delete("/:id", deleteDocument);

export default router;
