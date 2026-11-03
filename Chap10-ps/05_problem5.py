#Write a class Train which has methods to book a ticket,get status(no of seats) and get fare of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"Train no: {self.trainNo} is running on time!")

    def get_fare(self, fro, to):
        print(f"Fare of train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t=Train(12399)
t.book("Delhi","Mumbai")
t.get_status()
t.get_fare("Delhi","Mumbai")