import time
print("\n--- Bem vindo ao quiz ---\n")
time.sleep(1)
points = 0
def validador_quest(promp,valido):
    while True:
        resp = input(promp).upper()
        if resp in valido:
            return resp
        print("digite uma opção valida")

        
def askquestions(question,options,correct_resp):
    print(question)
    for option in options:
        print(option)
    resp = validador_quest("Resposta:", ["A","B","C"])

    if resp == correct_resp:
        print("está correto")
        return 1
    else:
        print("está incorreto")
        return 0
    



print("\n----------------------------------------\n")

points += askquestions("Qual o nome do jogo da Mojang?", 
                       ["(A) Minecraft", "(B) GTA", "(C) Call of Duty"], 
                       "A")
print("\n----------------------------------------\n")
points += askquestions("Qual o nome do jogo da rockstar?", 
                       ["(A) Minecraft", "(B) GTA", "(C) Call of Duty"], 
                       "B")
print("\n----------------------------------------\n")
points += askquestions("Qual o nome do jogo da Activision?", 
                       ["(A) Minecraft", "(B) GTA", "(C) Call of Duty"], 
                       "C")
print("\n----------------------------------------\n")
points += askquestions("Qual o nome do jogo da 2k?", 
                       ["(A) NBA", "(B) GTA", "(C) Call of Duty"], 
                       "A")
print("\n----------------------------------------\n")
points += askquestions("Qual o nome do jogo da rockstar?", 
                       ["(A) Midnight Club", "(B) GTA", "(C) Call of Duty"], 
                       "A")
total_quest= 5

media=(points/total_quest)* 100
print(f"você acerto{points} de {total_quest} perguntas ({media:.2f}%)")
