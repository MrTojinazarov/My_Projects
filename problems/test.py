qatorlar_soni = 3
ustunlar_soni = 3

matritsa = [[0 for _ in range(ustunlar_soni)] for _ in range(qatorlar_soni)]

son = 1
for i in range(qatorlar_soni):
    for j in range(ustunlar_soni):
        matritsa[i][j] = son
        son += 1

print(matritsa)
