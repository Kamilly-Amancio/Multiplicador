#AULA 02 - PARADIGMAS DA PROGRMAÇÃO EM PYTHON - 29/08/2023
#ALUNA: KAMILLY AMANCIO BATISTA - 202202570397

def multiplicador(numero):
    a=2 
    print(f"dentro da funçao, a variavel vale {a}")
    return a * numero
a=3
b=multiplicador(5)
print(f"fora da funçao, a variavel a vale: {a}")

def multiplicador(numero):
    return a*numero
a=3
b=multiplicador(5)
print(f"a variavel b vale: {b}")

def multiplicador(numero):
    global a 
    a=2
    print(f"dentro da funçao multiplicador, variavel a vale: {a}")
    return a * numero
a=3
b=multiplicador(5)
print(f"a variavel b vale: {b}")
print(f"fora da funçao multiplicador, a varivavel a vale: {a}")