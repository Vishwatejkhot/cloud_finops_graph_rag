CREATE CONSTRAINT instance_id IF NOT EXISTS
FOR (i:Instance)
REQUIRE i.id IS UNIQUE;

CREATE CONSTRAINT env_name IF NOT EXISTS
FOR (e:Environment)
REQUIRE e.name IS UNIQUE;

CREATE CONSTRAINT type_name IF NOT EXISTS
FOR (t:InstanceType)
REQUIRE t.name IS UNIQUE;

CREATE CONSTRAINT pricing_name IF NOT EXISTS
FOR (p:PricingModel)
REQUIRE p.name IS UNIQUE;  


