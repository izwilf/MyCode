# Programming Exercise 10-7
import sys
from retailitem import RetailItem
import cashregister
# Constants to hold the options of purchase items
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# define get user choice
def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Pants')
    print('2. Shirt')
    print('3. Dress')
    print('4. Socks')
    print('5. Sweater')
    print()

    choice = int(input('Enter the menu number of the item ' + \
                       'you would like to purchase: '))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input('Please enter a valid item number: '))
        print()

    return(choice)


# main method
def main():

    # Create sale items.
    pants = RetailItem('Pants', 10, 19.99, 1)
    shirt = RetailItem('Shirt', 15, 12.50, 2)
    dress = RetailItem('Dress', 3, 79.00, 3)
    socks = RetailItem('Socks', 50, 1.00, 4)
    sweater = RetailItem('Sweater', 5, 49.99, 5)
    items = [pants, shirt, dress, socks, sweater ]
    # Create dictionary of sale items.
    sale_items = {PANTS:pants, SHIRT:shirt,
                  DRESS:dress, SOCKS:socks,
                  SWEATER:sweater}

    # Initialize loop test.
    checkout = 'N'
    totalprice = 0
    # Create a cash register.
    register = []
    # User wants to purchase more items:
    while checkout == 'N':
        user_choice = get_user_choice() - 1
        item = items[user_choice]
        
        '''
        #If the item's iventory is 0 type 'The item is out of stock.'
        Otherwise,  1) add the item to the register  
                    2) change the inventory number of the item in the sale_items dictionary
                    3) ask the user if they're ready to checkout Y/N and save that in the checkout var
        '''
        if item.units == 0:
            print("The item is out of stock")
        else:
            register.append(item)
            totalprice += item.price
            item.units -= 1
            checkout = input("Are you ready to check out (Y/N)? ")
    print()
    print('Your purchase total is: ', \
          format(totalprice, '0.2f') + "\n")
    print("The items in the cash register are: \n")
    for item in register:
        print("Description: " + str(item.description))
        print("Units in inventory: " + str(item.units))
        print("Price: $" + format(item.price, '0.2f') + "\n")


# Call the main function.
main()