# import pytest
# pytest.main()

# The above code can be uncommented to run the tests 

from utils import name_helper

name = input("Enter your full name: ")

first, last = name_helper.split_name(name)

print(f"Your first name is {first} and your last name is {last}")