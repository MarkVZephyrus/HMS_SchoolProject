import json
import locale

customers = {}

room_types = {'T1': 500, 'T2': 650, 'T3': 700, 'T4': 1000, 'T5': 2000}

try:
    with open('customers.json', 'r') as f:
        if f.read():
            f.seek(0)
            customers = json.load(f)
        else:
            customers = {}
except FileNotFoundError:
    with open('customers.json', 'w') as f:
        customers = {}


def check_in(room_number, customer_name, check_in_date, check_out_date):
    global customers
    if check_in_date > check_out_date:
        raise ValueError('Check-in date must be before check-out date')
    try:
        customers[int(list(customers)[-1])+1] = [room_number, customer_name,
                                                 check_in_date, check_out_date, "T"+str(room_number)[0],
                                                 {'Room Cost':room_types["T"+str(room_number)[0]]}]
    except IndexError:
        customers["101"] = [room_number, customer_name,
                            check_in_date, check_out_date, "T"+str(room_number)[0],
                            {'Room Cost':room_types["T"+str(room_number)[0]]}]
    dump_customers()


def check_out(srno):
    global customers
    if srno in customers:
        ret = customers[srno]
        del customers[srno]
        dump_customers()
        return ret
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
        json.dump(customers, f, indent=4)


def load_customers():
    global customers
    with open('customers.json', 'r') as f:
        if f.read():
            return json.load(f)
        else:
            return {}


def display_customer(srno):
    global customers
    print("{:<10} | {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Sr. No.", "Room No.", "Customer Name", "Check-in Date", "Check-out Date", "Room Type"))
    print("{:<10} | {:<20} {:<20} {:<20} {:<20} {:<20}".format(srno, customers[srno][0], customers[srno]
          [1], customers[srno][2], customers[srno][3], customers[srno][4]))
    print("##################################################################\n")
    print("Net cost: : \n")
    netCost = 0
    for i in customers[srno][5].keys():
        print("{} -- {}".format(i, locale.currency(customers[srno][5][i], grouping=True)))
        netCost+=customers[srno][5][i]
    print("_"*10)
    print("\nNet Cost = {}".format(locale.currency(netCost)))
    print("\n")
    print("_"*10)
    

meals = {"Breakfast":60,'Lunch': 65,'Dinner':70,'Snacks':30,'Tea':20}

def take(srno, meal):
    if meal.capitalize() in meals.keys():
        customers[srno][5][meal.capitalize()]=meals[meal.capitalize()]
        dump_customers()
        return 0
    return -1