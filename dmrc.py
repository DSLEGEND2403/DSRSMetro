from tkinter import *
from tkinter.tix import StdButtonBox
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from collections import defaultdict
from tkinter import messagebox
import pickle
import sys

tk= Tk() 
tk.title("                                                                                                                                                                                                       DMRC METRO दिल्ली मेट्रो रेल")
tk.iconbitmap("E:/document/NewCode/DMRC/metro.ico")
'''stations_v= [
    "Kashmere Gate",
    "Lal Quila",
    "Jama Masjid",
    "Delhi Gate",
    "ITO",
    "Mandi House",
    "Janpath",
    "Central Secretariat",
    "Khan Market",
    "Jawarhar Lal Nehru Stadium",
    "Jangpura",
    "Lajpat Nagar",
    "Moolchand",
    "Kailash Colony",
    "Nehru Place",
    "Kalkaji Mandir",
    "Govind Puri",
    "Harkesh Nagar Okhla",
    "Jasola-Apollo",
    "Sarita Vihar",
    "Mohan Estate",
    "Tughlakabad Station",
    "Badarpur Border",
    "Sarai",
    "NHPC Chowk",
    "Mewala Maharajpur",
    "Sector-28 Faridabad",
    "Neelam Chowk Ajronda",
    "Bata Chowk",
    "Escorts Mujesar",
    "Sant Surdas Sihi",
    "Raja Nahar Singh"
]
stations_b= [
    "Dwarka Sector-21",
    "Dwarka Sector-8",
    "Dwarka Sector-9",
    "Dwarka Sector-10",
    "Dwarka Sector-11",
    "Dwarka Sector-12",
    "Dwarka Sector-13",
    "Dwarka Sector-14",
    "Dwarka Metro Station",
    "Dwarka Mor",
    "Nawada",
    "Uttam Nagar West",
    "Uttam Nagar East",
    "Janak Puri West",
    "Janak Puri East",
    "Tilak Nagar",
    "Subash Nagar",
    "Tagore Garden",
    "Rajouri Garden",
    "Ramesh Nagar",
    "Moti Nagar",
    "Kirti Nagar",
    "Shadipur",
    "Patel Nagar",
    "Rajendra Place",
    "Karol Bagh",
    "Jhandewalan",
    "RK Ashram Marg",
    "Rajiv Chowk",
    "Barkhamba",
    "Mandi House",
    "Pragati Maidan",
    "Indraprastha",
    "Yamuna Bank",
    "Akshardham",
    "Mayur Vihar-I",
    "Mayur Vihar Ext.",
    "New Ashok Nagar",
    "Noida Sector-15",
    "Noida Sector-16",
    "Noida Sector-18",
    "Botanical Garden",
    "Golf Course",
    "Noida City Centre",
    "Noida Sector-34",
    "Noida Sector-52",
    "Noida Sector-61",
    "Noida Sector-59",
    "Noida Sector-62",
    "Noida Electronic City",
    "Laxmi Nagar",
    "Nirman Vihar",
    "Karkarduma",
    "Anand Vihar",
    "Kaushambi",
    "Vaishali"
]
stations_g=[
    "Inderlok Metro Station",
    "Ashok Park Main Metro Station",
    "Satguru Ram Singh Marg",
    "Kirti Nagar Metro Station",
    "Punjabi Bagh Metro Station",
    "Shivaji Park Metro Station",
    "Madipur Metro Station",
    "Paschim Vihar East Metro Station",
    "Paschim Vihar West Metro Station",
    "Peera Gandhi Metro Station",
    "Udyog Nagar Metro Station",
    "Maharaja Surajmal Stadium Metro Station",
    "Nangloi Metro Station",
    "Rajdhani Park Metro Station",
    "Mundka Metro Station",
    "Mundka Industrial area Metro Station",
    "Ghevra Metro Station",
    "Tikri Kalan Metro",
    "Tikri Border Metro Station",
    "Pandit Shree Ram Sharma Metro Station",
    "Bahadurgarh City Metro Station",
    "Brigadier Hoshiyar Singh Metro Station"
]
stations_m= [
    "Botanical Garden",
    "Okhla Bird Sanctuary",
    "Kalindi Kunj",
    "Jasola Vihar Shaheen Bagh",
    "Okhla Vihar",
    "Jamia Millia Islamia",
    "Sukhdev Vihar",
    "NSIC Okhla",
    "Kalkaji Mandir",
    "Nehru Enclave",
    "Greater Kailash",
    "Chirag Delhi",
    "Panchsheel Park",
    "Hauz Khas",
    "I.I.T",
    "R.K.Puram",
    "Munirka",
    "Vasant Vihar",
    "Shankar Vihar",
    "Terminal 1- IGI Airport",
    "Sadar Bazar Contonment",
    "Palam",
    "Dashrath Puri",
    "Dabri Mor",
    "Janakpuri, South",
    "Janak Puri West"
]
stations_r= [
    "Shahid Nagar Metro Station",
    "Dilshad Garden Metro Station",
    "Jhilmil Metro station",
    "Mansrover Park Metro Station",
    "Shahdara Metro Station",
    "Welcome Metro Station",
    "Seelam pur Metro Station",
    "Shastri Park Metro Station",
    "Kashmere Gate",
    "Tis Hazari Metro Station",
    "Pul Bangash Metro Station",
    "Pratap Nagar Metro Station",
    "Shastri Nagar Metro Station",
    "Inderlok",
    "Kanhaiya nagar",
    "Keshav Puram",
    "Netaji Subash Place",
    "Kohat Enclave",
    "Pitampura",
    "Rohini East",
    "Rohini West",
    "Rithala"
]
stations_p= [
    "Majlis Park",
    "Azadpur",
    "Shalimar Bagh",
    "Netaji Subash Place",
    "Shakurpur",
    "Punjabi Bagh West",
    "ESI Hospital",
    "Rajouri Garden",
    "Mayapuri",
    "Naraina Vihar",
    "Delhi Cantonment",
    "Durgabai Deshmukh South Campus",
    "Sir Vishweshwaraiah Moti Bagh",
    "Bhikaji Cama Place",
    "Sarojini Nagar",
    "INA",
    "South Extension",
    "Lajpat Nagar",
    "Vinobapuri",
    "Ashram",
    "Hazrat Nizamuddin",
    "Mayur Vihar-I",
    "Mayur Vihar Pocket 1",
    "Trilokpuri Sanjay Lake",
    "East Vinod Nagar - Mayur Vihar-II",
    "Mandawali - West Vinod Nagar",
    "IP Extension",
    "Anand Vihar",
    "Karkarduma","Karkarduma Court",
    "Krishna Nagar",
    "East Azad Nagar",
    "Welcome",
    "Jafrabad",
    "Maujpur - Babarpur",
    "Gokulpuri",
    "Johri Enclave",
    "Shiv Vihar"
]
stations_o= [
    "New Delhi",
    "Shivaji Station",
    "Dhaula Kuan",
    "Delhi Aerocity",
    "Airport",
    "Dwarka Sector 21"
]
stations_y= [
    "Samaypur Badli"
    "Rohini Sector 18, 19",
    "Haiderpur Badli Mor",
    "Jahangirpuri",
    "Adarsh Nagar",
    "Azadpur",
    "Model Town",
    "GTB Nagar",
    "Viswavidyalaya",
    "Vidhan Sabha",
    "Civil Lines",
    "Kashmere Gate",
    "Chandhni Chowk",
    "Chawri Bazar",
    "New Delhi",
    "Rajiv Chowk",
    "Patel Chowk",
    "Central Secretariat",
    "Udyog Bhawan",
    "Lok Kalyan Marg",
    "Jorbagh",
    "INA",
    "AIIMS",
    "Green Park",
    "Hauz Khas",
    "MalviaNagar",
    "Saket",
    "Qutab Minar",
    "Chhattarpur",
    "Sultanpur",
    "Ghotorni",
    "Arjan Garh",
    "Gurudronacharya",
    "Sikandarpur",
    "MG Road",
    "IFFCO Chowk",
    "Huda City Centre",
]
'''

