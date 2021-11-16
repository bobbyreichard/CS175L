def main():
    try: 
        file = open('numbers.txt','r')
        infile_lines = "x"
        total = 0
        n = 0
        while infile_lines != '':
            infile_lines = file.readline()
            if infile_lines == '':
                break
            n = n + 1
            infile_lines = int(infile_lines)
            total = total + infile_lines
        
        file.close
        return average_numbers(total, n)
        except IOError:
            print('There was an IOError.')
        except ValueError:
            print('There was an ValueError')    

def average_numbers(total, n):
    average = total/n
    print(average)


if__name__='__main':
main()
