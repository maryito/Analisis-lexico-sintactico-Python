import ply.lex as lex
import os
import token_Roles as tkRoles

class Compilador(object):
    """ Compilador """
    tokens = tkRoles.getTokens()

# Reglas de Expresiones Regualres para token de Contexto simple

    t_SUMA = r'\+'
    t_RESTA = r'-'
    t_MINUSMINUS = r'\-\-'
    t_PUNTO = r'\.'
    t_MULT = r'\*'
    t_DIV = r'/'
    t_ASIGNAR = r'='
    t_MENORQUE = r'<'
    t_MAYORQUE = r'>'
    t_PUNTOCOMA = ';'
    t_COMA = r','
    t_PARIZQ = r'\('
    t_PARDER = r'\)'
    t_CORIZQ = r'\['
    t_CORDER = r'\]'
    t_LLAIZQ = r'{'
    t_LLADER = r'}'
    t_COMDOB = r'\"'
 

    def t_INCLUDE(self,t):
        r'include'
        return t

    def t_USING(self,t):
        r'using'
        return t

    def t_NAMESPACE(self,t):
        r'namespace'
        return t

    def t_STD(self,t):
        r'std'
        return t

    def t_COUT(self,t):
        r'cout'
        return t

    def t_CIN(self,t):
        r'cin'
        return t

    def t_GET(self,t):
        r'get'
        return t

    def t_ENDL(self,t):
        r'endl'
        return t

    def t_SINO(self,t):
        r'else'
        return t

    def t_SI(self,t):
        r'if'
        return t

    def t_RETURN(self,t):
        r'return'
        return t

    def t_VOID(self,t):
        r'void'
        return t

    def t_MIENTRAS(self,t):
        r'while'
        return t

    def t_PARA(self,t):
        r'for'
        return t

    def t_ENTERO(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

#exprecion regular para reconocer los identificadores

    def t_IDENTIFICADOR(self,t):
        r'\w+(_\d\w)*'
        return t

    def t_CADENA(self,t):
    #expresion RE para reconocer los String
        r'\"?(\w+ \ *\w*\d* \ *)\"?'
        return t

    def t_NUMERAL(self,t):
        r'\#'
        return t

    def t_PLUSPLUS(self,t):
        r'\+\+'
        return t

    def t_MENORIGUAL(self,t):
        r'<='
        return t

    def t_MAYORIGUAL(self,t):
        r'>='
        return t

    def t_IGUAL(self,t):
        r'=='
        return t

    def t_LGREATER(self,t):
        r'<<'
        return t

    def t_RGREATER(self,t):
        r'>>'
        return t

    def t_DISTINTO(self,t):
        r'!='
        return t

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_comments(self,t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    def t_comments_C99(self,t):
        r'//(.)*?\n'
        t.lexer.lineno += 1

############################################################################################

    def t_error(self,t):
        print(" No es valido el caracter '%s'"%t.value[0])
        t.lexer.skip(1)

    #Constructor del analizar lexico
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    #Prueba de ingreso
    def prueba(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break;
            print(tok)

if __name__ == '__main__':
    m = Compilador()
    m.build()
    while True:
        a = input("Ingresa datos: ")
        m.prueba(a)
