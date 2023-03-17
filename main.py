from tkinter import *
import math


root = Tk()

root.title("Ventilation slider")

v=IntVar()
u=StringVar()
clickedRad = StringVar()
clickedRec = StringVar()

def selection():
   selected = str(v.get())
   return selected

def unitselect():
   u = (clickedRad.get())
   return u
def unitselect1():
   u = (clickedRec.get())
   return u


def cal_sum():
   v= selection()
   unitselect()
   unitselect1()


   flowc=int(flowIn.get())
   if v == "0":
      radc=int(radiusIn.get())
      if unitselect() == "mm":
         ve1=round((flowc * 4)/(3600 * math.pi * (radc / 1000)**2), 3)
         areao = round(float(((radc/1000)**2 * math.pi)/4), 3)
      else:
         ve1=round((flowc * 4)/(3600 * math.pi * (radc / 100)**2), 3)
         areao =round(float(((radc/100)**2 * math.pi)/4), 3)
      ve2 = round(float(ve1 * 3.6), 3)

   elif v=="1":
      widc = int(widthIn.get())
      heigc = int(heightIn.get())
      if unitselect1() == "mm":
         ve1 = round(flowc/(3600 * (widc/1000) * (heigc / 1000)), 3)
         areao = round(float((widc * heigc /1000000 )), 3)
      else:
         ve1 = round(flowc / (3600 * (widc / 100) * (heigc / 100)), 3)
         areao = round(float((widc * heigc / 10000)), 3)
      ve2 = round(float(ve1 * 3.6), 3)

   else:
      areac = str(areaIn.get()).replace(",", ".")
      convert = float(areac)
      ve1 = round(flowc / (3600 * convert), 3)
      ve2 = round(float(ve1 * 3.6), 3)
      areao = areac

   vol = round(flowc / 0.2777777778, 3)
   veloOut.config(text=ve1)
   veloOut1.config(text=ve2)
   volumeOut.config(text=vol)
   areaOut.config(text=areao)


# Create a Frame
frame = LabelFrame(root, text="Ventilator Slider", padx=10, pady=10)
frame.pack(padx=15,pady=15)

# Define labels
data = Label(frame, text="INPUT YOUR DATA")
flow = Label(frame, text="Air flow:")
radius = Label(frame, text="Radius:")
width = Label(frame, text="Duct width:")
height = Label(frame, text="Duct height:")
area = Label(frame, text="Area of duct:")
calcarea = Label(frame, text="Area")
velo = Label(frame, text="Velocity units")
volume = Label(frame, text="Volume units")
calc = Label(frame, text="CALCULATIONS")

# Define unit labels
flow1 = Label(frame, text="[m^3/h]")
area1 = Label(frame, text="[m^2]")
velo1 = Label(frame, text="[m/s]")
velo2 = Label(frame, text="[km/h]")
volume1 = Label(frame, text="[l/s]")
area2 = Label(frame, text="[m^2]")

# Define a input field
flowIn = Entry(frame, width=20, borderwidth=2)
radiusIn = Entry(frame, width=20, borderwidth=2)
widthIn = Entry(frame, width=20, borderwidth=2)
heightIn = Entry(frame, width=20, borderwidth=2)
areaIn = Entry(frame, width=20, borderwidth=2)
areaOut = Label(frame, text="", width=20, borderwidth=2)
veloOut = Label(frame, text="", width=20, borderwidth=2)
veloOut1 = Label(frame, text="", width=20, borderwidth=2)
volumeOut = Label(frame, text="", width=20, borderwidth=2)

# Define a unit dropdowns
options = ["mm", "cm"]
clickedRad.set(options[0])
clickedRec.set(options[0])
unitRadius=OptionMenu(frame, clickedRad,*options)
unitWidth=OptionMenu(frame, clickedRec, *options)
unitHeight=OptionMenu(frame, clickedRec,*options)

# Define a radiobutton
v.set(0)
checkb1 = Radiobutton(frame, text="Round duct",value=0, variable=v,command=selection)
checkb2 = Radiobutton(frame, text="Rectangular duct",value=1, variable=v,command=selection)
checkb3 = Radiobutton(frame, text="Calculated area",value=2, variable=v, command=selection)


# Create button
button = Button(frame, text="Calculate!", padx=40, pady=1, command=cal_sum)


# Position elements
data.grid(row=0, column=0, columnspan=2)
flow.grid(row=1, column=0)
flowIn.grid(row=1, column=1)
flow1.grid(row=1, column=2)
checkb1.grid(row=2, column=0, columnspan=1)
radius.grid(row=3, column=0)
radiusIn.grid(row=3, column=1)
unitRadius.grid(row=3, column=2)
checkb2.grid(row=4, column=0, columnspan=1)
width.grid(row=5, column=0)
widthIn.grid(row=5, column=1)
unitWidth.grid(row=5, column=2)
height.grid(row=6, column=0)
heightIn.grid(row=6, column=1)
unitHeight.grid(row=6, column=2)
checkb3.grid(row=7, column=0, columnspan=1)
area.grid(row=8, column=0)
areaIn.grid(row=8, column=1)
area1.grid(row=8, column=2)
button.grid(row=9, column=0, columnspan=3)
calc.grid(row=10, column=0, columnspan=2)
velo.grid(row=11, column=0)
veloOut.grid(row=11, column=1)
velo1.grid(row=11, column=2)
veloOut1.grid(row=12, column=1)
velo2.grid(row=12, column=2)
volume.grid(row=13, column=0)
volume1.grid(row=13, column=2)
volumeOut.grid(row=13, column=1)
calcarea.grid(row=14, column=0)
areaOut.grid(row=14, column=1)
area2.grid(row=14, column=2)

root.mainloop()
