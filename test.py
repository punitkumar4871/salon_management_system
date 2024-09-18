class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_all(self):
        customers = []
        current = self.front
        while current:
            customers.append(current.data)
            current = current.next
        return customers

    def size(self):
        return self._size

    def clear(self):
        self.front = self.rear = None
        self._size = 0

# Command-line interface
def show_menu():
    print("\nQueue Operations:")
    print("1. Enqueue (Add Customer)")
    print("2. Dequeue (Serve Customer)")
    print("3. Peek (See Next Customer)")
    print("4. View All Customers")
    print("5. Clear Queue")
    print("6. Exit")

def main():
    queue = Queue()
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            customer = input("Enter customer name: ")
            queue.enqueue(customer)
            print(f"{customer} added to the queue.")
        elif choice == '2':
            served_customer = queue.dequeue()
            if served_customer:
                print(f"{served_customer} has been served.")
            else:
                print("Queue is empty, no customer to serve.")
        elif choice == '3':
            next_customer = queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("Queue is empty.")
        elif choice == '4':
            all_customers = queue.get_all()
            if all_customers:
                print("Current customers in queue:", ', '.join(all_customers))
            else:
                print("Queue is empty.")
        elif choice == '5':
            queue.clear()
            print("Queue cleared.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
1