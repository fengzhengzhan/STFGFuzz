import graphviz

with open("../Programs/base64/base64.bc.callgraph.dot") as f:
    dot_praph = f.read()

dot = graphviz.Source(dot_praph)
print(dot)
dot.view(directory="InfoData/graph_data/dot_view/")