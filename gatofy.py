texto = input("Digite um texto para ser gatificado: ")
def gatofy(texto):
    representacao_binaria = [format(ord(char), '08b') for char in texto]
    representacao_gatificada = ['meow, ' if bit == '0' else 'meow-meow, ' if bit == '1' else 'MEOW, ' for bit in ''.join(representacao_binaria)]
    return representacao_binaria, representacao_gatificada

texto_binario, texto_gatificado = gatofy(texto)
print(''.join(texto_gatificado))