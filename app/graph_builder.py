import networkx as nx

class AStarGraph:
    def __init__(self, recommendations):
        self.graph = nx.Graph()
        self.build_graph(recommendations)

    def build_graph(self, recs):
        for i, movie in enumerate(recs):
            self.graph.add_node(movie['title'], h=1-movie['score'])

        for i in range(len(recs)-1):
            self.graph.add_edge(
                recs[i]['title'],
                recs[i+1]['title'],
                g=recs[i]['score']
            )

    def compute_f(self):
        data = []
        for node in self.graph.nodes:
            h = self.graph.nodes[node]['h']
            g = sum([self.graph.edges[e]['g'] for e in self.graph.edges(node)]) if self.graph.edges(node) else 0
            f = g + h
            data.append((node, g, h, f))
        return data