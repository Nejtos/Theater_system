import user


class Seats:

    list_of_seats = []

    def __init__(self):
        self.num_of_rows = 9
        self.num_of_cols = 10

    def create_seats(self):
        for i in range(self.num_of_rows + 1):
            a = []
            for j in range(self.num_of_cols + 1):
                a.append("S")
            self.list_of_seats.append(a)
        # print(self.list_of_seats)

    def show_seats(self):
        for i in range(0, self.num_of_rows + 1):
            if i == 0:
                for j in range(0, self.num_of_cols + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(0, self.num_of_cols):
                    print(self.list_of_seats[i - 1][k], end=" ")
            print()


class Ticket:

    def __init__(self):
        self.book_row = int(input("Enter number of the row: "))
        self.book_col = int(input("Enter number of the column: "))

    def make_reservation(self):
        confirmation = input("Confirm to book your ticket (Yes/No): ")
        if confirmation == 'Yes' or confirmation == 'yes' or confirmation == 'YES':
            Seats.list_of_seats[self.book_row - 1][self.book_col - 1] = "B"
            u = user.User()
            u.user(self.book_row, self.book_col)
        else:
            print("Not booked\n")

    def cancel_reservation(self):
        cond = True
        surname = input("Enter your surname: ")
        confirmation = input("Confirm cancel your reservation (Yes/No): ")
        if confirmation == 'Yes' or confirmation == 'yes' or confirmation == 'YES':
            lista = user.User.list_booked_seats
            for i in range(len(lista)):
                if cond is True:
                    tmp_list = lista[i]
                    for j in tmp_list:
                        tmp_surname = j.get("Surname")
                        if tmp_surname == surname:
                            lista.pop(i)
                            Seats.list_of_seats[self.book_row - 1][self.book_col - 1] = "S"
                            print("Reservation have been cancelled\n")
                            cond = False
                else:
                    break
            # print(lista)
        else:
            print("Nothing changed")
