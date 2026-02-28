from graph.graph_client import GraphClient

def retrieve_graph_data(cypher_query):
    graph = GraphClient()
    result = graph.execute(cypher_query)
    graph.close()
    return result