def search():
    e1_= e1.get()
    if e1_ == "":
        messagebox.showerror("DMRC METRO", "Error 404, Input Not Found")
    elif e1.get() == "Violet":
        def costv():
            if e3s.get() == "Central Secretariat":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Sant Surdas Sihi":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e3s.get() == "Escorts Mujesar":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e3s.get() == "Bata Chowk":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Neelam Chowk Ajronda":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Sector-28 Faridabad":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Mewala Maharajpur":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "NHPC Chowk":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()    
            elif e3s.get() == "Sarai":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Badarpur Border":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Tughlakabad Station":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Mohan Estate":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Sarita Vihar":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Jasola-Apollo":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Harkesh Nagar Okhla":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Govind Puri":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Kalkaji Mandir":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Nehru Place":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Kailash Colony":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Moolchand":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Lajpat Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Jangpura":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Jawarharlal Nehru Stadium":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e3s.get() == "Khan Market":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Central Secratariat":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Janpath":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Mandi House":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "ITO":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Delhi Gate":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Jama Masjid":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Lal Quila":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e3s.get() == "Kashmere Gate":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            else:
                messagebox.showerror("DMRC METRO", "Problem!!!!")
        l3s= Label(linebook, text= "Starting from Raja Nahar Singh")
        l3s.pack()
        e3s= Entry(linebook)
        e3s.pack()
        b2= ttk.Button(linebook, text= "Fare", command= costv)
        b2.pack()
    elif e1.get() == "Red":
        def costr():
            if e4s.get() == "Rohini West":
                l3f= Label(linebook, text= "₹10")
                l3f.pack()
            elif e4s.get() == "Rohini East":
                l3f= Label(linebook, text= "₹20")
                l3f.pack()
            elif e4s.get() == "Pitampura":
                l3f= Label(linebook, text= "₹20")
                l3f.pack()
            elif e4s.get() == "Kohat Enclave":
                l3f= Label(linebook, text= "₹20")
                l3f.pack()
            elif e4s.get() == "Netaji Subash Place":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()
            elif e4s.get() == "Keshav Puram":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()
            elif e4s.get() == "Kanhaiya Nagar":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()    
            elif e4s.get() == "Inderlok":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()
            elif e4s.get() == "Shastri Nagar":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()
            elif e4s.get() == "Pratap Nagar":
                l3f= Label(linebook, text= "₹30")
                l3f.pack()
            elif e4s.get() == "Pul Bangash":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Kashmere Gate":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Shastri Park":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Seelam Pur":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Welcome":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Shahdara":
                l3f= Label(linebook, text= "₹40")
                l3f.pack()
            elif e4s.get() == "Mansrover park":
                l3f= Label(linebook, text= "₹50")
                l3f.pack()
            elif e4s.get() == "Jhilmil":
                l3f= Label(linebook, text= "₹50")
                l3f.pack()
            elif e4s.get() == "Dilshad Garden":
                l3f= Label(linebook, text= "₹50")
                l3f.pack()
            elif e4s.get() == "Shahid Nagar":
                l3f= Label(linebook, text= "₹50")
                l3f.pack()
            else:
                messagebox.showerror("DMRC METRO", "Problem!!!!")
        l4s= Label(linebook, text= "Rithala Metro Station")
        l4s.pack()
        e4s= Entry(linebook)
        e4s.pack()
        b3= ttk.Button(linebook, text= "Fare", command= costr)
        b3.pack()
    elif e1.get() == "Orange":
        def costo():
            if e5s.get() == "Shivaji Stadium":
                l4f= Label(linebook, text= "₹20")
                l4f.pack()
            elif e5s.get() == "Delhi Aerocity":
                l4f= Label(linebook, text= "₹40")
                l4f.pack()
            elif e5s.get() == "Dhaula Kuan":
                l4f= Label(linebook, text= "₹50")
                l4f.pack()
            elif e5s.get() == "IGI Airport":
                l4f= Label(linebook, text= "₹60")
                l4f.pack()
            elif e5s.get() == "Dwarka Sector 21":
                l4f= Label(linebook, text= "60")
                l4f.pack()
            else:
                messagebox.showerror("DMRC METRO", "Problem!")
        l5s= Label(linebook, text= "New Delhi")
        l5s.pack()
        e5s= Entry(linebook)
        e5s.pack()
        b4= ttk.Button(linebook, text= "Fare", command= costo)
        b4.pack()
    elif e1.get() == "Pink":
    
        def costp():
            if e6s.get() == "Azadpur":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e6s.get() == "Shalimar Bagh":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e6s.get() == "Netaji Subhash Place":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e6s.get() == "Shakurpur":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "Punjabi Bagh West":
                l2f= Label(linebook, text= "₹30")

            elif e6s.get() == "ESI Hospital":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e6s.get() == "Rajouri Garden":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Mayapuri":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Naraina Vihar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Delhi Cantonment":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Durgabai Deshmukh South Campus":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Sir Vishweshwaraiah Moti Bagh":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Bhikaji Cama Place":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Sarojini Nagar":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "INA":
                l2f= Label(linebook, text= "40")
                l2f.pack()
            elif e3s.get() == "South Extensions":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Lajpat Nagar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Vinobapuri":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e3s.get() == "Ashram":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e3s.get() == "Sarai Kale Khan-Nizamuddin":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "Mayur Vihar - I":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()         
            elif e6s.get() == "Mayur Vihar Pocket I":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "Trilokpuri-Sanjay Lake":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "East Vinod Nagar-Mayur Vihar-II":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "Mandawali-West Vinod Nagar":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "IP Extension":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Anand Vihar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Karkarduma":
                l2f= Label(linebook, text= "₹50")
            elif e6s.get() == "Munirka":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Karkarduma Court":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Krishna Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "East Azad Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Welcome":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Jaffrabad":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Maujpur-Babarpur":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Gokulpuri":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e6s.get() == "Johri Enclave":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e6s.get() == "Shiv Vihar":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
        l6s= Label(linebook, text= "Starting from Majlis Park")
        l6s.pack()
        e6s= Entry(linebook)
        e6s.pack()
        b5= ttk.Button(linebook, text= "Fare", command= costp)
        b5.pack()

    elif e1.get() == "Green":
        def costg():
            if e7s.get() == "Ashok Park Main":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e7s.get() == " Punjabi Bagh":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e7s.get() == "Shivaji Park":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e7s.get() == "Madipur":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e7s.get() == "Paschim Vihar East":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e7s.get() == "Paschim Vihar West":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == "Peera Garhi":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == " Udyog Nagar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == "Surajmal Stadium":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == "Nangloi":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == "Nangloi Railway Station":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e7s.get() == "Rajdhani Park":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Mundka":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Mundka Industrial Area":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Ghevra":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Tikri Kalan":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Tikri Border":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Pandit Shree Ram Sharma":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e7s.get() == "Bahadurgarh City":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e7s.get() == " Brigadier Hoshiyar Singh":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
        l7s= Label(linebook, text= "Starting from Ashok Park Main")
        l7s.pack()
        e7s= Entry(linebook)
        e7s.pack()
        b6= ttk.Button(linebook, text= "Fare", command= costg)
        b6.pack()
    elif e1.get() == "Blue":
        def costb():
            if e8s.get() == "Botanical Garden":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e8s.get() == "Noida Sector 18":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e8s.get() == "Noida Sector 16":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e8s.get() == "Noida Sector 15":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e8s.get() == "New Ashok Nagar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e8s.get() == "Mayur Vihar Extension":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e8s.get() == "Mayur Vihar - I":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e8s.get() == "Akshardham":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e8s.get() == "Yamuna Bank":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e8s.get() == "Indraprastha":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Pragati Maidan":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Mandi House":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Barakhambha Road":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Rajiv Chowk":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Ramakrishna Ashram Marg":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Jhandewalan":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Karol Bagh":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e8s.get() == "Rajendra Place":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Patel Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Shadipur":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Kirti Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Moti Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Ramesh Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Rajouri Garden":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Tagore Garden":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Subhash Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Tilak Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Janakpuri East":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Janakpuri West":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e8s.get() == "Uttam Nagar East":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Uttam Nagar West":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Nawada":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Morh":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 14":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 13":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 12":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 11":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 10":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 9":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 8":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e8s.get() == "Dwarka Sector 21":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
        l8s= Label(linebook, text= "Starting from Noida Golf Course")
        l8s.pack()
        e8s= Entry(linebook)
        e8s.pack()
        b7= ttk.Button(linebook, text= "Fare", command= costb)
        b7.pack()
    elif e1.get() == "Yellow":
        def costy():
            if e9s.get() == "Rohini Sector 18, 19":
                l2f= Label(linebook, text= "₹10")
                l2f.pack()
            elif e9s.get() == "Haiderpur Badli-Mor":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e9s.get() == "Jahangirpuri":
                l2f= Label(linebook, text= "₹20")
                l2f.pack()
            elif e9s.get() == "Adarash Nagar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e9s.get() == "Model Town":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e9s.get() == "G.T.B Nagar":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e9s.get() == "Vishwavidyalaya":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e9s.get() == "Vidhan Sabha":
                l2f= Label(linebook, text= "₹30")
                l2f.pack()
            elif e9s.get() == "Civil Lines":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Kashmere Gate":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Chandni Chowk":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Chawri Bazar":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "New Delhi":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Rajiv Chowk":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Patel Chowk":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Udyog Bhawan":
                l2f= Label(linebook, text= "₹40")
                l2f.pack()
            elif e9s.get() == "Lok Kalyan Marg":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Jor Bagh":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "INA":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "AIIMS":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Green Park":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Hauz Khas":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Malviya Nagar":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Saket":
                l2f= Label(linebook, text= "₹50")
                l2f.pack()
            elif e9s.get() == "Qutub Minar":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Chattarpur":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Sultanpur":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Ghitorni":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Arjangarh":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Guru Dronacharya":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "Sikanderpur":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "M.G Road":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "IFFCO Chowk":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
            elif e9s.get() == "HUDA City Centre":
                l2f= Label(linebook, text= "₹60")
                l2f.pack()
        l8s= Label(linebook, text= "Starting from Samaypur Badli")
        l8s.pack()
        e9s= Entry(linebook)
        e9s.pack()
        b7= ttk.Button(linebook, text= "Fare", command= costy)
        b7.pack()
        l4= Label(linebook, text= "Important Information: \n Passengers desirous to travel in the Rapid Metro Gurugram are requested to get down in Sikanderpur Station.")
        l4.pack()
    
