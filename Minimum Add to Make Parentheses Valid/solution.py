def minAddToMakeValid(self, S: str) -> int:
    left = right = 0

    for x in S:
        if x == '(':
            left += 1
        else:
            if left == 0:
                right += 1
            else:
                left -= 1

    return left + right
