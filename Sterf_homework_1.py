"""

Joe Sterf
 3/27/2019
 Python 1 - DAT-119 - Spring 2019
 Inclass/Homework Week 8
 Todo list application

"""
#initalize empty lists as global variables
todo_list = []
finished_list =[]

def display_menu():
    #reset user_selection to 0
    user_selection = 0
    #display menu
    print('1) View the items on your todo list \n 2) View the items you have finished \n 3) Add an item to the todo list'
          '\n 4) Mark a todo list item as completed \n 5) Exit the todo list application (your list will not be saved)')
    print('')
    user_selection = int(input('Please choose one of the options above: '))
    print('')
    #check that user picked 1 thru 5
    while user_selection < 1 or user_selection > 5:
        user_selection=int(input('Not a valid selection. Please select 1-5 for one of the menu items above: '))
    return user_selection


def add_item(list, item):
    #add new item to list
    list.append(item)


def delete_item (list, index):
    #delete selected index from list
    del list[index]


def display_list (list_name):
    #if list is blank then display a message, other display list
    if len(list_name) == 0:
        print('There is nothing to display.')
    else:
        list_value = 0
        while list_value < len(list_name):
            print(list_value + 1, ')', list_name[list_value])
            list_value += 1


def main():
    menu_on = 'y'
    while menu_on == 'y':
        menu_selection = display_menu()
        if menu_selection == 1:
            #show todo list
            display_list(todo_list)
            print('')
            #pause so user can read results before showing menu
            pause = input('Hit Enter when finished viewing: ')
            print('')

        elif menu_selection == 2:
            # show completed list
            print('This is your finished list:')
            display_list(finished_list)
            print('')
            # pause so user can read results before showing menu
            pause = input('Hit Enter when finished viewing: ')
            print('')
        elif menu_selection == 3:
            #ask user what they want to add and then append it to todo list
            item_add = input("What would you like to add? ")
            add_item(todo_list, item_add)
            print('')
        elif menu_selection == 4:
            #if todo list is empty then don't ask for input
            if len(todo_list) == 0:
                print('Your todo list is empty.  Add an item first.')
                print('')
                # pause so user can read results before showing menu
                pause = input('Hit Enter when finished viewing: ')
                print('')
            #ask user task to complete, make sure it's in todo list.  If so remove and add to finished_list
            else:
                print('Choose an item to mark complete')
                display_list(todo_list)
                item_complete = int(input('Please choose one of the options above: '))

                while item_complete > len(todo_list):
                    item_complete = int(input('Invalid selection. Please choose one of the options above: '))
                #reduce item_complete by 1 to get correct index value
                selection_index = item_complete - 1
                #get item from todo list in order to add to finished_list
                item_remove = todo_list[selection_index]
                #add completed item to finished list
                add_item(finished_list,item_remove)
                #remove completed item from todo list
                delete_item(todo_list,selection_index)
                print('')
        elif menu_selection ==5:
            #if user selects 5 stop while loop and end program
            menu_on ='n'




if __name__ == "__main__":
    main()