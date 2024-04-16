import ply.lex as lex
tokens = ['FLOAT', 'INT']


# Ignorar espacios y tabs
t_ignore = ' \t'


# Regla para enteros simples
def t_INT(t):
    r'\d(_?\d)*'
    t.value = int(t.value.replace('_', ''))
    return t


# Error handling rule
def t_error(t):
    raise lex.LexError(f"Illegal character {t.value[0]}", t.value)


def getLexer():
    return lex.lex()
