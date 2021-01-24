#_____TOKENIZER______

import re

def tokenizer(string: str):
    token_rexes = [
        (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "iden"), # variables
        (re.compile(r"^[0-9]+"), "num"), # integers
        (re.compile(r"^[+*/-]"), "op"), # operators
        (re.compile(r"^[()]"), "paran"), # parantehses
        (re.compile(r"^="), "ass"), # assignment
    ]

    tokens = []

    while len(string):
        string = string.lstrip()

        matched = False

        for token_rex, token_type in token_rexes:
            mo = token_rex.match(string)
            if mo:
                matched = True
                token = (mo.group(0), token_type)
                tokens.append(token)
                string  = token_rex.sub('', string)
                string = string.lstrip()
                break # break out of the inner loop

        if not matched:
            raise Exception("Invalid String")

    return tokens

#_____TABLA DE SIMBOLOS_______

class SymbolTable:
    symbols = dict()

    @staticmethod
    def add_symbol(name, value):

        for key in SymbolTable.symbols:
            if key == name:
                SymbolTable.symbols[key] = value
                return

        SymbolTable.symbols[name] = value


    @staticmethod
    def find_symbol(name):
        for key in SymbolTable.symbols:
            if key == name:
                return SymbolTable.symbols[key]

        raise Exception("Symbol not defined")

#_____PARSER______

precedence = {
    "-": 1,
    "+": 2,
    "*": 3,
    "/": 4,
}

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

operator_mapping = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def parse_expr(tokens: list):
    # Shunting Yard Algorithm

    operator_stack = []
    expression_stack = []

    tokens.append( (')', "paran") )

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token[0] == "(":
            value, tokens = parse_expr(tokens[i+1:])
            i = -1

            expression_stack.append(value)

        elif token[1] == "num":
            expression_stack.append(float(token[0]))

        elif token[1] == "iden":
            value = SymbolTable.find_symbol(token[0])
            expression_stack.append(float(value))

        elif token[1] == "op":
            # Shunting yard
            while len(operator_stack) and precedence[token[0]] < precedence[operator_stack[-1]]:
                operator = operator_stack.pop()
                operand_2 = expression_stack.pop()
                operand_1 = expression_stack.pop()

                value = operator_mapping[operator] (operand_1, operand_2)
                expression_stack.append(value)

            operator_stack.append(token[0])

        elif token[0] == ")":
            while len(operator_stack):
                operator = operator_stack.pop()
                operand_2 = expression_stack.pop()
                operand_1 = expression_stack.pop()

                value = operator_mapping[operator] (operand_1, operand_2)
                expression_stack.append(value)

            return expression_stack[-1], tokens[i+1:-1]

        i += 1




def parse_ass(tokens: list):
    name = tokens[0][0]
    value = tokens[2:]
    value, tokens = parse_expr(value)

    SymbolTable.add_symbol(name, value)


def mini_parser(tokens: list):
    # assignment statement
    if tokens[1][0] == "=":
        parse_ass(tokens)
    else: # expressions
        return parse_expr(tokens)[0]  