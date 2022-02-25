import graphviz

with open("llvm_mode/Programs/IR/.main.dot") as f:
    dot_praph = f.read()

dot = graphviz.Source(dot_praph)
print(dot)
dot.view()