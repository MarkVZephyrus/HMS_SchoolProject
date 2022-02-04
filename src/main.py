import pickle

rooms = {'1':1,'2':2,'3':3}

customers = []

try:
    with open('customers.hms','rb') as f:
        if f.read() == b'':
            customers = []
        else:
            try: customers = pickle.load(f)
            except EOFError: pass
except FileNotFoundError:
    with open('customers.hms','wb') as f:
        customers = []

class Customer:
    
    global customers

    def __init__(self,srno,name,check_in,check_out,room_no,room_type):
        self.name = name
        self.check_in = check_in
        self.check_out = check_out
        self.room_no = room_no
        if room_type in rooms.keys():
            self.room_type = room_type
        else:
            raise ValueError('Invalid room type')
        self.srno = srno
    

def check_in(srno,name,check_in,check_out,room_no,room_type):
    customer = Customer(srno,name,check_in,check_out,room_no,room_type)
    if customer.check_in > customer.check_out:
        raise ValueError('Check in date cannot be greater than check out date')
    for customer in customers:
        if customer.srno == srno:
            raise ValueError('SrNo must be unique')
    customers.append(customer)
    with open('customers.hms','wb') as f:
        pickle.dump(customers,f)

def check_out(srno):
    for customer in customers:
        if customer.srno == srno:
            customers.remove(customer)
            break
    else:
        raise ValueError('Customer not found')
    with open('customers.hms','wb') as f:
        pickle.dump(customers,f)

def display_customers():
    for customer in customers:
        print('{} _ {} _ {} _ {} _ {} _ {}'\
            .format(customer.srno,\
            customer.name,customer.check_in,customer.check_out,customer.room_no,customer.room_type))

check_in(1, 'John', '12/12/12', '12/12/12', '1', '1')
check_in(2, 'ohn', '12/12/12', '12/12/12', '2', '2')
check_in(3, 'hn', '12/12/12', '12/12/12', '3', '3')
input('Press enter to continue')
display_customers()
input('Press enter to continue')
check_out(1)
display_customers()
input('Press enter to continue')