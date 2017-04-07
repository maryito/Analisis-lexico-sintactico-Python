import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import analizador

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right','ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]

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
# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER 
                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

    # print('logica ',[x for x in t])

# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion 
                |   expresion OR expresion 
                |   expresion NOT expresion 
                |  PARIZQ expresion AND expresion PARDER
                |  PARIZQ expresion OR expresion PARDER
                |  PARIZQ expresion NOT expresion PARDER
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] =  t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] =  t[2] is not t[4]



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

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)



# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_sintactica(s)