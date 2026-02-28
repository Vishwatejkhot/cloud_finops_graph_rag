from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from config import GROQ_API_KEY
import json

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-120b",
    temperature=0
)

def multi_hop_plan(user_query):
    prompt = f"""
Break this cloud cost question into reasoning steps.

User Query:
{user_query}

Return JSON list of steps.
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content.replace("```json", "").replace("```", "").strip()
    return json.loads(content) 