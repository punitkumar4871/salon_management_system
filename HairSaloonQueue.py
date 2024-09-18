import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from test import Queue  # Import the custom Queue class

class HairSalonQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hair Salon Queue Manager")

        # Set the window size to full screen height and full width
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{int(screen_height * 1)}")

        # Create and place the left frame for the image
        self.left_frame = tk.Frame(root, bg='#ffe5d9', padx=0, pady=0)
        self.left_frame.place(x=0, y=0, relwidth=0.6, relheight=1)

        # Load, resize, and display the image
        self.original_image = Image.open("salon1.png")
        self.resized_image = self.original_image.resize(
            (int(screen_width * 0.6), int(screen_height * 1)), Image.LANCZOS)
        self.salon_image = ImageTk.PhotoImage(self.resized_image)

        # Image label with fill and stick to ensure no gaps
        self.image_label = tk.Label(self.left_frame, image=self.salon_image, bg='#ffe5d9')
        self.image_label.place(relwidth=1, relheight=1)

        # Create and place the right frame for admin controls
        right_frame = tk.Frame(root, bg='#ffe5d9', padx=0, pady=0)
        right_frame.place(x=screen_width * 0.6, y=0, relwidth=0.4, relheight=1)

        # Title for Queue
        tk.Label(right_frame, text="HAIR SALON QUEUE", font=("Georgia", 25, "bold"), bg='#ffe5d9').pack(pady=10)

        # Admin controls frame
        admin_frame = tk.Frame(right_frame, bg='#ffe5d9')
        admin_frame.pack(pady=10)

        # Entry and Label to Add User
        tk.Label(admin_frame, text="Customer Name:", font=("Helvetica", 12), bg='#ffe5d9').grid(row=0, column=0, padx=5)
        self.customer_name_entry = tk.Entry(admin_frame, font=("Helvetica", 12), width=20)
        self.customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Additional Details Entry
        tk.Label(admin_frame, text="Service Type:", font=("Helvetica", 12), bg='#ffe5d9').grid(row=1, column=0, padx=5)
        self.service_type_entry = tk.Entry(admin_frame, font=("Helvetica", 12), width=20)
        self.service_type_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add and Remove Buttons
        self.add_button = tk.Button(admin_frame, text="Add Customer", command=self.add_customer, bg='#ffb3a7', font=("Helvetica", 12))
        self.add_button.grid(row=2, column=0, pady=5)
        self.next_button = tk.Button(admin_frame, text="Serve Customer", command=self.next_customer, bg='#ffb3a7', font=("Helvetica", 12))
        self.next_button.grid(row=2, column=1, pady=5)
        self.clear_button = tk.Button(admin_frame, text="Remove All", command=self.clear_queue, bg='#ffb3a7', font=("Helvetica", 12))
        self.clear_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Search Functionality
        search_frame = tk.Frame(right_frame, bg='#ffe5d9')
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Search Customer:", font=("Helvetica", 12), bg='#ffe5d9').grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 12), width=20)
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)
        self.search_button = tk.Button(search_frame, text="Search", command=self.search_customer, bg='#ffb3a7', font=("Helvetica", 12))
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        # Queue List Display
        queue_frame = tk.Frame(right_frame, bg='#ffe5d9')
        queue_frame.pack(pady=10)

        tk.Label(queue_frame, text="Queue List", font=("Helvetica", 14, "bold"), bg='#ffe5d9').pack()
        self.queue_listbox = tk.Listbox(queue_frame, width=40, height=15, font=("Helvetica", 12), bg='#fff0f3')
        self.queue_listbox.pack(pady=10)

        # Queue Summary
        self.queue_summary_label = tk.Label(right_frame, text="REMAINING CUSTOMERS: 0", font=("Helvetica", 12), bg='#ffe5d9')
        self.queue_summary_label.pack(pady=5)

        # Info Display for Next Customer
        self.info_label = tk.Label(right_frame, text="Serving customer will be displayed here", font=("Helvetica", 12), bg='#ffe5d9')
        self.info_label.pack(pady=10)

        # Exit Button
        tk.Button(right_frame, text="Exit", command=root.quit, bg='#ffb3a7', font=("Helvetica", 12)).pack(pady=10)

        # Initialize the queue
        self.queue = Queue()

    def add_customer(self):
        name = self.customer_name_entry.get()
        service = self.service_type_entry.get()
        if name:
            customer_info = f"{name} ({service})"
            self.queue.enqueue(customer_info)
            self.customer_name_entry.delete(0, tk.END)
            self.service_type_entry.delete(0, tk.END)
            self.update_queue_display()
        else:
            messagebox.showwarning("Input Error", "Please enter a customer name")

    def next_customer(self):
        if not self.queue.is_empty():
            next_customer = self.queue.dequeue()
            self.info_label.config(text=f"Current Customer: {next_customer}")
            self.update_queue_display()

            # After serving the first customer, change the button text to "Next Customer"
            if self.next_button.cget('text') == "Serve Customer":
                self.next_button.config(text="Next Customer")
        else:
            messagebox.showinfo("Queue Empty", "No more customers in the queue")
            self.info_label.config(text="Serving customer will be displayed here")
            # Reset button text to "Serve Customer" when the queue is empty
            self.next_button.config(text="Serve Customer")

    def clear_queue(self):
        self.queue = Queue()
        self.update_queue_display()
        self.info_label.config(text="Next customer will be displayed here")
        # Reset button text to "Serve Customer" when clearing the queue
        self.next_button.config(text="Serve Customer")
    def search_customer(self):
        query = self.search_entry.get().lower()
        if query:
            self.queue_listbox.delete(0, tk.END)
            customers = self.queue.get_all()
            filtered_customers = [customer for customer in customers if query in customer.lower()]
            if filtered_customers:
                for customer in filtered_customers:
                    self.queue_listbox.insert(tk.END, customer)
            else:
                self.queue_listbox.insert(tk.END, "No matching customers found")
        else:
            messagebox.showwarning("Input Error", "Please enter a search query")

    def update_queue_display(self):
        self.queue_listbox.delete(0, tk.END)
        customers = self.queue.get_all()
        for customer in customers:
            self.queue_listbox.insert(tk.END, customer)
        # Update queue summary
        self.queue_summary_label.config(text=f"REMAINING CUSTOMERS: {self.queue.size()}")
        
        # Only change button text if the queue is empty, but keep "Serve Customer" on first run
        if self.queue.is_empty():
            self.next_button.config(text="Serve Customer")
# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HairSalonQueueApp(root)
    root.mainloop()
