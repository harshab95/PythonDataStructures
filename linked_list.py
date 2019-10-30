class Node: #the node type is same for all types of linkedlists

    def __init__(self,value):
        self.data = value
        self.next = None

class singlelinkedlist:
    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            print("list is empty")
        else:
            p = self.start
            print("list is: ")
            while p is not None:
                print(p.data, ", ")
                p = p.next
            print()

    def count_nodes(self):
        count = 0
        if self.start is None:
            print("List doesn't exist")
        else: 
            p = self.start
            while p is not None:
                count+=1
                p = p.next
        print("Number of nodes: {}".format(count))

    def search(self,x):
        i = 0
        if self.start is None:
            print("List doesn't exist")
        else:
            p = self.start
            while p is not None:
                i+=1
                if(p.data == x):
                    print("Search Result: {} at index {}".format(p.data,i))
                    break
                elif (p.next is None):
                    print("End Of List Reached. Search criteria not matched.")
                    break
                else:
                    p = p.next
            

    def insert_at_beginning(self):
        pass

    def insert_at_end(self):
        pass
    
    def create_list(self):
        self.start = Node(17)

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


if __name__ == "__main__":
#creating an instance of the linked list
    list = singlelinkedlist()
    list.create_list()

    while True:
        print("1. Display List")
        print("2. Count Nodes")
        print("3. Search for an Element")
        print("4. Quit")

        option = int(input("Enter your choice (number): "))
        x = 0
        if option == 1:
            list.display_list()
        elif option == 2:
            list.count_nodes()
        elif option == 3:
            print("You selected \"Search for an Element\"")
            x = int(input("Enter the number you are searching for in the list: "))
            print(x)
            list.search(x)
        elif option == 4:
            break;
        else:
            print("Invalid Choice. Enter a number between 1 and 3 to choose.")