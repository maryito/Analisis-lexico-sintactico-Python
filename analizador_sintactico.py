import ply.yacc as yacc
from analizador_lexico import tokens

precedence = (
    ('left', 'ASIGNAR', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : NOMBRE ASIGNAR expresion'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    print("Resultado: " + str(t[1]))

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    '''
    expresion  : PARIZQ expresion PARDER
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    t[0] = t[2]

def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : NOMBRE'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido %s " % t[1])
        t[0] = 0

# sintactico de expresiones logicas
def p_expresiones_logicas(t):
    '''
    expresiones : PARIZQ expresiones AND expresiones  PARDER
                | PARIZQ expresiones OR expresiones PARDER
                | PARIZQ expresiones NOT expresiones PARDER
                | PARIZQ expresiones MENORQUE expresiones PARDER
                | PARIZQ expresiones MAYORQUE expresiones PARDER
                | PARIZQ expresiones MENORIGUAL expresiones PARDER
                | PARIZQ expresiones MAYORIGUAL expresiones PARDER
                | PARIZQ expresiones IGUAL expresiones PARDER
                | PARIZQ expresiones DISTINTO expresiones PARDER
    '''
    # if t[2] == "AND":

def p_error(t):
    '''
    Manejo de errores del analisis sintactico
    :param t: expresion analizar
    :return: 
    '''
    if t:
        print("Error de sintactico de tipo: ",t.type," en el valor ", t.value)
    else:
        print("Error desconocido",t)

# instanciamos el analizador sistactico
parse =  yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s =  input("Expresion analizar: ")
        except EOFError                                                                                                                                                                                                            :
            break
        parse.parse(s)
        print()