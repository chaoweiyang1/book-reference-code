#Default Arguments
def calCost(price, taxRate = 0.05):
    return price + price*taxRate

print(calCost(100))
# Output: 105.0
print(calCost(100, 0.075))
# Output: 107.5
