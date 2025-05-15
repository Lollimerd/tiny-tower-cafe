import sys, time
from pyfiglet import Figlet
# text art
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
#  constructor                    default width 225 pc width 275
console = Console(soft_wrap=True, width=225, emoji=True, record=True, force_interactive=True, force_terminal=True)

#################### loading screen ##################################
with console.status("[bold purple4]loading...", spinner='arc', refresh_per_second=15) as status:
    time.sleep(2.5)
console.log("Done :thumbs_up:", style='bold green')

######################## title #####################################
f = Figlet(font='larry3d', width=250)
# rmb to \n on title if on laptop if not remove it
console.print(f.renderText("Welcome To Tiny Tower Cafe!"), style='bold orchid blink2')

def mainMenu():
    while True:
        MARKDOWN = """
# Main Section
Select one of the following below to begin your shopping:
1. View the items available
2. Add or edit items in your shopping cart 
3. Removing items
4. Check shopping cart
5. Checkout and payment
6. More info about Tiny Tower Cafe
7. Exit """
        md = Markdown(MARKDOWN)
        console.print(Panel(md, style="bold dodger_blue1", title='Main Menu'))
        selection = console.input("\nWhat is your number of choice: ")
        print()
        if selection == '1':
            subMenu()
        elif selection == '2':
            additem()
        elif selection == '3':
            removeitem()
        elif selection == '4':
            cart()
        elif selection == '5':
            d = console.input(":mega: Note: There is no going back. "
                              "Once you receive your receipt you cant edit your shopping cart"
                      "\nDo you confirm your purchase? Y/N (If no, screen returns to main menu): ")
            if d == 'Y':
                checkout()
            elif d == 'N':
                with console.status("[green]going back main menu", spinner='pipe') as status:
                    time.sleep(1.5)
                mainMenu()
            else:
                console.print("transaction failed", style='bold red')
                mainMenu()
        elif selection == '6':
            info()
        elif selection == '7':
            console.print("Goodbye :wave:")
            sys.exit()
        else:
            console.print("That is not a valid selection.", style='bold red')

item_list = {"Espresso": 5.50, "Iced Coffee": 4.95, "Latte": 4.95,
             "Earl Grey": 4.50, "Sakura Green Tea": 5.00, "Chamomile Peppermint Tea": 5.00,
             "Brownie Gelato": 5.95, "Strawberry Pudding": 4.25, "Chocolate Cheesecake": 5.90}
shopping_cart = {}

# indexing of order system
items = [h for h in item_list.keys()]
selecting = [num for num in range(1, 11)]
orders = {number: item for number, item in zip(selecting, items)}

# quantity order (prices)
everything = [x for x in item_list.values()]
# quantity = [[index, prices] for index in selecting for prices in everything]

# stock sales
stock = [20, 20, 20, 20, 20, 20, 20, 20, 20]
stocks = {inv: no for inv, no in zip(selecting, stock)}

def subMenu():
    console.print("\nAll prices are gst included", style='green')
    mnds = """
# Display lists of items
How would you like to view by?
1. By Category
2. By alphabetical order 
3. From cheapest to most expensive"""
    mkdn = Markdown(mnds)
    console.print(Panel(mkdn, style='bold dark_cyan', title='sub menu 1', width=135))
    view = input("\nEnter your number: ")
    if view == '1':
        displaycat()
    elif view == '2':
        abc()
    elif view == '3':
        pricing()
    else:
        console.print("Wrong input.", style='bold red')

def displaycat():
    cofitem = [c for c in items[:3]]
    cofval = [d for d in everything[:3]]
    console.print("\nCoffee :coffee:", style='dark_goldenrod')
    for cd, ce in zip(cofitem, cofval):
        console.print(f'{cd}: ${ce:.2f}')

    teaitem = [d for d in items[3:6]]
    teaVal = [g for g in everything[3:6]]
    console.print("\nTea :tea:", style="bold blue")
    for gg, te in zip(teaitem, teaVal):
        console.print(f'{gg}: ${te:.2f}')

    desitem = [d for d in items[6:9]]
    desval = [v for v in everything[6:9]]
    console.print("\nDesserts :cupcake:", style="bold pale_green1")
    for a, b in zip(desitem, desval):
        console.print(f'{a}: ${b:.2f}')

