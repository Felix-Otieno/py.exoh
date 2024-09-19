def operaMix(number1, number2):
    product = number1 * number2
    total = number1 + number2

    
    if product <= 1000:
       return product
    else:
        return total
result = operaMix(20, 30)
print(result)
