MATCH (n:class)-[:is]-(m)  WHERE n.name = "Readers" and m.telephone CONTAINS "(33)" RETURN m