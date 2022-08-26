# this example show an example tip calculator, very easy, very fun
import msvcrt

def costo():
	taxes = 3 / 100
	tip = 10.0 / 100
	print ("Welcome to the calculator of tips")
	print ("")
	food = input("Enter the cost of the dish you ordered, only digits: ")
	print("")
	total = float(food) + float(food) * taxes
	print("The total is: "+"$" + "%.2f" % total + " with taxes")
	print("The tip is: $" + str("%.2f" %(total * tip)))
	print("Press any key to exit.")
	while True:
		if msvcrt.kbhit():
			break

costo()