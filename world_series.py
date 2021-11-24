def main():
    try:
        #read file
        input_file = open('WorldSeriesWinners.txt', 'r')
        winners = input_file.readlines()

        input_file.close

    except IOError:
        print('There was an error opening the file')
    except ValueError:
        print('There was an error with the value input')
            
        #team and count wins
        repeat = True
        while repeat == True:
            team = str(input("Enter the name of a team, or enter 'Quit' to exit: "))
            if team == 'Quit':
                repeat = False
                break
            
            for team in winners:
                if(team == winners):
                    win_count += 1
        #results
            if win_count == 1:
                print('The', team, 'won the World Series', win_count, 'time between 1903 and 2009.')
            elif win_count > 1:
                print('The', team, 'won the World Series', win_count, 'times between 1903 and 2009.')
            else:
                print('The', team, 'never won the World Series between 1903 and 2009.')

if __name__=='__main__':
    main()
