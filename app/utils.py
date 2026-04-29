from pyvis.network import Network
import os

def draw_interactive_graph(graph, start_node=None, goal_node=None, path=[]):
    net = Network(height="700px", width="100%", bgcolor="#0b0f1a", font_color="white")

    net.barnes_hut()

    for node in graph.nodes:
        h = graph.nodes[node].get("h", 0)
        g = sum([graph.edges[e]['g'] for e in graph.edges(node)]) if graph.edges(node) else 0
        f = g + h

        if node == start_node:
            color = "green"
        elif node == goal_node:
            color = "gold"
        elif node in path:
            color = "purple"
        else:
            color = "blue"

        net.add_node(
            node,
            label=node,
            title=f"g(n): {round(g,2)}\nh(n): {round(h,2)}\nf(n): {round(f,2)}",
            color=color
        )

    for u, v in graph.edges:
        weight = graph.edges[(u, v)]['g']
        net.add_edge(u, v, label=str(round(weight,2)))

    output_path = os.path.join("static", "graph.html")

    net.save_graph(output_path)