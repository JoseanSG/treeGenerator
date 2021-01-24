from graphviz import Digraph
from pdf2image import convert_from_path

def create_tree(tokens):
    dot = Digraph(comment='The Round Table')

    dot

    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')

    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='false')

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE

    dot.render('graficas/arbol.gv', view=True)


pages = convert_from_path('graficas/arbol.pdf', 500)
for page in pages:
    page.save('graficas/out.png', 'PNG')