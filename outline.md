# Outline of week 14

## Chapter 1: Errors vs exceptions

### **Errors**: Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:
```
>>> while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

### **Exceptions**: Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions. Give a few examples of exceptions such as `ZeroDivisionError`, `NameError` and `TypeError`.
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
```


### **Tracebacks**: Explain tracebacks and how to read them.
```
>>> open("/path/to/mars.jpg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'
```

For example on a program they can write in the editor:
```py
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()
```
They would get the following error:
```
Traceback (most recent call last):
  File "/tmp/config.py", line 9, in <module>
    main()
  File "/tmp/config.py", line 3, in main
    configuration = open('config.txt')
IsADirectoryError: [Errno 21] Is a directory: 'config.txt'
```

## Chapter 2: Handling exceptions

- It is possible to write programs that handle selected exceptions. Look at the following example:
```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

- Explain what happens in this code and what happens if the user enters a non-integer value.
- Explain the `try` statement and the `except` clause with a few basic examples. No need to show how to raise exceptions or custom exceptions.
In the earlier error example in file reading they could do:
```py
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()
```

- Explain when it is appropriate and non appropriate to use `try` statements. For example if asking a number from the user, you can check using `isalpha()` if the input is a number or not. If it is not a number, you can ask the user to enter a number again. In this case, you do not need to use `try` statements and an `if` statement is enough.


## Chapter 3: Debugging

My students are mainly using Thonny as their IDE. I know that it has a simple debugger. The students just press Ctrl+F5 instead of F5 and they can run their programs step-by-step, no breakpoints needed. Press F6 for a big step and F7 for a small step. Steps follow program structure, not just code lines.
But some of them use Visual Studio Code and PyCharm.
For PyCharm I can direct the reader to [this documentation page](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html#debug) but the discussion should be similar.

- Explain tracebacks and how to read them.
```
>>> open("/path/to/mars.jpg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'
```
- Explain the concept of debugging and how it is different from testing program manually.
- Explain the concept of breakpoints and how to use them in Thonny, PyCharm and Visual Studio Code. Introduce some sample programs and show how to use breakpoints to debug them.
- Explain the concept of stepping through the code and how to use it in Thonny, PyCharm and Visual Studio Code.

As examples you can have a medium sized textual program like:
```python

from random import random

def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)

def takeAWalk(numSteps):
    stepsForwardOfStart = 0
    for step in range(numSteps):
        if random() < 0.5:
            stepsForwardOfStart = stepsForwardOfStart - 1
        else:
            stepsForwardOfStart = stepsForwardOfStart + 1
    return abs(stepsForwardOfStart)
```

Or a visual GUI program like:
```python
from tkinter import *

class PosApp:
    def __init__(self):
        self.win = Tk()
        self.win.title("POS System")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack()

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
        totalLabel.pack()

        addItemButton = Button(
            self.mainFrame,
            text="Add Item",
            command=lambda: self.createNewWin(totalLabel)
        )
        addItemButton.pack()

    def createNewWin(self, totalLabel):
        newWin = Toplevel(self.win)
        newWin.title("Add Item to Bill")

        newWinFrame = Frame(newWin)
        newWinFrame.pack()

        itemPriceLabel = Label(newWinFrame, text="Item Price (£):")
        itemPriceLabel.pack()

        itemPriceEntry = Entry(
            newWinFrame,
            textvariable=self.newItemPrice
        )
        itemPriceEntry.pack()

        addButton = Button(
            newWinFrame,
            text="Add to Bill",
            command=lambda: self.updateBill(
                totalLabel, newWin)
        )
        addButton.pack()

    def updateBill(self, totalLabel, newWin):
        newTotal = self.total.get() + self.newItemPrice.get()
        self.total.set(newTotal)
        self.newItemPrice.set(0.00)
        totalLabel.config(
            text=f"Total Bill: £{self.total.get():.2f}")

        newWin.destroy()


def main():
    app = PosApp()
    app.run()
```

Ideally I want you to change the sample code, presenting an issue in the code and then teach them to use debugging tools to find the issue.


## Programming exercises:

1. A divide application that checks if the divisor is not 0. First a simple textual version and then a GUI version. I can provide the skeleton code for both (students need to add the exception handling part).
Here is a calculator app that the students already have:
```py
from tkinter import *


class Calculator:
    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("200x150")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack()

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result: 0")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblNum1 = Label(self.mainFrame, text="Number 1:")
        lblNum1.pack()

        entryNum1 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num1
        )
        entryNum1.pack()

        lblNum2 = Label(self.mainFrame, text="Number 2:")
        lblNum2.pack()

        entryNum2 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num2
        )
        entryNum2.pack()

        lblResult = Label(
            self.mainFrame,
            textvariable=self.result
        )
        lblResult.pack()

        btnMultiply = Button(
            self.mainFrame,
            text="Multiply",
            command=self.multiply
        )
        btnMultiply.pack(side="left")

        btnClear = Button(
            self.mainFrame,
            text="Clear",
            command=self.win.quit
        )
        btnClear.pack(side="right")

    def multiply(self):
        num1 = self.num1.get()
        num2 = self.num2.get()

        result = num1 * num2
        self.result.set(f"Result: {result}")


def main():
    calc = Calculator()
    calc.run()
```
2. Update the GUI apps from last week so a new customer's name cannot be empty. Here is the code that the students already have:
This is the code that the students already have:
```python
from tkinter import *
from backend import CoffeeShop

