# 1

from os import name
from unique_name import unique, a

# print("Hello World")

# # 2
# name = input("Enter your name : ")
# print(f"welcome {name}")

# # 3
# if name == "Alice" or name =="Bob":
#     print(f"welcome {name}")
# else:
#     print(name)

# 4
# number = int(input("Enter a number : "))
# sum =0
# product=1
# for num in range(1,number+1):
#     sum += num
# print(sum)

# 5

# for i in range(1,number):
#     if i % 3 ==0 or i % 5 ==0:
#         sum+=i
# print(sum)

# 6
# choose = int(input("""
# choose your calculation
# 1.sum
# 2.product
# """))


# if choose == 1:
#     for num in range(1,number+1):
#                 sum += num
#     print(sum)
# elif choose == 2:
#     for num in range(1,number+1):
#             product*=num
#     print(product)


# def largestNumber(n, sum):
#     password =""
#     if sum > 9*n:
#         return -1
#     else:
#         while len(password) != n:
#             if sum > 9:
#                 sum -=9
#                 password+=str(9)

#             else:
#                 password+=str(sum)
#                 sum = 0
#         return password

# print(largestNumber(3,29))

# def no_space(x) :
#   return ("").join(x.split(" "))


# print(no_space("hello world"));
my__name = "my name is {name}"
print(type(my__name))
print(my__name.split(" "))
name = {name: "safras"}
print(my__name.format(name="safras"))
print(my__name.replace("a", "a"))
print(my__name.count("a"))
print(my__name.isalnum())
print(my__name.index("m"))
print(my__name.isascii())
print(my__name.endswith("s"))
print(my__name.isdecimal())
print(my__name.islower())
print(my__name.isidentifier())

print(10 >> 2, 10 << 2)
print(~10)

print("safras".endswith("as"))


def spin__words(string):
    new_string = []
    words = string.split(" ")

    for one_word in words:
        if len(one_word) >= 5:
            new_string.append(one_word[::-1])
        else:
            new_string.append(one_word)
    return " ".join(new_string)


print(spin__words("Hey fellow warriors"))

lists = ["safras", "mohamed"]

for word in lists:
    if len(word) >= 5:
        word = word.replace(word, word[::-1])
        print(word)

word = "ACEGIKMOQSUWY"

match word:
    case "a":
        print("das")
    case "GIKMOQSUWY":
        print("yes")
    case _:
        print("no")

no = -10.3
print(int(no // 2))

print(float(True))
print(type(str(True)))

dict = {
    "name": "safras",
    "age": 23,
    "school": "kinniya"
}

print(complex(no).imag, complex(True).real, complex(no).__abs__(), complex(False).conjugate())

no1 = 10
no2 = 10.0

print(type(no1), type(no2))
print(id(no1), id(no2))
print(no1 is not no2)

my__name = "safras"

values = [90, 98, 80, 30]
values[0] = 30
# print(bytes(values[0]))
values = bytes(values)

print(values[0])
print(type(values))

for val in values:
    print(val)

new__values = [1, 2, 3, 4, 5, 6, 7, 5, 23]

print(new__values[2::])

no3 = [1, 34, 45, ]

new__values.append(no3)
print(new__values.pop())
new__values.clear()
new__values.append(1)
new__values.append(2)
print(new__values)
new__values.reverse()
new__values.sort()
print(new__values.__contains__(1))
print(new__values)
#
# print(n.)
squares = [1, 4, 9, 16, 25]
print(squares[-3:])

squares[-3:] = [10, 30]
print(squares)
squares += [1, 3, 4]
print(squares)

my_name = "Safras"
mine = "Afros"

print(my__name < mine)
print(my__name == mine)

print(my__name.capitalize(), mine.capitalize())

no4 = 30 if my_name > mine else 20
print(no4)

print("s" in my__name)

print(40 if 10 > 10 else 50)

print(10 > 100 > 1000 > 8)

names = ["mohamed", "afros", "safras", "safras", "afros", "Ishalina"]

print(10 >> 2)
print(10 << 2)

print(unique(names))
