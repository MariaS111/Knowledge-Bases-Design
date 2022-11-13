MATCH (n: class)-[:is]-(m) WHERE n.name = "Readers" 
CALL {
  WITH m
  MATCH (m)-[:borrow]-(c)-[:is]-(k: class) WHERE k.name= "Books"
  RETURN count(c) AS y
}
RETURN m.name, y