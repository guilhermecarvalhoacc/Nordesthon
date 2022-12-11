import sys

TT_INT		= 'INT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MULT     = 'MULT'
TT_DIV      = 'DIV'
TT_OP       = 'OP'
TT_CP       = 'CP'
TT_OC       = 'OC'
TT_CC       = 'CC'
TT_EQUAL    = "EQUAL"
TT_VAR      = "IDENTIFIER"
TT_PV       = "PV"
TT_EE       = "EE"
TT_GT       = "GT"
TT_LT       = "LT"
TT_AND      = "and"
TT_OR       = "or"
TT_NOT      = "not"
TT_DOT      = "dot"
TT_STR      = "String"
TT_VIR      = "virgula"
TT_DP       = 'DP'
TT_ARROW    = 'ARROW'
TT_EOF      = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

class Tokenizer:
    def __init__(self,source):
        self.source = source
        self.position = 0
        self.next = None
    
    def selectNext(self):
        lista_Reservadas = ["Amostre","DigaAi","Sose","SeNumFor","ArrochaAté","var","inteiro","String","fn","retorne","main"]
        while self.position < len(self.source) and self.source[self.position] == " ":
            self.position += 1

        if  self.position >= len(self.source):
            self.next = Token(TT_EOF,None)
        else:
            source = self.source
            caracter = source[self.position]

            if caracter.isalpha():
                variavel = self.make_identifier()
                if variavel in lista_Reservadas:
                    self.next = Token(variavel,variavel)
                else:
                    self.next = Token(TT_VAR,variavel)
                return self.next

            if caracter.isdigit():
                if source[self.position + 1].isalpha():
                    raise Exception("variavel invalida")
                else:
                    num = self.make_number()
                    self.next = Token(TT_INT,num)
                    return self.next

            elif caracter == "+":
                self.next = Token(TT_PLUS,None)
                self.position += 1
                return self.next

            elif caracter == "*":
                self.next = Token(TT_MULT,None)
                self.position += 1
                return self.next
            
            elif caracter == "/":
                self.next = Token(TT_DIV,None)
                self.position += 1
                return self.next

            elif caracter == "(":
                self.next = Token(TT_OP,None)
                self.position += 1
                return self.next

            elif caracter == ")":
                self.next = Token(TT_CP,None)
                self.position += 1
                return self.next
            elif caracter == "{":
                self.next = Token(TT_OC,None)
                self.position += 1
                return self.next

            elif caracter == "}":
                self.next = Token(TT_CC,None)
                self.position += 1
                return self.next

            elif caracter == ";":
                self.next = Token(TT_PV,None)
                self.position += 1
                return self.next

            elif caracter == "=":
                if source[self.position + 1] == "=":
                    self.next = Token(TT_EE,None)
                    self.position += 2
                else:
                    self.next = Token(TT_EQUAL,None)
                    self.position += 1
                return self.next


            elif caracter == "-":
                if source[self.position + 1] == ">":
                    self.next = Token(TT_ARROW,None)
                    self.position += 2
                else:
                    self.next = Token(TT_MINUS,None)
                    self.position += 1
                return self.next

            elif caracter == ">":
                self.next = Token(TT_GT,None)
                self.position += 1
                return self.next

            elif caracter == "<":
                self.next = Token(TT_LT,None)
                self.position += 1
                return self.next
            elif caracter == "&" and source[self.position + 1] == "&":
                self.next = Token(TT_AND,None)
                self.position += 2
                return self.next
            elif caracter == "|" and source[self.position + 1] == "|":
                self.next = Token(TT_OR,None)
                self.position += 2
                return self.next

            elif caracter == "!":
                self.next = Token(TT_NOT,None)
                self.position += 1
                return self.next

            elif caracter == ":":
                self.next = Token(TT_DP,None)
                self.position += 1
                return self.next

            elif caracter == ".":
                self.next = Token(TT_DOT,None)
                self.position += 1
                return self.next

            elif caracter == ",":
                self.next = Token(TT_VIR,None)
                self.position += 1
                return self.next

            elif caracter == '"':
                self.position += 1
                palavra = ""
                while (self.source[self.position] != '"'):
                    palavra += self.source[self.position]
                    self.position +=1 
                    if (self.position >= len(self.source)):
                        raise Exception("não fechou aspas")
                self.position += 1 
                self.next = Token(TT_STR,palavra)
                return self.next
            else:
                raise Exception("Invalido")

    def make_number(self):
        source = self.source
        num_str = ''
        while source[self.position] != None and source[self.position].isdigit():
            num_str += source[self.position]

            if (self.position == len(source) - 1):
                self.position += 1
                break

            self.position += 1


        return int(num_str)

    def make_identifier(self):
        source = self.source
        variavel = ''
        while source[self.position] != None and (source[self.position].isalpha() or source[self.position].isdigit() or source[self.position] == "_"):
            variavel += source[self.position]
            if (self.position == len(source) - 1):
                self.position += 1
                break

            self.position += 1

        return variavel


