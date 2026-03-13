import products
import store

product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(best_buy):

    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            active_products = best_buy.get_all_products()

            print("------")
            for i, product in enumerate(active_products, start=1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total of {total} items in store")

        elif choice == "3":
            active_products = best_buy.get_all_products()

            print("------")
            for i, product in enumerate(active_products, start=1):
                print(f"{i}. ", end="")
                product.show()
            print("------")
            print("When you want to finish order, enter empty text.")

            shopping_list = []

            while True:
                product_num = input("Which product # do you want? ")

                if product_num == "":
                    break

                amount = input("What amount do you want? ")

                if amount == "":
                    break

                try:
                    product_index = int(product_num) - 1
                    quantity = int(amount)

                    if product_index < 0 or product_index >= len(active_products):
                        print("Error adding product!")
                        continue

                    if quantity <= 0:
                        print("Error adding product!")
                        continue

                    shopping_list.append((active_products[product_index], quantity))

                except ValueError:
                    print("Error adding product!")

            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"Order made! total payment: {total_price} dollars.")
                except Exception as e:
                    print(e)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    start(best_buy)