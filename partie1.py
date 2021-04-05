"""Module partie1
https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""

# Exercice 2
import sys
# Exercice 3
from datetime import datetime
# Exercice 4
from math import pi


def exercice1():
    """
    Write a Python program to print the following string in a specific format (see the output).
    Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a
    diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
    """
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a "
          "diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are")


def exercice2():
    """
    Write a Python program to get the Python version you are using.
    """
    print(sys.version)


def exercice3():
    """
    Write a Python program which accepts the radius of a circle from the user and compute the area
    """
    now = datetime.now()
    print(str(now).split(".")[0])
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def exercice4():
    """
    Write a Python program which accepts the radius of a circle from the user and compute the area
    """
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str((r * r) * pi))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))


def exercice5():
    """
    Write a Python program which accepts the user's first and last name and print them in reverse order with a space
    between them.
    """
    firstName = str(input("Input your first Name : "))
    lastName = str(input("Input your last Name : "))
    print(lastName + " " + firstName)


def exercice6():
    """
    Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
    tuple with those numbers.
    """
    values = input("Input some comma seprated numbers : ")
    list_list = values.split(",")
    tuple_list = tuple(list_list)
    print('List : ', list_list)
    print('Tuple : ', tuple_list)


def exercice7():
    """
    Write a Python program to accept a filename from the user and print the extension of that.
    """
    filename = input("Input filename : ")
    print("The extension of the file is : '" + filename.split(".")[1] + "'")
    f_extns = filename.split(".")
    print("The extension of the file is : " + repr(f_extns[-1]))


def exercice8():
    """
    Write a Python program to display the first and last colors from the following list
    color_list = ["Red","Green","White" ,"Black"]
    """
    color_list = ["Red", "Green", "White", "Black"]
    print(color_list[0], color_list[len(color_list) - 1])
    print("%s %s" % (color_list[0], color_list[-1]))


def exercice9():
    """
    Write a Python program to display the examination schedule. (extract the date from exam_st_date).
    exam_st_date = (11, 12, 2014)
    """
    exam_st_date = (11, 12, 2014)
    print("The examination will start from : " + str(exam_st_date[0]) + ' / ' + str(exam_st_date[1]) + ' / ' +
          str(exam_st_date[2]))
    print("The examination will start from : %i / %i / %i" % exam_st_date)


def exercice10():
    """
     Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
    """
    n = int(input("Input an integer : "))
    n1 = int("%s" % n)
    n2 = int("%s%s" % (n, n))
    n3 = int("%s%s%s" % (n, n, n))
    print(n1 + n2 + n3)


if __name__ == '__main__':
    # print("exercicer1: ")
    # exercice1()
    # print("\nexercice2: ")
    # exercice2()
    # print("\nexercice3: ")
    # exercice3()
    # print("\nexercice4: ")
    # exercice4()
    # print("\nexercice5: ")
    # exercice5()
    # print("\nexercice6: ")
    # exercice6()
    print("\nexercice7: ")
    exercice7()
    print("\nexercice8: ")
    exercice8()
    print("\nexercice9: ")
    exercice9()
    print("\nexercice10: ")
    exercice10()
