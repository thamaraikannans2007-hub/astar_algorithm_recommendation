from pyvis.network import Network
import os

def draw_interactive_graph(graph, start_node=None, goal_node=None, path=[]):
    net = Network(
        height="750px",
        width="100%",
        bgcolor="#0f172a",
        font_color="white"
    )

    net.barnes_hut(
        gravity=-3000,
        central_gravity=0.3,
        spring_length=200,
        spring_strength=0.05,
        damping=0.9
    )

    for node in graph.nodes:
        h = graph.nodes[node].get("h", 0)
        g = sum([graph.edges[e]['g'] for e in graph.edges(node)]) if graph.edges(node) else 0
        f = g + h

        if node == start_node:
            color = "#22c55e"
            label = f"START\n{node}"
            size = 35
        elif node == goal_node:
            color = "#facc15"
            label = f"GOAL\n{node}"
            size = 30
        elif node in path:
            color = "#a855f7"   # purple
            label = node
            size = 28
        else:
            color = "#38bdf8"   # light blue
            label = node
            size = 25

        net.add_node(
            node,
            label=label,
            size=size,
            color=color,
            borderWidth=2,
            title=f"""
            <b>{node}</b><br>
            g(n): {round(g,2)}<br>
            h(n): {round(h,2)}<br>
            f(n): {round(f,2)}
            """
        )

    for u, v in graph.edges:
        weight = graph.edges[(u, v)]['g']

        net.add_edge(
            u,
            v,
            label=str(round(weight, 2)),
            color="#94a3b8",
            width=2
        )

    net.set_options("""
    var options = {
      "nodes": {
        "shape": "dot",
        "font": {
          "size": 16,
          "color": "white"
        }
      },
      "edges": {
        "font": {
          "size": 12,
          "align": "middle"
        },
        "smooth": true
      },
      "physics": {
        "enabled": true
      },
      "interaction": {
        "hover": true,
        "zoomView": true,
        "dragView": true
      }
    }
    """)
    output_path = os.path.join("static", "graph.html")
    net.save_graph(output_path)