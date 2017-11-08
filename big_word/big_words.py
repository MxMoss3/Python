word = input('')
alphabet = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
output = []


with open('letters.txt', 'r+') as let:
    full = (let.read().split('\n'))

for i in range(5):
    line = ''
    for char in word:
        num = (alphabet.index(char))*5
        line += full[(num + i)] + ' '
    output.append(line)

for i in output:
    print(i)
   
