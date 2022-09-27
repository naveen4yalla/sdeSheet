def productOfAllElements(lst):
    product= []
    left = 1
    for f in lst:
        product.append(left)
        left = left * f
    right = 1
    for f in range(len(lst),-1,-1):
        product[f] = product[f] * right
        right = right * lst[f]
    return product