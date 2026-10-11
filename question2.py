def main():
    inventory = {
        "Notebook": {"quantity": 120, "price": 150.00},
        "Ball Pen": {"quantity": 300, "price": 30.00},
        "Calculator": {"quantity": 25, "price": 1850.00},
        "School Bag": {"quantity": 40, "price": 2200.00},
        "Water Bottle": {"quantity": 60, "price": 650.00},
    }

    print("Question # 02: Store Inventory Using Loops")

    print("\nItems in the inventory")
    print("-" * 30)
    print(f"{'Item':<18}{'Quantity':>12}")
    print("-" * 30)

    for item, details in inventory.items():
        print(f"{item:<18}{details['quantity']:>12}")

    print("\nValue of the inventory (quantity * price)")
    print("-" * 62)
    print(f"{'Item':<18}{'Quantity':>12}{'Price':>14}{'Value':>18}")
    print("-" * 62)

    total_value = 0.0

    for item, details in inventory.items():
        quantity = details["quantity"]
        price = details["price"]
        item_value = quantity * price
        total_value += item_value
        print(f"{item:<18}{quantity:>12}{price:>14,.2f}{item_value:>18,.2f}")

    print("-" * 62)
    print(f"Total value of the inventory: {total_value:,.2f}")


if __name__ == "__main__":
    main()