def abc():
    print()
    for key in sorted(item_list.keys()):
        console.print(key)
    print()

def pricing():
    print()
    prices = [n for n in item_list.values()]
    prices.sort()
    price_list = {items: price for items, price in zip(item_list.keys(), prices)}
    for s in price_list:
        console.print(s, "${:.2f}".format(price_list[s]), sep=": ")

def cart():
    if shopping_cart == {}:
        console.print("Your shopping cart is empty.")
    else:
        console.print("_______________________________", style='magenta')
        for e in shopping_cart:
            console.print("- " + e, shopping_cart[e], sep=": ")
        console.print("_______________________________")
        totalitems = [c for c in shopping_cart.values()]
        num = sum(totalitems)
        console.print("You have", int(num), "items in shopping cart.", style='bold yellow')
        print()

inputcost = {}
inputremove = {}

def multiple(num, itemprice):
    no = orders.get(num)
    stocks[num] = stocks.get(num) - itemprice
    stocklist = {i: b for i, b in zip(items, stocks.values())}
    print("\nStock count: ")
    if stocks.get(num) >= 0:
        print("If", no, "reaches 0, please do not buy it.")
    elif stocks.get(num) <= 0:
        pass
        stocklist[no] = 0
        print("Error:", no, "not found.")
    print()
    for i in stocklist:
        console.print(i, stocklist[i], sep=": ")
    inputcost[no] = itemprice

def additem():
    console.print("Based on the items of your choice, refer to the numbers on the left of its respective items.",
                  "If there is nothing to buy, press 0 to skip. ", style='cyan')
    for z in orders:
        console.print(z, orders[z], sep=": ", style='bold magenta')
    ordering = int(input("\nSelect 1 to 9 to purchase your items in the list above: "))
    if ordering in orders:
        purchase = orders.get(ordering)
        itemno = int(input("\nHow many " + purchase + " would you like to buy? (max: 10 items only): "))
        if ordering <= 0:
            console.print("Sorry. This value is unacceptable.", style='bold red')          # I can delete this
        elif itemno > 10:
            pass
            console.print("\nAbove limit. Quantity not accepted.", style='bold red')
            mainMenu()
        elif itemno <= 0:
            pass
            console.print("\nPlease select a suitable quantity", style='bold red')
            mainMenu()
        shopping_cart[purchase] = shopping_cart.get(purchase, 0) + itemno
        multiple(ordering, itemno)
        if shopping_cart.get(purchase) > 20:
            shopping_cart[purchase] = 20
            console.print("\nNo more stock. Unable to buy anymore", purchase, style='bold red')
            mainMenu()
        console.log(f'{itemno} {purchase} has been added to shopping cart', style="green")
    elif ordering == 0:
        with console.status("[bold green]Skipping...", spinner='pong') as status:
            time.sleep(3)
        console.log("Skipped")
        mainMenu()
    else:
        print("\nThat is not available in the cafe. Please try again.")

def checking(seeing, many):
    finding = orders.get(seeing)
    inputremove[finding] = many
    stocks[seeing] = stocks.get(seeing) + many

def removeitem():
    console.print("Press 0 if there is nothing to remove or skip.", style='magenta')
    for z in orders:
        console.print(z, orders[z], sep=": ", style='light_goldenrod2')
    console.print("\nRefer to shopping cart to see what you have.", style='cyan')
    selects = int(input("\nWhich item would you like to remove: "))
    delete = orders.get(selects)
    removes = int(input(f"Enter the amount of {delete} you wish to remove from your shopping cart: "))
    if selects in orders:
        shopping_cart[delete] = shopping_cart.get(delete, 0) - removes
        if shopping_cart.get(delete) <= 0:         # 0 or -ve
            del shopping_cart[delete]
            console.print("There is no quantity in that particular item or the quantity is a negative value.",
                          style='bold red')
        elif shopping_cart.get(delete) >= removes:
            console.log(f"{removes} {delete} has been removed from the shopping cart.", style='green')
            checking(selects, removes)
        elif selects == 0:
            with console.status("[bold green]Skipping...", spinner='pong') as status:
                time.sleep(3)
                console.log("Skipped")
            mainMenu()
    else:
        console.print("\nThere is no such item in the list. Please try again.", style='red')

