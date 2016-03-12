import urllib2
import re
import string
from Tkinter import *

def Select_Quote(quote_list):
    '''
    selecting quote from the list of quotes
    '''
    for quote in quote_list:
        if quote != "":
            return quote

def FormatDate(date):

    return "{} {},{}".format(date[0][0],date[0][1],date[0][2])

def ColorSchema():

    Titlefg = "red"
    Titlebg = "white"
    horizontalLine = "black"

    return Titlebg,Titlefg,horizontalLine

def Get_Quote():

    root = Tk()
    root.geometry("450x110")
    root.title("Aravind-Today's Quote")

    the_page = ""

    try:
        req = urllib2.Request('http://www.eduro.com/')
        response = urllib2.urlopen(req)
        the_page = response.read()

    except urllib2.URLError:
        DisplayErrorWindow(root)

    else:
        pat1 = re.compile(r'<p>+(.*)</p>+',re.MULTILINE)
        quote_link = re.findall(pat1,str(the_page))

        #getting date
        pat_date = re.compile(r'<span\sclass="wdate">(.*)</span>')
        date = re.findall(pat_date,str(the_page))
        return DisplayAppWindow(root,Select_Quote(quote_link),date)


def DisplayAppWindow(root,tquote,tdate):

    quote = tquote
    date = tdate

    Color = ColorSchema()

    #frame for heading
    head_frame = Frame(root)
    head_frame.pack()

    canvas = Canvas(head_frame,width="450",height="5")


    #this is the heading

    heading_label = Label(head_frame,text="Today's Quote",bg=Color[0],fg=Color[1])
    line = canvas.create_line(0,5,450,5,fill=Color[2])

    heading_label.pack()
    canvas.pack()



    #frame for actuall quote
    body_frame = Frame(root)
    body_frame.pack(side=BOTTOM)

    #the quote
    quote_label = Label(body_frame,text= quote)
    quote_label.pack()

    #the date
    date_label = Label(body_frame,text="Lastest quote updated on :" +" "+date[0])
    date_label.pack()

    root.mainloop()

def DisplayErrorWindow(root):

    #frame for heading
    head_frame = Frame(root)
    head_frame.pack()

    #this is the heading
    heading_label = Label(head_frame,text="Today's Quote")
    heading_label.pack()

    #frame for actuall quote
    body_frame = Frame(root)
    body_frame.pack(side=BOTTOM)

    #the quote
    quote_label = Label(body_frame,text="A wise man always turns on his internet")
    quote_label.pack()

    #the date
    date_label = Label(body_frame,text="Lastest quote updated on :" +" "+"seriously!?")
    date_label.pack()

    root.mainloop()


Get_Quote()