class CoffeeShopApp:
    def __init__(self, coffeeShop):
        self.coffeeShop = coffeeShop

        self.win = Tk()
        self.win.title("Coffee Shop")

        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(
            row=0,
            column=0,
        )

        self.newCustomerName = StringVar()

        self.customerWidgets = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        self.deleteAllCustomerWidgets()

        customerEntry = Entry(
            self.mainFrame,
            textvariable=self.newCustomerName
        )
        customerEntry.grid(
            row=0,
            column=0,
        )

        addCustomerButton = Button(
            self.mainFrame,
            text="Add",
            command=self.addCustomer
        )
        addCustomerButton.grid(
            row=0,
            column=1,
        )

        numCustomers = self.coffeeShop.getNumCustomers()
        for i in range(numCustomers):
            customer = self.coffeeShop.getCustomerAt(i)
            customerLabel = Label(
                self.mainFrame,
                text=customer
            )
            customerLabel.grid(
                row=i+1,
                column=0,
            )
            self.customerWidgets.append(customerLabel)

            removeCustomerButton = Button(
                self.mainFrame,
                text="Remove",
                command=lambda index=i: self.removeCustomer(index)
            )
            removeCustomerButton.grid(
                row=i+1,
                column=1,
            )
            self.customerWidgets.append(removeCustomerButton)

    def addCustomer(self):
        name = self.newCustomerName.get()
        self.coffeeShop.addCustomer(name)
        self.createWidgets()
        self.newCustomerName.set("")

    def removeCustomer(self, index):
        self.coffeeShop.removeCustomerAt(index)
        self.createWidgets()

    def deleteAllCustomerWidgets(self):
        for widget in self.customerWidgets:
            widget.destroy()


def main():
    coffeeShop = CoffeeShop()

    coffeeShop.addCustomer("Alice")
    coffeeShop.addCustomer("Bob")
    coffeeShop.addCustomer("Charlie")

    app = CoffeeShopApp(coffeeShop)
    app.run()
```

And this is what is in `backend.py`:
```python
class CoffeeShop:
    def __init__(self):
        self.customers = []

    def addCustomer(self, name):
        self.customers.append(name)

    def removeCustomerAt(self, index):
        del self.customers[index]

    def getCustomerAt(self, index):
        return self.customers[index]

    def getNumCustomers(self):
        return len(self.customers)
```

3. A similar change on the POS app (shown earlier) to prevent a new number on the new window app/new bill on to be empty/negative


## Lecture multiple choice questions

2. **What does the `try` block do?**
   - A. It tests a block of code for errors.
   - B. It executes code regardless of the result of error handling.
   - C. It only runs if no errors are found in the code.
   - D. It declares variables used in error handling.
   - F. It checks the syntax of the enclosed code.

The correct answer is: A because the `try` block lets you test a block of code for errors.



5. What is the right syntax to catch two exceptions in the same except line? 
    raise (ValueError, TypeError)
    except ValueError, TypeError:
    except (ValueError, TypeError):
    except ValueError or TypeError:

The correct answer is: except (ValueError, TypeError):







Let's talk about section 1 of chapter 3 (introduction to debugging)
I want to teach the students some basic concepts of debugging before showing them how to use the debugger in Thonny.

And then I want to show them how to debug in Thonny (I will also add links how to do it in other IDEs like PyCharm and Visual Studio Code so don't worry about that).

Content for slides and worksheets (bullet points for slides, short instructions for worksheets). Paraphrase the content below in your own words.

Thonny has a "debugger," which lets us walk through our program step-by-step to actually see what it is doing. At the top of the Thonny window, next to the run button, you will see a series of buttons that look like this:
[Image will be added here](#)

The buttons at the top of the Thonny window starting with the run button (a white triangle in a green circle). Next to that there's a debug button, whose icon looks like a bug, and then a series of grayed-out buttons with different yellow arrows on them. Finally, there's the 🛑 button, which is a red stop sign.
[Image will be added here](#)

To activate the debugger, simply click on the button that looks like a 🪲 (the creepy-crawly kind), instead of the normal run button. When you do that, the buttons will change so that they look like this:
[Image will be added here](#)

These buttons allow you to control the flow of the program step-by-step, and Thonny will show you exactly what is happening by highlighting the part of the code being evaluated. Note that it can only debug a program (in the top window), not code in the shell (the bottom window).

Try it out
In the `pract14.py` add the following functions:

```python
def mystery(a, b):
    print(a, b)

def main():
    a = 7
    b = 3
    mystery(b, a)
```

Now, click the debug button and then use the "step into" button (the middle yellow button with an arrow pointing down between two lines) to go through the steps of this program.

Before you step through it completely, take a guess at how many steps are in this program (it's more than you might think).

The next time you're stuck on something, try using the debugger to see what's happening in detail.

Breakpoints
Since programs have so many steps, it may take a while to get to the part of your code that you're interested in when debugging. To speed things up, you can set a "breakpoint" by clicking on the left-hand margin where the line numbers are. A red dot will appear in the margin near whichever line you clicked on (as long as it wasn't a comment or a blank line where there isn't any code). If you set a breakpoint on line 3 of `pract14.py` it will look like this:
[Image will be added here](#)

The code in `pract14.py`, as displayed in Thonny, with a red dot in the
left margin next to the start of the third line.

Now, if you run in debug mode, it will fast forward straight to that line of code, and if you use the "Resume" button while debugging, it will also stop as soon as it gets to any line of code with a breakpoint on it. To remove a breakpoint, simply click the line number again.
