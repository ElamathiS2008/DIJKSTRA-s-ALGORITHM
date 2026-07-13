import streamlit as st
from PROGRAM import dijkstra, reconstruct_path

st.title("Dijkstra's Shortest Path Algorithm")

n = st.number_input(
    "Enter Number of Vertices",
    min_value=1,
    step=1
)

st.write(
    "Enter edges in the format:\n"
    "source destination weight\n"
    "One edge per line."
)

edge_text = st.text_area(
    "Edges",
    height=200,
    placeholder="0 1 4\n0 2 1\n2 1 2\n1 3 1\n2 3 5"
)

source = st.number_input(
    "Enter Source Vertex",
    min_value=0,
    step=1
)

if st.button("Find Shortest Paths"):
    try:
        graph = {}

        for i in range(int(n)):
            graph[i] = []

        lines = edge_text.strip().split("\n")

        for line in lines:
            u, v, w = map(int, line.split())
            graph[u].append((v, w))

        dist, prev = dijkstra(graph, int(source))

        st.subheader(
            f"Shortest Paths from Vertex {int(source)}"
        )

        result = []

        for v in range(int(n)):
            path = reconstruct_path(
                prev,
                int(source),
                v
            )

            if path:
                path_str = " -> ".join(
                    map(str, path)
                )
            else:
                path_str = "No Path"

            distance = (
                dist[v]
                if dist[v] != float('inf')
                else "INF"
            )

            result.append(
                (v, distance, path_str)
            )

        st.table(
            {
                "Vertex":
                [r[0] for r in result],

                "Distance":
                [r[1] for r in result],

                "Path":
                [r[2] for r in result],
            }
        )

    except:
        st.error(
            "Please enter valid input."
        )
