import ply.lex as lex
import token_Roles as tkRoles

class Compilador(object):
    """ Compilador """
    tokens = tkRoles.getTokens()

# Reglas de Expresiones Regualres para token de Contexto simple

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MINUSMINUS = r'\-\-'
    t_POINT = r'\.'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUAL = r'='
    t_LESS = r'<'
    t_GREATER = r'>'
    t_SEMICOLON = ';'
    t_COMMA = r','
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBLOCK = r'{'
    t_RBLOCK = r'}'
    t_QUOTES = r'\"'


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

    def t_ELSE(self,t):
        r'else'
        return t

    def t_IF(self,t):
        r'if'
        return t

    def t_RETURN(self,t):
        r'return'
        return t

    def t_VOID(self,t):
        r'void'
        return t

    def t_WHILE(self,t):
        r'while'
        return t

    def t_FOR(self,t):
        r'for'
        return t

    def t_NUMBER_int(self,t):
        r'\d+'
        t.value = int(t.value)
        return t

#exprecion regular para reconocer los identificadores

    def t_ID(self,t):
        r'\w+(_\d\w)*'
        return t

    def t_STRING(self,t):
    #expresion RE para reconocer los String
        r'\"?(\w+ \ *\w*\d* \ *)\"?'
        return t

    def t_HASH(self,t):
        r'\#'
        return t

    def t_PLUSPLUS(self,t):
        r'\+\+'
        return t

    def t_LESSEQUAL(self,t):
        r'<='
        return t

    def t_GREATEREQUAL(self,t):
        r'>='
        return t

    def t_DEQUAL(self,t):
        r'=='
        return t

    def t_LGREATER(self,t):
        r'<<'
        return t

    def t_RGREATER(self,t):
        r'>>'
        return t

    def t_DISTINT(self,t):
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
    m.prueba("3 + 10  %    8")