class Node:
    def __init__(self,value,children):
        self.value = value
        self.children = children

    def Evaluate(self,symbol_table):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
        self.value = value
        self.children = children

    def Evaluate(self,symbol_table):
        filho_esquerda = self.children[0].Evaluate(symbol_table)[0]
        filho_direita = self.children[1].Evaluate(symbol_table)[0]
        tipo_filho_esquerda = self.children[0].Evaluate(symbol_table)[1]
        tipo_filho_direita = self.children[1].Evaluate(symbol_table)[1]

        if self.value in ["+", "-", "*", "/", "||", "&&"] and (tipo_filho_esquerda != "inteiro" or tipo_filho_direita != "inteiro"):
            raise ValueError("Erro de conta")

        if self.value == "+":
            return ((filho_esquerda + filho_direita), "inteiro")
        elif self.value == "-":
            return ((filho_esquerda - filho_direita),"inteiro")
        elif self.value == "*":
            return ((filho_esquerda * filho_direita),"inteiro")
        elif self.value == "/":
            return ((filho_esquerda // filho_direita), "inteiro")
        elif self.value == "==":
            return ((int(filho_esquerda == filho_direita)), "inteiro")
        elif self.value == "&&":
            return ((int(filho_esquerda and filho_direita)), "inteiro")
        elif self.value == "||":
            return ((int(filho_esquerda or filho_direita)), "inteiro")
        elif self.value == ">":
            return ((int(filho_esquerda > filho_direita)), "inteiro")
        elif self.value == "<":
            return ((int(filho_esquerda < filho_direita)), "inteiro")
        elif self.value == ".":
            return ((str(self.children[0].Evaluate(symbol_table)[0]) + str(self.children[1].Evaluate(symbol_table)[0])), "String")

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        if self.value == "+":
            return (self.children[0].Evaluate(symbol_table)[0], "inteiro")
        elif self.value == "-":
            return (-self.children[0].Evaluate(symbol_table)[0], "inteiro")
        elif self.value == "!":
            return (not(self.children[0].Evaluate(symbol_table)[0]), "inteiro")


class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        return (self.value,"inteiro")

class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self,symbol_table):
        pass



class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self, symbol_table):
        for child in self.children:
            if child.__class__.__name__ == "ReturnNode":
                return child.Evaluate(symbol_table)
            child.Evaluate(symbol_table)

class EqualNode(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        symbol_table.set(self.children[0].value,self.children[1].Evaluate(symbol_table))

class IdentifierNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self, symbol_table):
        if self.value == "variable":
            return symbol_table.get(self.children[0])

        return FuncTable.get(self.children[0])

class PrintNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self, symbol_table):
        print(self.children[0].Evaluate(symbol_table)[0])

class SymbolTable:
    def __init__(self):
        self.table = {}

    def create(self, identifier: IdentifierNode, type):
        if identifier in self.table.keys():
            raise Exception("ja declarada")
        if type == "inteiro":
            self.table[identifier] = (0, type)
        elif type == "String":
            self.table[identifier] = ("", type)

    def get(self,identifier):
        if identifier in self.table:
            return self.table[identifier]
        else:
            raise Exception("variable not found")

    def set(self,identifier,value):
        if identifier not in self.table.keys():
            raise ValueError("Variavel ainda nao foi decalrada")

        if identifier in self.table:
            if self.table[identifier][1] == value[1]:
                self.table[identifier] = value
            else:
                raise Exception("erro de tipo")

class WhileNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        while(self.children[0].Evaluate(symbol_table)[0]):
            self.children[1].Evaluate(symbol_table)

class IfNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        if (self.children[0].Evaluate(symbol_table) == True):
            self.children[1].Evaluate(symbol_table)
        elif (len(self.children)) > 2:
            self.children[2].Evaluate(symbol_table)

class ReadNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        return (int(input()),"inteiro")


class VarDecNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        for child in self.children:
            symbol_table.create(child, self.value)

class StringNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        return (self.value,TT_STR)

class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def Evaluate(self, symbol_table):
        FuncTable.create(self.children[0].children[0], self, self.value)

class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def Evaluate(self, symbol_table):
        argumentos = []
        new_func, type_func = FuncTable.get(self.value)
        new_ST = SymbolTable()
        for i in range(1, len(new_func.children) - 1):
            argumentos.append(new_func.children[i].children[0])
            new_func.children[i].Evaluate(new_ST)
        if len(argumentos) != len(self.children):
            raise ValueError("Invalid number of argumentos")
        for i in range(len(argumentos)):
            new_ST.set(argumentos[i], self.children[i].Evaluate(symbol_table))
        ret = new_func.children[-1].Evaluate(new_ST)
        if type_func not in ["MAIN", "VOID"]:
            if type_func != ret[1]:
                raise ValueError(
                    f"Cannot return {ret[1]} from function expecting {type_func}"
                )
        return ret

class ReturnNode(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self, symbol_table):
        return self.children[0].Evaluate(symbol_table)


class FuncTable:
    table = {}
    def create(Identifier, pointer, type):
        if Identifier in FuncTable.table.keys():
            raise ValueError(f"Function already declared")
        FuncTable.table[Identifier] = (pointer, type)
    def get(identifier):
        if identifier in FuncTable.table:
            return FuncTable.table[identifier]
        else:
            raise Exception("variable not found")



