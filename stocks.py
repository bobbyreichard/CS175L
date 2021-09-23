#user input of data
COMMISSION_RATE = float(input('What was the commission rate?: '))
NUM_SHARES = int(input('How many shares did you purchase?: '))
PURCHASE_PRICE = float(input('What was the purchase price?: '))
SELLING_PRICE = float(input('What was the selling price?: '))
#data calculation
amountPaidForStock = (NUM_SHARES * PURCHASE_PRICE)
purchaseCommission = (COMMISSION_RATE * amountPaidForStock)
totalPaid = (amountPaidForStock + purchaseCommission)
stockSoldFor = (NUM_SHARES * SELLING_PRICE)
sellingCommission = (COMMISSION_RATE * stockSoldFor)
totalRecieved = (stockSoldFor - sellingCommission)
totalCommission = (purchaseCommission + sellingCommission)
profitOrLoss = (totalRecieved - totalPaid)
#end results
print('Amount Paid for Stock:',(f'${amountPaidForStock:,.2f}'))
print('Commission paid on the purchase:',(f'${purchaseCommission:,.2f}'))
print('Amount the stock sold for',(f'${stockSoldFor:,.2f}'))
print('Commission paid on the sale:',(f'${sellingCommission:,.2f}'))
print('Total commission paid:',(f'${totalCommission:,.2f}'))
#determining profit, loss, or breakeven
if profitOrLoss > 0:
    print('Your loss is:',(f'${profitOrLoss:,.2f}'))
if profitOrLoss < 0:
    print('Your profit is:',(f'${profitOrLoss:,.2f}'))
if profitOrLoss == 0:
    print('Your return is:',(f'${profitOrLoss:,.2f}'))
