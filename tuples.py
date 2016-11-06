def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            # it has a divisor and is not prime
            return False
    # it does not divisor and IS prime
    return True

def main ():
    input = ""
    while (input != "exit"):
        input = raw_input("Enter a number: ")
        if input == "exit":
            break
        num = int(input)
        print "Is the number", input, "prime?", is_prime(num)

# if __name__ == '__main__':
main()
