#Variaveis são usadas para salvar algo na memoria do computador.
#PEP8: inicie variaveis com letras minusculas, pode usar 
# numeros e underline, 
# mas não pode usar caracteres especiais, nem iniciar com numeros.
# O sinal de = é um operador de atribuição. ELe é usado para
#atribuir um valor a um nome (variavel). 
# O nome da variavel é o identificador, 
# e o valor que ela recebe é o objeto.
#Uso: nome_variavel = expressão.

idade = 23 #atribuição de valor a variavel idade
nome = 'Fabio' #atribuição de valor a variavel nome
escola = 'Atheneu' #atribuição de valor a variavel escola
namorada = "Ket"#atribuição de valor a variavel namorada

print(nome,"conheceu", namorada, "na escola", escola)
print(nome + " tem " + str(idade) + " anos") 
#concatenação de strings e conversão de int para str


maior_idade = idade >= 18 #atribuição de valor a variavel maior_idade
#, que é uma expressão booleana
print(nome, "é maior de idade?", maior_idade) #imprime se a pessoa é maior de idade