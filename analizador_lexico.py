import ply.lex as lex

tokens = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'ENDL',
    'SINO',
    'SI',
    'INT',
    'CADENA',
    'RETURN',
    'VOID',
    'MIENTRAS',
    'PARA',

    # Symbolos
    'NUMERAL',
    'PUNTO',
    'SUMA',
    'PLUSPLUS',
    'RESTA',
    'MINUSMINUS',
    'MULT',
    'DIV',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'ASIGNAR',
    'IGUAL',
    'DISTINTO',
    'PUNTOCOMA',
    'COMA',
    'LGREATER',
    'RGREATER',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    'COMDOB',
    
    #Otros
    'IDENTIFICADOR',
    'ENTERO',
)

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


def t_INCLUDE(t):
    r'include'
    return t


def t_USING(t):
    r'using'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_STD(t):
    r'std'
    return t


def t_COUT(t):
    r'cout'
    return t


def t_CIN(t):
    r'cin'
    return t


def t_GET(t):
    r'get'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_SINO(t):
    r'else'
    return t


def t_SI(t):
    r'if'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_MIENTRAS(t):
    r'while'
    return t


def t_PARA(t):
    r'for'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    """
    expresion regular para reconocer los identificadores
    :param self: 
    :param t: token 
    :return: 
    """
    r'\w+(_\d\w)*'
    return t


def t_CADENA(t):
    """
    expresion regular para reconocer los String
    :param self: 
    :param t: 
    :return: 
    """
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_NUMERAL(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_LGREATER(t):
    r'<<'
    return t


def t_RGREATER(t):
    r'>>'
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

t_ignore  =' \t'

def t_error( t):
    '''
    Manejo de errores del analisis lexico
    :param t: la exprexion a analizar
    :return: nada
    '''
    print(" No es valido el caracter '%s'" % t.value[0])
    t.lexer.skip(1)
# instanciamos el analizador lexico
analizador = lex.lex()


# Prueba de ingreso
def prueba():
    while True:
        data = input("ingrese: ")
        analizador.input(data)
        tok = analizador.token()
        if not tok:
            # print("omitido");
            break
        print(tok)

if __name__ == '__main__':
    prueba()