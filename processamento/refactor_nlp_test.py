# coding=<utf-8>    

# import pytest
import Natural_Language
import json

"""
TODO 

• Mover frases para um json com frases ✖
"""


def test_main():
    with open('processamento/dataset_test.json', 'r', encoding='utf8') as file:
        testes = json.load(file)
    
    true_test = 0
    test_len = 0

    for test in testes.keys():
        test_len += 1
        for k in test.keys():
            print(k)
        #     teste_process = Natural_Language.NLP(k)
        #     retorno = json.loads(teste_process.process)
        #     for v in test.values():
        #         if v == retorno:
        #             true_test += 1
        #         else:
        #             true_test -= 1

    assert true_test == test_len

test_main()