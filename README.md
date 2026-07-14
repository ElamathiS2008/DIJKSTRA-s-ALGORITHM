# Comparative Analysis of Dijkstra's Algorithm for Shortest Path Finding

## Overview

This project implements Dijkstra's Algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph.

The application allows users to:

- Input a graph
- Select a source vertex
- Find shortest distances
- Display the corresponding shortest paths

---

## Features

✅ User-friendly Streamlit interface

✅ Computes shortest paths efficiently

✅ Displays path and distance to every vertex

✅ Easy deployment on Streamlit Cloud

---

## Algorithm Used

### Dijkstra's Algorithm

Dijkstra's Algorithm is a greedy algorithm that finds the shortest path from a source node to all other nodes in a graph with non-negative edge weights.

---

## Time Complexity

```text
O((V + E) log V)
```

## Space Complexity

```text
O(V)
```

---

## Project Structure

```text
Dijkstra-Shortest-Path/
│
├── app.py
├── PROGRAM.py
├── requirements.txt
└── README.md
```

---

## Sample Input

Number of Vertices

```text
4
```

Edges

```text
0 1 4
0 2 1
2 1 2
1 3 1
2 3 5
```

Source Vertex

```text
0
```

---

## Sample Output

| Vertex | Distance | Path |
|--------|----------|------|
| 0 | 0 | 0 |
| 1 | 3 | 0 → 2 → 1 |
| 2 | 1 | 0 → 2 |
| 3 | 4 | 0 → 2 → 1 → 3 |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Dijkstra-Shortest-Path.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Deployment on Streamlit Cloud

1. Push the project to GitHub.

2. Visit:

https://streamlit.io/cloud

3. Click **New App**.

4. Select your repository.

5. Set:

```text
Main file path: app.py
```

6. Click **Deploy**.

---

## Applications

- GPS Navigation Systems
- Computer Networks
- Transportation Systems
- Routing Protocols
- Social Networks
- Robotics and Path Planning

---

## Author
ELAMATHI S
B.Tech AI&DS
Chennai Institute of Technology


