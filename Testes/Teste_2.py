from IPython import get_ipython
from IPython.display import display
# %%
import unittest

def soma(a, b):
    # Retorna a soma de dois números.
    return a + b

def multiplica_e_soma(a, b, c):
    # Multiplica dois números e soma o resultado com um terceiro.
    return soma(a * b, c)

class TesteIntegracao(unittest.TestCase):
    def test_multiplica_e_soma(self):
    # Teste de Integração: multiplica e soma corretamente.
        resultado = multiplica_e_soma(2, 3, 4)  # (2*3)+4=10
        self.assertEqual(resultado, 10)

if __name__ == '__main__':
    # Modifica a chamada para unittest.main() para não sair do processo em Jupyter
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
