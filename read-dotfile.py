import graphviz

with open("LLVM/OLLVM++/Test/main.dot") as f:
    dot_praph = f.read()

dot = graphviz.Source(dot_praph)
print(dot)
dot.view()