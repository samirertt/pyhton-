from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pandas as pd


klasik_pizza_malzeme = ['Mozarella', 'Pepperoni', 'Basil', 'Green Pepper']
turk_pizza_malzeme = ['Mozarella', 'Mushroom', 'Green Pepper', 'Onion']
margarita_pizza_malzeme = ['Spicy Tomato Sauce', 'Mozarella']
sade_pizza_malzeme = ['Mozarella', 'Basil', 'Green Pepper']
extra_malzemeler = ['mushrooms', 'olives', 'onions', 'peppers', 'garlic', 'anchovies', 'sausage', 'pepperoni', 'bacon',
                    'ham', 'pineapple', 'extra cheese']
card = []



class MainWindow:
    def __init__(self, master):
        self.master = master
        self.father = master
        self.father.title("Serdar pizza Registration")
        self.father.geometry("600x400")

        self.name_label = Label(root, text="Name")
        global txt_name

        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(root)
        txt_name = self.name_entry
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.tckn_label = Label(root, text="Identity Number")
        global txt_tckn

        self.tckn_label.grid(row=1, column=0, padx=10, pady=10)
        self.tckn_entry = Entry(root)
        txt_tckn = self.tckn_entry
        self.tckn_entry.grid(row=1, column=1, padx=10, pady=10)





        Button(master, text="Enter", command=self.open_new_window).grid(row=3, column=1, padx=10, pady=10)



    def open_new_window(self):
        order_Window(self.master)



