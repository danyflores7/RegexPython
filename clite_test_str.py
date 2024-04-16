import unittest
import ply.lex as lex
import clite3


class TestStrings(unittest.TestCase):
    def setUp(self):
        self.lexer = clite3.getLexer()


    def test_basic_strings(self):
        self.lexer.input('Le petit prince')
        token = self.lexer.token()
        self.assertEqual(token.type, 'STR')
        self.assertEqual(token.value, 'Le petit prince')


    def test_basic_strings(self):
        self.lexer.input('"Hola \\\"%s\\\""')
        token = self.lexer.token()
        self.assertEqual(token.type, 'STR')
        self.assertEqual(token.value, '"Hola \\\"%s\\\""')


if __name__ == '__main__':
    unittest.main()




