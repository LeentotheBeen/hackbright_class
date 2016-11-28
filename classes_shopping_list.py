class Item(object):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def print_full_name(self):
        print "%s by %s" % (self.name, self.brand)

class Cart(object):
    def __init__(self, store, owner):
        self.store = store
        self.owner = owner
        self.items = []
        self.active = True
    def is_active_and_empty_cart(self):
        

shopping_dictionary = {"berkeley bowl": ["milk", "pomegranate", "cheese"], "target": []}

###
def display_menu():
    print """
    0 - Main Menu
    1 - Show all lists
    2 - Show a specific list
    3 - Add a new shopping list
    4 - Add an item to a shopping list
    5 - Remove an item from a shopping list
    6 - Remove a shopping list by nickname
    7 - Exit when you are done
    """

#Allow user to choose from the Display Menu
def user_choice(user_choice):
    user_choice = raw_input("Choose a number from the menu above. ")
    return user_choice

#Selection 1 - Show all the store lists in the dictionary
def show_all_lists():
    list_carts = ""
    for cart_name in shopping_dictionary.keys():
        list_carts = list_carts + "\n\n" + show_specific_list(cart_name)
    return list_carts

#Selection 2 - Show a specific store list and its items
def show_specific_list(cart):
    cart = cart.lower()
    return_string = "%s: " % (cart.capitalize())
    for item in shopping_dictionary[cart]:
        return_string = return_string + "\n %s" % (item)
    return return_string

#Selection 3 - Add a new store list to the dictionary
def add_new_list(cart):
    shopping_dictionary[cart.lower()] = []
    return shopping_dictionary

#Selection 4 - Add an item to a specific store list
def add_new_item_to_list(cart, item):
    # allow it to add multiple items (milk, sugar, eggs)
    item_split = item.split(",")
    cart = cart.lower()
    item = item.lower()
    if cart not in shopping_dictionary.keys():
        return "%s is not an existing list. Choose from an existing list: %s" % (cart, shopping_dictionary.keys())
    else:
        new_cart = shopping_dictionary[cart] + item_split
        return new_cart

#Selection 5 - Remove an item from a specific store list
#remove item in list (remove value, return new list)
def remove_item_from_list(cart, item):
    # allow it to remove multiple items (milk, sugar, eggs)

    if cart in shopping_dictionary:
        shopping_dictionary[cart.lower()].remove(item)
        return shopping_dictionary[cart.lower()]
    else:
        return "There is no %s in this list. Try another item. " % (item)
    return shopping_dictionary[cart.lower()]

#Selection 6 - Remove an entire store list from the dictionary
#remove store (key) from dictionary (return dictionary)
def remove_cart(cart):
    del shopping_dictionary[cart.lower()]
    return shopping_dictionary

#Selection 7 - Exit from the program
#Exit
def exit_program():
    return "You've completed your changes. Goodbye!"

def main():
    # display_menu()
    # print user_choice(3)
    # print show_all_lists()
    # print show_specific_list("Berkeley Bowl")
    # print add_new_list("Target")
    # print add_new_item_to_list("Target", "grapes")
    # print remove_item_from_list("Berkeley Bowl", "oatmeal")
    # print remove_cart("Berkeley Bowl")
    # print exit_program()

    while(True):
        display_menu()
        user_choice = int(raw_input("Select a number from the menu. "))
        print user_choice
        if user_choice == 1:
            print show_all_lists()
        elif user_choice == 2:
            cart = raw_input("Select the list you would like to show. ")
            print show_specific_list(cart)
        elif user_choice == 3:
            cart = raw_input("Name your new list. ")
            print add_new_list(cart)
        elif user_choice == 4:
            cart = raw_input("Select the list you would like to add to. ")
            item = raw_input("Add an item to the list. Add multiple items by separating with a comma. (e.g., milk, eggs, sugar) ")
            print add_new_item_to_list(cart,item)
        elif user_choice == 5:
            cart = raw_input("Select the list you would like to remove from. ")
            item = raw_input("Remove an item from the list. Remove multiple items by separating with a comma. (e.g., milk, eggs, sugar) ")
            print remove_item_from_list(cart,item)
        elif user_choice == 6:
            cart = raw_input("Select the list you would like to remove. ")
            print remove_cart(cart)
        else:
            print exit_program()
            break


if __name__ == '__main__':
    main()
