spend = int(input("How much did the customer spend? "))
if spend < 10:
    print("The customer will get no voucher.")
elif spend > 20:
    print("The customer will get a $3 voucher.")
elif spend > 10:
    print("The customer will get a $1 voucher.")
         