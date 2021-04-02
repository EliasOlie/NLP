from typing import NamedTuple
from typing import TypedDict
from epp import normalization
import json

"""
TODO
* JSON Colocar como valor das chaves(frases base) a soma total que assim vai ser dividido
todo espaçõ amostral pelo score da frase atual, creio porém que isso acarretará em scores muito baixos
* Método de cadastrar frases no "Banco de dados"
*REFATORAR TUDO
"""
class Resultado(NamedTuple):
    """
    Classe que segura os resultados de saída do modelo
    
    Types:
    
    score: float, 
    frase: str, 
    mensagem: str
    """
    score: float
    frase: str
    mensagem: str

class Spcb(NamedTuple):
    """
    (EN)Single purpose conversational bot.
    (PT-BR) Bot de conversa de proposito único.

    Classe do modelo, onde temos o método de atribuir intenções.
    
    Types:

    phrase: str,
    base_list: list, Arquivo json que contém as frases de "treino"
    keywords: list. Lista contendo as palavras-chave para identificação de intenção
    Aconselhavel usar keywords no plural (se cabivel)
    """
    phrase: str
    base_list: list
    keywords: list

    def get_intents(self):
        symbols = ['!', '?']
        for symbol in symbols:
            if symbol in self.phrase:
                analisys_phrase = self.phrase.replace(symbol, "")
            else:
                analisys_phrase = self.phrase
        
        score = 0

        analisys_phrase = analisys_phrase.split(" ")

        for k in self.base_list.keys():
            k = k.split(" ")
            for word in k:
                if word in analisys_phrase:
                    score+=1

        score_max = len(analisys_phrase)

        final_score = score_max/score

        if self.keywords[0] in analisys_phrase or self.keywords[1] in analisys_phrase:
            msg = f'{round(final_score*100)}%  intenção de obter informação sobre criação de ficha'
        elif self.keywords[2] in analisys_phrase or self.keywords[3] in analisys_phrase:
            msg = f'{round(final_score*100)}% intenção de obter informação sobre comando'
        else:
            msg = f'{round(final_score*100)}% Dados insulficientes para classificar intenção, ou intenção implicita'

        output = Resultado(final_score, self.phrase, msg)
        return output

with open('./backend/phrases.json', 'r', encoding='utf-8') as json_file:
    frases = json.load(json_file)

a = Spcb('Como faço uma fichas aqui', frases, ['ficha', 'fichas', 'dado', 'dados']).get_intents()
print(a)