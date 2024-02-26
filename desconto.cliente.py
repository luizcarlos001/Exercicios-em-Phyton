n = str(input("Qual é o seu nome? "))
print("Seja bem-vindo, {}!" .format(n))

c = float(input("Você ganhou um cupom de desconto na sua primeira compra! Para validar digite: '12345' \n"))

if c == 12345:
    f = float(input("Digite o preço para o pagamento: "))
else:
    print("Cupom inválido, digite novamente")
    input()

d = (f*5)/100

print("Cupom aplicado, de {}R$ foi para {}R$".format(f,f-d))
print("Obrigado pela compra!")