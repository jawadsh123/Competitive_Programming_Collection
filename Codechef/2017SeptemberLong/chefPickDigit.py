

t = int(input())
ans = []

for i in range(t):
    number = input()

    digitPresent = [False for j in range(10)]
    digitCount = [0 for j in range(10)]
    fillCount = 0
    for idx, num in enumerate(number):
        num = int(num)
        if digitPresent[num] is False:
            digitPresent[num] = True
            fillCount += 1
        digitCount[num] += 1

    pickedChars = ""
    for asc_char in range(65, 91):
        asc_char = str(asc_char)
        
        if asc_char[0] == asc_char[1]:
            if digitPresent[int(asc_char[0])] and digitCount[int(asc_char[0])] > 1:
                # print(asc_char)
                pickedChars += chr(int(asc_char))
        elif digitPresent[int(asc_char[0])] and  digitPresent[int(asc_char[1])]:
            # print(asc_char)
            pickedChars += chr(int(asc_char))

    ans.append(pickedChars)

for x in ans:
    print(x)


