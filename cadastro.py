# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")

    # Salvar os dados em um arquivo
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email}\n")

    print(f"\nUsuário {nome} cadastrado com sucesso!")

# Função para exibir mensagem para o usuário
def exibir_mensagem():
    nome = input("\nDigite seu nome para exibir a mensagem: ")
    
    with open("usuarios.txt", "r") as arquivo:
        usuarios = arquivo.readlines()
    
    for usuario in usuarios:
        dados = usuario.strip().split(",")
        if dados[0] == nome:
            print(f"\nOlá, {nome}! Bem-vindo ao nosso sistema! 😊")
            return
    
    print("\nUsuário não encontrado. Cadastre-se primeiro!")

# Menu principal
while True:
    print("\n1 - Cadastrar Usuário")
    print("2 - Exibir Mensagem")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        exibir_mensagem()
    elif opcao == "3":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
