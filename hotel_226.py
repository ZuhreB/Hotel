from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from tkcalendar import Calendar
from PIL import Image, ImageTk
place_dict = dict({
    "Rome": "-126693",
    "Atina": "-814876",
    "Malesina": "-822930",
    "Milano": "-121726",
    "Bremen": "-1752234",
    "Salta": "-1011490",
    "Bilbao": "-373608",
    "Porto": "-2173088",
    "Eindhoven": "-2144027",
    "Zürih": "-2554935"
})
hotels_data = []
hotels_df = None  #fonksiyonun iiçinde kullanabilmek için ilk önce tanımladım

def start():
    get_inputs()
    global hotels_df
    selection = var.get()
    selection2 =combobox.get()
    if selection == "Euro":
        hotels_df["price"] = hotels_df["price"] / 30
        if selection2=="ASC":
            hotels_df = hotels_df.sort_values(by="price", ascending=True)
            hotels_df_head = hotels_df.head(5)
            hotels_df.to_csv('hotels.csv', index=False)

            bg_new = Image.open("../../../AppData/Roaming/JetBrains/PyCharmCE2023.1/scratches/Tecna_düzenlenmiş.jpg")
            new_width = 1470
            new_height = 640
            resized_image = bg_new.resize((new_width, new_height), Image.LANCZOS)

            tk_image = ImageTk.PhotoImage(resized_image)
            label1 = Label(root, image=tk_image)
            label1.image = tk_image
            label1.place(x=0, y=0)
            text_widget = Text(root)
            text_widget.config(bg="white", fg="purple",width=100,height=26)
            text_widget.place(x=200,y=100)
            for index, hotel in hotels_df_head.iterrows():
                hotel_info = f"Hotel title: {hotel['title']}\n"
                hotel_info += f"Hotel address: {hotel['address']}\n"
                hotel_info += f"Hotel distance: {hotel['distance']}\n"
                hotel_info += f"Hotel rate: {hotel['rate']}\n"
                hotel_info += f"Hotel price: {hotel['price']}\n"
                text_widget.insert(END, hotel_info)

        elif selection2=="DSC":
            hotels_df = hotels_df.sort_values(by="price", ascending=False)
            hotels_df_head = hotels_df.head(5)
            hotels_df.to_csv('hotels.csv', index=False)
            bg_new = Image.open("../../../AppData/Roaming/JetBrains/PyCharmCE2023.1/scratches/Tecna_düzenlenmiş.jpg")
            new_width = 1470
            new_height = 640
            resized_image = bg_new.resize((new_width, new_height), Image.LANCZOS)

            tk_image = ImageTk.PhotoImage(resized_image)
            label1 = Label(root, image=tk_image)
            label1.image = tk_image
            label1.place(x=0, y=0)
            text_widget = Text(root)
            text_widget.config(bg="white", fg="purple")
            text_widget.place(x=200,y=100)
            for index, hotel in hotels_df_head.iterrows():
                hotel_info = f"Hotel title: {hotel['title']}\n"
                hotel_info += f"Hotel address: {hotel['address']}\n"
                hotel_info += f"Hotel distance: {hotel['distance']}\n"
                hotel_info += f"Hotel rate: {hotel['rate']}\n"
                hotel_info += f"Hotel price: {hotel['price']}\n"
                text_widget.insert(END, hotel_info)
    else:
        if selection2 == "ASC":
            hotels_df = hotels_df.sort_values(by="price", ascending=True)
            hotels_df_head = hotels_df.head(5)
            hotels_df.to_csv('hotels.csv', index=False)

            bg_new = Image.open("../../../AppData/Roaming/JetBrains/PyCharmCE2023.1/scratches/Tecna_düzenlenmiş.jpg")
            new_width = 1470
            new_height = 640
            resized_image = bg_new.resize((new_width, new_height), Image.LANCZOS)

            tk_image = ImageTk.PhotoImage(resized_image)
            label1 = Label(root, image=tk_image)
            label1.image = tk_image
            label1.place(x=0, y=0)
            text_widget = Text(root)
            text_widget.config(bg="white", fg="purple")
            text_widget.place(x=200,y=100)
            for index, hotel in hotels_df_head.iterrows():
                hotel_info = f"Hotel title: {hotel['title']}\n"
                hotel_info += f"Hotel address: {hotel['address']}\n"
                hotel_info += f"Hotel distance: {hotel['distance']}\n"
                hotel_info += f"Hotel rate: {hotel['rate']}\n"
                hotel_info += f"Hotel price: {hotel['price']}\n"
                text_widget.insert(END, hotel_info)


        elif selection2 == "DSC":
            hotels_df = hotels_df.sort_values(by="price", ascending=False)
            hotels_df_head = hotels_df.head(5)
            hotels_df.to_csv('hotels.csv', index=False)

            bg_new = Image.open("../../../AppData/Roaming/JetBrains/PyCharmCE2023.1/scratches/Tecna_düzenlenmiş.jpg")
            new_width = 1470
            new_height = 640
            resized_image = bg_new.resize((new_width, new_height), Image.LANCZOS)

            tk_image = ImageTk.PhotoImage(resized_image)
            label1 = Label(root, image=tk_image)
            label1.image = tk_image
            label1.place(x=0, y=0)

            text_widget = Text(root)
            text_widget.config(bg="white", fg="purple")
            text_widget.place(x=200,y=100)
            for index, hotel in hotels_df_head.iterrows():
                hotel_info = f"Hotel title: {hotel['title']}\n"
                hotel_info += f"Hotel address: {hotel['address']}\n"
                hotel_info += f"Hotel distance: {hotel['distance']}\n"
                hotel_info += f"Hotel rate: {hotel['rate']}\n"
                hotel_info += f"Hotel price: {hotel['price']}\n"
                text_widget.insert(END, hotel_info)



