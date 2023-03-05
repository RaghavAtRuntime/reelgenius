import networkx as nx

# Define the nodes
movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Fight Club']
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Define the edges
edges = [('The Shawshank Redemption', 'The Godfather', 0.9),
         ('The Shawshank Redemption', 'The Dark Knight', 0.7),
         ('The Shawshank Redemption', 'Pulp Fiction', 0.6),
         ('The Godfather', 'The Dark Knight', 0.8),
         ('The Godfather', 'Pulp Fiction', 0.7),
         ('The Dark Knight', 'Pulp Fiction', 0.5),
         ('The Shawshank Redemption', 'Alice', 5),
         ('The Shawshank Redemption', 'Bob', 4),
         ('The Shawshank Redemption', 'Charlie', 3),
         ('The Godfather', 'Bob', 5),
         ('The Godfather', 'Charlie', 4),
         ('The Dark Knight', 'Charlie', 5),
         ('Pulp Fiction', 'David', 4),
         ('Pulp Fiction', 'Eve', 5)]

# Build the graph
G = nx.DiGraph()
G.add_nodes_from(movies, bipartite=0)
G.add_nodes_from(users, bipartite=1)
G.add_weighted_edges_from(edges)

# Recommend movies to a user based on their ratings
user = 'Alice'
recommendations = {}
for movie in movies:
    if not G.has_edge(user, movie):
        score = sum([G[user][rating]['weight'] * G[rating][movie]['weight'] for rating in G.neighbors(user) if G.has_edge(rating, movie)])
        recommendations[movie] = score
print(sorted(recommendations.items(), key=lambda x: x[1], reverse=True))
