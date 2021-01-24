from tkinter import *
from proyecto_automatas import *

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title("Calculadora")

        #_______EXPRESIONES________
        #Agregar una caja de texto para que sea la pantalla de la calculadora
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

        #Crear los botones de la calculadora
        boton1=self.crearBoton("analizar")
        boton1.grid(row=6, column=0, columnspan=4, padx=5, pady=5)
        

        # #Ubicar los botones con el gestor grid
        # botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        # contador=0
        # for fila in range(1,5):
        #     for columna in range(4):
        #         botones[contador].grid(row=fila,column=columna)
        #         contador+=1
        # #Ubicar el último botón al final
        # botones[16].grid(row=5,column=0,columnspan=4)

        # return


    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15),command=self.analize)

    def analize(self):  
        ejemplo = self.textAsignacion.get(1.0, "end-1c")
        tokens = tokenizer(ejemplo)
        self.tokens.config(state=NORMAL)
        for token in tokens:
            self.tokens.insert(INSERT, token)
            self.tokens.insert(INSERT, "\n")
        self.tokens.config(state=DISABLED)


        self.pantalla.config(state=NORMAL)
        self.pantalla.delete('1.0', END)
        expresion_separada = ejemplo.split("\n")
        for exp in expresion_separada:    
            list_tokens = tokenizer(exp)    
            mini_parser(list_tokens)

        for simbol in SymbolTable.symbols:
            self.pantalla.insert(INSERT, "%s = %i" % (simbol, SymbolTable.symbols[simbol] ))
            self.pantalla.insert(INSERT, "\n")                    

        self.pantalla.config(state=DISABLED)
        self.textAsignacion.delete('1.0', END)

    # #Controla el evento disparado al hacer click en un botón
    # def click(self, texto, escribir):
    #     #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
    #     if not escribir:
    #         #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
    #         if texto=="=" and self.operacion!="":
    #             #Reemplazar el valor unicode de la división por el operador división de Python '/'
    #             self.operacion=re.sub(u"\u00F7", "/", self.operacion)
    #             resultado=str(eval(self.operacion))
    #             self.operacion=""
    #             self.limpiarPantalla()
    #             self.mostrarEnPantalla(resultado)
    #         #Si se presionó el botón de borrado, limpiar la pantalla
    #         elif texto==u"\u232B":
    #             self.operacion=""
    #             self.limpiarPantalla()
    #     #Mostrar texto
    #     else:
    #         self.operacion+=str(texto)
    #         self.mostrarEnPantalla(texto)
    #     return


    # #Borra el contenido de la pantalla de la calculadora
    # def limpiarPantalla(self):
    #     self.pantalla.configure(state="normal")
    #     self.pantalla.delete("1.0", END)
    #     self.pantalla.configure(state="disabled")
    #     return


    # #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    # def mostrarEnPantalla(self, valor):
    #     self.pantalla.configure(state="normal")
    #     self.pantalla.insert(END, valor)
    #     self.pantalla.configure(state="disabled")
    #     return


ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()