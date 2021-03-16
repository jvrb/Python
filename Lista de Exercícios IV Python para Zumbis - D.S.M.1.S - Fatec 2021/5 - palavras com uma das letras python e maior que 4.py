'''Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
minúsculas e de remover antes os caracteres especiais.'''

def tem_python(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False


print('programa split')
frase = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""

newFrase = frase.lower()
newFrase = frase.replace('.', '')
newFrase = frase.replace(',', '')
newFrase = frase.replace(':', '')
newFrase = frase.split()

palavras = 0

for palavra in newFrase:
    if len(palavra) > 4 and tem_python(palavra) == True:
        palavras += 1
    

print(f'Palavras: {palavras}')
