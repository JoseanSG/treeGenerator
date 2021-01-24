from graphviz import Digraph
from pdf2image import convert_from_path

def create_tree(tokens):    
    dot = Digraph(comment='Arbol de expresion')
    i = 1
    # dot.node('A', 'King Arthur')
    # dot.node('B', 'Sir Bedevere the Wise')
    # dot.node('L', 'Sir Lancelot the Brave')

    # dot.edges(['AB', 'AL'])
    # dot.edge('B', 'L', constraint='false')      
    def create_hijo(i, npadre):
        padre = npadre
        hijo1 = 0
        hijo2 = 0
        while 0 < len(tokens):
            token = tokens[-1]
            if token == "+" or token == "-" or token == "*" or token != "/":
                if padre == 0:
                    dot.node(str(i), token)
                    tokens.pop()
                    padre = i
                    i += 1
                else:
                    if hijo1 == 0:                        
                        pass
                    else:
                        dot.node(str(i), token)
                        hijo2 = i
                        tokens.pop()
                        create_hijo(i, 3)
            else:
                if hijo1 == 0:
                    dot.node(str(i), token)
                    hijo1 = i
                    i += 1
                else:
                    dot.node(str(i), token)
                    hijo2 = i
                    tokens.pop()
                    i += 1
        dot.edge(str(padre), str(hijo1))
        dot.edge(str(padre), str(hijo2))

    create_hijo(1, 0)

    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE

    dot.render('graficas/arbol.gv', view=False)      

#HACER UNA FUNCION QUE ME VAYA GENERANDO LOS INDICES AUTOMATICAMENTE
#AVERIGUAR COMO PODER HACER LAS RELACIONES CON LOS INDICES GENERAOS


# pages = convert_from_path('graficas/arbol.pdf', 500)
# for page in pages:
#     page.save('graficas/out.png', 'PNG')