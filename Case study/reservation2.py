import tkinter as tk
from tkinter import messagebox
from pygame import mixer
import os

class ReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Reservation System")
        self.root.geometry("400x400")
        self.root.configure(bg='lightblue')

        mixer.init()

        self.tables = {f"Table {i+1}": None for i in range(10)}  # Example of 10 tables

        self.main_menu()

    def main_menu(self):
        self.clear_frame()
        
        self.title_label = tk.Label(self.root, text="Restaurant Reservation System", font=("Helvetica", 16), bg='lightblue')
        self.title_label.pack(pady=10)

        self.menu_frame = tk.Frame(self.root, bg='lightblue')
        self.menu_frame.pack(pady=10)

        self.book_btn = tk.Button(self.menu_frame, text="Book Table", command=self.book_table, font=("Helvetica", 12))
        self.book_btn.pack(side=tk.LEFT, padx=5)

        self.view_btn = tk.Button(self.menu_frame, text="View Reservations", command=self.view_reservations, font=("Helvetica", 12))
        self.view_btn.pack(side=tk.LEFT, padx=5)

        self.edit_btn = tk.Button(self.menu_frame, text="Edit Reservation", command=self.edit_reservation, font=("Helvetica", 12))
        self.edit_btn.pack(side=tk.LEFT, padx=5)

        self.cancel_btn = tk.Button(self.menu_frame, text="Cancel Reservation", command=self.cancel_reservation, font=("Helvetica", 12))
        self.cancel_btn.pack(side=tk.LEFT, padx=5)

    def book_table(self):
        self.clear_frame()
        self.create_back_button()

        self.name_label = tk.Label(self.root, text="Enter Name:", font=("Helvetica", 12), bg='lightblue')
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.name_entry.pack(pady=5)

        self.table_label = tk.Label(self.root, text="Select Table:", font=("Helvetica", 12), bg='lightblue')
        self.table_label.pack(pady=5)

        self.table_var = tk.StringVar(self.root)
        self.table_var.set("Select Table")
        self.table_menu = tk.OptionMenu(self.root, self.table_var, *self.get_available_tables())
        self.table_menu.pack(pady=5)

        self.book_confirm_btn = tk.Button(self.root, text="Confirm Booking", command=self.confirm_booking, font=("Helvetica", 12))
        self.book_confirm_btn.pack(pady=5)

    def edit_reservation(self):
        self.clear_frame()
        self.create_back_button()

        self.edit_label = tk.Label(self.root, text="Select Reservation to Edit:", font=("Helvetica", 12), bg='lightblue')
        self.edit_label.pack(pady=5)

        self.edit_var = tk.StringVar(self.root)
        self.edit_var.set("Select Table")
        self.edit_menu = tk.OptionMenu(self.root, self.edit_var, *self.get_booked_tables())
        self.edit_menu.pack(pady=5)

        self.edit_confirm_btn = tk.Button(self.root, text="Edit Selected", command=self.edit_booking, font=("Helvetica", 12))
        self.edit_confirm_btn.pack(pady=5)

    def edit_booking(self):
        selected_table = self.edit_var.get()
        if selected_table != "Select Table":
            self.book_table()
            self.table_var.set(selected_table)
            self.table_menu.config(state="disabled")
        else:
            messagebox.showerror("Error", "Please select a table to edit.")

    def get_available_tables(self):
        return [table for table, name in self.tables.items() if name is None]

    def get_booked_tables(self):
        return [table for table, name in self.tables.items() if name is not None]

    def confirm_booking(self):
        name = self.name_entry.get()
        table = self.table_var.get()

        if name and table != "Select Table":
            self.tables[table] = name
            messagebox.showinfo("Success", f"Table {table} booked for {name}.")
            mixer.music.load('order_received.mp3')
            mixer.music.play()
            self.main_menu()
        else:
            messagebox.showerror("Error", "Please enter a name and select a table.")

    def view_reservations(self):
        self.clear_frame()
        self.create_back_button()

        for table, name in self.tables.items():
            reservation = f"{table}: {'Available' if name is None else name}"
            tk.Label(self.root, text=reservation, font=("Helvetica", 12), bg='lightblue').pack(pady=2)

    def cancel_reservation(self):
        self.clear_frame()
        self.create_back_button()

        self.cancel_label = tk.Label(self.root, text="Select Table to Cancel:", font=("Helvetica", 12), bg='lightblue')
        self.cancel_label.pack(pady=5)

        self.cancel_var = tk.StringVar(self.root)
        self.cancel_var.set("Select Table")
        self.cancel_menu = tk.OptionMenu(self.root, self.cancel_var, *self.get_booked_tables())
        self.cancel_menu.pack(pady=5)

        self.cancel_confirm_btn = tk.Button(self.root, text="Confirm Cancellation", command=self.confirm_cancellation, font=("Helvetica", 12))
        self.cancel_confirm_btn.pack(pady=5)

    def confirm_cancellation(self):
        table = self.cancel_var.get()

        if table != "Select Table":
            self.tables[table] = None
            messagebox.showinfo("Success", f"Reservation for {table} cancelled.")
            mixer.music.load('thank_you.mp3')
            mixer.music.play()
            self.main_menu()
        else:
            messagebox.showerror("Error", "Please select a table to cancel.")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
            elif isinstance(widget, tk.Label) and widget != self.title_label:
                widget.destroy()
            elif isinstance(widget, tk.Button) and widget != self.book_btn:
                widget.destroy()
            elif isinstance(widget, tk.Entry):
                widget.destroy()
            elif isinstance(widget, tk.OptionMenu):
                widget.destroy()

    def create_back_button(self):
        self.back_btn = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, font=("Helvetica", 12))
        self.back_btn.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReservationSystem(root)
    root.mainloop()
