from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from config import GROQ_API_KEY
import json

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-120b",
    temperature=0
)

SCHEMA = """
Nodes:
Instance(id)
Environment(name)
InstanceType(name)
PricingModel(name)
CostRecord(cpu, memory, hours, cost)
Date(value)

Relationships:
RUNS_IN
HAS_TYPE
USES_PRICING
HAS_COST
ON_DATE
"""

def generate_structured_cypher(step):
    prompt = f"""
You are a Neo4j expert.

Schema:
{SCHEMA}

Generate READ-ONLY Cypher.

Return JSON:
{{ "cypher": "...", "reasoning": "..." }}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)