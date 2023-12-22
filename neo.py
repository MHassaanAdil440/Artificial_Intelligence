from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._uri = uri
        self._user = user
        self._password = password
        self._driver = None

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def run_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return result.data()

# Example usage
uri = "bolt://localhost:7687"  # Replace with your Neo4j server URI
user = "neo4j"                  # Replace with your Neo4j username
password = "12345678"      # Replace with your Neo4j password

neo4j_connection = Neo4jConnection(uri, user, password)
neo4j_connection.connect()

# Example query
query = "MATCH (n) RETURN n LIMIT 5"
result = neo4j_connection.run_query(query)
print(result)

# Close the connection when done
neo4j_connection.close()
