from tkinter import *


class PosApp:

    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")
        self.win.geometry("300x100")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10)

        self.total = DoubleVar()
        self.total.set(0.00)

        self.newItemPrice = DoubleVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        totalLabel = Label(
            self.mainFrame,
            text=f"Total Bill: £{self.total.get():.2f}"
        )
        totalLabel.pack(padx=5, pady=5)

        addItemButton = Button(
            self.mainFrame,
            text="Add Item",
            command=lambda: self.createNewWin(totalLabel)
        )
        addItemButton.pack(padx=5, pady=5)

    def createNewWin(self, totalLabel):
        newWin = Toplevel(self.win)
        newWin.title("Add Item to Bill")
        newWin.geometry("300x175")

        newWinFrame = Frame(newWin)
        newWinFrame.pack(padx=10, pady=10)

        itemPriceLabel = Label(newWinFrame, text="Item Price (£):")
        itemPriceLabel.pack(padx=5, pady=5)

        itemPriceEntry = Entry(
            newWinFrame,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack(padx=5, pady=5)

        infoLabel = Label(
            newWinFrame,
            text="Please enter the price of the item."
        )
        addButton = Button(
            newWinFrame,
            text="Add to Bill",
            command=lambda: self.updateBill(totalLabel, newWin, infoLabel)
        )

        addButton.pack(padx=5, pady=5)
        infoLabel.pack(padx=5, pady=5)

    def updateBill(self, totalLabel, newWin, infoLabel):
        newValue = 0.00
        try:
            newValue = self.newItemPrice.get()
        except Exception:
            infoLabel.config(
                fg="red",
                text="The value entered is not a number",
            )
            return

        if newValue <= 0:
            infoLabel.config(
                fg="red",
                text="The value entered is not a positive number",
            )
            return

        newTotal = self.total.get() + newValue
        self.total.set(newTotal)
        self.newItemPrice.set(0.00)
        totalLabel.config(text=f"Total Bill: £{self.total.get():.2f}")
        newWin.destroy()


def main():
    app = PosApp()
    app.run()
