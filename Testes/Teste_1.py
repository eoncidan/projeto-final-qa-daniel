import unittest

# Função que retorna a soma de dois números.
# Parâmetros:
#   a: primeiro valor a ser somado (int ou float)
#   b: segundo valor a ser somado (int ou float)
# Retorna:
#   a soma de a e b (int ou float)
def soma(a, b):
    return a + b

# Classe de testes para a função soma
class TesteUnidade(unittest.TestCase):
    # Teste de soma de números positivos
    # Verifica se a soma de 2 e 3 retorna 5
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    # Teste de soma de números negativos
    # Verifica se a soma de -1 e -1 retorna -2
    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    # Teste de soma com zero
    # Verifica se a soma de 0 e 7 retorna 7
    def test_soma_zero(self):
        self.assertEqual(soma(0, 7), 7)

# Em notebooks ou ambientes interativos, use o seguinte para rodar os testes:
# Em arquivos .py, use: unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TesteUnidade)
unittest.TextTestRunner(verbosity=2).run(suite)
