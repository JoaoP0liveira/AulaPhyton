print("Digite um número:")
n1 = int(input())

print("Digite outro número:")
n2 = int(input())

print("==========================")

# if n1 % 2 != 0:
#     n1 += 1
    
# for x in range(n1, n2 + 1, 2):
#     print(x)

for y in range (n1, n2 + 1):
    if y % 2 == 0: 
        print("o Numero é par: ", y)
