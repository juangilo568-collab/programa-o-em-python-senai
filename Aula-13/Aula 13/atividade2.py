import statistics

def estatistica(lista_notas):
    moda = statistics.mode(lista_notas)
    media = statistics.mean(lista_notas)
    desvio = statistics.stdev(lista_notas)
    mediana = statistics.median(lista_notas)
    variancia = statistics.variance(lista_notas)
    menor = min(lista_notas)
    maior = max(lista_notas)

    return moda, media, desvio, mediana, variancia, menor, maior

def cadastrar_notas():
    notas = []
    quantidade = int(input("Digite a quantidade de alunos: "))

    for i in range(quantidade):
        nota = float(input(f"Digite a nota do {i+1}º aluno: "))
        notas.append(nota)

cadastrar_notas()


def mostrar_resultados(notas):
    print("ESTATÍSTICAS DAS NOTAS")
    print(f"Notas: {notas}")
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Moda: {calcular_moda(notas)}")
    print(f"Desvio Padrão: {calcular_desvio_padrao(notas):.2f}")
    print(f"Menor Nota: {menor_nota(notas):.2f}")
    print(f"Maior Nota: {maior_nota(notas):.2f}")