def nsmrs():
    if e2.get() == "C.R Park":
        l2.config(text= "Govind Puri in Violet Line or Kalkaji Mandir in Violet Line or in Magenta Line")
    elif e2.get() == "Lotus Temple":
        l2.config(text= "Kalkaji Mandir in Violet Line or in Magenta Line")
    elif e2.get() == "India Gate":
        l2.config(text= "Central Secretariat in Violet Line or in Yellow Line")
    elif e2.get() == "Surajkund Mela":
        l2.config(text= "Badarpur Border in Violet Line")
    elif e2.get() == "SelectCity Walk":
        l2.config(text= "Malviya Nagar in Yellow Line")
    elif e2.get() ==  "Delhi Airport T3":
        l2.config(text= "IGI Airport in Orange line")
    elif e2.get() ==  "Delhi Airport T2":
        l2.config(text= "IGI Airport in Orange line")
    elif e2.get() == "Delhi Airport T1":
        l2.config(text= "Terminal 1 IGI Airport in Magenta Line")
    elif e2.get() ==  "Tughlakabad Station":
        l2.config(text= "Tughlakabad Metro Station in Violet Line")
    elif e2.get() == "Hazrat Nizamuddin Station":
        l2.config(text= "Hazrat Nizamuddin Station in Pink Line")
    elif e2.get() == "Qutub Minar":
        l2.config(text= "Hauz Khas in Magenta and Yellow Line")
    elif e2.get() == "Jantar Mantar":
        l2.config(text= "Janpath Metro Station in Violet Line")
    elif e2.get() == "Lodhi Garden":
        l2.config(text= "Jor Bagh in Yellow Line")
    else:
        messagebox.showerror("DMRC METRO", "Error 404")
