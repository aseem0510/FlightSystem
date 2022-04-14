class Flight:

    def __init__(self, sta1=None, sta2=None):

        self.flight = {"MAA-BOM":(4,[4000,5000,6000,7000],["6:00AM - 7:00AM","7:00AM - 8:00AM","8:00AM - 9:00AM","9:00AM - 10:00AM"], [7,4,1,9]), "MAA-DEL":(4,[3000,4000,5000,6000],["5:00AM - 6:00AM","6:00AM - 8:00AM","5:00AM - 6:00AM","10:00AM - 11:00AM"], [1,2,4,6])}
        self.sta1 = sta1
        self.sta2 = sta2
        self.refNo = {}
        self.id = [str(i) for i in range(100, 1000)]

    def display(self, des):

        temp = self.flight[des]

        print("Avaliable Flights:-", temp[0])

        k = 1
        for j in range(len(temp[1])):
            print()
            print("Flight", k)
            print("Fare:-", temp[1][j])
            print("Time:-", temp[2][j])
            print("Available Seats:-", temp[3][j])
            k += 1


    def booking(self, date, des):

        num = int(input("Enter Flight Number for booking:- "))
        seat = input("Enter Prefered Seat Number:- ")

        meal = input("Do you want to add meal(yes/no):- ")
        meal_charge = 0
        if meal == "yes":
            cnf = input("Exrta charge for meal is Rs.500: Do you want to confirm it(yes/no):- ")
            if cnf == "yes":
                meal_charge = 500

        temp = self.flight[des]

        flight_num_fare = temp[1][num-1]
        flight_num_time = temp[2][num-1]
        flight_num_seat = temp[3][num - 1]

        id = self.id[0]
        self.id.pop(0)

        print()
        print("Summary of Booking:-")
        print()

        print("Date:-", date)
        print("From-To:-", des)
        print("Time:-", flight_num_time)

        extra_fare = 0
        if flight_num_seat <= 5:
            extra_fare = flight_num_fare * (0.05)

        total_amount = flight_num_fare+meal_charge+extra_fare
        print("Fare (Flight Fare + Meal + Extra Charge(5%):-", flight_num_fare, "+", meal_charge, "+", extra_fare, "=", total_amount)
        print("Transaction Id:", id)

        self.refNo[id] = total_amount
        temp[3][num-1] -= 1

        print()
        cnf_booking = input("Do you want to confirm your booking?(yes/no) ")
        print()

        if cnf_booking == "yes":

            print("Total Amount paid:-", total_amount)
            print("Transaction Id:", id)

        else:
            self.cancel(date, des, flight_num_time)


    def cancel(self, date, des, time):

        cnf_cancel = input("Do you want to cancel your booking?(yes/no) ")

        if cnf_cancel == "yes":

            trans = input("Enter your transaction ID:- ")

            print()
            print("Summary of Booking:-")
            print()

            print("Date:-", date)
            print("From-To:-", des)
            print("Time:-", time)

            try:
                print("Total amount to refunded:-", self.refNo[trans])
            except:
                print("No booking found with this transaction ID")

        else:
            return



if __name__ == "__main__":

    short = {"Chennai": "MAA", "Mumbai": "BOM", "Delhi": "DEL"}

    print("Welcome to our Flight Reservation System")
    print()

    date = str(input('Enter Travel Date(dd-mm-yyyy):- '))
    print()

    print("Enter Airports Details")
    print()
    sta1 = input("From(From Where):- ")
    sta2 = input("To(To where):- ")

    sta1 = short[sta1]
    sta2 = short[sta2]

    des = sta1 + "-" + sta2

    f = Flight()

    print()
    f.display(des)
    print()

    f.booking(date, des)

