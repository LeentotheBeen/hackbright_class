def tip_calc(bill, tip_per):
    return bill * float(tip_per)/100

def total_bill(bill, tip_per):
    tip_amt = tip_calc(bill, tip_per)
    return tip_amt + bill

def splitsies(bill, tip_per, party):
    bill_amt = total_bill(bill, tip_per)
    return bill_amt / party

def main():
    user_choice = int(raw_input("Pick a number: 1 - calculate tip, 2 - split the bill "))
    if user_choice == 1:
        bill = float(raw_input("What's the bill? "))
        tip_per = float(raw_input("What tip percentage sounds good? "))
        print "Your tip is $", tip_calc(bill, tip_per)
        print "Your total bill is $", total_bill(bill, tip_per)
    else:
        bill = float(raw_input("What's the bill? "))
        tip_per = float(raw_input("What tip percentage sounds good? "))
        party = int(raw_input("How many people are in your party? (Enter a number) "))
        print "Each person pays $", splitsies(bill, tip_per, party)

if __name__ == '__main__':
    main()