class Parser():
    tokenizer = None


    @staticmethod
    def parseProgram():
        nodes = []
        while Parser.tokenizer.next.type != "EOF":
            node = Parser.parseDeclaration()
            nodes.append(node)
        Parser.tokenizer.selectNext()
        nodes.append(FuncCall("Main", []))
        return Block("Program", nodes)

    @staticmethod
    def parseDeclaration():
        if Parser.tokenizer.next.type == "fn":
            Parser.tokenizer.selectNext()
            function_identifier = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "OP":
                raise ValueError("Expected '(' after function identifier")
            Parser.tokenizer.selectNext()
            arguments: list[FuncDec] = []
            var_identifiers: list[str] = []
            while Parser.tokenizer.next.type != "CP":
                if var_identifiers == []:
                    if Parser.tokenizer.next.type != "IDENTIFIER":
                        raise ValueError("esperador identifier")
                    var_identifier = Parser.tokenizer.next.value
                    var_identifiers = [var_identifier]
                    Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "virgula":
                    while Parser.tokenizer.next.type == "virgula":
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type != "IDENTIFIER":
                            raise ValueError("Esperado identifier depois de ','")
                        var_identifiers.append(Parser.tokenizer.next.value)
                        Parser.tokenizer.selectNext()
                elif Parser.tokenizer.next.type == "DP":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type not in ["String", "inteiro"]:
                        raise ValueError("Erro de tipo de variavel")
                    var_type = Parser.tokenizer.next.value
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "virgula":
                        Parser.tokenizer.selectNext()
                    arguments.append(VarDecNode(var_type, var_identifiers))
                    var_identifiers = []
            Parser.tokenizer.selectNext()
            function_type = "VOID" if function_identifier != "Main" else "MAIN"
            if Parser.tokenizer.next.type == "ARROW":
                Parser.tokenizer.selectNext()
                function_type = Parser.tokenizer.next.value
                if function_type not in ["inteiro", "String"]:
                    raise ValueError("Erro de tipo apos seta")
                Parser.tokenizer.selectNext()
            children = [IdentifierNode("function", [function_identifier])]
            for argument in arguments:
                children.append(argument)
            children.append(Parser.parseBlock())
            return FuncDec(function_type, children)
        else:
            raise ValueError("Invalid declaration")
    @ staticmethod
    def parseRelExpression():
        resultado_exp = Parser.parseExpression()
        while (Parser.tokenizer.next.type == "EE" or Parser.tokenizer.next.type == "GT" or Parser.tokenizer.next.type == "LT" or Parser.tokenizer.next.type == "dot"):
            tipo = Parser.tokenizer.next.type
            if tipo == "EE":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp("==",[resultado_exp,Parser.parseExpression()])
            elif tipo == "GT":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp(">",[resultado_exp,Parser.parseExpression()])
            elif tipo == "LT":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp("<",[resultado_exp,Parser.parseExpression()])
            elif tipo == "dot":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp(".",[resultado_exp,Parser.parseExpression()])
        return resultado_exp

    @ staticmethod
    def parseExpression():
        resultado_Term = Parser.parseTerm()
        while (Parser.tokenizer.next.type == "MINUS" or Parser.tokenizer.next.type == "PLUS" or Parser.tokenizer.next.type == "or"):
            tipo = Parser.tokenizer.next.type
            if tipo == "MINUS":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("-",[resultado_Term,Parser.parseTerm()])
            elif tipo == "PLUS":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("+",[resultado_Term,Parser.parseTerm()])
            elif tipo == "or":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("||",[resultado_Term,Parser.parseTerm()])
        return resultado_Term


    @ staticmethod
    def parseTerm():

        resultado_factor = Parser.parseFactor()
        while (Parser.tokenizer.next.type == "DIV" or Parser.tokenizer.next.type == "MULT" or Parser.tokenizer.next.type == "and"):
            tipo = Parser.tokenizer.next.type
            if tipo == "MULT":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("*",[resultado_factor,Parser.parseFactor()])
            elif tipo == "DIV":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("/",[resultado_factor,Parser.parseFactor()])
            elif tipo == "and":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("&&",[resultado_factor,Parser.parseFactor()])
        return resultado_factor

    @ staticmethod
    def parseFactor():
        if Parser.tokenizer.next.type == "INT":
            reul_op = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            return IntVal(reul_op,[])
        if Parser.tokenizer.next.type == "String":
            node_str = StringNode(Parser.tokenizer.next.value, TT_STR)
            Parser.tokenizer.selectNext()
            return node_str

        elif Parser.tokenizer.next.type == "IDENTIFIER":
            id_token = Parser.tokenizer.next.value
            identifier = IdentifierNode("variable", [Parser.tokenizer.next.value])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                argumentos = []
                while Parser.tokenizer.next.type != "CP":
                    argumentos.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type == "virgula":
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                return FuncCall(id_token, argumentos)
            return identifier


        if Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.selectNext()
            return UnOp("+",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.selectNext()
            return UnOp("-",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "not":
            Parser.tokenizer.selectNext()
            return UnOp("!",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "OP":
            Parser.tokenizer.selectNext()
            reul_op = Parser.parseRelExpression()
            if Parser.tokenizer.next.type == "CP":
                Parser.tokenizer.selectNext()
                return reul_op
            else:
                raise Exception("Não fechou parenteses")

        if Parser.tokenizer.next.type == "DigaAi":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()    
                    return ReadNode([],[])  
        else:
            raise Exception("Invalido")

    @ staticmethod
    def parseBlock():
        if Parser.tokenizer.next.type == "OC":
            Parser.tokenizer.selectNext()
        else:
            raise("não começa com chaves")
        node = Block("",[])
        while (Parser.tokenizer.next.type != "CC"):
            child = Parser.parseStatement()
            if child != None:
                node.children.append(child)
        Parser.tokenizer.selectNext()
        return node

    @ staticmethod
    def parseStatement():
        if Parser.tokenizer.next.type == "PV":
            Parser.tokenizer.selectNext()
            return NoOp("","")
        if Parser.tokenizer.next.type == "IDENTIFIER":
            Id_token = Parser.tokenizer.next.value
            node_identifier = IdentifierNode(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                Parser.tokenizer.selectNext()
                node_equal = EqualNode("",[node_identifier,Parser.parseRelExpression()])
                if Parser.tokenizer.next.type == "PV":
                    Parser.tokenizer.selectNext() 
                    return node_equal
                else:
                    raise Exception("Não terminou com Ponto e Virgula")
            elif Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                arguments = []
                while Parser.tokenizer.next.type != "CP":
                    arguments.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type == "virgula":
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "PV":
                    Parser.tokenizer.selectNext() 
                    return FuncCall(Id_token, arguments)
                
        
        elif Parser.tokenizer.next.type == "Amostre":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                node_print = PrintNode("Amostre",[Parser.parseRelExpression()])
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "PV":
                        Parser.tokenizer.selectNext()
                        return node_print
                    else:
                        raise Exception("Não terminou com Ponto e Virgula")
                else:
                    raise Exception("Não fechou parenteses")
            else:
                raise Exception("Não abriu parenteses")
            
        elif Parser.tokenizer.next.type == "var":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "IDENTIFIER":
                lista_nodes = []
                ident_nod = IdentifierNode(Parser.tokenizer.next.value, [])
                lista_nodes.append(Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                while Parser.tokenizer.next.type == "virgula":
                    Parser.tokenizer.selectNext()
                    ident_nod2 = IdentifierNode(Parser.tokenizer.next.value, [])
                    lista_nodes.append(Parser.tokenizer.next.value)
                    Parser.tokenizer.selectNext()
                    
                if Parser.tokenizer.next.type == "DP":
                    Parser.tokenizer.selectNext()
                    node_var = VarDecNode(Parser.tokenizer.next.type,lista_nodes)
                    if Parser.tokenizer.next.type in ["inteiro", "String"]:
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == "PV":
                            Parser.tokenizer.selectNext()
                            return node_var
                        else:
                            raise Exception("Não terminou com Ponto e Virgula")
                    else:
                        raise Exception("declaracao invalida")


        elif Parser.tokenizer.next.type == "retorne":
            Parser.tokenizer.selectNext()
            return ReturnNode("retorne", [Parser.parseRelExpression()])


        elif Parser.tokenizer.next.type == "ArrochaAté":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                resul_relexp = Parser.parseRelExpression()
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()
                    resulStat = Parser.parseStatement()
                    node_while = WhileNode("ArrochaAté",[resul_relexp,resulStat])
                    return node_while
                else:
                    raise Exception("Não fechou parenteses do while")

        elif Parser.tokenizer.next.type == "Sose":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                resul_relexp = Parser.parseRelExpression()
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()
                    resulStat = Parser.parseStatement()
                    if Parser.tokenizer.next.type == "SeNumFor":
                        Parser.tokenizer.selectNext()
                        resulstat2 = Parser.parseStatement()
                        node_if = IfNode("Sose",[resul_relexp,resulStat,resulstat2])
                        return node_if
                    node_if = IfNode("Sose",[resul_relexp,resulStat])
                    return node_if
                else:
                    raise Exception("não fechou parenteses do if")

        else:
            return Parser.parseBlock()

    @ staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()
        symboltable = SymbolTable()
        resultado_final = Parser.parseProgram()
        if Parser.tokenizer.next.type != "EOF":
            raise Exception("não consumiu até o fim")
        resultado_final.Evaluate(symboltable)

class PrePro():
    @ staticmethod
    def filter(source):
        source = source.split("\n")
        for i in range(len(source)):
            if "//" in source[i]:
                source[i] = source[i].partition("//")[0]
        source = "".join(source)
        return source

def main(argv):
    file_name = argv[1]
    # file_name = "input.carbon"
    with open(file_name, "r") as file:
        source = file.read()
        prepro = PrePro()
        param = prepro.filter(source)
        Parser.run(param)
        # if param[-1] != "}":
        #     raise Exception("não fecha parenteses")
        # parser = Parser()
        # resultado_main = parser.run(param)
        # resultado_main.Evaluate()

if __name__ == '__main__':
    main(sys.argv)