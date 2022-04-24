class User:

    list_booked_seats = []

    @staticmethod
    def user(row, column):
        dict_info = {"Name": "", "Surname": "", "Phone_number": int, "Row": int, "Column": int}

        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        phone_num = int(input("Enter your phone number: "))

        dict_info["Name"] = name
        dict_info["Surname"] = surname
        dict_info["Phone_number"] = phone_num
        dict_info["Row"] = row
        dict_info["Column"] = column

        list_booked = [dict_info]
        User.list_booked_seats.append(list_booked)
        print("Booked successfully")
        # print(self.list_booked_seats)

    def is_booked(self, c_row, c_col):
        found = 0
        for i in range(len(self.list_booked_seats)):
            tmp_list = self.list_booked_seats[i]
            for j in tmp_list:
                tmp_row = j.get("Row")
                tmp_col = j.get("Column")
                if tmp_row == c_row and tmp_col == c_col:
                    print("Seat is occupied\n")
                    found = 1
        if found == 0:
            print("Seat is vacant\n")

    def check_is_booked(self, c_row, c_col):
        for i in range(len(self.list_booked_seats)):
            tmp_list = self.list_booked_seats[i]
            for j in tmp_list:
                tmp_row = j.get("Row")
                tmp_col = j.get("Column")
                if tmp_row == c_row and tmp_col == c_col:
                    return True
        else:
            return False
