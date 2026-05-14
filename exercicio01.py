n1 = int(input("digite 01 n"))
n2 = int(input("digite 01 n"))

resultado = n1 + n2
resultado2 = n1 % n2
resultado3 = n1 ** n2

print("o resultado e 1 : " , resultado)

print("o resultado da parte inteira da divisão e : ", resultado)
print("o resultado2 do resto da divisão e : " , resultado2)
print("o resultado da potencia e : " , resultado3)

print("-----------------------------------")
print("  OPERADORES RELACIONAIS   ")


relacao1 = n1 > n2
relacao2 = n1 < n2
relacao3 = n1 < n2
relacao4 = n1 <= n2 
relacao5 = n1 == n2
relacao6 = n1 != n2


print("os resultados das relacao estarao abaixo: \n{} \n {} \n {} \n{} \n{} \n{}".format(relacao1, relacao2, relacao3, relacao4,relacao5, relacao6))