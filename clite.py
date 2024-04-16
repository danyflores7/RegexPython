import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'


def getLexer():
  return lex.lex()