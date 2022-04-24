import theater_info
import user

user_input = 10
s = theater_info.Seats()
u = user.User()
total_seats = s.num_of_rows * s.num_of_cols
total_seats_booked = 0
s.create_seats()

while user_input != 0:
    print("1: Show the Seats\n2: Make a reservation\n3: Cancel reservation\n4: Check seat\n0: Exit")
    user_input = int(input("Choose option: "))

    if user_input == 1:
        ave_seats = total_seats - total_seats_booked
        s.show_seats()
        print("Number of available seats: " + str(ave_seats) + "\n")

    elif user_input == 2:
        if total_seats_booked < total_seats:
            t = theater_info.Ticket()
            if t.book_row <= s.num_of_rows and t.book_col <= s.num_of_cols:
                if u.check_is_booked(t.book_row, t.book_col) is False:
                    t.make_reservation()
                    if u.check_is_booked(t.book_row, t.book_col) is True:
                        total_seats_booked = total_seats_booked + 1
                    print("Number of reserved places: " + str(total_seats_booked) + "\n")
                else:
                    print("This seat is actually booked\n")
            else:
                print("You are trying to book the wrong seat\n")
        else:
            print("All seats are occupied\n")

    elif user_input == 3:
        t = theater_info.Ticket()
        if t.book_row <= s.num_of_rows and t.book_col <= s.num_of_cols:
            if u.check_is_booked(t.book_row, t.book_col) is True:
                t.cancel_reservation()
                if u.check_is_booked(t.book_row, t.book_col) is False:
                    total_seats_booked = total_seats_booked - 1
            else:
                print("Something went wrong, this seat is vacant")
        else:
            print("There is no such seat\n")

    elif user_input == 4:
        checkR = int(input("Enter the row you want to check: "))
        checkC = int(input("Enter the column you want to check: "))
        if checkR <= s.num_of_rows and checkC <= s.num_of_cols:
            u.is_booked(checkR, checkC)
        else:
            print("There is no such seat\n")
