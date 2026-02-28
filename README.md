# 🚀 Cloud FinOps Graph RAG Agent

Agentic Knowledge Graph powered Cloud Cost Optimization using:

- 🧠 Groq LLM (openai/gpt-oss-120b)
- 🗄 Neo4j Aura (Knowledge Graph)
- ⚡ Streamlit (Interactive UI)
- 🔎 Multi-hop Graph Reasoning
- 🛠 Tool-Orchestrated Cost Simulation

---

## 📌 Overview

Cloud teams often overspend due to:

- Over-provisioned compute
- Idle resources
- Lack of commitment discounts
- Poor storage tiering
- Missing governance

This project builds an **Agentic Graph RAG FinOps Copilot** that:

1. Converts natural language questions into Cypher
2. Queries a Neo4j knowledge graph
3. Performs multi-hop reasoning
4. Simulates cost savings
5. Produces structured optimization recommendations
6. Visualizes subgraphs interactively

---

## 🧠 Architecture

```
User Question
      ↓
Multi-hop Planner (Groq LLM)
      ↓
Structured Cypher Generator (JSON)
      ↓
Neo4j Graph Retrieval
      ↓
Auto Query Correction (if needed)
      ↓
Cost Simulation Tool
      ↓
Grounded LLM Recommendation
      ↓
Streamlit Visualization
```

---

## 🗂 Project Structure

```
cloud_finops_graph_rag/
│
├── streamlit_app.py
├── config.py
│
├── graph/
│   ├── graph_client.py
│   └── ingest.py
│
├── rag/
│   ├── agent.py
│   ├── planner.py
│   ├── cypher_generator.py
│   ├── correction.py
│   ├── graph_retriever.py
│   └── answer_generator.py
│
├── tools/
│   └── cost_simulator.py
│
├── data/
│   └── synthetic_cloud_cost_dataset.csv
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd cloud_finops_graph_rag
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
.venv\Scripts\activate      # windows
```

---

### 3️⃣ Install Dependencies

```bash
uv add -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file in project root:

```
GROQ_API_KEY=your_groq_api_key

NEO4J_URI=neo4j+s://your_instance.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
NEO4J_DATABASE=neo4j
```

⚠️ No quotes. No spaces.

---

### 5️⃣ Ingest Data into Neo4j Aura

```bash
python -m graph.ingest
```

Verify in Neo4j browser:

```cypher
MATCH (n) RETURN count(n);
```

You should see thousands of nodes.

---

### 6️⃣ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## 📊 Features

### 🔹 Multi-Hop Reasoning
Breaks user questions into structured reasoning steps.

### 🔹 JSON Structured Cypher Output
Prevents hallucinated queries.

### 🔹 Automatic Query Correction
If Neo4j query fails, LLM fixes it.

### 🔹 Cost Simulation Tool
Simulates savings from:
- Reserved instances
- Rightsizing
- Discount strategies

### 🔹 Graph Visualization
Interactive subgraph display with:

- Instance nodes
- Environment nodes
- Pricing model relationships
- Cost relationships

### 🔹 FinOps Insights
Produces structured output:

1. Insight
2. Root Cause
3. Savings Strategy
4. Estimated Impact

---

## 🧠 Example Query

```
How can we reduce prod cost by 20%?
```

Output includes:

- Multi-hop plan
- Real cost breakdown
- Estimated savings
- Interactive graph
- Structured business recommendation

---

## 🔐 Security Best Practices

- Never commit `.env`
- Rotate API keys regularly
- Use Neo4j Aura encrypted connection (`neo4j+s`)
- Validate Cypher to block destructive queries
- Use read-only LLM prompts

---

## 🏗 Future Improvements

- Hybrid Graph + Vector RAG
- Monte Carlo cost simulation
- Policy enforcement agent
- Memory layer
- Dockerized deployment
- Real-time cloud billing integration
- FinOps dashboard with time filtering

---

## 📈 Why This Project Matters

This is not simple RAG.

This is:

> Agentic, Tool-Orchestrated, Multi-Hop Graph RAG  
> Applied to Cloud FinOps Optimization.

Demonstrates:

- LLM orchestration
- Knowledge graph modeling
- Cypher generation
- Error recovery
- Tool calling
- Business-driven AI engineering

---

## 👨‍💻 Author
Vishwatej Khot 

---
