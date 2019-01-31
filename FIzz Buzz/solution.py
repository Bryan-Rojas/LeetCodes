def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    answer = []
    for i in range(1, n+1):
        temp = ''
        if i % 3 == 0:
            temp += 'Fizz'
        if i % 5 == 0:
            temp += 'Buzz'
        if temp == '':
            temp += str(i)
        answer.append(temp)
    return answer

print(fizzBuzz(100))