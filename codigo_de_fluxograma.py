#def banco():
    #saldo_numero = int(input("digite o valor"))
    #saque_numero = int(input("digite seu saque"))

    #if saldo_numero >= saque_numero:
        #saldo_numero = saldo_numero - saque_numero 
        #print('voce realizou um saque com sucesso. ')

    #else:
        #print("voce não possui saldo suficiente para realizar essa operação.")

#banco()




def media_nota():
    
    nota1 = int(input("digite a primeira nota: "))
    nota2 = int(input("digite a segunda nota: "))
    media_nota = (nota1+nota2)/2

    if media_nota >= 6:
    print("aprovado")
    else:
    print("reprovado")

media_nota()