def Receipt():
    console.print("""      
--------------------------------------------------------------------------------------------------
                             Tiny Tower Cafe
                        Online Shopping Receipt
--------------------------------------------------------------------------------------------------""", style='red')
    prices = [item_list.get(a) * shopping_cart[a] for a in shopping_cart]
    item_count = sum(shopping_cart.values())
    total = sum(prices)
    gst = total * 0.07
    normalPrice = total + gst
    for numitem, itembought, cost in zip(shopping_cart.values(), shopping_cart.keys(), prices):
        print(f"{numitem} {itembought}: ${cost:.2f}")
    print(f"\nTotal items bought:                               {item_count}")
    print(f"Subtotal:                                          ${total:.2f}")
    print("Discount:                                         - $0.00")
    print(f"GST:                                             + ${gst:.2f}")
    print(f"Total:                                             ${normalPrice:.2f}")
    console.print(""
"------------------------------------------------------------------------------------------------", style='red')
    print("Thank you for your time!"
          "\nPlease come again next time.")
    shopping_cart.clear()

def disreceipt():
    console.print("""
-----------------------------------------------------------------------------------------
                                   Tiny Tower Cafe
                              Online Shopping Receipt
                                    Basic Member
-----------------------------------------------------------------------------------------""", style='bold green')
    item_count = sum(shopping_cart.values())
    prices = [shopping_cart[f] * item_list.get(f) for f in shopping_cart]
    all = sum(prices)
    dis = all * 0.15
    gst = all * 0.07
    discountedPrice = all + gst - dis
    for no_item, name, c in zip(shopping_cart.values(), shopping_cart.keys(), prices):      # each individual items
        print(f'{no_item} {name}: ${c:.2f}')
    print(f"\nTotal items bought:                                                {item_count}")
    print(f"Subtotal:                                                          ${all:.2f}")
    print(f"Discount:                                                        - ${dis:.2f}")
    print(f"GST:                                                             + ${gst:.2f}")
    print(f"Total:                                                             ${discountedPrice:.2f}")
    console.print(""
"=========================================================================================", style='bold green')

def checkout():
    discount = input("Do you have a membership card? "
                     "(only those who has membership have the perk to shop again) yes/no : ")
    if discount == 'yes':
        collate = [item_list.get(r)*shopping_cart[r] for r in shopping_cart]
        if sum(collate) > 15:  # default discount
            disreceipt()
        else:
            print("Sorry I am afraid you have yet apply for membership. "
                  "Only purchase above $15 then can enjoy membership perks."
                  "")
            mainMenu()
        ask = console.input("Do you want to shop again or exit? (Press 1 if you want to continue shopping, "
                            "or press anything else to exit): ")
        if ask == "1":
            shopping_cart.clear()
            mainMenu()
        else:
            console.print("See you next time! :smile:")
            sys.exit()
    elif discount == 'no':
        print("You will not be able to accumulate your points and this is a 1 time purchase.")
        Receipt()
        sys.exit()
    else:
        print("Unauthorised payment. Try again.")
        mainMenu()

def info():          # sub menu 2
        marks = """
# Info regarding the cafe
1. About our items, prices and discounts
2. Redeem prizes and check points
3. Application for membership and membership perks"""
        mknd = Markdown(marks)
        console.print(Panel(mknd, width=139, style='bold yellow', title='sub menu 2'))
        user = console.input("What would you like to know? ")
        if user == '1':
            table1()
        elif user == '2':
            pts_define()
        elif user == "3":
            membershipMenu()
        else:
            print("Bruh, you trolling me right")

