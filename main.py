import ply.lex as lex
import token_Roles as tkRoles

class Compilador(object):
    """ Compiador """
    tokens = tkRoles.getTokens()

    # Expresiones Aritmetica
    t_SUMA = r'\+'
    t_RESTA = r'\-'
    t_MULT = r'\*'
    t_DIV = r'\/'
    t_MODULO= r'\%'
    t_POTENCIA = r'\^'
    t_PARIZQ= r'\('
    t_PARDER= r'\)'
    t_CORIZQ= r'\['
    t_CORDER= r'\]'
    t_LLAIZQ= r'\{'
    t_LLADER= r'\}'
    #Expresiones Logicas
    t_AND = r'\&'
    # t_OR = r''
    # t_NOT = r''
    # #Expresiones relacionales
    # t_MENORQUE= r''
    # t_MAYORQUE= r''
    # t_MENORIGUAL= r''
    # t_MAYORIGUAL= r''
    # t_IGUAL= r'=='
    # t_DISTINTO= r''
    # #Expresiones condicionales
    # t_SI= r''
    # t_SINO= r''
    # t_MIENTRAS= r''
    # t_PARA= r''
    # t_CONTINUAR= r''
    # t_ROMPER= r''
    # t_REGRESAR= r''
    # #Expresiones caracteres
    # t_ASIGNAR= r'='
    # t_COMA= r''
    # t_PUNTOCOMA= r''
    # t_DOSPUNTOS= r''
    # t_CARACTER= r''
    # t_ENTERO= r''
    # t_VACIO= r''
    t_IDENTIFICADOR= r'[a-zA-Z_][a-zA-Z0-9_]*'
    # t_ENTERO= r''
    # t_CADENA= r''
    # t_IMPRIMIR= r''
    # t_LEER= r''
    # t_IMPORTAR= r''
    # t_PUNTO= r''
    # t_NUMERAL= r''
    # t_MAIN= r''

    def t_NUMERO(self,t):
    	r'\d+'
    	t.value = int(t.value)
    	return t

    t_ignore = ' \t'

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