note= ttk.Notebook(tk)
note.grid(row= 0, column= 1)
##################################################
home= Frame(note, height= 500, width = 500)
home.pack(fill= "both", expand= 1)
note.add(home, text= "Home")
l1= Label(home, text= "Hello User, Where are you going today? \n If you plan to stay at home you can close the app", font= ("Athletic Outfit", 20))
l1.pack(padx= 10, pady= 250)
##################################################
redbook= Frame(note, height= 500, width= 500)
redbook.pack(fill= "both", expand= 1)
note.add(redbook, text= "Red line")
    
violetbook= Frame(note, height= 500, width= 500)
violetbook.pack(fill= "both", expand= 1)
note.add(violetbook, text= "Violet Line")

bluebook= Frame(note, height= 500, width= 500)
bluebook.pack(fill= "both", expand= 1)
note.add(bluebook, text= "Blue Line")

greenbook= Frame(note, height= 500, width= 500)
greenbook.pack(fill= "both", expand= 1)
note.add(greenbook, text= "Green Line")

magbook= Frame(note, height= 500, width= 500)
magbook.pack(fill= "both", expand= 1)
note.add(magbook, text= "Magenta Line")

pinkbook= Frame(note, height= 500, width= 500)
pinkbook.pack(fill= "both", expand= 1)
note.add(pinkbook, text= "Pink Line")

