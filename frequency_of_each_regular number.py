# Named constants
LOTTERY_NUMBERS = 69

def main():
    # Get a list of all the lottery numbers.
    lottery_list = get_numbers()
        
    # Create a list to hold each number's frequency. The list
    # is initialized with each element set to 0.
    reg_frequency = [0] * (LOTTERY_NUMBERS + 1)
    
    # Get the frequency of each regular number.
    for i in range(len(lottery_list)):
        
        # Get the next number in the list.
        n = int(lottery_list[i])
        
        # Increment that number's frequency.
        reg_frequency[n] += 1
        
    # Display the frequency of each regular number.
    print('Frequencies of the regular numbers')
    print('--------------------')
    for i in range(1, len(reg_frequency)):
        print(i, 'was chosen', reg_frequency[i], 'times')

# The get_numbers function returns a 2-dimensional list with
# two elements. The first element is a list of the regular lottery
# numbers, and the 2nd element is a list of the PowerBall numbers.
def get_numbers():

    # First 3 days of numbers: (ignore the last number (6th) in each row(day)
    #17 22 36 37 52 24
    #14 22 52 54 59 04
    #05 08 29 37 38 24
    # Open the lottery number file.
    lottery_file = open('pbnumbers.txt', 'r')
    
    # Read the file contents into a list hint: use .readlines.
    lottery_lines = lottery_file.readlines()
    
    # Close the file.
    lottery_file.close
    
    # Strip the newline ('\n') from each element.
    for i in range(len(lottery_lines)):
        lottery_lines[i] = lottery_lines[i].rstrip('\n')
        
    # Split .split() each element into 5 individual numbers, and store the
    # individual regular numbers in a list named lotto_nums. Hint: use nested 'for' loops.
    # For example, for first 3 days lotto_nums [17,22,36,37,52,14,22,52,54,59,05,08,29,37,38....]
    lotto_nums = []
    
    for x in range(len(lottery_lines)):
        numbers = lottery_lines[x].split()
        for y in range(len(numbers)- 1):
            lotto_nums.append(numbers[y])

    # Return the  list.
    return lotto_nums

# Call the main function.
if __name__ == '__main__':
    main()