class order_Window:

    def pizza_sizes_selected_comboclick(self):
        print("size: %s" % (self.pizza_sizes_selection_combobox.get()))




    def __init__(self, master):
        self.master = master
        self.top = Toplevel(self.master)
        self.top.title("Welcome to Serdar Pizza")
        self.top.geometry("1640x1000")

        self.image1 = Image.open("klasik_pizza.png").resize((250, 250), Image.LANCZOS)
        self.image2 = Image.open("turk_pizza.jpg").resize((250, 250), Image.LANCZOS)
        self.image3 = Image.open("margarita_pizza.jpg").resize((250, 250), Image.LANCZOS)
        self.image4 = Image.open("sade_pizza.jpg").resize((250, 250), Image.LANCZOS)
        self.image5 = Image.open("pizza_image.png").resize((250, 250), Image.LANCZOS)

        self.tk_image1 = ImageTk.PhotoImage(self.image1)
        self.tk_image2 = ImageTk.PhotoImage(self.image2)
        self.tk_image3 = ImageTk.PhotoImage(self.image3)
        self.tk_image4 = ImageTk.PhotoImage(self.image4)
        self.tk_image5 = ImageTk.PhotoImage(self.image5)

        self.image1_label = Label(self.top, image=self.tk_image1)
        self.image2_label = Label(self.top, image=self.tk_image2)
        self.image3_label = Label(self.top, image=self.tk_image3)
        self.image4_label = Label(self.top, image=self.tk_image4)
        self.image5_label = Label(self.top, image=self.tk_image5)

        self.image1_label.grid(row=0, column=0, padx=10, pady=10)
        self.image2_label.grid(row=0, column=1, padx=10, pady=10)
        self.image3_label.grid(row=0, column=2, padx=10, pady=10)
        self.image4_label.grid(row=0, column=3, padx=10, pady=10)
        self.image5_label.grid(row=0, column=4, padx=10, pady=10)

        Label(self.top, text="Klasik Pizza", font="Arial").grid(row=1, column=0, padx=10, pady=10)
        Label(self.top, text="Turk Pizza", font="Arial").grid(row=1, column=1, padx=10, pady=10)
        Label(self.top, text="Margarita Pizza", font= "Arial").grid(row=1, column=2, padx=10, pady=10)
        Label(self.top, text="Sade Pizza", font="Arial").grid(row=1,column=3, padx=10, pady=10)
        Label(self.top, text="Select Pizza", font="Arial").grid(row=1, column=4, padx=10, pady=10)

        Label(self.top, text="Please select size", font=("Times", 13)).grid(row=2, column=0, pady=10)
        Label(self.top, text="Please select size", font=("Times", 13)).grid(row=2, column=1, pady=10)
        Label(self.top, text="Please select size", font=("Times", 13)).grid(row=2, column=2, pady=10)
        Label(self.top, text="Please select size", font=("Times", 13)).grid(row=2, column=3, pady=10)
        Label(self.top, text="Please select size", font=("Times", 13)).grid(row=2, column=4, pady=10)

        #1
        self.options_pizza_sizes = [
            "Small",
            "Medium",
            "Large",
        ]

        self.pizza_sizes_selection_combobox_1 = ttk.Combobox(self.top, values=self.options_pizza_sizes)
        self.pizza_sizes_selection_combobox_1.current(0)
        self.pizza_sizes_selection_combobox_1.bind("<<CompoboxSelected>>", self.pizza_sizes_selected_comboclick)
        self.pizza_sizes_selection_combobox_1.grid(row=3, column=0, padx=50)

        #2
        self.options_pizza_sizes = [
            "Small",
            "Medium",
            "Large",
        ]

        self.pizza_sizes_selection_combobox_2 = ttk.Combobox(self.top, values=self.options_pizza_sizes)
        self.pizza_sizes_selection_combobox_2.current(0)
        self.pizza_sizes_selection_combobox_2.bind("<<CompoboxSelected>>", self.pizza_sizes_selected_comboclick)
        self.pizza_sizes_selection_combobox_2.grid(row=3, column=1, padx=50)

        #3
        self.options_pizza_sizes = [
            "Small",
            "Medium",
            "Large",
        ]

        self.pizza_sizes_selection_combobox_3 = ttk.Combobox(self.top, values=self.options_pizza_sizes)
        self.pizza_sizes_selection_combobox_3.current(0)
        self.pizza_sizes_selection_combobox_3.bind("<<CompoboxSelected>>", self.pizza_sizes_selected_comboclick)
        self.pizza_sizes_selection_combobox_3.grid(row=3, column=2, padx=50)

        #4
        self.options_pizza_sizes = [
            "Small",
            "Medium",
            "Large",
        ]

        self.pizza_sizes_selection_combobox_4 = ttk.Combobox(self.top, values=self.options_pizza_sizes)
        self.pizza_sizes_selection_combobox_4.current(0)
        self.pizza_sizes_selection_combobox_4.bind("<<CompoboxSelected>>", self.pizza_sizes_selected_comboclick)
        self.pizza_sizes_selection_combobox_4.grid(row=3, column=3, padx=50)

        #5
        self.options_pizza_sizes = [
            "Small",
            "Medium",
            "Large",
        ]

        self.pizza_sizes_selection_combobox_5 = ttk.Combobox(self.top, values=self.options_pizza_sizes)
        self.pizza_sizes_selection_combobox_5.current(0)
        self.pizza_sizes_selection_combobox_5.bind("<<CompoboxSelected>>", self.pizza_sizes_selected_comboclick)
        self.pizza_sizes_selection_combobox_5.grid(row=3, column=4, padx=50)

        for i, malzeme in enumerate(klasik_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=0, pady=3)

        for i, malzeme in enumerate(turk_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=1, pady=3)

        for i, malzeme in enumerate(margarita_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=2, pady=3)

        for i, malzeme in enumerate(sade_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=3, pady=3)

        for i, malzeme in enumerate(extra_malzemeler):
            Label(self.top, text=malzeme).grid(row=4+i, column=5, pady=3)

        Label(self.top, text="Extra Malzemeler", font=("Times", 14)).grid(row=3, column=5, pady=3)

        


        Button(self.top, text="Choose", command=self.pizza_malzeme_choose_1).grid(row=12, column=0)
        Button(self.top, text="Choose", command=self.pizza_malzeme_choose_2).grid(row=12, column=1)
        Button(self.top, text="Choose", command=self.pizza_malzeme_choose_3).grid(row=12, column=2)
        Button(self.top, text="Choose", command=self.pizza_malzeme_choose_4).grid(row=12, column=3)

        Button(self.top, text="cashout", command=self.open_cashout_window).grid(row=2, column=5, padx=10, pady=10)

    def button_click_pizza(button_number):
        print(f"Button {button_number} clicked.")

    def pizza_malzeme_choose_1(self):
        pizza_size = self.pizza_sizes_selection_combobox_1.get()
        pizza_type = "Klasik_pizza"
        print(pizza_size + " " + pizza_type)
        self.pizza_malzeme_choosing_1()

    def pizza_malzeme_choose_1_and_button_click_pizza(self):
        self.button_click_pizza()
        self.pizza_malzeme_choose_1()

    def pizza_malzeme_choose_2(self):
        pizza_size = self.pizza_sizes_selection_combobox_2.get()
        pizza_type = "turk_pizza"
        print(pizza_size + " " + pizza_type)
        self.pizza_malzeme_choosing_2()

    def pizza_malzeme_choose_2_and_button_click_pizza(self):
        self.button_click_pizza()
        self.pizza_malzeme_choose_2()

    def pizza_malzeme_choose_3(self):
        pizza_size = self.pizza_sizes_selection_combobox_3.get()
        pizza_type = "margarita_pizza"
        print(pizza_size + " " + pizza_type)
        self.pizza_malzeme_choosing_3()
    
    def pizza_malzeme_choose_3_and_button_click_pizza(self):
        self.button_click_pizza()
        self.pizza_malzeme_choose_3()

    def pizza_malzeme_choose_4(self):
        pizza_size = self.pizza_sizes_selection_combobox_4.get()
        pizza_type = "sade_pizza"
        print(pizza_size + " " + pizza_type)
        self.pizza_malzeme_choosing_4()

    def pizza_malzeme_choose_4_and_button_click_pizza(self):
        self.button_click_pizza()
        self.pizza_malzeme_choose_4()

    def klasik_icerik(self):
        for i, malzeme in enumerate(klasik_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=0, pady=3)

    def turk_icerik(self):
        for i, malzeme in enumerate(turk_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=1, pady=3)


    def margarita_icerik(self):
        for i, malzeme in enumerate(margarita_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=2, pady=3)


    def sade_icerik(self):
        for i, malzeme in enumerate(sade_pizza_malzeme):
            Label(self.top, text=malzeme).grid(row=4+i, column=3, pady=3)


    def pizza_malzeme_choosing_1(self):
        self.pizza_choose_entry = Entry(self.top)
        self.pizza_choose_entry.grid(row=13, column=0)
        Button(self.top, text="Add",command=self.klasik_pizza_ekleme).grid(row=14, column=0)
        Button(self.top, text="Remove",command=self.klasik_pizza_malzeme_cikar).grid(row=15, column=0)
        Button(self.top, text="Add To Card",command=self.addto_card1).grid(row=16, column=0)
    def klasik_pizza_ekleme(self):
        value = self.pizza_choose_entry.get()
        klasik_pizza_malzeme.append(value)
        self.klasik_icerik()
        print(klasik_pizza_malzeme)

    def klasik_pizza_malzeme_cikar(self):
        value = self.pizza_choose_entry.get()
        klasik_pizza_malzeme.remove(value)
        self.klasik_icerik()
        print(klasik_pizza_malzeme)


    def pizza_malzeme_choosing_2(self):
        self.pizza_choose_entry = Entry(self.top)
        self.pizza_choose_entry.grid(row=13, column=1)
        Button(self.top, text="Add",command=self.turk_pizza_ekleme).grid(row=14, column=1)
        Button(self.top, text="Remove",command=self.turk_pizza_malzeme_cikar).grid(row=15, column=1)
        Button(self.top, text="Add To Card",command=self.addto_card2).grid(row=16, column=1)
    
    def turk_pizza_ekleme(self):
        value = self.pizza_choose_entry.get()
        turk_pizza_malzeme.append(value)
        self.turk_icerik()
        print(turk_pizza_malzeme)

    def turk_pizza_malzeme_cikar(self):
        value = self.pizza_choose_entry.get()
        turk_pizza_malzeme.remove(value)
        
        self.turk_icerik()
        print(turk_pizza_malzeme)





    def pizza_malzeme_choosing_3(self):
        self.pizza_choose_entry = Entry(self.top)
        self.pizza_choose_entry.grid(row=13, column=2)
        Button(self.top, text="Add",command=self.margarita_pizza_ekleme).grid(row=14, column=2)
        Button(self.top, text="Remove",command=self.margarita_pizza_malzeme_cikar).grid(row=15, column=2)
        Button(self.top, text="Add To Card",command=self.addto_card3).grid(row=16, column=2)
    def margarita_pizza_ekleme(self):
        value = self.pizza_choose_entry.get()
        margarita_pizza_malzeme.append(value)
        self.margarita_icerik()
        print(margarita_pizza_malzeme)

    def margarita_pizza_malzeme_cikar(self):
        value = self.pizza_choose_entry.get()
        margarita_pizza_malzeme.remove(value)
        
        self.margarita_icerik()
        print(margarita_pizza_malzeme)
    


    def pizza_malzeme_choosing_4(self):
        self.pizza_choose_entry = Entry(self.top)
        self.pizza_choose_entry.grid(row=13, column=3)
        Button(self.top, text="Add",command=self.sade_pizza_ekleme).grid(row=14, column=3)
        Button(self.top, text="Remove",command=self.sade_pizza_malzeme_cikar).grid(row=15, column=3)
        Button(self.top, text="Add To Card",command=self.addto_card4).grid(row=16, column=3)
    
    def addto_card1(self):
        card.append("Klasik Pizza")   
   
    def addto_card2(self):
        card.append("Turk Pizza")

    def addto_card3(self):
        card.append("Margarita Pizza")

    def addto_card4(self):
        card.append("Sade Pizza")

    def sade_pizza_ekleme(self):
        value = self.pizza_choose_entry.get()
        sade_pizza_malzeme.append(value)
        self.sade_icerik()
        print(sade_pizza_malzeme)

    def sade_pizza_malzeme_cikar(self):
        value = self.pizza_choose_entry.get()
        sade_pizza_malzeme.remove(value)
        
        self.sade_icerik()
        print(sade_pizza_malzeme)

    def open_cashout_window(self):
        cashout_Window(self.master)


