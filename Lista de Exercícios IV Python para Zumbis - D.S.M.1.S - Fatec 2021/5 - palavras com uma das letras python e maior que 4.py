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

frase = frase.lower()
frase = frase.replace('.', '')
frase = frase.replace(',', '')
frase = frase.replace(':', '')
frase = frase.split()

palavras = 0

for palavra in frase:
    resp = tem_python(palavra)
    if len(palavra) > 4:
        palavras += 1
    

print(f'Palavras: {palavras}')



