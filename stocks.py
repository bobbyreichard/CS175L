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
profitOrLoss = (totalRecieved - totalPaid)
#end results
print('Amount Paid for Stock: $', amountPaidForStock)
print('Commission paid on the purchase: $', purchaseCommission)
print('Amount the stock sold for $', stockSoldFor)
print('Commission paid on the sale: $', sellingCommission)
print('Profit (or loss if negative): $', profitOrLoss)
