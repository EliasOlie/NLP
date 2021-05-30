import json
from typing import NewType
import utils

"""
TODO:
• Colocar nome dos metodos em portugues
• Comentar o código (PT-BR) e (EN)
• Integrar com o servidor (JS, Flask)
• TypeHints e datatype personalizado
• Ajustar NewType
• Refatorar código para não se repetir. Usar comprehensions
• Validar frases e exeption handlers
"""

polaridade = NewType('Polaridade', int)
indice_confianca = NewType('Indice de confianca', [float or str])

with open('./backend/nlp_database.json', 'r', encoding='utf-8') as json_file:
    dados = json.load(json_file)

class NLP(object):
    Natural_Language_Processing_Intance = NewType('NLP_Instance', object)

    """
    (PT-BR) Classe básica. Aceita apenas um argumento que é a frase (do tipo str) a ser processada e retorna
    um JSON com os dados do processamento da frase 

    (EN) Basic class. Accepts only one argument the phrase itself (str type) 
    the phrase is processed and then it returns a JSON with the processed data.
    """

    def __init__(self, frase:str) -> Natural_Language_Processing_Intance:

        self.frase = utils.normalization(frase)
        self.process = {'resultado': f'{self.__processing()["Mensagem"]}, ' f'score: {round(self.__processing()["Confidence"]*100)}%'}
        
        # 'Confianca': {self.__processing()["Confidence"]}}

    def __separar_frase(self, frase):
        len_sentimento = [] #Lista que conterá a polaridade de cada palavra, para posteriormente obter o total, como neutro, positivo ou negativo
        unknow_words = 0 #Palavras desconhecidas é importante sua contagem, pois, dessa forma um indice de confiança fica mais preciso
        know_words = 0 #Palavras conhecidas, mesma razão das palavras desconhecidas
        
        lista_palavra = self.frase.split()

        for word in lista_palavra:
            
            actual_word = dados.get(word)
            
            if actual_word is not None:

                for key, value in actual_word.items():
                    
                    temp = [key,value]
                    len_sentimento.append(temp[1])
                    know_words += 1
                    
            else:
                
                unknow_words += 1
                len_sentimento.append(0)

        polarity = sum(len_sentimento)

        return [polarity, know_words, unknow_words]

    def __indice_de_confiança(self, phrase_list: list, know_words: list) -> indice_confianca:
        if know_words > 0:

            total_words = len(phrase_list.split()) #mover para processos iniciais <-*
            cf =  know_words / total_words  #exeption handle (Zero divisin error) | Função especifica

        else:
            cf = 'Baseado nos dados já coletados não posso chegar numa conclusão precisa'

        return cf 

    def __get_context(self,phrase_list, overallpolarity) -> indice_confianca:

        score = 0

        #Aumentar lista de palavras com contexto
        negative_context = ['não', 'nao', 'Não', 'Nao']
        palavras_neutras = ['gostei']


        phrase_list = phrase_list.split()
        try:
            context1 =  phrase_list.index(palavras_neutras[0]) - 1
            if context1 >= 0: #Separar para função isolada
                if palavras_neutras[0] in phrase_list and phrase_list[context1] in negative_context:
                    score -= 1
                else:
                    score += 1
                    pass
            else:
                pass
        except:
            pass

        overallpolarity += score


        return overallpolarity

    def __nutshell(self,score, cf, tw, uw, msg) -> object:
   
        retorno = { # função isolada
                
                "Polaridade":score,
                "Confidence":cf, 
                "Numero de palavras":tw, 
                "Palavras desconhecidas":uw, 
                "Mensagem":msg
                
                }

        return retorno


    def __processing(self) -> Natural_Language_Processing_Intance:
    
        #Análise da polaridade da frase e atribuição de variáveis úteis
        nluscore = self.__separar_frase(self.frase)

        #Atualizar o score através das variáveis de contexto
        contextscore = self.__get_context(self.frase, nluscore[0])

        #Calcular o índice de confiança
        cf = self.__indice_de_confiança(self.frase, nluscore[1])

        #Criação da mensagem de análise de polaridade sentimental da frase
        if contextscore > 0:
            msg = f'A frase "{self.frase}" é positiva' # {self.frase}
        elif contextscore == 0:
            msg = f'A frase "{self.frase}" é neutra'
        else:
            msg = f'A frase "{self.frase}" é negativa'

        #Criação do objeto Json
        nut = self.__nutshell(contextscore, cf, len(self.frase.split()), nluscore[2], utils.normalization(msg))

        return nut


    def __repr__(self) -> str:
        return f'(frase= {self.frase})'

if __name__ == "__main__":
    
    # print(utils.normalization('Olá'))
    a1 = NLP('Não gostei do pão')
    print(a1.process)
 