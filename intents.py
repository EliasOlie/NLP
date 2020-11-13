import time

def intents_processing(phrase):
    
    intents = ['que', 'qual', 'quando', 'quem', 'quais']
    entity = ['horas', 'tempo', 'clima', 'cotação', 'carro']
    tempo = ['são', 'serão', 'seria']

    detected_intents = []
    detected_entity = []
    detected_time = []

    future_handler = []

    phrase_collection = phrase.split()

    for word in phrase_collection:

        word = word.lower()
        
        if word in intents:
            detected_intents.append(word)
        elif word in entity:
            detected_entity.append(word)
        elif word in tempo:
            detected_time.append(word)
        else:
            future_handler.append(word)
        
    return {
        "Intenções" : detected_intents,
        "Entidades" : detected_entity,
        "Tempo" : detected_time,
        "Desconhecido" : future_handler
    }


teste = intents_processing("Que horas são")

if teste['Intenções'][0] == 'que' and teste["Entidades"][0] == 'horas':
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
