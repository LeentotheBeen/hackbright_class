shopping_dict = {"Berkeley Bowl": ["milk", "pomegranate", "cheese"]}

###
def display_menu():
    print """
    "0 - Main Menu", 
    "1 - Show all lists.", 
    "2 - Show a specific list.", 
    "3 - Add a new shopping list.",
    "4 - Add an item to a shopping list.",
    "5 - Remove an item from a shopping list.",
    "6 - Remove a list by nickname.",
    "7 - Exit when you are done."
    """
def user_input():
    user_choice = 1#raw_input("choose from menu")
    return user_choice

def show_all_lists():
    return shopping_dict

def show_specific_list(store):
    return shopping_dict[store]

def add_new_list(new_store):
    shopping_dict[new_store]

def main():


    # while(True):
    #     display_menu()
    #     user_input()
    # if user_input == 1:
    #     display_all_lists()
    # is user_input == 2:
    #     display_list

    display_menu()
    print user_input()
    print show_all_lists()
    print show_specific_list("Berkeley Bowl")

if __name__ == '__main__':
    main()