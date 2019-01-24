def diStringMatch(S):
    i, j, answer = 0, len(S), []

    for char in S:
        if char == 'I':
            answer.append(i)
            i += 1
        else:
            answer.append(j)
            j -= 1

    answer.append(j if S[-1] == 'D' else i)

    return answer

input1 = 'IDID'
input2 = 'III'
input3 = 'DDDDDDDDDDDDDDDDDDDD'

print(diStringMatch(input1))
print(diStringMatch(input2))
print(diStringMatch(input3))