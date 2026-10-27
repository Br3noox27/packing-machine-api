# packing-machines-api / paradas.py
# Código escrito por mim (Breno), sem IA.



# 1) total_parado(minutos): recebe uma lista de minutos e DEVOLVE a soma (sem usar sum)

def total_parado(minutos):
    soma = 0 

    for minuto in minutos:
        soma += minuto
    valor_total = soma

    return valor_total
        


# 2) teste: antes de rodar, escrever aqui na mão qual número deve sair
# print(total_parado([10, 25, 5, 60]))

print(total_parado([1, 2, 3]))
print(total_parado([10, 25, 5, 60]))