orangebook= Frame(note, height= 500, width= 500)
orangebook.pack(fill= "both", expand= 1)
note.add(orangebook, text= "Orange Line")

yellowbook= Frame(note, height= 500, width= 500)
yellowbook.pack(fill= "both", expand= 1)
note.add(yellowbook, text= "Yellow Line")

dmrc= Frame(note, height= 500, width= 500)
dmrc.pack(fill= "both", expand= 1)
note.add(dmrc, text= "DMRC Network")

nsmr= Frame(note, height= 500, width= 500)
nsmr.pack(fill= "both", expand= 1)
note.add(nsmr, text= "Nearest Station")
e2= Entry(nsmr)
e2.pack()
b2= ttk.Button(nsmr, text= "Search Nearest Metro Station", command = nsmrs)
b2.pack()
l2= Label(nsmr, text= "")
l2.pack()
l3= Label(nsmr, text= "Important Information: \n The Shankar Vihar metro station on Magenta Line falls within a defence/cantonment area, \nall passengers desirous to get down at this station must possess the requisite permission or identification documents necessary for entering defence/cantonment areas.")
l3.pack()
##############################################################
sbptd= Frame(note, height= 500, width= 500)
sbptd.pack(fill= "both", expand= 1)
note.add(sbptd, text= "Stations Between Pick-Up Point to Destination")
class Graph(object):
    def __init__(self):
        f=open("C:/Users/Administrator1/Downloads/Delhi-Metro-Path-Finder-master/Delhi-Metro-Path-Finder-master/station_map","rb")
        self.a=pickle.load(f)
        self.b=pickle.load(f)
        self.graph =self.a
        self.station=[]
        self.distance=0
    def BFS(self,s,f):
        visited = [False] * (len(self.graph))
        queue=[]
        dist=[None]*(len(self.graph))
        pred=[None]*(len(self.graph))
        queue.append(s)
        visited[s]=True
        dist[s]=0
        s1=s
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    dist[i]=dist[s]+1
                    pred[i]=s
                    if i==f:
                        p=pred[i]
                        self.distance=dist[i]
                        self.station.append(self.b[f])
                        while p!=s1:
                            self.station.append(self.b[p])
                            p=pred[p]
                        else:
                            self.station.append(self.b[s1])

                        break
















