from tkinter import Tk, Frame, Entry, Button, Label, DoubleVar, Toplevel


class PosApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")
        self.win.geometry("300x100")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.total = DoubleVar()
        self.total.set(0.00)

        self.new_item_price = DoubleVar()

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        total_label = Label(
            self.main_frame,
            text=f"Total Bill: £{self.total.get():.2f}"
        )
        total_label.pack(padx=5, pady=5)

        add_item_button = Button(
            self.main_frame,
            text="Add Item",
            command=lambda: self.create_new_win(total_label)
        )
        add_item_button.pack(padx=5, pady=5)

    def create_new_win(self, total_label):
        new_win = Toplevel(self.win)
        new_win.title("Add Item to Bill")
        new_win.geometry("300x175")

        new_win_frame = Frame(new_win)
        new_win_frame.pack(padx=10, pady=10)

        item_price_label = Label(new_win_frame, text="Item Price (£):")
        item_price_label.pack(padx=5, pady=5)

        item_price_entry = Entry(
            new_win_frame,
            textvariable=self.new_item_price
        )
        item_price_entry.pack(padx=5, pady=5)

        info_label = Label(
            new_win_frame,
            text="Please enter the price of the item."
        )
        add_button = Button(
            new_win_frame,
            text="Add to Bill",
            command=lambda: self.update_bill(total_label, new_win, info_label)
        )

        add_button.pack(padx=5, pady=5)
        info_label.pack(padx=5, pady=5)

    def update_bill(self, total_label, new_win, info_label):
        new_value = 0.00
        try:
            new_value = self.new_item_price.get()
        except Exception:
            info_label.config(
                fg="red",
                text="The value entered is not a number",
            )
            return

        if new_value <= 0:
            info_label.config(
                fg="red",
                text="The value entered is not a positive number",
            )
            return

        new_total = self.total.get() + new_value
        self.total.set(new_total)
        self.new_item_price.set(0.00)
        total_label.config(text=f"Total Bill: £{self.total.get():.2f}")
        new_win.destroy()


def main():
    app = PosApp()
    app.run()
