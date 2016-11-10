# my_list = [3, 7, 2, 8]
# for item in my_list:
#     print item,

# Part 2: For Loops
#for loop printing out numbers from 1to 20
# for numbers in range(1,21):
#     if numbers == 13:
#         print "hello"
#     else:
#         print numbers,

# Part 3: Putting it all together
# fruits_list = ["apples", "oranges", "bananas"]
# for fruits in fruits_list:
#     print fruits
# #
# for fruits in fruits_list[0:len(fruits_list)]:
#     print fruits

# create function sum_nums
# def sum_nums(num):
#     sum_list = sum(range(int(num) + 1))
#     return sum_list
#
# print sum_nums(34)

def sum_nums2(num):
    if int(num) < 0:
        sum_list = sum(range(num))
        return sum_list
    else:
        return "Naw, I'm not going to do anything."

print sum_nums2(raw_input("Give a number."))
#
#         sum_list = sum(list)
# def main():
#
# print sum_nums(raw_input("What's your favorite number?"))
#
# if __name__ == '__main__':
#     main()
