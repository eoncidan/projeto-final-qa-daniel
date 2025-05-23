from IPython import get_ipython
from IPython.display import display
# %%
import unittest

def multiplica_e_soma(a, b, c):
    # Multiplica dois números e soma o resultado com um terceiro.
    return soma(a * b, c)

def soma(a, b):
    # Retorna a soma de dois números.
    return a + b

class TesteAceitacao(unittest.TestCase):
    def test_requisito_aceitacao(self):
        # Teste de Aceitação: verifica resultado esperado do requisito.
        resultado = multiplica_e_soma(3, 3, 3)  # (3*3)+3=12
        self.assertEqual(resultado, 12)

if __name__ == '__main__':
    # Run the tests without exiting, suitable for Jupyter Notebook
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
