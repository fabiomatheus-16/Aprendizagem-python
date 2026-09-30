
#Tipos Int e Float

#Int: números inteiros, positivos ou negativos, sem casas decimais.
#Positivo ou negativo. int sem sinal é considerado positivo. 

print(11) #int
print(-11) #int
print(0) #int

#float: números reais, positivos ou negativos, com casas decimais.
#o tipo float representa qualquer número
#positivo ou negativo, com casas decimais.
#float sem sinal é considerado positivo.
#sempre usar ponto para separar a parte inteira da parte decimal.

print(1.1) #float 
print(-1.1) #float
print(0.0) #float

#a função type mostra o tipo que o Python inferiu ao valor.

print(type(11)) #int
print(type(-11)) #int
print(type(0)) #int
print(type(1.1)) #float
print(type(-1.1)) #float
print(type(0.0)) #float
print(type("Olá mundo!")) #str
print(type(True)) #bool
print(type(False)) #bool
print(type(1.1), type(-1.1), type(0.0)) #float