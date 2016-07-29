mealCost=input()
tipPercent=input()
taxPercent=input()

tip = float(mealCost)*(float(tipPercent)/100)
tax= float(mealCost)*(float(taxPercent)/100)

totalCost= float(mealCost) + tip + tax

totalCost = round(totalCost)

print('The total meal cost is %d dollars.' % totalCost)