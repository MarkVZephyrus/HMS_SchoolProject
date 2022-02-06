import json
import locale

customers = {}

room_types = {'T1': 500, 'T2': 650, 'T3': 700, 'T4': 1000, 'T5': 2000}

try:
    with open('customers.json', 'r') as f:
        if f.read():
            customers = json.load(f)
        else:
            customers = {}
except FileNotFoundError:
    with open('customers.json', 'w') as f:
        customers = {}


def check_in(room_number, customer_name, check_in_date, check_out_date, room_type):
    global customers
    if room_type.capitalize() not in room_types:
        raise ValueError('Invalid room type')
    if check_in_date > check_out_date:
        raise ValueError('Check-in date must be before check-out date')
    try:
        customers[int(list(customers)[-1])+1] = [room_number, customer_name,
                                                 check_in_date, check_out_date, room_type]
    except IndexError:
        customers["101"] = [room_number, customer_name,
                            check_in_date, check_out_date, room_type]
    dump_customers()


def check_out(srno):
    global customers
    if srno in customers:
        del customers[srno]
        dump_customers()
        return 0
    else:
        return -1


def display_customers():
    global customers
    print("{:<10} | {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Sr. No.", "Room No.", "Customer Name", "Check-in Date", "Check-out Date", "Room Type"))
    for customer in customers:
        print("{:<10} | {:<20} {:<20} {:<20} {:<20} {:<20}".format(customer, customers[customer][0], customers[customer]
              [1], customers[customer][2], customers[customer][3], customers[customer][4]))


def dump_customers():
    global customers
    with open('customers.json', 'w') as f:
        json.dump(customers, f)


def load_customers():
    global customers
    with open('customers.json', 'r') as f:
        if f.read():
            return json.load(f)
        else:
            return {}


def display_customer(srno):
    global customers
    print("{:<10} | {:<20} {:<20} {:<20} {:<20}".format(
        "Sr. No.", "Room No.", "Customer Name", "Check-in Date", "Check-out Date"))
    print("{:<10} | {:<20} {:<20} {:<20} {:<20} {:<20}".format(srno, customers[srno][0], customers[srno]
          [1], customers[srno][2], customers[srno][3], customers[srno][4]))
    print("##################################################################\n")
    print("net cost: ", locale.currency(
        room_types[customers[srno][4].capitalize()], grouping=True))
