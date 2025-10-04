def luhn(card_number):
    card_number = card_number.replace('-', "").replace(" ", "")[::-1] 
    odd_digits=sum(int(k) for k in card_number[::2])
    even_digits=sum((int(k) *2-9) if int(k) *2>9 else int(k) *2 for k in card_number[1::2])  
    total=odd_digits + even_digits
    return total % 10 ==0
card_number=input("ENTER THE CARD NUMBER:")
if luhn(card_number):
    print("CARD NUMBER IS VALID")
else:
    print("CARD NUMBER IS NOT  VALID")
