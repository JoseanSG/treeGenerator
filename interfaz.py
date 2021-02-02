from tkinter import *
from proyecto_automatas import *
from tree_generator import *
from tree import *
from PIL import ImageTk,Image

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Expresiones")

        #_______EXPRESIONES________
        #Agregar una caja de texto 
        self.textAsignacion=Text(self.ventana, state="normal", width=20, height=20, font=("Helvetica",15))
        #Label de asignaciones
        self.labelExp = Label(text = "Expresiones", font = ("Helvetica",15))

        #Ubicar el label
        self.labelExp.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        #Ubicar la textAsignacion en la ventana
        self.textAsignacion.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        #_______TOKENS_________
        #Agregar una caja de texto para que sea donde se muestre la tabla de simbolos
        self.tokens=Text(self.ventana, state="disabled", width=20, height=20, font=("Helvetica",15))
        #Label de Simbolos
        self.labelTokens = Label(text = "tabla de tokens", font = ("Helvetica",15))

        #Ubicar el label
        self.labelTokens.grid(row=0, column=4, columnspan=4, padx=5, pady=5)
        #Ubicar la tokens en la ventana
        self.tokens.grid(row=1, column=4, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

        #_______TABLA DE SIMBOLOS________
        #Agregar una caja de texto para que sea donde se muestre la tabla de simbolos
        self.pantalla=Text(self.ventana, state="disabled", width=20, height=20, font=("Helvetica",15))
        #Label de Simbolos
        self.labelTabSimb = Label(text = "tabla de simbolos", font = ("Helvetica",15))

        #Ubicar el label
        self.labelTabSimb.grid(row=0, column=8, columnspan=4, padx=5, pady=5)
        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=1, column=8, columnspan=4, padx=5, pady=5)

        #_______CUADRO DE IMAGEN PARA EL ARBOL_________
        #creamos el cuadro de imagen
        self.canvas = Canvas(self.ventana, width = 500, height = 500) 
        self.img = ImageTk.PhotoImage(Image.open("graficas/nada.png"))  
        self.canvas.create_image(50, 50, anchor=NW, image=self.img)
        #agregamos la etiqueta
        self.labelArbol = Label(text = "Arbol de expresion", font = ("Helvetica",15))
        self.labelArbol.grid(row=0, column=16, columnspan=4, padx=5, pady=5)


        self.canvas.grid(row=1, column=16, columnspan=4, padx=5, pady=5)
        #Crear boton de analizar
        botonAnalizar=Button(self.ventana, text="analizar", width=9, height=1, font=("Helvetica",15),command=self.analize)
        botonAnalizar.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

        #Crear boton de analizar
        botonArbol=Button(self.ventana, text="Generar Arbol", width=15, height=1, font=("Helvetica",15),command=self.generateTree)
        botonArbol.grid(row=6, column=4, columnspan=4, padx=5, pady=5)

        #crear boton de limpiar
        botonArbol=Button(self.ventana, text="Limpiar", width=15, height=1, font=("Helvetica",15),command=self.cleanAll)
        botonArbol.grid(row=6, column=8, columnspan=4, padx=5, pady=5)


    def analize(self):  
        expresion = self.textAsignacion.get(1.0, "end-1c")
        tokens = tokenizer(expresion)
        self.tokens.config(state=NORMAL)
        for token in tokens:
            self.tokens.insert(INSERT, token)
            self.tokens.insert(INSERT, "\n")
        self.tokens.config(state=DISABLED)


        self.pantalla.config(state=NORMAL)
        self.pantalla.delete('1.0', END)
        expresion_separada = expresion.split("\n")
        for exp in expresion_separada:    
            list_tokens = tokenizer(exp)    
            mini_parser(list_tokens)

        for simbol in SymbolTable.symbols:
            self.pantalla.insert(INSERT, "%s = %i" % (simbol, SymbolTable.symbols[simbol] ))
            self.pantalla.insert(INSERT, "\n")                    

        self.pantalla.config(state=DISABLED)
        self.textAsignacion.delete('1.0', END)

    def generateTree(self):
        expresion = self.textAsignacion.get(1.0, "end-1c")
        tokens = tokenizer(expresion)
        print(tokens)
        # create_tree(tokens)
        tree_tokens = postfix(tokens)
        tree_tokens_fixed = []
        for tok in tree_tokens:
            if tok != "(" and tok != ")":
                tree_tokens_fixed.append(tok)
        #print(tree_tokens_fixed)
        #Tree.create_tree(tree_tokens_fixed)
        treeMaker = Tree_maker(tree_tokens_fixed)
        #print(treeMaker.ajuste_negativos(tree_tokens_fixed))
        treeMaker.create_tree()
        self.img = ImageTk.PhotoImage(Image.open("graficas/arbol.gv.png"))  
        self.canvas.create_image(50, 50, anchor=NW, image=self.img)

    def cleanAll(self):
        #limpiamos escritura
        self.textAsignacion.delete('1.0', END)
        #limpiamos tabla de simbolos
        self.pantalla.config(state=NORMAL)
        self.pantalla.delete('1.0', END)
        self.pantalla.config(state=DISABLED)
        #limpiamos tabla de tokens
        self.tokens.config(state=NORMAL)
        self.tokens.delete('1.0', END)
        self.tokens.config(state=DISABLED)
        #limpiamos el diccionario de simbolos
        SymbolTable.symbols = dict()
        #limpiamos el arbol
        self.img = ImageTk.PhotoImage(Image.open("graficas/nada.png"))  
        self.canvas.create_image(50, 50, anchor=NW, image=self.img)

ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()