filename = input("Enter the filename: ")
word = input("Enter the word to search for: ")
count = 0

file= open(filename, 'r')
line = file.readline()



while line:
    if word in line:
        count+=1
    line= file.readline()

print(count)

file.close()




