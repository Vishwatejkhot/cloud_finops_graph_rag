from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from config import GROQ_API_KEY
import json

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-120b",
    temperature=0
)

def correct_cypher(original_query, error_message):
    prompt = f"""
This Cypher failed:

Query:
{original_query}

Error:
{error_message}

Fix it.

Return JSON:
{{ "cypher": "..." }}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)["cypher"]