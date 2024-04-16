import ply.lex as lex


tokens = [ 'FLOAT']


t_ignore  = ' \t'


# Regla para números de punto flotante
def t_FLOAT(t):
    r'(\d+(_\d+)*\.(\d+(_\d+)*)?|\.?\d+(_\d+)*)([eE][+-]?(\d+(_\d+)*))?'
    t.value = float(t.value.replace('_', ''))  # Remover los guiones bajos antes de convertir a flotante
    return t


# Error handling rule
def t_error(t):
    raise lex.LexError(f"Illegal character {t.value[0]}", t.value)




def getLexer():
  return lex.lex()
