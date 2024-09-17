def charge(price):
    if price <= 50:
       total = 50 * 1.05
    else:
        total = price
    return total
print(charge(100)) 
print(charge(50))  