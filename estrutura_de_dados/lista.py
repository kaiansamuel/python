numeros = [1,2,3]
numeros.append(100)#add ao fim da lista

print(numeros)# saida: [1,2,3,100]

numeros.insert(1, 200)#add na posição 1 o valor 200

print(numeros)# saida: [1,200,2,3,100]

numeros.remove(200)#remove o valor 200
numeros.remove(100)#remove o valor 100

print(numeros)# saida: [1,2,3]

pilha_livros = ["MMM", "DDD", "Hábitos Atômicos"]

print(f"Acabei de ler o livro {pilha_livros.pop()}")
