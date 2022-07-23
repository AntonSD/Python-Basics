start = int(input())
end = int(input())
magic_number = int(input())
flag = False
counter = 0
for i in range (start, end + 1):
    for j in range (start, end + 1):
        sum = i + j
        counter += 1
        if sum == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")