import pandas as pd
from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE

df = pd.read_csv("data/synthetic_cloud_cost_dataset.csv")

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

def load_data(tx, row):
    tx.run("""
    MERGE (i:Instance {id: $instance_id})
    MERGE (e:Environment {name: $environment})
    MERGE (t:InstanceType {name: $instance_type})
    MERGE (p:PricingModel {name: $pricing_model})
    MERGE (d:Date {value: $date})

    CREATE (c:CostRecord {
        cpu: $cpu,
        memory: $memory,
        hours: $hours,
        cost: $cost
    })

    MERGE (i)-[:RUNS_IN]->(e)
    MERGE (i)-[:HAS_TYPE]->(t)
    MERGE (i)-[:USES_PRICING]->(p)
    MERGE (i)-[:HAS_COST]->(c)
    MERGE (c)-[:ON_DATE]->(d)
    """,
    instance_id=row["instance_id"],
    environment=row["environment"],
    instance_type=row["instance_type"],
    pricing_model=row["pricing_model"],
    date=row["date"],
    cpu=row["cpu_avg_percent"],
    memory=row["memory_avg_percent"],
    hours=row["hours_used"],
    cost=row["daily_cost_usd"]
    )

# 🔥 IMPORTANT: specify database
with driver.session(database=NEO4J_DATABASE) as session:
    for _, row in df.iterrows():
        session.execute_write(load_data, row)

driver.close()
print("✅ Data ingestion complete.")