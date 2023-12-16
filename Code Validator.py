import tkinter as tk
from tkinter import simpledialog, messagebox

def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "")
    
    if not (len(isbn) == 10 or len(isbn) == 13):
        return False
    
    digits = [int(digit) for digit in isbn]
    
    if len(digits) == 10:
        check_sum = sum((i + 1) * digit for i, digit in enumerate(digits[:-1])) % 11
        return (check_sum if check_sum < 10 else 'X') == digits[-1]
    elif len(digits) == 13:
        check_sum = sum((3 if i % 2 else 1) * digit for i, digit in enumerate(digits[:-1])) % 10
        return (check_sum if check_sum == 0 else 10 - check_sum) == digits[-1]
    else:
        return False

def is_valid_upc(upc):
    upc = upc.replace("-", "")
    upc = str(upc)
    
    if not upc.isdigit() or (len(upc) != 12 and len(upc) != 13):
        return False

    if len(upc) == 12:
        sum_odd = sum(int(upc[i]) for i in range(0, 11, 2))
        sum_even = sum(int(upc[i]) for i in range(1, 11, 2))
    else:
        sum_odd = sum(int(upc[i]) for i in range(1, 12, 2))
        sum_even = sum(int(upc[i]) for i in range(0, 12, 2))

    total = 3 * sum_odd + sum_even

    checksum = (10 - total % 10) % 10
    return checksum == int(upc[-1])

def is_valid_credit_card(card_number):
    card_number = ''.join(card_number.split())

    digits = [int(digit) for digit in str(card_number)][::-1]

    doubled_digits = [2 * digit if index % 2 == 1 else digit for index, digit in enumerate(digits)]

    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

    total_sum = sum(subtracted_digits)

    return total_sum % 10 == 0

def validate_isbn():
    isbn = simpledialog.askstring("ISBN Validation", "Enter the ISBN:")
    result = f"ISBN {isbn} is valid: {is_valid_isbn(isbn)}"
    tk.messagebox.showinfo("Validation Result", result)

def validate_upc():
    upc = simpledialog.askstring("UPC Validation", "Enter the UPC:")
    result = f"UPC {upc} is valid: {is_valid_upc(upc)}"
    tk.messagebox.showinfo("Validation Result", result)

def validate_credit_card():
    credit_card = simpledialog.askstring("Credit Card Validation", "Enter the credit card number:")
    result = f"Credit Card {credit_card} is valid: {is_valid_credit_card(credit_card)}"
    tk.messagebox.showinfo("Validation Result", result)

def start_validation_program(root):  # Pass 'root' as an argument
    user_name = simpledialog.askstring("User Name", "Please enter your name:")

    while True:
        choice = simpledialog.askinteger("Select Option", "Select an option:\n1. Validate ISBN\n2. Validate UPC\n3. Validate Credit Card\n4. Exit", minvalue=1, maxvalue=4)

        if choice == 1:
            validate_isbn()
        elif choice == 2:
            validate_upc()
        elif choice == 3:
            validate_credit_card()
        elif choice == 4:
            tk.messagebox.showinfo("Goodbye", f"Goodbye, {user_name}! Exiting the program.")
            break
        else:
            tk.messagebox.showwarning("Invalid Choice", "Invalid choice. Please enter a valid option.")

    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Code Validator")

    root.geometry("300x100")

    welcome_label = tk.Label(root, text="Welcome to the Validation Program!")
    welcome_label.pack(pady=15)

    button_frame = tk.Frame(root)
    button_frame.pack()

    proceed_button = tk.Button(button_frame, text="Proceed", command=lambda: start_validation_program(root))
    proceed_button.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.LEFT)

    root.mainloop()