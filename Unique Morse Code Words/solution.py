def uniqueMorseRepresentations(words):
    alpha = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    temp1 = []
    temp2 = ''
    for item in words:
        for letter in item:
            temp2 += alpha[ord(letter)-97]
        temp1.append(temp2)
        temp2 = ''
    return(len(set(temp1)))

words1 = ['gin', 'zen', 'gig', 'msg']

print(uniqueMorseRepresentations(words1))