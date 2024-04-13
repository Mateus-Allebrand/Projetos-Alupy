
import os 
from time import sleep

def Nome_Programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def Menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

restaurantes =[]
    
def cadastrando_restaurante():
    os.system("cls")
    print("Cadastrar Restaurante: \n")
    nome = input("Digite o nome do restaurante que você deseja cadastrar: \n")
    restaurantes.append(nome)
    print(f"Restaurante {nome} Cadastrado com sucesso!\n")
    sleep(2)


def listando_restaurante():
    os.system("cls")
    print("Listando Restaurantes: \n")
    
    for restaurante in restaurantes:
        print(f"°{restaurante}\n")
        sleep(1)
    main()
    
   






def Exibir_opções():
    try:
        opcao_escolhida = int(input("Escolha uma opção: \n"))
        
        match opcao_escolhida:

            case 1 :    
                cadastrando_restaurante()

            case 2:
                listando_restaurante()

            case 3:
                print("Ativar restaurante! \n")

            case 4:
                Finalizar_ap() 
            case _:
                Op_Invalida()
        return opcao_escolhida
    except ValueError:
        print("Você digitou um valor inválido! \n")
        sleep(2)
        main()




def Op_Invalida():
    print("Opção Invalida! ")
    sleep(1)
    main()



#Funções: 
def Finalizar_ap():
    os.system('cls')
    print("Finalizando App...")

def main():
    while True:
        os.system("cls")
        Nome_Programa()
        Menu()
        x = Exibir_opções()
        if x == 4:
            break
    

    


if __name__ == "__main__":
    main()