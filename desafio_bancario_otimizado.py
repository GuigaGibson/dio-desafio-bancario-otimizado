def menu():
    return print("""

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """,end="")

def depositar(saldo,extrato):
    deposito=float(input("Digite o valor do deposito: "))
    saldo+=deposito
    extrato=adicionar_extrato(deposito,extrato,1)
    print("Deposito efeituado!")
    return saldo,extrato
    
def adicionar_extrato(valor,extrato,op):
    if op==1:
        extrato+=f"Deposito no valor de: R$ {valor}\n" 
    else:
        extrato+=f"Saque no valor de: R$ {valor}\n"
    return extrato;    

def exibir_extrato(extrato,saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def sacar(numero_saques,limite_saques,limite,saldo,extrato):
    if numero_saques>limite_saques:
        print("Numero de saques excedidos!")
        return saldo,extrato,numero_saques
    
    else:
        saque=float(input("Digite o valor do saque: "))
        
        if saque>limite:
            print(f"Erro.\nLimite de saque: {limite}")
            return saldo,extrato,numero_saques
            

        elif saque>saldo:
            print("Valor indisponivel.")
            return saldo,extrato,numero_saques
        
        else:
            saldo-=saque
            extrato=adicionar_extrato(saque,extrato,0)

            print(f"Novo saldo: {saldo}")
            numero_saques+=1
            return saldo,extrato,numero_saques

def cadastrar_usuario(usuarios_cadastrados):
    cpf=input("Digite o seu cpf: ")
    if cpf in usuarios_cadastrados:
        print("Usuario ja cadastrado")
        return usuarios_cadastrados
    else:
        nome=input("Digite o seu nome: ")
        nascimento=input("Digite a sua data de nascimento(xx xx xxxx): ")
        logradouro=input("Logradouro (Rua cidade/sigla do estado): ")
        usuarios_cadastrados[cpf]={"nome":nome,"nascimento":nascimento,"logradouro":logradouro}
        print("Usuario cadastrado com sucesso!")
        return usuarios_cadastrados

def criar_conta(usuarios_cadastrados, contas_criadas):
    cpf = input("Digite o seu cpf: ")
    if cpf in usuarios_cadastrados:
        nova_conta = ["0001", str(contas_criadas + 1)]
        usuarios_cadastrados[cpf].setdefault("contas", []).append(nova_conta) #cria a chave se não tiver, caso tenha, só adiciona um novo valor a lista
        print("Conta criada com sucesso:")
        return usuarios_cadastrados,contas_criadas+1
    else: 
        print("Usuario nao encontrado.")
        return usuarios_cadastrados,contas_criadas
        
def listar_contas(usuarios_cadastrados):
    texto=''
    for i in usuarios_cadastrados:
        if "contas" in usuarios_cadastrados[i]:
            texto+=f"{usuarios_cadastrados[i]["nome"]}, contas:\n"
            for j in range(len(usuarios_cadastrados[i]["contas"])):
                texto+= f"Agencia:{usuarios_cadastrados[i]["contas"][j][0]} Conta:{usuarios_cadastrados[i]["contas"][j][1]}\n"
            texto+="\n"
            texto+="x="*10
            texto+="\n"
    if texto!='':
        print(texto)       
    else:print("nenhuma conta foi criada")
    


saldo = 0
limite_saque_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas_criadas=0
usuarios_cadastrados={}



while True:
    menu()
    opcao = input().lower()

    if opcao == "d":
      saldo,extrato=depositar(saldo,extrato)
      
    elif opcao == "s":
        saldo,extrato,numero_saques=sacar(saldo=saldo,extrato=extrato,numero_saques=numero_saques,limite=limite_saque_diario,limite_saques=LIMITE_SAQUES)
    elif opcao == "e":
        exibir_extrato(extrato=extrato,saldo=saldo)
    
    elif opcao == "nu":
        usuarios_cadastrados=cadastrar_usuario(usuarios_cadastrados)
    
    elif opcao == "nc":
        usuarios_cadastrados,contas_criadas=criar_conta(usuarios_cadastrados,contas_criadas)
    
    elif opcao == "lc":
        listar_contas(usuarios_cadastrados)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")