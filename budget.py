budget = 5000000  # Budget for car purchase
purchase_price = int(input("Enter the purchase price of the car: "))

if purchase_price <= budget:
    print("Car purchased successfully!")
else:
    print("Order cancelled due to budget constraint.")
