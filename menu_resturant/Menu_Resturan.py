from tkinter import * 

window = Tk()
window.title("Beau Resturant")
window.minsize(width=500 , height=700)
window.configure(bg="#00c3c3")

def button_clicked():
    burger_total = int(burger_sb.get()) * 5
    steak_total = int(steack_sb.get()) * 15
    crab_total = int(crab_sb.get()) * 30
    ct_total = int(ct_sb.get()) * 3
    coffee_total = int(coffee_sb.get()) * 4
    Coca_Cola_total = int(Coca_Cola_sb.get()) * 2
    total_bills = burger_total + steak_total + crab_total + ct_total + Coca_Cola_total + coffee_total
    bills = Label(text=f"Your Total Bill : ${total_bills}",font=("Times New Roman",18,"bold"),bg="tomato")
    bills.place(x=140,y=600)

resto_name = Label(text="WELCOME TO\nBEAU RESTURANT", font=("Times New Roman",20,"bold"), bg="#00c3c3")
resto_name.grid(column=1,row=0)

quote = Label(text="We Serve What You Deserve", font=("Times New Roman",18,"italic"), bg="#00c3c3")
quote.grid(column=1,row=2)

food_label = Label(text="Choose Your Food", font=("Times New Roman",12,"normal"), bg="#00c3c3")
food_label.grid(column=0,row=3)

burger = PhotoImage(file="burger3.png")
burger_label = Label(image=burger, borderwidth=0)
burger_label.place(x=40,y=130)
burger_info = Label(text="Spicy Chicken Burger\n$5", font=("Times New Roman",10,"normal"), bg="#00c3c3")
burger_info.place(x=40,y=260)
burger_sb = Spinbox(from_=0,to=10,width=5)
burger_sb.place(x=80,y=300)

steack = PhotoImage(file="Steak2.png")
steack_label = Label(image=steack, borderwidth=0)
steack_label.place(x=190,y=130)
steack_info = Label(text="Rid Eye Steak\n$15", font=("Times New Roman",10,"normal"), bg="#00c3c3")
steack_info.place(x=210,y=260)
steack_sb = Spinbox(from_=0,to=10,width=5)
steack_sb.place(x=225,y=300)

crab = PhotoImage(file="crab2.png")
crab_label = Label(image=crab, borderwidth=0)
crab_label.place(x=340,y=130)
crab_info = Label(text="Indian Crab Curry\n$30", font=("Times New Roman",10,"normal"), bg="#00c3c3")
crab_info.place(x=350,y=260)
crab_sb = Spinbox(from_=0,to=10,width=5)
crab_sb.place(x=380,y=300)

drink_label = Label(text="Choose Your Drink", font=("Times New Roman",12,"normal"), bg="#00c3c3")
drink_label.place(x=0,y=325)

ct = PhotoImage(file="ct.png")
ct_label = Label(image=ct, borderwidth=0)
ct_label.place(x=40,y=350)
ct_info = Label(text="Orenge Lagoon Cocktail\n$3 ", font=("Times New Roman",10,"normal"), bg="#00c3c3")
ct_info.place(x=40,y=480)
ct_sb = Spinbox(from_=0,to=10,width=5)
ct_sb.place(x=80,y=520)

coffee = PhotoImage(file="coffee.png")
coffee_label = Label(image=coffee, borderwidth=0)
coffee_label.place(x=190,y=350)
coffee_info = Label(text="American bitter coffee\n$4 ", font=("Times New Roman",10,"normal"), bg="#00c3c3")
coffee_info.place(x=185,y=480)
coffee_sb = Spinbox(from_=0,to=10,width=5)
coffee_sb.place(x=225,y=520)

Coca_Cola = PhotoImage(file="Coca Cola.png")
Coca_Cola_label = Label(image=Coca_Cola, borderwidth=0)
Coca_Cola_label.place(x=340,y=350)
Coca_Cola_info = Label(text="Coca soft drink\n$2 ", font=("Times New Roman",10,"normal"), bg="#00c3c3")
Coca_Cola_info.place(x=360,y=480)
Coca_Cola_sb = Spinbox(from_=0,to=10,width=5)
Coca_Cola_sb.place(x=380,y=520)

finish = Button(text="Order" , command=button_clicked)
finish.place(x=210,y=560)

window.mainloop()
