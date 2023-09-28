import pickle


# Funktion för att skapa en ny order
def create_order(order_number, customer_name, order_details):
    order = {
        "order_number": order_number,
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


# Huvudmeny
while True:
    print("\nHuvudmeny:")
    print("1. Sök efter en order")
    print("2. Avsluta")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        search_order_number = int(input("Ange ordernummer att söka efter: "))
        found_order = search_order_by_number(search_order_number, "orders.pickle.txt")

        if found_order is not None:
            print("Found Order:")
            print(f"Order Number: {found_order['order_number']}")


            # Skriv ut varje vara och dess pris
            print("Order Details:")
            for item_name, item_price in found_order['order_details']:
                print(f"  {item_name}: {item_price}")

            # Beräkna och skriv ut den totala summan
            total_price = sum(item_price for _, item_price in found_order['order_details'])
            print(f"Total Price: {total_price}")

        else:
            print(f"Order with Order Number {search_order_number} not found.")

    elif choice == "2":
        break

    input("Tryck på Enter för att återgå till menyn...")
