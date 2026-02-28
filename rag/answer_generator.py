from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from config import GROQ_API_KEY

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-120b",
    temperature=0.2
)

def generate_answer(user_query, graph_data, simulation):
    prompt = f"""
You are a Cloud FinOps AI Copilot.

User Question:
{user_query}

Graph Data:
{graph_data}

Simulation Result:
{simulation}

Provide structured recommendation:
1. Insight
2. Root cause
3. Savings strategy
4. Estimated impact
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()