total = 0
def main():
    file_object = open('numbers.txt,'r')
        for line in file_object:
            n += int(line)
            total += total + n
            average = total/n
            return(average)
main()
print(average)
