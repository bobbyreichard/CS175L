#declaring variables
years = int(input("How many years?: "))
months = 12
rainfall = 0
total_rainfall = 0
total_months = years * 12
#loops
if years < 1 or years > 3:
    print("Re-Enter Year")
else:
    for year in range (years):
        print('For year: ', year + 1,'')
        for months in range(0,12):
            print('Enter the inches of rainfall for month', months + 1, '')
            rainfall = float(input())
            total_rainfall = total_rainfall + rainfall
            average_rainfall = total_rainfall/months
#final
print('Total inches of rainfall: ', total_rainfall)
print('Number of months: ', total_months)
print('Average rainfall per month:', f'{average_rainfall: .2f}', 'inches')
