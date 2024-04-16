import ply.lex as lex


tokens = [ 'STR' ]


t_ignore  = ' \t'


# Regla para cadenas de texto
def t_STR(t):
    r'\"([^"\\]|\\.)*\"'
    return t




# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




def getLexer():
  return lex.lex()



