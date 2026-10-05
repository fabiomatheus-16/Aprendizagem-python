nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2
#f significa que é uma f-string, ou seja, uma string formatada, 
# uma string formatada é uma string que permite a inclusão de expressões dentro dela, 
# que serão avaliadas e substituídas pelo seu valor.
#2f se trata de duas casas decimais, 3f de três casas decimais, e assim por diante.
#,.2f coloca a vírgula como separador de milhar e duas casas decimais.

#f-strings são uma forma de formatar strings em Python, permitindo a inclusão de expressões dentro delas.

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)