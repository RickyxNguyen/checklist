from termcolor import colored
import random
from os import system, name 
import time

checklist = []


# def color_picker():
#     color_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
#     return random.choice(color_list)
def color_selector():
    color_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    return random.choice(color_list)

def create(item):
    # color_chosen = colored = (item, color_picker())
    checklist.append(colored(item, color_selector()))

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = colored(item, color_selector())
    print(checklist)

def destroy(index):
    checklist.pop(index)
    return checklist

def mark_completed(index):
    update(index,("{} {}".format('√', read(index))))
    print(read(index))


def mark_notcompleted(index):
    if '√' in checklist[index]:
        placeholder = checklist[index]
        checklist[index]= placeholder[7:len(placeholder)]
        print(read(index))
    else:
        print('Index is already not completed!')
        
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    def clear(): 
  
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    # Create item
    if function_code == "a":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "r":
        item_index = int(user_input("Index Number: "))
        print("\n" + read(item_index))

    # Print all items
    elif function_code == "l":
        list_all_items()

    # Update item
    elif function_code == "u":
        item_index = int(user_input("Index Number: "))
        update_item = user_input("Input item: ")
        print(update(item_index, update_item))

    # Destroy item
    elif function_code == "d":
        item_index = int(user_input("Index Number: "))
        print(destroy(item_index))
    # Mark Complete/Incomplete
    elif function_code == "m":
        complete_incomplete = user_input("Mark as Complete or Incomplete?(Enter C/I): ").lower()

        if complete_incomplete == "c":
            item_index = int(user_input("Index Number: "))
            mark_completed(item_index)
        
        elif complete_incomplete == "i":
            item_index = int(user_input("Index Number: "))
            mark_notcompleted(item_index)
        
        else:
            print("Invalid Option")

    elif function_code == "q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    time.sleep(3)
    clear()
    return True

def test():
    create("apple")
    create("pear")

    
    # View results
    list_all_items()
    # Continue until all code is run
test()

running = True
while running:
    selection = user_input(
        "Press A to Add to list, R to Read from list, L to Display list, U to Update item, D to Destroy item, M to Mark Complete/Incomplete, and Q to quit: ")
    selection_both_cases = selection.lower()
    running = select(selection_both_cases)