class ItemToPurchase:
    
    def __init__(self, item_name = "", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity 
    
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$" + str(format(self.item_price,".2f")), "=", "$"+ str(format((self.item_price *self.item_quantity),".2f")))
    #Set up printing statement



item1 = ItemToPurchase()
item2 = ItemToPurchase() 
#Created Item #1 and #2


#Set Up
print("Please enter two items:")

print("Item #1")


print("Enter the item name:")
name1= input()


print("Enter the item price:")
price1= float(input())


print("Enter the item quantity:")
quantity1= int(input())
#Collects Data for Item #1


print("Item #2")


print("Enter the item name:")
name2= input()


print("Enter the item price:")
price2= float(input())


print("Enter the item quantity:")
quantity2= int(input())
#Copy and paste of Item #1 with item2 instered in


item1 =ItemToPurchase(name1,price1,quantity1)
item2 =ItemToPurchase(name2,price2,quantity2) 



print("TOTAL COST")

item1.print_item_cost()
item2.print_item_cost()

print("Total:", "$"+ str(format(((item1.item_price*item1.item_quantity) + (item2.item_price * item2.item_quantity)),".2f")))
