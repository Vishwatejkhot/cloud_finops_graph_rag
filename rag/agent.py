from rag.planner import multi_hop_plan
from rag.cypher_generator import generate_structured_cypher
from rag.graph_retriever import retrieve_graph_data
from rag.answer_generator import generate_answer
from rag.correction import correct_cypher
from tools.cost_simulator import simulate_reserved_savings

def run_agent(user_query):

    steps = multi_hop_plan(user_query)

    aggregated_results = []
    total_cost = 0

    for step in steps:
        structured = generate_structured_cypher(step)
        cypher_query = structured["cypher"]

        try:
            result = retrieve_graph_data(cypher_query)
        except Exception as e:
            cypher_query = correct_cypher(cypher_query, str(e))
            result = retrieve_graph_data(cypher_query)

        aggregated_results.append(result)

        for record in result:
            for value in record.values():
                if isinstance(value, (int, float)):
                    total_cost += value

    simulation = simulate_reserved_savings(total_cost)

    final_answer = generate_answer(
        user_query,
        aggregated_results,
        simulation
    )

    return {
        "plan": steps,
        "simulation": simulation,
        "answer": final_answer
    }