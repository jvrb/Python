print('programa split')
frase = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""

frase = frase.replace('.', '')
frase = frase.replace(',', '')
frase = frase.replace(':', '')
frase = frase.lower()
frase = frase.split()


palavras = []

for palavra in frase:
    #Se a primeira letra não for MAIUSCULA
    if palavra[0] != palavra[0].upper():
        if palavra[0] in 'python' or palavra[-1] in 'python':
            palavras.append(palavra)


print(f'LISTA DE PALAVRAS\n{palavras}')
