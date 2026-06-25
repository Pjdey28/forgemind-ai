# ⚙️ ForgeMind AI Backend

The backend powers the core intelligence of ForgeMind AI. It provides secure APIs, document processing, AI orchestration, knowledge graph generation, semantic search, and authentication services.

---

# 🚀 Responsibilities

* User Authentication
* Document Upload
* OCR Processing
* Metadata Extraction
* Embedding Generation
* RAG Pipeline
* Knowledge Graph Generation
* Gemini AI Integration
* Compliance Analysis
* Maintenance Intelligence
* REST APIs

---

# 🏗 Architecture

```text
Client Request
      │
      ▼
Express Routes
      │
      ▼
Controllers
      │
      ▼
Services
      │
      ▼
AI Layer
      │
      ▼
Database
```

---

# 📂 Folder Structure

```text
backend/

src/
│
├── config/
├── controllers/
├── middlewares/
├── models/
├── routes/
├── services/
├── utils/
├── agents/
├── rag/
├── graph/
├── prompts/
└── server.js

uploads/
package.json
```

---

# 🤖 AI Modules

## Document Agent

Responsible for

* OCR
* Parsing
* Chunking
* Metadata Extraction

---

## RAG Engine

Responsible for

* Embedding Generation
* Vector Search
* Context Retrieval
* Prompt Construction

---

## Knowledge Graph Engine

Responsible for

* Entity Extraction
* Relationship Detection
* Graph Generation

---

## Maintenance Agent

Responsible for

* Failure Analysis
* Maintenance Suggestions
* RCA Generation

---

## Compliance Agent

Responsible for

* Compliance Checks
* Safety Analysis
* Audit Reports

---

# 🗄 Database

MongoDB Collections

* Users
* Documents
* Equipment
* Maintenance
* Incidents
* Compliance Reports

---

# 🔌 API Modules

Authentication

```http
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/profile
```

Documents

```http
POST   /api/documents/upload
GET    /api/documents
GET    /api/documents/:id
DELETE /api/documents/:id
```

AI

```http
POST /api/chat
POST /api/rag/query
POST /api/maintenance/analyze
POST /api/compliance/check
```

Knowledge Graph

```http
GET /api/graph
GET /api/graph/:equipmentId
```

---

# 🛠 Tech Stack

* Node.js
* Express.js
* MongoDB
* Mongoose
* Gemini API
* LangChain
* ChromaDB
* Neo4j
* Multer
* Tesseract OCR
* PyMuPDF

---

# 📌 Status

🚧 Under Development
