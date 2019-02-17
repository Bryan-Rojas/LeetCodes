def isValid(self, s: 'str') -> 'bool':
    if len(s) == 0:
        return True
    stack = []
    for letter in s:
        if (letter == '[') or (letter == '{') or (letter == '('):
            stack.append(letter)
        elif letter == ' ':
            return False
        else:
            if not stack:
                return False
            elif (letter == ']') and (stack.pop() != '['):
                return False
            elif (letter == ')') and (stack.pop() != '('):
                return False
            elif (letter == '}') and (stack.pop() != '{'):
                return False
    return stack == []