# coding=<utf-8>    

import pytest
import processamento.Natural_Language as Natural_Language
import json

"""
TODO 

• Mover frases para um json com frases ✔
"""

def test_main():
    true_test = 0

    with open('processamento/dataset_test.json', 'r', encoding='utf8') as file:
        testes = json.load(file)
    
    for test_phrase, test_value in testes.items():
        teste_process = Natural_Language.NLP(test_phrase).process       
        retorno = json.loads(teste_process)
        if test_value == retorno:
            true_test += 1
        else:
            true_test -= 1

    assert true_test == len(testes)