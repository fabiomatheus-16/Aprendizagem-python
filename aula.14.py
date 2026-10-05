# Format é um método de formatação de strings em Python, 
# que permite inserir valores em uma string de forma organizada.
# Ele utiliza chaves {} como marcadores de posição para os valores que serão inseridos.

a = 'A'
b = 'B'
c = 1.1
d = 'D'

string = 'a = {0}, b = {1}, c = {2:.2f}, d = {3}' 
formato = string.format( nome1= a , nome2= b, nome3= c, nome4= d) 

print(formato)