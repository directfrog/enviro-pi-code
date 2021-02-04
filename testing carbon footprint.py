import tkinter as tk 
import time
import csv

root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=800)
canvas.pack()


q_frame = tk.Frame(root, bg='#80c1ff', bd=5)
q_frame.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.15, anchor='n')

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.6, anchor='n')


def refresh_label(text):
	label = tk.Label(q_frame, bg="#80c1ff", bd=5, font=("Courier", 16))
	label.place(relwidth=1, relheight=1)
	label["text"] = text
	lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
	lower_frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.6, anchor='n')

	return label, lower_frame


##################### FIRST QUESTION ALL BRANCHES #####################
	
file = open('data.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["co2 emmisions from car per week (kg)"])

def car_q_total(refuel, fuel):
	if fuel > 1:
		e = refuel*fuel
		writer.writerow([e])
	else:
		writer.writerow(["electric car"])

def car_branch_1(root):
	def type_of_gas(refuel, root):
		label, lower_frame = refresh_label("What type of gas do you usually get? ")
		petrol = tk.Button(lower_frame, text="petrol", font=40, command=lambda: car_q_total(refuel, 2.31))
		petrol.place(relx=0.8, rely=0.1, relheight=0.8, relwidth=0.2)
		diesel = tk.Button(lower_frame, text="diesel", font=40, command=lambda: car_q_total(refuel, 2.68))
		diesel.place(relx=0.4, rely=0.1, relheight=0.8, relwidth=0.2)
		other = tk.Button(lower_frame, text="other", font=40, command=lambda: car_q_total(refuel, 2))
		other.place(relx=0.0, rely=0.1, relheight=0.8, relwidth=0.2)

	def car_branch_3(root):
		label, lower_frame = refresh_label("on average how many times you refuel your car per week")
		a = tk.Button(lower_frame, text="3", font=40, command=lambda: type_of_gas(3, root))
		a.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.2)
		b = tk.Button(lower_frame, text="2", font=40, command=lambda: type_of_gas(2, root))
		b.place(relx=0.4, rely=0.1, relheight=0.8, relwidth=0.2)
		c = tk.Button(lower_frame, text="1", font=40, command=lambda: type_of_gas(1, root))
		c.place(relx=0.7, rely=0.1, relheight=0.8, relwidth=0.2)
	


	label, lower_frame = refresh_label("What type of car do you have. Gas, hybrid or electric?")

	hybrid = tk.Button(lower_frame, text="hybrid", font=40, command=lambda: car_branch_3(root))
	hybrid.place(relx=0.8, rely=0.1, relheight=0.8, relwidth=0.2)

	electric = tk.Button(lower_frame, text="electric", font=40, command=lambda: car_q_total(0, 0))
	electric.place(relx=0.4, rely=0.1, relheight=0.8, relwidth=0.2)

	gas = tk.Button(lower_frame, text="gas", font=40, command=lambda: car_branch_3(root))
	gas.place(relx=0, rely=0.1, relheight=0.8, relwidth=0.2)	


def car_branch_2(root):
	label, lower_frame = refresh_label("ok cool. Do you have a car at all?")

	def car_branch_no(root):
		label, lower_frame = refresh_label("cool, ummm not having a car helps lol.")
		moveon = tk.Button(lower_frame, text="cool, move on to the next questions", font=40, command=lambda: question2())
		moveon.place(relx=0.25, rely=0.1, relheight=0.8, relwidth=0.5)

	yes = tk.Button(lower_frame, text="yes", font=40, command=lambda: car_branch_1(root))
	yes.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.4)
	no = tk.Button(lower_frame, text="no", font=40, command=lambda: car_branch_no(root))
	no.place(relx=0.55, rely=0.1, relheight=0.8, relwidth=0.4)
	


def question1(root):
	label, lower_frame = refresh_label("Did you drive a car today")

	yes = tk.Button(lower_frame, text="Yes", font=40, command=lambda: car_branch_1(root))
	yes.place(relx=0.6, rely=0.1, relheight=0.8, relwidth=0.3)
	no = tk.Button(lower_frame, text="no", font=40, command=lambda: car_branch_2(root))
	no.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.3)


##################### FIRST QUESTION ALL BRANCHES END HERE #####################
def question2():
	def sub_elec(root):
		pass
	label, lower_frame = refresh_label("Appriximately what is your electrical usage per day? ")

	large = tk.Button(lower_frame, text="large: 12+kWh", font=40, command=lambda: sub_elec(root))
	large.place(relx=0.7, rely=0.1, relheight=0.8, relwidth=0.3)
	moderate = tk.Button(lower_frame, text="9-10kWk", font=40, command=lambda: sub_elec(root))
	moderate.place(relx=0.35, rely=0.1, relheight=0.8, relwidth=0.3)
	small = tk.Button(lower_frame, text="less than 8kWh", font=40, command=lambda: sub_elec(root))
	small.place(relx=0, rely=0.1, relheight=0.8, relwidth=0.3)
	
question1(root)
root.mainloop()
