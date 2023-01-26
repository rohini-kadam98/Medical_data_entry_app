from tkinter import*
root=Tk()

def getvals():
    print("submitting form")
    print(f"{visit_datevalue.get(),namevalue.get(),product_namevalue.get(),total_billvalue.get()}")

    with open("medical_bill_records.txt","a") as f:
        f.write(f"{visit_datevalue.get(),namevalue.get(),product_namevalue.get(),total_billvalue.get()}\n")

root.geometry("455x305")

Label(root,text="welcome to Disha medical",font="comicsansms 20 bold",pady=15).grid(row=0,column=3)

visit_date=Label(root,text="visit_date")
name=Label(root,text="name")
product_name=Label(root,text="product_name")
total_bill=Label(root,text="total_bill")

visit_date.grid(row=1,column=2)
name.grid(row=2,column=2)
product_name.grid(row=3,column=2)
total_bill.grid(row=4,column=2)

visit_datevalue=StringVar()
namevalue=StringVar()
product_namevalue=StringVar()
total_billvalue=StringVar()

visit_dateentry=Entry(root,textvariable=visit_datevalue)
nameentry=Entry(root,textvariable=namevalue)
product_nameentry=Entry(root,textvariable=product_namevalue)
total_billentry=Entry(root,textvariable=total_billvalue)

visit_dateentry.grid(row=1,column=3)
nameentry.grid(row=2,column=3)
product_nameentry.grid(row=3,column=3)
total_billentry.grid(row=4,column=3)

Button(text="submit to krishna medical",command=getvals).grid(row=6,column=3)

root.mainloop()