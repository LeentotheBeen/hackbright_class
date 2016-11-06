#Original shopping list
shopping_list = ["apples", "cherries", "pumpkins", "chicken noodle soup"]

#defining add_to_list function
def add_to_list(item):
    shopping_list.append(item.lower()) #add one or more item to the list
    return shopping_list #return back to new list with new item

#function not allowing something to be added that already exists
#allow for all cases
def check_duplicate(item):
    if item.lower() not in shopping_list:
        clean_list = add_to_list(item)
        clean_list.sort()
        return "This is your new list: " + str(clean_list)
    else:
        return "You already added that. Try again."

#function that returns list in alphabetical order
def alphbetize_list():
    return shopping_list.sort()

#function that removes an item from the list
def remove_from_list(removed_item):
    removed_item.lower()
    if removed_item in shopping_list:
        shopping_list.remove(removed_item)
    else:
        print "That's not in your list."
    return "This is your current list: " + str(shopping_list)
#print a message if item isn't there
#allow for all cases

def main():

    question_1 = raw_input("Do you want to add something to your shopping list? Reply Y for yes, or N for no. ")
    if question_1.lower() in ["yes", "y"]:
        new_item = raw_input("Awesome! Tell me what you want to add. ")
        print check_duplicate(new_item)
    elif question_1.lower() in ["no", "n"]:
        print "Ok, maybe next time."
    else:
        print "I didn't get that. Try again."

    question_2 = raw_input("Do you want to remove something to your shopping list? Reply Y for yes, or N for no. ")
    if question_2.lower() in ["yes", "y"]:
        removed_item = raw_input("Ok, what do you want to take out of your list? ")
        print remove_from_list(removed_item)
    elif question_2.lower() in ["no", "n"]:
        print "Cool, we'll keep your list as is."
        print "This is your current shopping list:", shopping_list
    else:
        print "I didn't get that. Try again."

if __name__ == '__main__':
    main()
