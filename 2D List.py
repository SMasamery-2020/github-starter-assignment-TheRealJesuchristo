#create a 2d list (array)
#first commit
#Second commit
from array import *
#Glasses of water per day in a week
water = [[11, 12, 5, 2],
         [15, 6, 10],
         [10, 8, 12, 5],
         [12, 15, 8, 6]]
'''print(water) #printing the array
print(water[3][3]) #printing row 3 column 3
print(water[2]) #printing row number 2'''

'''for row in range(0, len (water), 1):
    for column in range(0, len(water[row]), 1):
        if row == 1 and column == 2:
            water[row][column] = "hello"
        print(water[row][column], end=" ")
    print(end="\n")

    #print(water[i], end =" ")
    #print (end= "\n")
    #for each in water:
        #print(each, end = " ")'''


'''print("Item \t \tItem Number  \tQuantity \tIndividual Cost")
print("Microbit \tItem 1 \t\t\t\t40 \t\t\t$50")
print("Computer \tItem 2 \t\t\t\t20 \t\t\t$200")
print("Charger \tItem 3 \t\t\t\t100 \t\t$15")
print("Helicopter \tItem 4 \t\t\t\t1 \t\t\t$100,000")
print("Water  \t\tItem 5 \t\t\t\t1000 \t\t$2.50")'''

Stock = [
[1,"Microbit", 2, "\t\t\t\t$30"],
[2,"Computer", 3, "\t\t\t\t$200"],
[3,"Charger", 1, "\t\t\t\t$14"],
[4,"Helicopter", 1, "\t\t\t\t$2000"],
[5, "Water", 40, "\t\t\t\t\t$20"]]


def show_price(item_id):
    for item in Stock:
        if item[0] == item_id:
            print(f"The price of {item[1]} is {item[3]}")  # F is a format that is a replacement field
            return item[3]
    print("Item not found")
    return None


# Main Loop
while True:
    item_id = input("Enter the ID of the item you want to buy (or 'exit' to quit): ")
    if item_id.lower() == "exit":
        print("You have left the program.")
        break
    else:
        item_id = int(item_id)
        price = show_price(item_id)
        if price:
            decision = input("Do you want to buy this? (yes/no): ")
            if decision.lower() == "yes":
                print("Thank you for buying our product! :)")
            else:
                print("Choose another item if you want. :)")

for row in range(0, len (Stock), 1):
    for column in range(0, len(Stock[row]), 1):
        print(Stock[row][column], end=" ")
    print(end="\n")



