print("Prograam Login e Senha!")
usuario = input("Digite um nome de usuario: ")
senha = input("Digite uma senha: ")
while usuario == senha:
    print("ERRO\nDigite uma senha diferente do nome de usuario!!")
    usuario = input("Digite um nome de usuario: ")
    senha = input("Digite uma senha: ")

print("Usuario e Senha Validos!")
