import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from rag.agent import run_agent
from graph.graph_client import GraphClient


st.set_page_config(
    page_title="Cloud FinOps Graph RAG",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.title("⚙️ Settings")

show_plan = st.sidebar.checkbox("Show Multi-hop Plan", value=True)
show_simulation = st.sidebar.checkbox("Show Cost Simulation", value=True)
show_graph = st.sidebar.checkbox("Show Graph Visualization", value=True)

st.sidebar.markdown("---")
st.sidebar.info(
    "🚀 Cloud FinOps Copilot\n\n"
    "Neo4j + Groq + Streamlit\n\n"
    "Agentic Graph RAG System"
)

st.title("🚀 Cloud FinOps Copilot (Graph RAG)")
st.markdown("Agentic Knowledge Graph powered Cloud Cost Optimization")

try:
    graph = GraphClient()

    total_cost = graph.execute(
        "MATCH (c:CostRecord) RETURN sum(c.cost) AS total"
    )[0]["total"] or 0

    prod_cost = graph.execute(
        """
        MATCH (i:Instance)-[:RUNS_IN]->(:Environment {name:'prod'})
        MATCH (i)-[:HAS_COST]->(c:CostRecord)
        RETURN sum(c.cost) AS total
        """
    )[0]["total"] or 0

    underutilized = graph.execute(
        """
        MATCH (i:Instance)-[:HAS_COST]->(c:CostRecord)
        WHERE c.cpu < 20
        RETURN count(DISTINCT i) AS count
        """
    )[0]["count"] or 0

    graph.close()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cost", f"${round(total_cost,2)}")
    col2.metric("Prod Cost", f"${round(prod_cost,2)}")
    col3.metric("Underutilized Instances", underutilized)

except Exception:
    st.warning("⚠️ Could not load summary metrics.")

st.markdown("---")

if "history" not in st.session_state:
    st.session_state.history = []


user_query = st.text_input(
    "Ask a cloud cost optimization question:",
    placeholder="Example: How can we reduce prod cost by 20%?"
)


if st.button("Run Analysis") and user_query:

    with st.spinner("Running Agentic Graph RAG..."):
        result = run_agent(user_query)

    st.session_state.history.append(result)

    
    st.subheader("💡 AI Recommendation")
    st.write(result.get("answer", "No answer generated."))

  
    if show_plan and "plan" in result:
        st.subheader("🧠 Multi-hop Reasoning Plan")
        st.json(result["plan"])

    
    if show_simulation and "simulation" in result:
        st.subheader("📊 Cost Simulation")

        sim = result["simulation"]

        col1, col2, col3 = st.columns(3)
        col1.metric("Current Cost", f"${sim.get('current_cost',0)}")
        col2.metric("Estimated New Cost", f"${sim.get('estimated_new_cost',0)}")
        col3.metric("Estimated Savings", f"${sim.get('estimated_savings',0)}")

   
    if show_graph and "graph_data" in result:

        st.subheader("🕸 Graph Visualization")

        graph_data = result["graph_data"]

        nodes_data = graph_data.get("nodes", [])
        edges_data = graph_data.get("edges", [])

        graph_nodes = []
        graph_edges = []

        color_map = {
            "Instance": "#1f77b4",
            "Environment": "#ff7f0e",
            "PricingModel": "#2ca02c",
            "InstanceType": "#d62728",
            "Date": "#9467bd"
        }

        for node in nodes_data:
            graph_nodes.append(
                Node(
                    id=str(node.get("id")),
                    label=node.get("label", ""),
                    size=25,
                    color=color_map.get(node.get("type"), "#7f7f7f")
                )
            )

        for edge in edges_data:
            graph_edges.append(
                Edge(
                    source=str(edge.get("source")),
                    target=str(edge.get("target")),
                    label=edge.get("label", "")
                )
            )

        config = Config(
            width=1000,
            height=600,
            directed=True,
            physics=True,
            nodeHighlightBehavior=True,
            highlightColor="#F7A7A6"
        )

        if graph_nodes:
            agraph(
                nodes=graph_nodes,
                edges=graph_edges,
                config=config
            )
        else:
            st.info("No graph relationships returned for this query.")

st.markdown("---")


if st.session_state.history:
    st.subheader("📜 Previous Queries")

    for i, item in enumerate(reversed(st.session_state.history[-5:])):
        with st.expander(f"Query {len(st.session_state.history)-i}"):
            st.write(item.get("answer", "No answer"))