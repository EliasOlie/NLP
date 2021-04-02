# -*- coding: utf-8 -*-
from epp import normalization
import json
from typing import TypedDict

#SPCB - Single Purpuse Conversational Bot

with open('./backend/phrases.json', 'r', encoding='utf-8') as json_file:
    frases = json.load(json_file)

class Resultado(TypedDict):
    """
    score: float, frase: str, mensagem: str
    """
    score: float
    frase: str
    mensagem: str


"""
TODO:
1 - Relações entre keywords e substantivos? HOWTO??
2 - Corrigir score (está dando 133% na frase 'Como faz para rolar um dado?')
3 - Abstrair código
4 - Refatorar o que for possível
5 - Implementar formas de personalizar as entradas (cadastrar frases e intenções p.ex)
6 - Implementar interação com server node e API ✔

DEFINIÇOES:

1 - Listas de base (base_list) = Lista de dicionários onde haverá a maioria das frases que o 'bot' 
encontrará e as respectivas intenções delas. a lista é inserida dessa forma:
                            | Frase | Intenção |

2 - Frase (word) = A frase que um usuário digitará e que passará pelo algoritmo para ser processada e 
extraída a intenção, ou a mais provável intenção do usuário.

PROCESSAMENTO:

1 - Separará cada palavra da frase e comparará com a frase do usuário frase  len <= true case


METRICAS:

1 - Como avaliar se "a" pertence a "x" ou a "y" (ou qqr outra classificação?) knnw! Quanto maior o score
relativo a x ou a y, logo, mais proximo a vai estar

"""

def get_intents(phrase:str, base_list:list, keywords: list) -> dict: 

    symbols = ['!', '?']
    for symbol in symbols:
        if symbol in phrase:
            analisys_phrase = phrase.replace(symbol, "")
        else:
            analisys_phrase = phrase
    
    score = 0

    analisys_phrase = analisys_phrase.split(" ")

    for k in base_list.keys():
        k = k.split(" ")
        for word in k:
            if word in analisys_phrase:
                score+=1

    score_max = len(analisys_phrase)

    final_score = score/score_max

    if keywords[0] in analisys_phrase:
        msg = f'{round(final_score*100)}%  intenção de obter informação sobre criação de ficha'
    if keywords[1] in analisys_phrase:
        msg = f'{round(final_score*100)}% intenção de obter informação sobre comando'
    else:
        msg = f'{round(final_score*100)}% Dados insulficientes para classificar intenção, ou intenção implicita'

    resultado: Resultado = {'score':final_score, 'frase': phrase, 'mensagem': msg}
    
    return resultado

def get_result(phrase):
    resultado = get_intents(phrase, frases, ['ficha', 'dado'])
    return print(normalization(resultado['mensagem']))

a=get_intents('como crio uma ficha', frases, ['ficha', 'dado'])
print(a['mensagem'])