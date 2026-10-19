Customers = []
TicketsSold = []
x = int(input("Number of customers: "))
most = " "
total = 0
for x in range(x):
    name = str(input("Enter name: "))
    Ticket = False
    while Ticket == False:
        ticketno = int(input("Enter number of tickets bought: "))
        if 1<=ticketno<=6:
            Ticket = True
            most = name
            total = total + ticketno
        else:
            print("Invalid")
    Customers.append(name)
    TicketsSold.append(ticketno)
print(Customers)
print(TicketsSold)
print("Person who bought most tickets is " , most)

        
        
        
        
        
