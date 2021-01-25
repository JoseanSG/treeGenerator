from graphviz import Digraph
from pdf2image import convert_from_path

class Tree:
    i = 1

    def get_index(self):
        self.i += 1
        return self.i - 1

    @staticmethod
    def create_tree2(tokens, i = i):    
        dot = Digraph(comment='Arbol de expresion')

        def create_hijo(i, npadre):
            padre = npadre
            hijo1 = 0
            hijo2 = 0
            while 0 < len(tokens):
                token = tokens[-1]
                print(token)
                if token == "+" or token == "-" or token == "*" or token == "/":                    
                    if padre == 0:
                        print("entro1")
                        dot.node(str(i), token)
                        padre = i
                        tokens.pop()
                        i +=1
                        #si tiene un simbolo como hijo
                    elif hijo1 == 0:
                        print("entro2")
                        hijo1 = i
                        #lo almacena como hijo y lo pasa recursivamente para calcular sus propios hijos
                        dot.node(str(i), token)
                        i = create_hijo(i, 0)  #
                        token = tokens[-1]
                        hijo2 = i
                        dot.node(str(i), token)                                       
                        tokens.pop()                        
                        i +=1
                        #para que la funcion no acabe si es que quedan mas elementos en la pila
                        if len(tokens) > 0:
                            dot.edge(str(padre), str(hijo2), rankdir="RL")
                            dot.edge(str(padre), str(hijo1), rankdir="RL")                            
                            padre = hijo2
                            hijo1 = 0
                            hijo2 = 0
                            #regresa al while
                        else:   
                            #si ya no hay mas elementos acaba la ejecucion                         
                            break
                        #REVISAR EL CASO CUANDO HIJO 1 E HIJO 2 NO SON IGUALES A CERO
                    elif hijo2 == 0:
                        print("entro3")
                        hijo2 = i
                        dot.node(str(i), token)
                        i = create_hijo(i, 0)
                        break
                #REVISAR EL DESMADER CON EL DEBUGGER
                else:
                    if hijo1 == 0:
                        print("entro4")
                        dot.node(str(i), token)
                        hijo1 = i
                        tokens.pop()
                        i +=1
                    elif hijo2 == 0:
                        print("entro5")
                        dot.node(str(i), token)
                        hijo2 = i
                        i +=1
                        if len(tokens) > 1:
                            print("entro6")
                            tokens.pop()
                            break
                                                        
                        else:
                            print("entro7")
                            tokens.pop()      
                    # else:
                    #     print("entro6")
                    #     dot.edge(str(padre), str(hijo1))
                    #     dot.edge(str(padre), str(hijo2))                        
                    #     padre = hijo2
                    #     hijo1 = 0
                    #     hijo2 = 0
            dot.edge(str(padre), str(hijo2), rankdir="RL")
            dot.edge(str(padre), str(hijo1), rankdir="RL")                                   
            return i
        create_hijo(i, 0)

        print(dot.source)
        dot.format = "png"
        dot.render('graficas/arbol.gv', view=False)      