#food is key
#price is value

MENU_LIST = [
    "food:hotdog,price:5.50",
    "food:burger,price:9.50",
    "food:fries,price:4.00",
    "food:shake,price:5.00"]

def menu_to_dictionary(menu_list):
    menu_dictionary = {}
    for line in menu_list:
        line_parts = line.split(',')
        name_parts = line_parts[0].split(':')
        name = name_parts[1]
        price_parts = line_parts[1].split(':')
        price = price_parts[1]
        menu_dict[name] = price
    return menu_dict

def main():

    menu = menu_to_dictionary(MENU_LIST)
    for name, price in menu.iteritems():
        print('%s - $%s' % (name, price))
    # .iteritems() gives you both dictionary key and value or .items()


if __name__ == '__main__':
    main()
#
