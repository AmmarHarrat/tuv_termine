from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
inputs = tk.Entry(root, width=40)
inputs.pack()
def myClick():
    print("ammar")
    myLabel = tk.Label(root, text=inputs.get())
    myLabel.pack()

treev = ttk.Treeview(root, selectmode='browse')
treev.pack(side='bottom')

verscrlbar = ttk.Scrollbar(root,
                           orient="vertical",
                           command=treev.yview)

# Calling pack method w.r.to verical
# scrollbar
verscrlbar.pack(side='right', fill='x')

# Configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to  the
# respective columns
treev.column("1", width=500, anchor='c')
treev.column("2", width=500, anchor='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text="Salat")
treev.heading("2", text="Time")

def generate_data(stadt):
    for i in treev.get_children():
        treev.delete(i)


    url = f"https://gebetszeiten.zone/{stadt}"
    url = f"https://timesprayer.com/en/prayer-times-in-{stadt}.html"


    req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header('user-agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
    page = urlopen(req)

    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    Children = soup.find('table', {'class': 'ptTable'})
    print(Children)
    tbody = Children.find("tbody")
    print(tbody)

    tr_children = tbody.find_all("tr")
    print(tr_children)
    for child in tr_children:
        time = child.find_all("td")
        time = time[1].get_text()
        salat = child.find('strong').get_text()
        treev.insert("", 'end',
             values=(salat, time))

Button = tk.Button(root, text="Connect", command=lambda:generate_data(inputs.get()))
Button.pack()

heute_datum = datetime.now()

time1 = ''
clock = tk.Label(root, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=tk.BOTH, expand=1)

def tick():
    global time1
    # get the current local time from the PC
    time2 = heute_datum.strftime('%d/%m/%Y %H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(1000, tick)

tick()

image1 = Image.open("mekka.jpg")
image1 = image1.resize((400,500),Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

label1.pack()

root.mainloop()


"""url = "https://gebetszeiten.zone/wuppertal"

req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(req)

html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

Children = soup.find_all('div', {'class': 'prayer-period'})
print(Children)
for child in Children:
    print(child.find("h2").get_text())
    print(child.find("p").getText())

"""

"""if __name__ == "__main__":
    application = App()
    myButton = Button(application.root, text="Click Me!", command=application.myClick())
    myButton.pack()
    application.loop()"""




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
