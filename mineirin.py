file = open('mineirin.txt', 'r')
lines = len(file.readlines())
file = file.readlines()


tokens = [{"soma": "+.+"}, {"subtracao": "-.-"}]

for linha in file:
    print(linha)
    # print(linhas[index])

# print(lines)
