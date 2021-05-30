import unicodedata

def normalization(word) -> str:
    
        #Normalização da frase, removendo caracteres especiais e afins
        
        normalized = unicodedata.normalize('NFD', word)
        
        return  normalized.encode('ascii', 'ignore').decode('utf8').casefold()


if __name__ == '__main__':
    print(normalization('Olá'))