import customerrec as cr
import locale
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')


def main():
    while True:
        print("##################################################################\n")
        print("Welcome to the Hotel Management System")
        print("1. Check-in")
        print("2. Check-out")
        print("3. Register meal")
        print("4. Display all customers")
        print("5. Display customer")
        print("6. Exit")
        print("\n##################################################################\n")
        choice = int(input("Enter your choice: "))
        print('\n')
        if choice == 1:
            try:
                room_number = int(input("Enter room number: "))
                customer_name = input("Enter customer name: ")
                check_in_date = input("Enter check-in date (dd/mm/yyyy): ")
                check_out_date = input("Enter check-out date (dd/mm/yyyy): ")
                cr.check_in(room_number, customer_name, check_in_date, check_out_date)
            except ValueError as e:
                print(e)
                continue
            print("Customer checked-in successfully!")
            print('\n')
            continue
        elif choice == 2:
            srno = input("Enter customer's Sr. No.: ")
            print(cr.display_customer(srno))
            if input("proceed to check-out? (y/n): ") == 'y':
                if cr.check_out(srno) == 0:
                    print("Customer checked-out successfully!")
                print('\n')
            continue
        elif choice == 3:
            srno = input("Enter SrNo: ")
            meal = input("Enter meal: ")
            cr.take(srno, meal)
            print("\nDone!")
        elif choice == 4:
            cr.display_customers()
            print('\n')
            continue
        elif choice == 5:
            srno = input("Enter customer's Sr. No.: ")
            cr.display_customer(srno)
            print('\n')
            continue
        elif choice == 6:
            cr.dump_customers()
            break
        else:
            print("Invalid choice")
            print('\n')
            continue


if __name__ == "__main__":
    main()