class cashout_Window:
    def __init__(self, master):
        self.master = master
        self.bottom = Toplevel(self.master)
        self.bottom.title("Cashout page")
        self.bottom.geometry("1000x1000")

        self.my_tree = ttk.Treeview(self.bottom)

        #Defining the columns
        self.my_tree['columns'] = ("Pizza Type", "Cost")

        #formating the columns
        self.my_tree.column("#0",width=0, stretch= NO)
        self.my_tree.column("Pizza Type", anchor=W, width=120)
        self.my_tree.column("Cost", anchor=CENTER, width=80)

        #creating heading
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Pizza Type", text="Name", anchor=W)
        self.my_tree.heading("Cost", text="Cost",anchor=CENTER)

        #data inserting

        toplam = 0
        for i,pizza in enumerate (card):
            if pizza == "Klasik Pizza":
                price = 70
            elif pizza == "Turk Pizza":
                price = 80
            elif pizza == "Margarita Pizza":
                price = 100
            elif pizza == "Sade Pizza":
                price = 60

            toplam += price
        
                

            self.my_tree.insert(parent='', index="end", iid=i, values=(pizza,price))



        self.my_tree.grid(row=0, column=0, padx=10, pady=10)


        global card_number
        global card_pass
        Label(self.bottom,text="Kart Numaranizi giriniz").grid(row=1, column=4)
        self.cc_entry = Entry(self.bottom)
        self.cc_entry.grid(row=2, column=4)
        card_number = self.cc_entry
        Label(self.bottom,text="Kart Numaranizi giriniz").grid(row=3, column=4)
        self.cc_entry_pass = Entry(self.bottom)
        self.cc_entry_pass.grid(row=4, column=4)
        card_pass = self.cc_entry_pass
        Button(self.bottom,text="Pay",command=dbwrite).grid(row=6, column=5,pady=10)
        Button(self.bottom,text=str(toplam)+" TL").grid(row=5, column=5,pady=10)

    
def dbwrite():

    with open("Orders_Database.txt","a") as dosya:
        name = txt_name.get()
        tckn = txt_tckn.get()
        credit_card = card_number.get()
        cc_pass = card_pass.get()


        z = ("\n",str(name)+","+str(tckn)+","+str(credit_card)+","+str(cc_pass))
        dosya.writelines(z)

    dbcsv = pd.read_csv('Orders_Database.txt',header=0,names=['nickname','id_card','card_number','card_password'])
    dbcsv.to_csv('Orders_Database.csv')




root = Tk()
main_window = MainWindow(root)
root.mainloop()



