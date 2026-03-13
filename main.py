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

                product_index = int(product_num) - 1
                quantity = int(amount)

                shopping_list.append((active_products[product_index], quantity))

            if shopping_list:
                total_price = best_buy.order(shopping_list)
                print(f"Order made! Total Payment: {total_price} dollars.")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    start(best_buy)