import re

with open('fizz.txt', 'w') as outfile:
    with open('numbers.txt', 'r') as file:
        for line in file:
            numbers = re.findall('(\d+)', line)
            a = int(numbers[0])
            b = int(numbers[1])
            c = int(numbers[2])
            for numbers in range(1, c+1):
                if numbers % a == 0:
                    outfile.write('F')
                elif numbers % b == 0:
                    outfile.write('B')
                elif numbers % a == 0 and numbers % b == 0:
                    outfile.write('FB')
                elif numbers == c:
                    outfile.write('  ')
                else:
                    outfile.write(str(numbers))