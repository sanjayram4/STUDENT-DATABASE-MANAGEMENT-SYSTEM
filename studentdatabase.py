class StudentDatabase:

    def __init__(self):
        self.data = {}

    def Data_store(self):
        subjects = ["Tamil", "English", "Maths", "Science", "Social"]
        marks_storage = []
        print()
        print("Enter The Student name and Marks \n")
        user_name = input("Enter The Name : ")
        print()
        for i in subjects:
            user_mark = input(f"Enter The {i} Mark : ")
            print()
            marks_storage.append(user_mark)
        self.data[user_name] = marks_storage
        marks_storage = []

    def Show_data(self):
        print()
        print("All Student Data Base \n")
        if len(self.data) == 0:
            print("**  There IS No Data Base in The Table. Add the data in the data base **")
        else:
            sub_cnt = 0  
            subjects = ["Name", "Tamil", "English", "Maths", "Science", "Social"]
            for k,v in self.data.items():
                print("-" * 30)
                print(f"{subjects[sub_cnt]} : {k}")
                sub_cnt += 1
                for j in v:
                    print(f"{subjects[sub_cnt]} : {j}")
                    sub_cnt += 1
                sub_cnt = 0
                print("-" * 30)
            sub_cnt = 0

    def Remove_database(self):
        print()
        user_del = input("Enter The Correct Name To Delete The data base : ")
        print()
        if user_del in self.data:
            self.data.pop(user_del)
        else:
            print()
            print("The Name Will Not In The Data Base. Check The name And Correct It!")
            print()

SD = StudentDatabase()
while True:
    print("_" * 40)
    print("Student Data Base\n")
    print("1. ADD Data Base \n2. All Student data base \n3. Deletee Data Base \n")
    print("_" * 40)
    print()
    user_inp = int(input("Enter Your Choice : "))
    if user_inp == 1:
        SD.Data_store()
    elif user_inp == 2:
        SD.Show_data()
    elif user_inp == 3:
        SD.Remove_database()
    else:
        print("Enter Correct Option")