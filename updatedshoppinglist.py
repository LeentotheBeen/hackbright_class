shopping_dictionary = {"Berkeley Bowl": ["milk", "pomegranate", "cheese"]}

###
def display_menu():
    print """
    0 - Main Menu,
    1 - Show all lists.,
    2 - Show a specific list.,
    3 - Add a new shopping list.,
    4 - Add an item to a shopping list.,
    5 - Remove an item from a shopping list.,
    6 - Remove a list by nickname.,
    7 - Exit when you are done.
    """
#Allow user to choose from the Display Menu
def user_input():
    user_choice = raw_input("Choose a number from the menu above. ")
    return user_choice

#Selection 1 - Show all the store lists in the dictionary
def show_all_lists():
    return shopping_dictionary

#Selection 2 - Show a specific store list and its items
def show_specific_list(store):
    return shopping_dictionary[store]

#Selection 3 - Add a new store list to the dictionary
def add_new_list(new_store):
    shopping_dictionary[new_store] = []
    return shopping_dictionary

#Selection 4 - Add an item to a specific store list
#add item in list (add value, return new list)

def add_new_item_to_list():
    store = raw_input("What shopping list do you want to add to? ")
    item = raw_input("What item do you want to add to this list? ")
    shopping_dictionary[store] = [item]
    
    return shopping_dictionary

#Selection 5 - Remove an item from a specific store list
#remove item in list (remove value, return new list)

#Selection 6 - Remove an entire store list from the dictionary
#remove store (key) from dictionary (return dictionary)

#Selection 7 - Exit from the program
#Exit

def main():
    # print add_new_list("Target")
    print add_new_item_to_list()

    # while(True):
    #     display_menu()
    #     user_input()
    # if user_input == 1:
    #     display_all_lists()
    # is user_input == 2:
    #     display_list

    # display_menu()
    # print user_input()
    # print show_all_lists()
    # print show_specific_list("Berkeley Bowl")


if __name__ == '__main__':
    main()
