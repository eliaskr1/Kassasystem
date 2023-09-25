import pickle

# Funktion för att skapa en ny order
def create_order(order_number, customer_name, order_details):
    order = {
        "order_number": order_number,
        "customer_name": customer_name,
        "order_details": order_details
    }
    return order

# Funktion för att spara en lista med ordrar i en pickle-fil
def save_orders_to_pickle(orders, file_name):
    with open(file_name, "wb") as file:
        pickle.dump(orders, file)

# Funktion för att söka efter en order med ett specifikt ordernummer
def search_order_by_number(order_number, file_name):
    try:
        with open(file_name, "rb") as file:
            orders = pickle.load(file)
            for order in orders:
                if order["order_number"] == order_number:
                    return order
            return None  # Returnera None om ordernumret inte hittades
    except FileNotFoundError:
        return None  # Returnera None om filen inte hittades

# Exempel: Skapa några ordrar och spara dem i en pickle-fil
orders = [
    create_order(1, "Alice", "Product A"),
    create_order(2, "Bob", "Product B"),
    create_order(3, "Charlie", "Product C")
]

save_orders_to_pickle(orders, "orders.pickle.txt")

# Fråga användaren efter ordernumret de vill söka efter
search_order_number = int(input("Ange ordernummer att söka efter: "))

# Sök efter en order med det angivna ordernumret och skriv ut den
found_order = search_order_by_number(search_order_number, "orders.pickle.txt")

if found_order is not None:
    print("Found Order:")
    print(f"Order Number: {found_order['order_number']}")
    print(f"Customer Name: {found_order['customer_name']}")
    print(f"Order Details: {found_order['order_details']}")
else:
    print(f"Order with Order Number {search_order_number} not found.")

#söka efter orde