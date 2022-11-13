MATCH (n: class)-[:is]-(m) WHERE n.name = "Books" 
CALL {WITH m
  MATCH (m)-[r:borrow]-(c)-[:is]-(k: class) WHERE k.name= "Readers"
  RETURN count(r) AS y}
RETURN m.name, y
ORDER BY y DESC
LIMIT 1