count=0
rate=10
totalcost=0
def add_keychain(n):
    global count
    count=count+n
    return (f"you have {count} keychains")

def remove_keychain(n):
    global count
    count=count-n
    return (f"now you have {count} keychains")

def view_order():
    global count
    global rate 
    global totalcost
    totalcost=rate*count
    return (f"you have {count} keychains \nThe price per keychain is ${rate} \nThe total cost is ${totalcost}")

def checkout(name):
    global count
    global rate 
    global totalcost
    return (f"you have {count} keychains \nThe price per keychain is ${rate} \nThe total cost is ${totalcost} \nThank you for order, {name}")

user=0
while user<4:
    print("\n1.Add ketchains to  order \n2.Remove keychain from the order \n3.View current order \n4.Checkout \n")
    user=int(input("Please enter your choice: "))
    if user==1:
        add=int(input("\nHow many chains you need to add: "))
        print("\n",add_keychain(add))
    if user==2:
        remove=int(input("\nHow many chains you want to remove: "))
        print("\n",remove_keychain(remove))
    if user==3:
        print("\n",view_order())
    if user==4:
        name=input("What is you name? ")
        print("\n",checkout(name))

