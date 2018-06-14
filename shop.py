####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Fllufy" 
signature_flavors = ["marshmallow", "salted caramel", "rice crispy"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    for item in menu:
        print ("- %s (KD %s)" % (item, menu[item]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for item in original_flavors:
        print ('- %s' % item)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for item in signature_flavors:
        print ("- %s" % item)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu:
        return True
    elif order in original_flavors:
        return True
    elif order in signature_flavors:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    user_input = input('Enter the exact spelling of the item you want. Type "Exit" to end your order')
    while user_input.lower() != 'exit':
        if is_valid_order(user_input):
            order_list.append(user_input)
        user_input = input()

    return order_list


def accept_credit_card(total):
    return total >= 5
    
    """
    Return whether an order is eligible for credit card payment.
    """
    


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for item in order_list:
        if item in menu:
            total += menu[item]
        elif item in original_flavors:
            total += original_price
        elif item in signature_flavors:
            total += signature_price



    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print (order_list)
    print ("your total price is : KD %s" % get_total_price(order_list))
    if accept_credit_card(get_total_price(order_list)):
        print ("You can make the purchase using a credit card")
    else:
        print ("You cannot make this order with credit card")
    print ("Thank you for shopping with us at %s" % (cupcake_shop_name))
