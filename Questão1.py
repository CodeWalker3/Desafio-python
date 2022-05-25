from collections import Counter
teste = input("Escreva algo: ")
teste2 = list(sorted(teste))
teste3 = Counter(teste2).most_common(3)
for i in teste3:
    print (i)




