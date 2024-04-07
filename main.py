import tkinter as tk
import customtkinter as ctk
from scapy.all import *
import socket

import banner_grabber #banner_grabber(target, port)
import nmapscan #scan(target) 
import geoip #get_loc(url, path, file)
import wifiscanner #wifi(ip_add_range_entered)
import packet_sniff #packet(count)

def scanmap():
    window = ctk.CTkToplevel(app)
    window.title("Nmap Scan")
    window.geometry("300x250")
    window.resizable(False, False)

    def domain():
        try:
            ans.insert('end', text="Scanning...\n\n")
            get = ctk.CTkInputDialog(text="Enter a domain: ", title="Nmap Scan")
            target = socket.gethostbyname(get.get_input())
            out = nmapscan.scan(target)
            ans.insert('end', text=out+ "\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid domain.\n\n")

    def ipaddr():
        try:
            ans.insert('end', text="Scanning...\n\n")
            get = ctk.CTkInputDialog(text="Enter an IP: ", title="Nmap Scan")
            target = get.get_input()
            out = nmapscan.scan(target)
            ans.insert('end', text=out + "\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid IP.\n\n")

    dom = ctk.CTkButton(window, text="Enter a domain: ", command=domain)
    dom.place(x=150, y=50, anchor="center")
    ip = ctk.CTkButton(window, text="Enter an IP: ", command=ipaddr)
    ip.place(x=150, y=100, anchor="center")

def get_ban():
    window = ctk.CTkToplevel(app)
    window.title("Banner Grabber")
    window.geometry("300x250")
    window.resizable(False, False)

    def domain():
        try:
            ans.insert('end', text="Grabbing...\n\n")
            get0 = ctk.CTkInputDialog(text="Enter a url: ", title="Banner Grabber")
            url = socket.gethostbyname(get0.get_input())
            get1 = ctk.CTkInputDialog(text="Enter a port: ", title="Banner Grabber")
            port = get1.get_input()
            out = banner_grabber.banner_grabber(url, int(port))
            ans.insert('end', text=out+ "\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid url and port.\n\n")
    
    def ipaddr():
        try:
            ans.insert('end', text="Grabbing...\n\n")
            get0 = ctk.CTkInputDialog(text="Enter an IP: ", title="Banner Grabber")
            ip = get0.get_input()
            get1 = ctk.CTkInputDialog(text="Enter a port: ", title="Banner Grabber")
            port = get1.get_input()
            out = banner_grabber.banner_grabber(ip, int(port))
            ans.insert('end', text=out+ "\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid ip and port.\n\n")

    dom = ctk.CTkButton(window, text="Enter a domain: ", command=domain)
    dom.place(x=150, y=100, anchor="center")
    ip = ctk.CTkButton(window, text="Enter an IP: ", command=ipaddr)
    ip.place(x=150, y=150, anchor="center")

def get_loc():
    window = ctk.CTkToplevel(app)
    window.title("GeoIP")
    window.geometry("300x250")
    window.resizable(False, False)

    def domain():
        try:
            ans.insert('end', text="Locating...\n\n")
            get = ctk.CTkInputDialog(text="Enter a url: ", title="GeoIP")
            url = get.get_input()
            out = geoip.get_loc(url, path.get(), file.get())
            ans.insert('end', text=out+ "\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid url.\n\n")

    pathlabel = ctk.CTkLabel(window, text="Enter a path to save the location: ")
    pathlabel.place(x=150, y=50, anchor="center")
    path = ctk.CTkEntry(window, placeholder_text="Enter a path", width=200)
    path.place(x=150, y=75, anchor="center")

    filelabel = ctk.CTkLabel(window, text="Enter the name of the file:")
    filelabel.place(x=150, y=125, anchor="center")
    file = ctk.CTkEntry(window, placeholder_text="Enter file-name", width=200)
    file.place(x=150, y=150, anchor="center")
    dom = ctk.CTkButton(window, text="GeoIP ", command=domain)
    dom.place(x=150, y=200, anchor="center")
    
def wifiscan():
    window = ctk.CTkToplevel(app)
    window.title("Wifi Scanner")
    window.geometry("300x250")
    window.resizable(False, False)

    def domain():
        try:
            ans.insert('end', text="Scanning...\n\n")
            out = wifiscanner.wifi(range.get())
            ans.insert('end', text=out+"\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid ip range.\n\n")

    iplabel = ctk.CTkLabel(window, text="Enter a ip range: ")
    iplabel.place(x=150, y=50, anchor="center")
    range = ctk.CTkEntry(window, placeholder_text="192.168.155.0/24", width=200)
    range.place(x=150, y=100, anchor="center")
    dom = ctk.CTkButton(window, text="Wifi Scanner", command=domain)
    dom.place(x=150, y=150, anchor="center")

def sniff():
    window = ctk.CTkToplevel(app)
    window.title("Packet Sniffer")
    window.geometry("300x250")
    window.resizable(False, False)

    def domain():
        try:
            ans.insert('end', "Sniffing...\n\n")
            out = packet_sniff.packet(int(count.get()))
            ans.insert('end', text=out+"\n\n")
        except Exception as e:
            ans.insert('end', text="Please enter a valid number.\n\n")

    countlabel = ctk.CTkLabel(window, text="Enter the number of packets to be sniffed: ")
    countlabel.place(x=150, y=50, anchor="center")
    count = ctk.CTkEntry(window, placeholder_text="Enter a number", width=200)
    count.place(x=150, y=100, anchor="center")
    dom = ctk.CTkButton(window, text="Packet Sniffer", command=domain)
    dom.place(x=150, y=150, anchor="center")

def copy():
    global clip
    clip = ans.get(0.0, 'end')

def clear():
    ans.delete(0.0, 'end')

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("Night_Purple.json")

app = ctk.CTk()
app.geometry("720x720")
app.resizable(False, False)

app.title("Network Security Toolkit")

title = ctk.CTkLabel(app, text="Choose an Option: ", font= ("Century Gothic", 20))
title.place(x=350, y=100, anchor="center")

nmaps = ctk.CTkButton(app, text="Nmap Scan", command=scanmap)
nmaps.place(x=350, y=150, anchor="center")

ban = ctk.CTkButton(app, text="Banner Grabber", command=get_ban)
ban.place(x=350, y=200, anchor="center")

loc = ctk.CTkButton(app, text="GeoIP", command=get_loc)
loc.place(x=350, y=250, anchor="center")

wifi = ctk.CTkButton(app, text="Wifi Scanner", command=wifiscan)
wifi.place(x=350, y=300, anchor="center")

pack = ctk.CTkButton(app, text="Packet Sniffer", command=sniff)
pack.place(x=350, y=350, anchor="center")

output = ctk.CTkLabel(app, text="Output: ", font= ("Century Gothic", 15))
output.place(x=350, y=400, anchor="center")

ans = ctk.CTkTextbox(app, width=500, height=200,)
ans.place(x=350, y=475, anchor="center")

copy_button = ctk.CTkButton(app, text="Copy", command=copy)
copy_button.place(x=275, y=600, anchor="center")

clear_out = ctk.CTkButton(app, text="Clear", command=clear)
clear_out.place(x=425, y=600, anchor="center")

quit = ctk.CTkButton(app, text="Quit", command=app.quit)
quit.place(x=350, y=650, anchor="center")

app.mainloop()