# Before refactoring
# Here's our original code, before we did any refactoring:

import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Abra ka dabra gili gili chu!!🧙‍♂️")
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
print("Before going further i wanna tell you a story of Two sweet potatos :)")
print("One day two sweet potatos, who were best friends, were walking together down the street./n They stepped off the curb and a speeding car came around the corner and ran one of them over./n The uninjured sweet potato called 911 and helped his injured friend as best he was able. The injured sweet potato was taken to emergency at the hospital and rushed into surgery./n After a long and agonizing wait, the doctor finally appeared. He told the uninjured sweet potato, I have good news, and I have bad news./n The good news is that your friend is going to pull through. The bad news is that he's going to be a vegetable for the rest of his life.")


time.sleep(2)

while True:
    while True:
        response = input("Please place your order. "
                         "Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    print("Your order will be ready shortly.")
    time.sleep(2)
    while True:
        order_again = input("Would you like to place another order? "
                            "Please say 'yes' or 'no'.\n").lower()
        if 'no' in order_again:
            print("OK, goodbye!")
            time.sleep(2)
            break
        elif 'yes' in order_again:
            print("Very good, I'm happy to take another order. :)")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand. :(")
            time.sleep(2)
    if 'no' in order_again: 
        break

