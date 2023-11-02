# importing all modules to be used tkinter and datetime

from tkinter import *
from tkinter import ttk
import datetime

# create a window or canvas
root = Tk()
root.geometry('500x300')
root.title('Metro_Loan_Calculator')
root.columnconfigure(0, weight=1)
# root.iconphoto(False, PhotoImage(file='logo.png'))

# Tab control to switch between tabs on canvas
tab_control = ttk.Notebook(root)
tab_control.grid(column=0, row=0)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Home')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='History')


# create function to compute results


def computePayment():
    monthPayment = getMonth(
        float(annualRate.get()) / 1200,
        float(loanAmount.get()),
        int(numberOfYears.get()))
    # in case of error removed this ^  (*12) its for trial
    monthly.set(format(monthPayment, '10.2f'))
    total_Payment = float(monthly.get()) * 12 * int(numberOfYears.get())
    totalPayment.set(format(total_Payment, '10.2f'))
    History()


def getMonth( monthlyRate, loan_Amount, noYears):
    monthPayment = loan_Amount * monthlyRate / (1 - 1 / (1 + monthlyRate) ** (noYears * 12))
    # monthPayment = (loan_Amount * monthlyRate) / (noYears * 12)
    # monthPayment = loanAmount * monthlyRate * (1 + monthlyRate) * noYears / ((1+ monthlyRate) * noYears -1)
    # monthPayment = loan_Amount * monthlyRate * (1 + monthlyRate) ** noYears / ((1 + monthlyRate)**noYears) - 1
    return monthPayment

# function to reset all input both labels and int input in tkinter


def reset_Func():
    Rate.delete(0, END)
    Year.delete(0, END)
    Amount1.delete(0, END)
    monthly.set('')
    totalPayment.set('')


# created a function to store all computed result in a text file


def History():
    store_Val = open("doc.txt", "a")
    store_Val.write('\n'),
    store_Val.write(str(datetime.date.today()))
    store_Val.write('\n'),
    store_Val.write('Rate:'),
    store_Val.write('\t'),
    store_Val.write(str(Rate.get())),
    store_Val.write('\n'),
    store_Val.write('Year:'),
    store_Val.write('\t'),
    store_Val.write(str(Year.get())),
    store_Val.write('\n'),
    store_Val.write('Loan Amount:'),
    store_Val.write('\t'),
    store_Val.write(str(Amount1.get())),
    store_Val.write('\n'),
    store_Val.write('Monthly Payment:'),
    store_Val.write('\t'),
    store_Val.write(str(monthly.get())),
    store_Val.write('\n'),
    store_Val.write('Total Payment:'),
    store_Val.write('\t'),
    store_Val.write(str(totalPayment.get()))
    store_Val.write('\n'),
    store_Val.close()

# function for reading the stored input on tab 2


def spy():
    f = open("doc.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        Label(tab2, text=contents,).grid(column=2, row=2, columnspan=3)
        f.close()


design = Label(tab1, text='*****************', font=("TkDefaultFont", 16))
design.grid(row=1, column=0, sticky='w')

design2 = Label(tab1, text='*****************', font=("TkDefaultFont", 16))
design2.grid(row=1, column=1, sticky='w')

loan_Rate = Label(tab1, text='Interest Rate', font=("TkDefaultFont", 16))
loan_Rate.grid(row=2, column=0, sticky='w')

loan_Year = Label(tab1, text='Number of years', font=("TkDefaultFont", 16))
loan_Year.grid(row=3, column=0, sticky='w')

loan_Amount = Label(tab1, text='Loan Amount', font=("TkDefaultFont", 16))
loan_Amount.grid(row=4, column=0, sticky='w')

monthly_payment = Label(tab1, text='Monthly Payment', font=("TkDefaultFont", 16))
monthly_payment.grid(row=5, column=0, sticky='w')

total_payment = Label(tab1, text='Total Payment', font=("TkDefaultFont", 16))
total_payment.grid(row=6, column=0, sticky='w')

annualRate = StringVar()
Rate = Entry(tab1, textvariable=annualRate, justify=LEFT, font=("TkDefaultFont", 16))
Rate.grid(row=2, column=1)

numberOfYears = StringVar()
Year = Entry(tab1, textvariable=numberOfYears, justify=LEFT, font=("TkDefaultFont", 16))
Year.grid(row=3, column=1)

loanAmount = StringVar()
Amount1 = Entry(tab1, textvariable=loanAmount, justify=LEFT, font=("TkDefaultFont", 16))
Amount1.grid(row=4, column=1)

monthly = StringVar()
Amount2 = Label(tab1, textvariable=monthly, font=("TkDefaultFont", 16))
Amount2.grid(row=5, column=1, sticky='e')

totalPayment = StringVar()
Amount3 = Label(tab1, textvariable=totalPayment, font=("TkDefaultFont", 16))
Amount3.grid(row=6, column=1, sticky='e')

compute = ttk.Button(tab1, text='Compute Payment', command=computePayment)
compute.grid(row=7, column=1, sticky=E + W)
trans = ttk.Button(tab2, text='Transaction', command=spy)
trans.grid(row=0, column=1, sticky=E + W)
reset_Btt = ttk.Button(tab1, text='Reset', command=reset_Func)
reset_Btt.grid(row=7, column=0, sticky=E + W)


root.mainloop()
