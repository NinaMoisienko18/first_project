def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price

price_bread = 15
discount = 0.5
price_after_discount = discount_price(price_bread, discount)
print(f"Original price - {price_bread}, price of bread after applying {int(discount * 100)} % of discount - {price_after_discount}")