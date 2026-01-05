#python prgram that will greet , manage , take order ,show summary and total amountof bill
menu= {
    "coffee":80,
    "tea":60,
    "sandwich":130,
    "salad":390,
    "dessert":150,
    "juice":120,
    "water":30
}

#------------------------------------------------------------------------------------------
#Greet the coustmer and display the menu
print("welcome to our cafe 😊")
print(''' here is the menu :
coffee : 80
tea : 60
sandwich : 130
salad : 390
dessert : 150
juice : 120
water : 30
      ''')

#-------------------------------------------------------------------------------------------
#taking orders
order_list= []
while True:
    item = input("ENTER THE ITEMS YOU WANT TO ORDER " \
    "IF DONE TYPE done :").lower()
    if item == 'done':
        break
    if item in menu :
        order_list.append(item)
        print(f"{item} added to your order. ")
    else:
        print("item not avaliable ")

#--------------------------------------------------------------------------------------------
# Calculating the total bill
total_bill=sum(menu[item] for item in order_list) 
print("\n your order summary :", order_list)

print(f" Total bill : ₹{total_bill}")

#---------------------------------------------------------------------------------------------
print(" Thank you for visiting our cafe! Have a great day! 😊😊")