leftside = LabelFrame(sbptd , bd = 0)
leftside.place(x = 100 , y = 200, height=200, width = 300)

start=Label(leftside,text="SOURCE",font=("Arial",18),fg="black")
start.pack(side = TOP,padx=10,pady=30)
dest=Label(leftside,text="DESTINATION",font=("Arial",18),fg="black")
dest.pack(side = TOP,padx=10,pady=27)

centerside = LabelFrame(sbptd , bd = 0)
centerside.place(x = 380 , y = 200, height=200, width = 300)
value1 = StringVar()
combo1 = ttk.Combobox(centerside,width=25,font=("Arial",16),height=10,textvariable=value1,state='readonly',justify = 'center')
combo1['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo1.current(0)
combo1.pack(side=TOP,pady=30)

value2 = StringVar()
combo2 = ttk.Combobox(centerside,width=25,font=("Arial",16),height=10,textvariable=value2,state='readonly',justify = 'center')

combo2['values']=['Select Station','AIIMS Yellow Line', 'ANVT Pink Line', 'Adarsh Nagar Yellow Line', 'Arjan Garh Yellow Line', 'Arthala Red Line', 'Ashram Pink Line', 'Azadpur', 'Badarpur Violet Line', 'Badkal Mor Violet Line', 'Bata Chownk Violet Line', 'Bhikaji Cama Place Pink Line', 'Central Secretariat', 'Chandhni Chowk Yellow Line', 'Chawri Bazar Yellow Line', 'Chhattarpur Yellow Line', 'Civil Lines Yellow Line', 'Delhi Cantt Pink Line', 'Delhi Gate Violet Line', 'Dilshad Garden Red Line', 'Durgabai Deshmukh South Campus Pink Line', 'ESI Hospital Pink Line', 'East Azad Nagar Pink Line', 'Escorts Mujesar Violet Line', 'Faridabad Old Violet Line', 'GTB Nagar Yellow Line', 'Ghotorni Yellow Line', 'Gokulpuri Pink Line', 'Govindpuri Violet Line', 'Green Park Yellow Line', 'Gurudronacharya Yellow Line', 'Haiderpur Badli Mor Yellow Line', 'Hauz Khas Yellow Line', 'Hazrat Nizamuddin Pink Line', 'Hindon Red Line', 'Huda City Centre Yellow Line', 'IFFCO Chowk Yellow Line', 'INA', 'IP Extension Pink Line', 'ITO Violet Line', 'Inder Lok Red Line', 'JLN Violet Line', 'Jaffrabad Pink Line', 'Jahangirpuri Yellow Line', 'Jama Masjid Violet Line', 'Jangpura Violet Line', 'Janpath Violet Line', 'Jasola-Apollo Violet Line', 'Jhil Mil Red Line', 'Johri Enclave Pink Line', 'Jorbagh Yellow Line', 'Kailash Colony Violet Line', 'Kalkaji Mandir Violet Line', 'Kanhaiya Nagar Red Line', 'Karkarduma Court Pink Line', 'Karkarduma Pink Line', 'Kashmere Gate', 'Keshav Puram Red Line', 'Khan Market Violet Line', 'Kohat Enclave Red Line', 'Krishna Nagar Pink Line', 'Lajpat Nagar', 'Lal Quila Violet Line', 'Lok Kalyan Marg Yellow Line', 'MG Road Yellow Line', 'Majlis Park Pink Line', 'Major Mohit Sharma Red Line', 'Malvia Nagar Yellow Line', 'Mandawali - West Vinod Nagar Pink Line', 'Mandi House Violet Line', 'Mansarovar Park Red Line', 'Maujpur Pink Line', 'Maya Puri Pink Line', 'Mayur Vihar 1 Pink Line', 'Mayur Vihar Pocket 1 Pink Line', 'Mewla Maharajpur Violet Line', 'Model Town Yellow Line', 'Mohan Estate Violet Line', 'Mohan Nagar Red Line', 'Moolchand Violet Line', 'NHPC Chownk Violet Line', 'Naraina Vihar Pink Line', 'Neelam Chownk Ajronda Violet Line', 'Nehru Place Violet Line', 'Netaji Subhash Place', 'New Delhi Yellow Line', 'Okhla Violet Line', 'Patel Chowk Yellow Line', 'Pitam Pura Red Line', 'Pratap Nagar Red Line', 'Pul Bangash Red Line', 'Punjabi Bagh West Pink Line', 'Qutab Minar Yellow Line', 'Raj Bagh Red Line', 'Raja Nahar singh marg Violet Line', 'Rajiv Chowk Yellow Line', 'Rajouri Garden Pink Line', 'Rithala Red Line', 'Rohini East Red Line', 'Rohini Sector 18, 19 Yellow Line', 'Rohini West Red Line', 'Saket Yellow Line', 'Samaypur Badli Yellow Line', 'Sant Surdas Violet Line', 'Sarai Violet Line', 'Sarita Vihar Violet Line', 'Sarojini Nagar Pink Line', 'Sector 28 Violet Line', 'Seelampur Red Line', 'Shahdara Red Line', 'Shaheed Nagar Red Line', 'Shaheed Sthal(New Bus Adda) Red Line', 'Shakurpur Pink Line', 'Shalimar Bagh Pink Line', 'Shastri Nagar Red Line', 'Shastri Park Red Line', 'Shiv Vihar Pink Line', 'Shyam park Red Line', 'Sikandarpur. Yellow Line', 'Sir Vishweshwaraiah Moti Bagh Pink Line', 'South Extension Pink Line', 'Sultanpur Yellow Line', 'Tis Hazari Red Line', 'Trilokpuri Sanjay Lake Pink Line', 'Tuglakabad Violet Line', 'Udyog Bhawan Yellow Line', 'Vidhan Sabha Yellow Line', 'Vinobapuri Pink Line', 'Vinod Nagar East Pink Line', 'Viswavidyalaya Yellow Line', 'Welcome']
combo2.current(0)
combo2.pack(side=TOP,pady=30)


def print_route(arr_sta,dis):
    global rightside
    rightside = LabelFrame(sbptd ,bg="yellow",bd=0)
    rightside.place(x = 900 , y = 150, height=600, width = 400)
    scrollbar = Scrollbar(rightside)
    scrollbar.pack( side = RIGHT, fill = Y )
    scrollbar2 = Scrollbar(rightside,orient="horizontal")
    scrollbar2.pack(fill=X,side=BOTTOM)
    listbox = Listbox(rightside,bd=2,fg="black",font=("Arial",14,"bold"),yscrollcommand = scrollbar.set,xscrollcommand = scrollbar2.set)
    scrollbar.config(command=listbox.yview)
    scrollbar2.config(command=listbox.xview)
    listbox.insert(END, "              STATIONS TO CROSS : "+str(dis))
    listbox.selection_clear(0, 'end')
    for i in range(len(arr_sta)-1,-1,-1):
        listbox.insert(END, "   ")
        listbox.insert(END, "   "+str(len(arr_sta)-i)+"."+" "+arr_sta[i])
    


    listbox.pack(fill=BOTH,expand=TRUE)



def find_route(s,d):
    g=Graph()
    dict_station=g.b
    try:
        for i in range(len(dict_station)):
            if dict_station[i]==s:
                s_index=i
            elif dict_station[i]==d:
                d_index=i
            else:
                continue
        g.BFS(s_index,d_index)
        print_route(g.station,g.distance)
    except:
        messagebox.showinfo("Select Station", "Enter Valid Station" , icon = "warning")

def click_me():
    try:
       rightside.destroy()
    except:
        a=5
    source=value1.get()
    destination=value2.get()
    find_route(source,destination)


click_button=Button(sbptd,text="Find Route",width=20,font=("Arial",14),command=click_me)
click_button.pack(padx=10, pady= 500)





###############################################################
def redirect():
    webbrowser.open("http://www.delhimetrorail.com/")
linebook= Frame(note, height= 500, width= 500)
linebook.pack(fill= "both", expand= 1)
e1= Entry(linebook)
e1.pack()
b1= ttk.Button(linebook, text= "Search", command= search)
b1.pack()
b2= ttk.Button(linebook, text= "Open DMRC Official Site", command= redirect)
b2.pack()
note.add(linebook, text= "Ticket Fare")



    



imar= Image.open("E:/document/NewCode/DMRC/red.png")
imav= Image.open("E:/document/NewCode/DMRC/violet.png")
imavr= imav.resize((1356, 750), Image.ANTIALIAS)
imab= Image.open("E:/document/NewCode/DMRC/blue.png")
imabr= imab.resize((1356, 800), Image.ANTIALIAS)
imag= Image.open("E:/document/NewCode/DMRC/green.png")
imagr= imag.resize((1356, 750), Image.ANTIALIAS)
imam= Image.open("E:/document/NewCode/DMRC/magenta.png")
imamr= imam.resize((1356, 750), Image.ANTIALIAS)
imap= Image.open("E:/document/NewCode/DMRC/pink.png")
imapr= imap.resize((1356, 750), Image.ANTIALIAS)
imao= Image.open("E:/document/NewCode/DMRC/orange.png")
imay= Image.open("E:/document/NewCode/DMRC/yellow.png")
imayr= imay.resize((1356, 720), Image.ANTIALIAS)
imadmrc= Image.open("E:/document/NewCode/DMRC/dmrc.png")
imadmrc= imadmrc.resize((1356, 720), Image.ANTIALIAS)

rpr= ImageTk.PhotoImage(imar)
rpv= ImageTk.PhotoImage(imavr)
rpb= ImageTk.PhotoImage(imabr)
rpg= ImageTk.PhotoImage(imagr)
rpm= ImageTk.PhotoImage(imamr)
rpp= ImageTk.PhotoImage(imapr)
rpo= ImageTk.PhotoImage(imao)
rpy= ImageTk.PhotoImage(imayr)
rpdmrc= ImageTk.PhotoImage(imadmrc)

ri= Label(redbook, image= rpr)
ri.grid(row= 1, column= 1)

vi= Label(violetbook, image= rpv)
vi.grid(row= 1, column= 1)

bi= Label(bluebook, image= rpb)
bi.grid(row= 1, column= 1)

gi= Label(greenbook, image= rpg)
gi.grid(row= 1, column= 1)

mi= Label(magbook, image= rpm)
mi.grid(row= 1, column= 1)

pi= Label(pinkbook, image= rpp)
pi.grid(row= 1, column= 1)

oi= Label(orangebook, image= rpo)
oi.grid(row= 1, column= 1)

yi= Label(yellowbook, image= rpy)
yi.grid(row= 1, column= 1)

dmrci= Label(dmrc, image= rpdmrc)
dmrci.grid(row= 1, column= 1)
tk.mainloop()

