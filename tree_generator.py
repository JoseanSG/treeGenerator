from graphviz import Digraph
from pdf2image import convert_from_path

class Tree:
    i = 1

    def get_index(self):
        self.i += 1
        return self.i - 1

    @staticmethod
    def create_tree(tokens, i = i):    
        dot = Digraph(comment='Arbol de expresion')

        def create_hijo(i, npadre):
            padre = npadre
            hijo1 = 0
            hijo2 = 0
            while 0 < len(tokens):
                token = tokens[-1]
                if token == "+" or token == "-" or token == "*" or token == "/":
                    if padre == 0:
                        dot.node(str(i), token)
                        tokens.pop()
                        padre = i
                        i += 1
                        print("padre1")
                    else:
                        if hijo1 == 0:                        
                            dot.node(str(i), token)
                            hijo1 = i                            
                            i = create_hijo(i, 0)# - 1
                            hijo2 = i - 1                            
                            # dot.edge(str(padre), str(hijo2))
                            # dot.edge(str(padre), str(hijo1))                            
                            #break
                            #tokens.pop()
                        else:
                            dot.node(str(i), token)
                            hijo2 = i
                            create_hijo(i, 0)
                            break
                            #tokens.pop()
                            print("padre2")
                            #break
                else:
                    if hijo1 == 0:
                        dot.node(str(i), token)
                        tokens.pop()
                        hijo1 = i
                        i += 1
                        print("padre3")
                    else:
                        if hijo2 == 0:
                            print(hijo2)
                            dot.node(str(i), token)
                            hijo2 = i
                            tokens.pop()
                            i += 1
                            break                                                                                                                                        
                        else:
                            if padre == 1:
                                return i + 1
                            else:                                    
                                dot.node(str(i), token)
                                hijo1 = padre
                                padre -= 1
                                hijo2 = i
                                return i + 1
                                break

            dot.edge(str(padre), str(hijo2))
            dot.edge(str(padre), str(hijo1))
            return i   
        create_hijo(i, 0)

        print(dot.source)

        dot.render('graficas/arbol.gv', view=False)
#________________________________________________________________3
    @staticmethod
    def create_tree2(tokens, i = i):    
        dot = Digraph(comment='Arbol de expresion')

        def create_hijo(i, npadre):
            padre = npadre
            hijo1 = 0
            hijo2 = 0
            while 0 < len(tokens):
                token = tokens[-1]
                if token == "+" or token == "-" or token == "*" or token == "/":
                    if padre == 0:
                        dot.node(str(i), token)
                        padre = i
                        tokens.pop()
                        i +=1
                    elif hijo1 == 0:
                        hijo1 = i
                        dot.node(str(i), token)
                        i = create_hijo(i, 0)  
                        token = tokens[-1]
                        hijo2 = i
                        dot.node(str(i), token)                                       
                        tokens.pop()                        
                        i +=1
                        break
                    elif hijo2 == 0:
                        hijo2 = i
                        dot.node(str(i), token)
                        i = create_hijo(i, 0)
                        break
                else:
                    if hijo1 == 0:
                        dot.node(str(i), token)
                        hijo1 = i
                        tokens.pop()
                        i +=1
                    elif hijo2 == 0:
                        dot.node(str(i), token)
                        hijo2 = i
                        tokens.pop()
                        i +=1
                        break
            dot.edge(str(padre), str(hijo1))
            dot.edge(str(padre), str(hijo2))                        
            return i
        create_hijo(i, 0)

        print(dot.source)

        dot.render('graficas/arbol.gv', view=False)      

#HACER UNA FUNCION QUE ME VAYA GENERANDO LOS INDICES AUTOMATICAMENTE
#AVERIGUAR COMO PODER HACER LAS RELACIONES CON LOS INDICES GENERAOS

# dot.node('A', 'King Arthur')
    # dot.node('B', 'Sir Bedevere the Wise')
    # dot.node('L', 'Sir Lancelot the Brave')

    # dot.edges(['AB', 'AL'])
    # dot.edge('B', 'L', constraint='false')  
    # 

# pages = convert_from_path('graficas/arbol.pdf', 500)
# for page in pages:
#     page.save('graficas/out.png', 'PNG')