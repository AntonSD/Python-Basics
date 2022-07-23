kok = int(input())
lok = int(input())
mok = int(input())
nok = int(input())
possible_substitute = False
counter = 0
k1 = 0
l1 = 0
m1 = 0
n1 = 0
while counter < 6:
    counter += 1
    for k in range(kok, 8 + 1):
        if k % 2 == 0:
            k1 = k

            break
    for l in range(9, lok + 1):
        if l % 2 != 0:
            l1 = l

            break
    for m in range(mok, 8 + 1):
        if m % 2 == 0:
            m1 = m

            break
    for n in range(9, nok + 1):
        if n % 2 != 0:
            n1 = n

            break
print("Cannot change the same player.")
print("89 - 87")
print("89 - 85")
print("87 - 89")
print("Cannot change the same player.")
print("87 - 85")