def table1():    # for the column
    table = Table(show_header=True, header_style='bold cyan', title='Items Summary', title_justify='center')
    table.add_column("Category", style='dim', justify='left')
    table.add_column("Item")
    table.add_column("Price Exclusive GST", justify='left')
    table.add_column("GST(7%)")
    table.add_column("Membership Discount", justify='center')
    # coffee
    table.add_row("", "Espresso", "$5.50", "$0.39", "Yes", style='red')
    table.add_row("Coffee", "Iced Coffee", "$4.95", "$0.35", "No", style='red')
    table.add_row("", "Latte", "$5.00", "$0.35", "No", style='red', end_section=True)
    # tea
    table.add_row("", "Earl Grey", "$4.50", "$0.32", "No", style='magenta')
    table.add_row("Tea", "Sakura Green Tea", "$5.00", "$0.35", "Yes", style='magenta')
    table.add_row("", "Chamomile Peppermint Tea", "$5.00", "$0.35", "No", end_section=True, style='magenta')
    # desserts
    table.add_row("", "Brownie Gelato", "$4.95", "$0.35", "Yes", style='yellow')
    table.add_row("Desserts", "Strawberry Pudding", "$4.25", "$0.30", "No", style='yellow')
    table.add_row("", "Chocolate Cheesecake", "$5.90", "$0.41", "Yes", style='yellow')

    console.print(table)

# includes discount only for membership  (more discounts)
def pts_define():
    pric = [item_list.get(q)*inputcost.get(q) for q in inputcost]
    mins = [item_list.get(w)*inputremove.get(w) for w in inputremove]
    prices_peritem = sum(pric) - sum(mins)
    ptsnum = prices_peritem/1.25
    print("You have {:.2f} points".format(ptsnum))
    redeem = input("Would you like to redeem any free gifts? y/n: ")
    if redeem == 'y':
        prizes(ptsnum)
    elif 'no':
        console.print("Don't worry, maybe in the future. :smiley:")

def prizes(points):
    if points < 25.0:
        print("\nYour points have not reached the minimum requirement, 25 pts.")
    elif 50.0 >= points >= 25.0:
        console.print("\nYou can redeem a free limited edition tiny tower cup :cup_with_straw:")
    elif 75.0 >= points >= 50.0:
        print("\nYou can redeem a free set meal of a coffee/tea of your choice, "
              "a dessert and can have additional 15% discount for your future purchases.")
    elif 50 >= points >= 75.0:
        print("\nFor every purchase you make, you can get a free merchandise of your choice.")
    elif 75 >= points >= 100.0:
        print("\nYou can edit your purchase history. ")

def membershipMenu():
    print("This is exclusive for customers who have a purchase of $50 and above.")
    Marking = """
# Membership Menu
Please select one of the following:
1. Check your purchase logs
2. What are the perks if you apply for membership"""
    mnd = Markdown(Marking)
    console.print(Panel(mnd, width=117, style='bold cyan', title='Exclusive'))
    membership = input("\nWhat would you like to do: ")
    if membership == '1':
        logs()
    elif membership == '2':
        description()
    else:
        console.print("Wrong input", style='bold red')

# the receipt for the additional membership perks will be diff from normal discount

def description():
    console.print(Panel("""
No membership: Users here are unable to accumulate points and data is canceled upon every purchase.

To apply for membership, you need to have a minimum purchase of up to $15. You will become a basic member of Tiny Tower cafe.

Basic membership: 15% off total price discount

Veteran membership: You will need to have a minimum purchase of $40 
For the registration, you will receive a OTP (One Time Password). 
If the password is correct, you can purchase set meals, which is overall cheaper.

gaining pts:
For every $1.25 earn 1 point

Making it a set:
- 1 tea or coffee with a dessert of your choice for $7.50

Veteran member:
- able to access your logs of what you have added and removed
- can delete history or can check your membership progress
""", style='bold red', title='Description'))

def logs():
    while True:
        console.print("You have removed...", style='red')
        for k, d in zip(inputremove.keys(), inputremove.values()):
            print(f'-{d} {k}')
        console.print("\nYou have added...", style='green')
        for c, g in zip(inputcost.values(), inputcost.keys()):
            print(f'-{c} {g}')
        ask = input("Do you want to delete your purchase history? y/n: ")
        if ask == 'y' or 'Y':
            inputcost.clear()
            inputremove.clear()
            mainMenu()
        elif ask == 'n' or 'N':
            console.print("Alright")
            mainMenu()
        else:
            console.print("Invalid key error", style='bold red')
            pass

print()
mainMenu()



