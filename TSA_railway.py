# satnam shri waheguru 
print()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_WELCOME TO T.S.A RAILWAYS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print()
class Train:    
    seats=[1,2,3,4,5,6,7,8,9,10]
    def __init__(self, name, fare ):
        self.name=name
        self.fare=fare
    def displayStatus(self):
        print(f"welcome to {self.name}, your fare for journey is Rs. {self.fare}")
        print(f"the number of available seats are {len(self.seats)}" )
        print(self.seats)
    def bookTicket(self):
        if (len(self.seats)>0):
            print(f"your ticket has been booked, your seat no. is {self.seats.pop()}")
        else:
            print("sorry, for the inconvinece all the tickets have been, try tatkal service. Thank you ")
    def cancelTicket(self,ticket):     
        self.ticket = self.seats.append(ticket)
    def displayCticket(self):
        print(f"your ticket has been cancelled")
        print("here is the list of available tickets")
        print(self.seats)
    

rajdhani=Train("Rajdhani Express", 3295)
rajdhani.displayStatus()
rajdhani.bookTicket()                             # seat no. 10 alloted
rajdhani.bookTicket()                             # seat no. 9 alloted
rajdhani.bookTicket()                             # seat no. 8 alloted
rajdhani.cancelTicket(9)                           # seat no. 9 cancelled
rajdhani.displayCticket()                           