def get_inputs():
    global hotels_df
    global hotels_data  # Global olarak tanımlanan listeyi kullanmak için
    hotels_data.clear()  # Önce listeyi temizle

    entered_place = place_new.get()
    dest_id = place_dict.get(entered_place)
    checkin = checkin_calendar.get_date()
    checkout = checkout_calendar.get_date()
    adult = adult_combobox.get()
    child = child_combobox.get()
    room_num = room_combobox.get()
    try:
        checkin_date = datetime.strptime(checkin, '%Y/%m/%d')
        checkout_date = datetime.strptime(checkout, '%Y/%m/%d')
    except ValueError:
        result_label.config(text="Please enter dates in YYYY/MM/dd format")
        return

    if checkin_date <datetime.today():
        result_label.config(text="You can't travel in time, please enter check-in according to today's date.")
        return

    if checkin_date >= checkout_date:
        result_label.config(text="Check-out date must be after check-in date")
        return

    if int(adult) < 1 or int(child) < 0 or int(room_num) < 1:
        result_label.config(text="Please enter valid counts")
        return

    if int(adult)==0 and int(child)>0 :
        result_label.config(text="Not available any children without parents ")
        return

    url = f'https://www.booking.com/searchresults.html?ss={entered_place}&ssne={entered_place}&ssne_untouched={entered_place}&efdco=1&label=gen173nr-1FCAEoggI46AdIM1gEaOQBiAEBmAExuAEHyAEP2AEB6AEBAECiAIBqAIDuAKo8sKxBsACAdICJGZlZWVmNGJjLWI2OGEtNGM0OS05ODk0LTM2ZGQ4YzkxYzY0MNgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id={dest_id}&dest_type=city&checkin={checkin}&checkout={checkout}&group_adults={adult}&no_rooms={room_num}&group_children={child}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    hotels = soup.findAll('div', {'data-testid': 'property-card'})[:10]

    for hotel in hotels:
        title_element = hotel.find('div', {'data-testid': 'title'})
        title = title_element.text.strip()

        if any(hotel_data['title'] == title for hotel_data in hotels_data):
            continue  # Eğer zaten varsa, bu oteli eklemeyi atla

        address_element = hotel.find('span', {'data-testid': 'address'})
        address = address_element.text.strip()

        distance_element = hotel.find("span", {"data-testid": "distance"})
        if distance_element:
            distance = distance_element.text.strip()
        else :
            "Not known"

        rate_element_detail = hotel.find('span', class_='a3332d346a')
        if rate_element_detail:
            rate = rate_element_detail.text.strip()
        else:
            rate_element = hotel.find('div', {'data-testid': 'review-score'})
            if rate_element:
                rate = rate_element.text.strip()

        price_element = hotel.find('span', {'data-testid': 'price-and-discounted-price'})
        if price_element:
            price = price_element.text.strip().replace(',', '')
        else :
            "Not known"

        hotels_data.append({'title': title,
                            'address': address,
                            'distance': distance,
                            'rate': rate,
                            'price': price[2:]})

    hotels_df = pd.DataFrame(hotels_data)
    hotels_df.to_csv('hotels.csv', index=False)
    hotels_df["price"] = hotels_df["price"].astype(float)

