import ply.yacc as yacc
from analizador_lexico import tokens

precedence = (
    ('left', 'ASIGNAR', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_librerias(t):
    'expresion : NUMERAL INCLUDE MENORQUE expresion MAYORQUE'
    print("Libreria")
    nombres [t[4]] = 'liberia'

def p_declaracion_encabezado(t):
    'declaracion : USING NAMESPACE expresion PUNTOCOMA'
    print("Encabezado = "+t[3])

def p_declaracion_imprimir(t):
    'expresion : COUT MAYORIZQ expresion PUNTOCOMA'
    t[0] = t[3]
    print("imprimiendo = "+str(t[3]))

def p_declaracion_asigna(t):
    'declaracion : CIN MAYORDER expresion PUNTOCOMA'
    t[0] = t[3]
    print("asigna cin = "+t[3])

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
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
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_cadena(t):
    'expresion : COMDOB expresion COMDOB'
    t[0] = t[2]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0



# sintactico de expresiones logicas
# def p_expresiones_logicas(t):
#     '''
#     expresiones : PARIZQ expresiones AND expresiones  PARDER
#                 | PARIZQ expresiones OR expresiones PARDER
#                 | PARIZQ expresiones NOT expresiones PARDER
#                 | PARIZQ expresiones MENORQUE expresiones PARDER
#                 | PARIZQ expresiones MAYORQUE expresiones PARDER
#                 | PARIZQ expresiones MENORIGUAL expresiones PARDER
#                 | PARIZQ expresiones MAYORIGUAL expresiones PARDER
#                 | PARIZQ expresiones IGUAL expresiones PARDER
#                 | PARIZQ expresiones DISTINTO expresiones PARDER
#     '''
#     # if t[2] == "AND":

def p_error(t):
    if t:
        print("Error de sintactico de tipo: ",t.type," en el valor ", t.value)
    else:
        print("Error desconocido",t)


# instanciamos el analizador sistactico
parse = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            s =  input("Expresion analizar: ")
        except EOFError                                                                                                                                                                                                            :
            break
        parse.parse(s)
        print()