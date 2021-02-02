from graphviz import Digraph

class Nodo(object):

    def __init__(self, ident, valor):
        self.ident = ident
        self.valor = valor
        self.isPadre = False

class Padre(Nodo):

    def __init__(self, ident, valor):

        Nodo.__init__(self, ident, valor)
        self.hijo1 = 0
        self.hijo2 = 0
        self.isPadre = True


    def tiene_hijo1(self):
        return self.hijo1 == 0

    def tiene_hijo2(self):
        return self.hijo2 == 0 

class Tree_maker(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.prefijo_stack = []
        self.ident = 1
        self.tree_stack = {}
        self.padre = 0
        self.padres = []
        self.hijos = []
        self.incompletos = []

    def create_hijo(self, ident, valor):
        self.ident += 1
        return Nodo(ident, valor)

    def create_padre(self, ident, valor):
        self.ident += 1
        return Padre(ident, valor)

    def create_tree(self):        
        while len(self.tokens) > 0:
            token = self.tokens.pop()                        
            if token == "+" or token == "-" or token == "*" or token == "/":
                if self.padre == 0:
                    self.padre = self.create_padre(self.ident, token)                    
                    self.padres.append(self.padre.ident)                    
                else:                        
                    if self.padre.hijo1 != 0:
                        hijo_padre = self.create_padre(self.ident, token)
                        self.padres.append(hijo_padre.ident)
                        self.padre.hijo2 = hijo_padre.ident
                        self.tree_stack[hijo_padre.ident] = hijo_padre
                        self.tree_stack[self.padre.ident] = self.padre
                        self.padre = hijo_padre                                            
                    else:
                        hijo_padre = self.create_padre(self.ident, token)
                        self.padres.append(hijo_padre.ident)
                        self.padre.hijo1 = hijo_padre.ident
                        self.incompletos.append(self.padre)
                        self.padre = hijo_padre                        
            elif self.padre != 0:
                if self.padre.hijo1 != 0:
                    hijo = self.create_hijo(self.ident, token)
                    self.hijos.append(hijo.ident)
                    self.padre.hijo2 = hijo.ident
                    self.tree_stack[hijo.ident] = hijo
                    self.tree_stack[self.padre.ident] = self.padre
                    if len(self.incompletos) == 0:
                        self.padre = 0
                    else:
                        self.padre = self.incompletos.pop()
                
                else:                    
                    hijo = self.create_hijo(self.ident, token)
                    self.hijos.append(hijo.ident)
                    self.padre.hijo1 = hijo.ident
                    self.tree_stack[hijo.ident] = hijo
                
        dot = Digraph(comment='Arbol de expresion')
        for node_ident in self.padres:
            self.padre = self.tree_stack[node_ident]
            hijo1 = self.tree_stack[self.padre.hijo1]
            hijo2 = self.tree_stack[self.padre.hijo2]
            dot.node(str(self.padre.ident), self.padre.valor)
            dot.node(str(hijo2.ident), hijo2.valor)
            dot.node(str(hijo1.ident), hijo1.valor)            
            dot.edge(str(self.padre.ident), str(hijo1.ident), rankdir="LR")
            dot.edge(str(self.padre.ident), str(hijo2.ident), rankdir="LR")            
        
        print(dot.source)
        dot.format = "png"
        dot.render('graficas/arbol.gv', view=False)

        print(self.add_hijos(self.tree_stack[self.padres[0]]))

    def ajuste_negativos(self, tok):
        copia = tok
        ajustado = []
        while len(copia) > 0:                
            actual = copia.pop(0)
            if actual == "-":
                if len(ajustado) == 0:
                    ajustado.append(0)
                    ajustado.append("-")
                elif ajustado[-1] == "+" or ajustado[-1] == "-" or ajustado[-1] == "*" or ajustado[-1] == "/":
                    ajustado.append(0)
                    ajustado.append("-")
                elif (ajustado[-1] == "+" or ajustado[-1] == "-" or ajustado[-1] == "*" or ajustado[-1] == "/") and copia[0] == "(":
                    ajustado.append(0)
                    ajustado.append("-")
            else:
                ajustado.append(actual)
        return ajustado
    
    def add_hijos(self, padre):
        self.prefijo_stack.append(padre.valor)
        if self.tree_stack[padre.hijo2].isPadre == True:
            self.add_hijos(self.tree_stack[padre.hijo2])
        else:
            self.prefijo_stack.append(self.tree_stack[padre.hijo2].valor)
        if self.tree_stack[padre.hijo1].isPadre == True:
            self.add_hijos(self.tree_stack[padre.hijo1])
        else:
            self.prefijo_stack.append(self.tree_stack[padre.hijo1].valor)
        return self.prefijo_stack
        