places_for_combox=["Rome","Atina","Malesina","Milano","Bremen","Salta","Bilbao","Porto", "Eindhoven","Zürih"]
root = Tk()
root.title("Hotel Booking Wıth Tecna")
root.geometry("1470x640+0+0")
root.config(bg="purple")


bg_new = Image.open("../../../AppData/Roaming/JetBrains/PyCharmCE2023.1/scratches/tecnam.png")
new_width=1470
new_height=640
resized_image=bg_new.resize((new_width,new_height),Image.LANCZOS)
tk_image=ImageTk.PhotoImage(resized_image)
label1 = Label(root, image=tk_image).place(x=0,y=0)

label = Label(root, text="Tecna search for you please choose the sorted and click the show hotel",
                  font=("Arial",12,"bold" ),bg="dark orchid",fg="white")
label.place(x=700, y=450)

places = Label(root, text="Enter the place you want to go:",bg="dark orchid",fg="white",width=30,height=1)
places.place(x=50, y=50)

place_new = Combobox(root,values=places_for_combox,state="readonly")
place_new.place(x=50, y=80)

root.option_add('*TCombobox*Listbox.background', 'orchid')
root.option_add('*TCombobox*Listbox.foreground', 'white')

checkin_label = Label(root, text="Check-in Date (YYYY-MM-DD):",bg="dark orchid",fg="white",width=30,height=1)
checkin_label.place(x=50, y=350)

checkin_calendar = Calendar(root, selectmode="day", date_pattern="yyyy/MM/dd")
checkin_calendar.place(x=50, y=380)

checkout_label = Label(root, text="Check-out Date (YYYY-MM-DD):",bg="dark orchid",fg="white",width=30,height=1)
checkout_label.place(x=350, y=350)

checkout_calendar = Calendar(root, selectmode="day", date_pattern="yyyy/MM/dd")
checkout_calendar.place(x=350, y=380)

checkin_calendar.bind("<<CalendarSelected>>", lambda event: get_inputs())
checkout_calendar.bind("<<CalendarSelected>>", lambda event: get_inputs())
numberofpeople=["1","2","3","4","5","6","7","8","9","10"]
numberofchilderen=["0","1","2","3","4","5","6","7","8","9","10"]
adult_label =Label(root, text="Number of Adults:",bg="dark orchid",fg="white",width=30,height=1)
adult_label.place(x=50,y=110)
adult_combobox=StringVar()
adult_combobox=Combobox(root,textvariable=adult_combobox,values=numberofpeople,state="readonly")
adult_combobox.place(x=50,y=140)

child_label = Label(root, text="Number of Children:",bg="dark orchid",fg="white",width=30,height=1)
child_label.place(x=50,y=170)
child_combobox=StringVar()
child_combobox = Combobox(root,textvariable=child_combobox,values=numberofchilderen,state="readonly")
child_combobox.place(x=50,y=200)

room_label = Label(root, text="Number of Rooms:",bg="dark orchid",fg="white",width=30,height=1)
room_label.place(x=50,y=230)
room_combobox=StringVar()
room_combobox =Combobox(root,textvariable=room_combobox,values=("1","2","3","4","5"),state="readonly")
room_combobox.place(x=50,y=260)

result_label=Label(root, text="")
result_label.place(x=50,y=290)

combobox=StringVar()
combobox=Combobox(root,textvariable=combobox,values=("ASC","DSC"),state="readonly")
combobox.place(x=1000,y=115)

sorter_label=Label(root,text="Please select the currency type you want",bg="dark orchid",fg="white",width=30,height=1)
sorter_label.place(x=1000,y=50)

var= StringVar(root)
var.set(None)
tl_radio=Radiobutton(root,text="TL",value="TL",variable=var)
tl_radio.place(x=1000,y=80)
eu_radio=Radiobutton(root,text="Euro",value="Euro",variable=var)
eu_radio.place(x=1050,y=80)

show=Button(text='Show Hotels', command =start,bg="dark orchid",fg="white",width=30,height=1)
show.place(x=1000,y=170)

root.mainloop()