# Tiny Tower Cafe - User Documentation

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Main Menu Options](#main-menu-options)
  - [View Items](#view-items)
  - [Add Items](#add-items)
  - [Remove Items](#remove-items)
  - [Check Shopping Cart](#check-shopping-cart)
  - [Checkout and Payment](#checkout-and-payment)
  - [Cafe Information](#cafe-information)
- [Membership System](#membership-system)
  - [Basic Membership](#basic-membership)
  - [Veteran Membership](#veteran-membership)
  - [Point System](#point-system)
  - [Rewards](#rewards)
- [Code Examples](#code-examples)
  - [Data Structures](#data-structures)
  - [Menu Navigation](#menu-navigation)
  - [Shopping Cart Management](#shopping-cart-management)
  - [Checkout Process](#checkout-process)
- [Console Output Examples](#console-output-examples)
- [Technical Information](#technical-information)

## Introduction

Tiny Tower Cafe is an interactive shopping application that allows users to browse and purchase various cafe items including coffee, tea, and desserts. The application features a user-friendly text-based interface enhanced with colorful visuals and animations.

## Getting Started

When you start the application, you'll see a loading screen followed by a welcome title "WELCOME TO TINY TOWER CAFE!" rendered in an artistic font. After the introduction, you'll be presented with the main menu where you can navigate through different options.

## Technical Information

The application is built using Python with the following libraries:
- `pyfiglet`: For text art and typography
- `rich`: For enhanced terminal formatting, tables, and visual elements including:
  - `Console`: For enhanced text output with styling
  - `Table`: For tabular data presentation
  - `Markdown`: For rendering markdown formatted text
  - `Panel`: For creating bordered text panels

The system tracks inventory through a stock management system that updates when items are added to or removed from the shopping cart.

## Main Menu Options

The main menu offers seven options:

### View Items

This option lets you browse the cafe's offerings in three different ways:

1. **By Category**: Items are grouped into Coffee, Tea, and Desserts
   - **Coffee**: Espresso ($5.50), Iced Coffee ($4.95), Latte ($4.95)
   - **Tea**: Earl Grey ($4.50), Sakura Green Tea ($5.00), Chamomile Peppermint Tea ($5.00)
   - **Desserts**: Brownie Gelato ($5.95), Strawberry Pudding ($4.25), Chocolate Cheesecake ($5.90)

2. **By Alphabetical Order**: Items are listed in alphabetical order

3. **From Cheapest to Most Expensive**: Items are listed from lowest to highest price

### Add Items

To add items to your shopping cart:

1. Select option 2 from the main menu
2. Choose an item by entering its corresponding number (1-9)
3. Specify the quantity you wish to purchase (maximum of 10 per transaction)
4. The system will update your shopping cart and show the remaining stock for the selected item

Note: Each item has a stock limit of 20 units. If you try to purchase more than what's available, the system will notify you.

### Remove Items

To remove items from your shopping cart:

1. Select option 3 from the main menu
2. Choose the item you wish to remove by entering its corresponding number
3. Specify the quantity to remove
4. The system will update your shopping cart accordingly

If you remove all of a particular item, it will be deleted from your cart entirely.

### Check Shopping Cart

This option displays:
- All items in your cart with their quantities
- The total number of items in your cart

If your cart is empty, you'll be notified.

### Checkout and Payment

To complete your purchase:

1. Select option 5 from the main menu
2. Confirm your purchase by entering 'Y' (or 'N' to return to the main menu)
3. Specify whether you have a membership card
   - With membership: You'll receive a 15% discount for orders over $15 and can continue shopping
   - Without membership: Your purchase will be processed once and you'll exit the application

Upon checkout, you'll receive a detailed receipt showing:
- Items purchased with quantities and prices
- Subtotal
- Discount (if applicable)
- GST (7%)
- Total amount

### Cafe Information

This section provides additional information about the cafe:

1. **About Items, Prices, and Discounts**: Displays a table with all items, their prices (exclusive of GST), GST amounts, and membership discount eligibility

2. **Redeem Prizes and Check Points**: Shows your current points and available rewards

3. **Membership Application and Perks**: Provides information about membership levels and benefits

## Membership System

Tiny Tower Cafe offers a tiered membership program with various benefits.

### Basic Membership

Requirements:
- Minimum purchase of $15

Benefits:
- 15% discount on all purchases
- Ability to accumulate points
- Option to continue shopping after checkout

### Veteran Membership

Requirements:
- Minimum purchase of $40
- OTP (One Time Password) verification

Benefits:
- All basic membership benefits
- Access to set meal options ($7.50 for a drink and dessert combination)
- Ability to view purchase logs and history
- Option to delete purchase history

### Point System

Points are earned at a rate of 1 point for every $1.25 spent.

### Rewards

Based on your accumulated points, you can redeem various rewards:
- 25-50 points: Free limited edition Tiny Tower cup
- 50-75 points: Free set meal and 15% discount on future purchases
- 75-100 points: Free merchandise with every purchase
- 100+ points: Ability to edit purchase history

## Code Examples

### Data Structures
The application uses several key data structures to manage inventory and the shopping cart:
Examples being used are list and dictionary comprehension.

```python
# Item inventory with prices
item_list = {
    "Espresso": 5.50, "Iced Coffee": 4.95, "Latte": 4.95,
    "Earl Grey": 4.50, "Sakura Green Tea": 5.00, "Chamomile Peppermint Tea": 5.00,
    "Brownie Gelato": 5.95, "Strawberry Pudding": 4.25, "Chocolate Cheesecake": 5.90
}

# Shopping cart to track user selections
shopping_cart = {}

# Item indexing system for the order process
items = [h for h in item_list.keys()]
selecting = [num for num in range(1, 11)]
orders = {number: item for number, item in zip(selecting, items)}

# Stock tracking system
stock = [20, 20, 20, 20, 20, 20, 20, 20, 20]
```

### Shopping Cart Management

Adding items to the shopping cart:

```python
# Display available items
for z in orders:
    console.print(z, orders[z], sep=": ", style='bold magenta')

# Get user selection and quantity
ordering = int(input("\nSelect 1 to 9 to purchase your items in the list above: "))
purchase = orders.get(ordering)
itemno = int(input("\nHow many " + purchase + " would you like to buy? (max: 10 items only): "))

# Update shopping cart
shopping_cart[purchase] = shopping_cart.get(purchase, 0) + itemno
multiple(ordering, itemno)

# Confirm addition to cart
console.log(f'{itemno} {purchase} has been added to shopping cart', style="green")
```

### Checkout Process

Processing payment and generating a receipt:

```python
# Check for membership status
discount = input("Do you have a membership card? "
                 "(only those who has membership have the perk to shop again) yes/no : ")

# Apply membership discount if eligible
if discount == 'yes':
    collate = [item_list.get(r)*shopping_cart[r] for r in shopping_cart]
    if sum(collate) > 15:  # default discount
        disreceipt()  # Generate receipt with discount
    else:
        print("Sorry I am afraid you have yet apply for membership. "
              "Only purchase above $15 then can enjoy membership perks.")
        
# For non-members, generate standard receipt
elif discount == 'no':
    print("You will not be able to accumulate your points and this is a 1 time purchase.")
    Receipt()  # Generate standard receipt
```

## Console Output Examples
### Main Menu
```python
┌Main Menu──────────────────────────────────────────────────────────────────────┐
│ # Main Section                                                                 │
│ Select one of the following below to begin your shopping:                      │
│ 1. View the items available                                                    │
│ 2. Add or edit items in your shopping cart                                     │
│ 3. Removing items                                                              │
│ 4. Check shopping cart                                                         │
│ 5. Checkout and payment                                                        │
│ 6. More info about Tiny Tower Cafe                                             │
│ 7. Exit                                                                        │
└────────────────────────────────────────────────────────────────────────────────

What is your number of choice:
```

### Category Display Output
```python
Coffee ☕
Espresso: $5.50
Iced Coffee: $4.95
Latte: $4.95

Tea 🍵
Earl Grey: $4.50
Sakura Green Tea: $5.00
Chamomile Peppermint Tea: $5.00

Desserts 🧁
Brownie Gelato: $5.95
Strawberry Pudding: $4.25
Chocolate Cheesecake: $5.90
```

### Sample Receipt Output
```python
--------------------------------------------------------------------------------------------------
                             Tiny Tower Cafe
                        Online Shopping Receipt
--------------------------------------------------------------------------------------------------
2 Espresso: $11.00
1 Sakura Green Tea: $5.00
1 Brownie Gelato: $5.95

Total items bought:                               4
Subtotal:                                          $21.95
Discount:                                         - $0.00
GST:                                             + $1.54
Total:                                             $23.49
------------------------------------------------------------------------------------------------
Thank you for your time!
Please come again next time.
```

### Membership Receipt Output
```python
-----------------------------------------------------------------------------------------
                                   Tiny Tower Cafe
                              Online Shopping Receipt
                                    Basic Member
-----------------------------------------------------------------------------------------
2 Espresso: $11.00
1 Sakura Green Tea: $5.00
1 Brownie Gelato: $5.95

Total items bought:                                                4
Subtotal:                                                          $21.95
Discount:                                                        - $3.29
GST:                                                             + $1.54
Total:                                                             $20.20
=========================================================================================
```

---

*©2021 Tiny Tower Cafe - All rights reserved*