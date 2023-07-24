item = []
quantity = []
price = []


about=('\nTHANKS FOR CHOOSING PELLAS STORE..\n We deal with all kind of gloceries,drinks,etc\nYou can order any product you want straight from home and will be delivered to you in less than 20 mins..\n\nTHANK YOU')
while True:
    
    user_choose= int(input('\n\n*****PELLA STORE****\n\n1.BUY ITEM\n2.VIEW CART\n3.REMOVE FROM CART\n4.MAKE PURCHASE\n5.ABOUT US\n6.EXIT APP\n\nPROVIDE OPTION: '))
    
    if user_choose==1:
        item = input('Enter Product: ')
        quantity = int(input('Enter Quantity: '))
        price = int(input('Enter Price: '))
        
    elif user_choose==2:
            print(item)
    
    elif user_choose==3:
        item.clear()
   
    elif user_choose==4:
       amount = (quantity*price)   
       print('TOTAL AMOUNT:GH',amount)
       payment = int(input('Enter PAYMENT: '))
       if payment==amount:
           print('PAYMENT DONE SUCCESSFULLY')
       elif payment>amount:
           addition=(payment-amount)
           print('PAYMENT SUCCESSFUL.. YOU HAVE A BALANCE OF GHC ',addition,)
       elif payment<amount:
           sub=(amount-payment)
           print('PAYMENT NOT INTACT...ADD A FUND OF GHC ',sub)
    elif user_choose==5:
        print(about)
    elif user_choose==6:
        break
                