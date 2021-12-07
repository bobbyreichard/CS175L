def main():

    text = input('Enter a sentence: ')
        
    sentence=text.lower()

    count = 0
    total = 0

    most_freq = ""

    for ch in sentence:
        for str in sentence:
            if str == ch:

                count += 1
                
        if count > total:
            total = count
            most_freq = ch   
         
    print('The characater that appears most frequently in the string is', most_freq)

main()
