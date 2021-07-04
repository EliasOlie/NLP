# coding=<utf-8>    

import pytest
from .  import Natural_Language
import json

"""
TODO 

• Mover frases para um json com frases ✖
"""

frase_nao_gostei_do_pao = 'Não gostei do pão' 

teste_nao_gostei_do_pao = {"Polaridade": -1, "Confidence": "75%", "Numero de palavras": 4, "Palavras desconhecidas": 1, "Mensagem": "a frase \"nao gostei do pao\" e negativa"}

teste1 = {frase_nao_gostei_do_pao:teste_nao_gostei_do_pao}

frase_gosto_muito_de_voce = 'Gosto muito de você'

teste_gosto_muito_de_voce = {"Polaridade": 1, "Confidence": "75%", "Numero de palavras": 4, "Palavras desconhecidas": 1, "Mensagem": "a frase \"gosto muito de voce\" e positiva"}

teste2 = {frase_gosto_muito_de_voce:teste_gosto_muito_de_voce}

frase_gostei_do_livro = 'Gostei do livro'

teste_gosto_do_livro = {"Polaridade": 1, "Confidence": "67%", "Numero de palavras": 3, "Palavras desconhecidas": 1, "Mensagem": "a frase \"gostei do livro\" e positiva"}

teste3 = {frase_gostei_do_livro:teste_gosto_do_livro}

testes = [teste1, teste2, teste3]

@pytest.fixture
def frase_list():
    return testes

def test_main(frase_list):
    true_test = 0
    for test in testes:
        for k in test.keys():
            teste_process = Natural_Language.NLP(k)
            retorno = json.loads(teste_process.process)
            for v in test.values():
                if v == retorno:
                    true_test += 1
                else:
                    true_test -= 1

    assert true_test == len(frase_list)