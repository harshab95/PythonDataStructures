from colorama import Fore, Back, Style 
import os
# print(Fore.RED + 'some red text') 
# print(Back.GREEN + 'and with a green background') 
# print(Style.DIM + 'and in dim text') 
# print(Style.RESET_ALL) 
# print('back to normal now') 

# init(autoreset=True)

class Node: #the node type is same for all types of linkedlists

    def __init__(self,value):
        self.data = value
        self.next = None

class level: 
    def __init__(self):
        self.WARNING = 0

def show_message(success, message):
    if success is False:
        print(Fore.RED + message)
        print(Fore.WHITE) 
    else:
        print(message)

class singlelinkedlist:
    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            show_message(False, "List doesn't exist. Please create the list first.")
        else:
            p = self.start
            print("List is: [", end="")
            while p is not None:
                print(p.data,"," ,end="")
                p = p.next
            print("]")
            show_message(True, "Displayed.")

    def count_nodes(self):
        count = 0
        if self.start is None:
            show_message(False, "List doesn't exist. Please create the list first.")
        else: 
            p = self.start
            while p is not None:
                count+=1
                p = p.next
        print("Number of nodes: {}".format(count))

    def search(self,x):
        i = 0
        if self.start is None:
            show_message(False, "List doesn't exist. Please create the list first.")
        else:
            p = self.start
            while p is not None:
                i+=1
                #element is found
                if(p.data == x):
                    show_message(True,"Search Result: {} at index {}".format(p.data,i))
                    break
                #There are no more nodes, reached the last node. The while loop only breaks when is None, but since we want to stop before we reach there, this is the condition
                elif (p.next is None):
                    show_message(False,"End Of List Reached. Search criteria not matched.")
                    break
                #keep looking
                else:
                    p = p.next
            

    def insert_at_beginning(self,x):
        """
        Only to change the beginning of the list. THe function will not create a list for you.
        """

        if self.start is None:
            show_message(False, "List doesn't exist. Please create the list first.")
        else:
            p = self.start
            if(p.next is not None):
                temp = p.next

            self.start = Node(x)
            self.start.next = p
            show_message(True, "Input {} inserted at beginning.".format(x))

    def insert_at_end(self,x):
        if self.start is None:
            show_message(False, "List doesn't exist. Please create the list first.")
        else: 
            p = self.start
            while p.next is not None:
                p = p.next
            p.next = Node(x)
            show_message(True, "Inserted {} at end.".format(x))
    
    def create_list(self):
        input_1 = 0
        input_1 = int(input("Enter a number to begin the list: "))
        self.start = Node(input_1)
        show_message(True, "List Created")

    def insert_after(self):

        pass

    def insert_before(self):
        pass

    def insert_at_position(self):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubblesort_xdata(self):
        pass


def main():
    list = singlelinkedlist()
    os.system('clear')

    while True:
        print("--- Linked List in Python ---")
        print("1. Create list")
        print("2. Display List")
        print("3. Count Nodes")
        print("4. Search for an Element")
        print("5. Insert at Beginning")
        print("6. Insert at End")
        print("7. Quit")

        option = int(input("Enter your choice (number): "))
        x = 0

        if option == 1:
            list.create_list()
        
        if option == 2:
            list.display_list()
        
        elif option == 3:
            list.count_nodes()
        
        elif option == 4:
            print("You selected \"Search for an Element\"")
            x = int(input("Enter the number you are searching for in the list: "))
            print(x)
            list.search(x)
        
        elif option == 5:
            x = int(input("Enter the value you would like at the beginning of the list: "))
            list.insert_at_beginning(x)
            
        elif option == 6:
            x = int(input("Enter the value you would like at the end of the list: "))
            list.insert_at_end(x)
        
        elif option == 7:
            break
        
        else:
            print("Invalid Choice. Enter a number between 1 and 7 to choose.")


if __name__ == "__main__":
#creating an instance of the linked list
    main()
    