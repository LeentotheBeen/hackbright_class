shopping_dictionary = {"Berkeley Bowl": ["milk", "pomegranate", "cheese"], "Target": []}

###
def display_menu():
    print """
    0 - Main Menu
    1 - Show all lists
    2 - Show a specific list
    3 - Add a new shopping list
    4 - Add an item to a shopping list
    5 - Remove an item from a shopping list
    6 - Remove a list by nickname
    7 - Exit when you are done
    """

#Allow user to choose from the Display Menu
def user_input(user_choice):
    user_choice = raw_input("Choose a number from the menu above. ")
    return user_choice

#Selection 1 - Show all the store lists in the dictionary
def show_all_lists():
    return shopping_dictionary

#Selection 2 - Show a specific store list and its items
def show_specific_list(cart):
    return shopping_dictionary[cart]

#Selection 3 - Add a new store list to the dictionary
def add_new_list(cart):
    shopping_dictionary[cart] = []
    return shopping_dictionary

#Selection 4 - Add an item to a specific store list
def add_new_item_to_list(cart, item):
    if cart not in shopping_dictionary:
        shopping_dictionary[cart] = [(item)]
    else:
        shopping_dictionary[cart].append(item)
    return shopping_dictionary

#Selection 5 - Remove an item from a specific store list
#remove item in list (remove value, return new list)
def remove_item_from_list(cart, item):
    if cart in shopping_dictionary:
        shopping_dictionary[cart].remove(item)
        return shopping_dictionary[cart]
    else:
        return "There is no %s in this list. Try another item. " % (item)
        return shopping_dictionary[cart]

#Selection 6 - Remove an entire store list from the dictionary
#remove store (key) from dictionary (return dictionary)
def remove_cart(cart):
    del shopping_dictionary[cart]
    return shopping_dictionary

#Selection 7 - Exit from the program
#Exit
def exit_program():
    return "You've completed your changes. Goodbye!"

def main():
    # display_menu()
    # print user_input(3)
    # print show_all_lists()
    # print show_specific_list("Berkeley Bowl")
    # print add_new_list("Target")
    # print add_new_item_to_list("Target", "grapes")
    # print remove_item_from_list("Berkeley Bowl", "oatmeal")
    # print remove_cart("Berkeley Bowl")
    # print exit_program()

    while(True):
        display_menu()
        user_choice = raw_input("Select a number from the menu. ")
        user_input(user_choice)
        if user_input == 1:
            print show_all_lists()
        elif user_input == 2:
            cart = raw_input("Select the list you would like to show. ")
            print show_specific_list(cart)
        elif user_input == 3:
            cart = raw_input("Name your new list. ")
            print add_new_list(cart)
        elif user_input == 4:
            cart = raw_input("Select the list you would like to add to. ")
            item = raw_input("Add an item to the list. ")
            print add_new_item_to_list(cart,item)
        elif user_input == 5:
            cart = raw_input("Select the list you would like to remove from. ")
            item = raw_input("Remove an item from the list. ")
            print remove_item_from_list(cart,item)
        elif user_input == 6:
            cart = raw_input("Select the list you would like to remove. ")
            print remove_cart(cart)
        else:
            print exit_program
            break


if __name__ == '__main__':
    main()
