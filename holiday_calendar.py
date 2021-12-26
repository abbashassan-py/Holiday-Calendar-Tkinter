
# python program demonstrating
# Combobox widget using tkinter
import holidays
from holidays import countries
from datetime import time
import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
window.configure(bg="black")

# label text for title
ttk.Label(window, text="holidays",
          font=("Century Gothic", 20), background="black", foreground="grey").grid(row=0, column=1)

# label
ttk.Label(window, text="Select the Country :",
          font=("Century Gothic", 10), background="black", foreground="grey").grid(column=0,
                                                                                   row=5, padx=10, pady=25)

# Combobox creation
n = tk.StringVar()
Countrychoosen = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
with open("country.txt", "r") as f:
    list = []
    for line in f:
        list.append(line)

Countrychoosen['values'] = (list)

Countrychoosen.grid(column=1, row=5)
Countrychoosen.current()
# ----------------------------------------------------------------------------------


def select(event):  # the function to get triggered each time you choose something
   # for x, res in enumerate(list):
    #print(x, ":", res)

    if Countrychoosen.get() == list[0]:  # if it is the first item
        for days in sorted(holidays.Angola(years=2022).items()):
            print(days)
        print('------------------------------------------------------')
    elif Countrychoosen.get() == list[1]:  # if it is the second item
        for days in sorted(holidays.Argentina(years=2022).items()):
            print(days)
        print('-----------------------------------------------------')
    elif Countrychoosen.get() == list[2]:  # or if it is the third item
        for days in sorted(holidays.Australia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[3]:  # or if it is the third item
        for days in sorted(holidays.Austria(years=2022).items()):
            print(days)
        print('-------------------------------')

    elif Countrychoosen.get() == list[4]:  # or if it is the third item
        for days in sorted(holidays.Bangladesh(years=2022).items()):
            print(days)
        print('-------------------------------')

    elif Countrychoosen.get() == list[5]:  # or if it is the third item
        for days in sorted(holidays.Belarus(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[6]:  # or if it is the third item
        for days in sorted(holidays.Belgium(years=2022).items()):
            print(days)
        print('-------------------------------')

    elif Countrychoosen.get() == list[7]:  # or if it is the third item
        for days in sorted(holidays.Brazil(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[8]:  # or if it is the third item
        for days in sorted(holidays.Bulgaria(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[9]:  # or if it is the third item
        for days in sorted(holidays.Burundi(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[10]:  # or if it is the third item
        for days in sorted(holidays.Canada(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[11]:  # or if it is the third item
        for days in sorted(holidays.Chile(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[12]:  # or if it is the third item
        for days in sorted(holidays.China(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[13]:  # or if it is the third item
        for days in sorted(holidays.Colombia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[14]:  # or if it is the third item
        for days in sorted(holidays.Croatia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[15]:  # or if it is the third item
        for days in sorted(holidays.Denmark(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[16]:  # or if it is the third item
        for days in sorted(holidays.Djibouti(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[17]:  # or if it is the third item
        for days in sorted(holidays.DominicanRepublic(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[18]:  # or if it is the third item
        for days in sorted(holidays.Egypt(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[19]:  # or if it is the third item
        for days in sorted(holidays.England(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[20]:  # or if it is the third item
        for days in sorted(holidays.Estonia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[21]:  # or if it is the third item
        for days in sorted(holidays.EuropeanCentralBank(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[22]:  # or if it is the third item
        for days in sorted(holidays.Finland(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[23]:  # or if it is the third item
        for days in sorted(holidays.France(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[24]:  # or if it is the third item
        for days in sorted(holidays.Georgia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[25]:  # or if it is the third item
        for days in sorted(holidays.Germany(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[26]:  # or if it is the third item
        for days in sorted(holidays.Greece(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[27]:  # or if it is the third item
        for days in sorted(holidays.Honduras(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[28]:  # or if it is the third item
        for days in sorted(holidays.HongKong(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[29]:  # or if it is the third item
        for days in sorted(holidays.Hungary(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[30]:  # or if it is the third item
        for days in sorted(holidays.iceland(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[31]:  # or if it is the third item
        for days in sorted(holidays.India(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[32]:  # or if it is the third item
        for days in sorted(holidays.Israel(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[33]:  # or if it is the third item
        for days in sorted(holidays.Italy(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[34]:  # or if it is the third item
        for days in sorted(holidays.Jamaica(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[35]:  # or if it is the third item
        for days in sorted(holidays.Japan(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[36]:  # or if it is the third item
        for days in sorted(holidays.Kenya(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[37]:  # or if it is the third item
        for days in sorted(holidays.Korea(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[38]:  # or if it is the third item
        for days in sorted(holidays.Latvia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[39]:  # or if it is the third item
        for days in sorted(holidays.Lesotho(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[40]:  # or if it is the third item
        for days in sorted(holidays.Luxembourg(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[41]:  # or if it is the third item
        for days in sorted(holidays.Malaysia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[42]:  # or if it is the third item
        for days in sorted(holidays.Malawi(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[43]:  # or if it is the third item
        for days in sorted(holidays.Mexico(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[44]:  # or if it is the third item
        for days in sorted(holidays.Morocco(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[45]:  # or if it is the third item
        for days in sorted(holidays.Mozambique(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[46]:  # or if it is the third item
        for days in sorted(holidays.Namibia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[47]:  # or if it is the third item
        for days in sorted(holidays.NewZealand(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[48]:  # or if it is the third item
        for days in sorted(holidays.Nicaragua(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[49]:  # or if it is the third item
        for days in sorted(holidays.Nigeria(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[50]:  # or if it is the third item
        for days in sorted(holidays.Norway(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[51]:  # or if it is the third item
        for days in sorted(holidays.Paraguay(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[52]:  # or if it is the third item
        for days in sorted(holidays.Peru(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[53]:  # or if it is the third item
        for days in sorted(holidays.Poland(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[54]:  # or if it is the third item
        for days in sorted(holidays.Portugal(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[55]:  # or if it is the third item
        for days in sorted(holidays.Romania(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[56]:  # or if it is the third item
        for days in sorted(holidays.Russia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[57]:  # or if it is the third item
        for days in sorted(holidays.SaudiArabia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[58]:  # or if it is the third item
        for days in sorted(holidays.Singapore(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[59]:  # or if it is the third item
        for days in sorted(holidays.Slovakia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[60]:  # or if it is the third item
        for days in sorted(holidays.SouthAfrica(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[61]:  # or if it is the third item
        for days in sorted(holidays.Spain(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[62]:  # or if it is the third item
        for days in sorted(holidays.Swaziland(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[63]:  # or if it is the third item
        for days in sorted(holidays.Sweden(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[64]:  # or if it is the third item
        for days in sorted(holidays.Switzerland(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[65]:  # or if it is the third item
        for days in sorted(holidays.Turkey(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[66]:  # or if it is the third item
        for days in sorted(holidays.Ukraine(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[67]:  # or if it is the third item
        for days in sorted(holidays.UnitedArabEmirates(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[68]:  # or if it is the third item
        for days in sorted(holidays.UnitedKingdom(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[69]:  # or if it is the third item
        for days in sorted(holidays.UnitedStates(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[70]:  # or if it is the third item
        for days in sorted(holidays.Venezuela(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[71]:  # or if it is the third item
        for days in sorted(holidays.Vietnam(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[72]:  # or if it is the third item
        for days in sorted(holidays.Wales(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[73]:  # or if it is the third item
        for days in sorted(holidays.Zambia(years=2022).items()):
            print(days)
        print('-------------------------------')
    elif Countrychoosen.get() == list[74]:  # or if it is the third item
        for days in sorted(holidays.Zimbabwe(years=2022).items()):
            print(days)
        print('-------------------------------')


b1 = tk.Button(window,  text='Show Value', bg="black",
               foreground="grey", font=("Century Gothic", 10), command=lambda: select(window))
b1.grid(column=1, row=8)
#Countrychoosen.bind('<<ComboboxSelected>>', select)
window.mainloop()
