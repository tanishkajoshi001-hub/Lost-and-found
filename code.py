# Two empty lists to store details
lost = []      # items that people lost
found = []     # items that people found

print("----- LOST AND FOUND TRACKER -----")

while True:
    # Showing the menu again and again
    print("\n1. Add Lost Item")
    print("2. Add Found Item")
    print("3. Show Lost Items")
    print("4. Show Found Items")
    print("5. Match Lost and Found")
    print("6. Exit")

    ch = input("Enter choice: ")

    # 1. Add Lost Item
    if ch == "1":
        name = input("Item name: ")
        place = input("Lost at: ")
        person = input("Owner name: ")

        # Storing the details in dictionary form
        lost.append({
            "item": name,
            "place": place,
            "person": person
        })

        print("Lost item added successfully!")

    # 2. Add Found Item
    elif ch == "2":
        name = input("Item name: ")
        place = input("Found at: ")
        finder = input("Finder name: ")

        found.append({
            "item": name,
            "place": place,
            "finder": finder
        })

        print("Found item added successfully!")

    # 3. Show Lost Items
    elif ch == "3":
        print("\n--- LOST ITEMS ---")

        if len(lost) == 0:
            print("No lost items yet.")
        else:
            for i in lost:
                print(f"Item: {i['item']}, Place: {i['place']}, Owner: {i['person']}")

    # 4. Show Found Items
    elif ch == "4":
        print("\n--- FOUND ITEMS ---")

        if len(found) == 0:
            print("No found items yet.")
        else:
            for f in found:
                print(f"Item: {f['item']}, Place: {f['place']}, Finder: {f['finder']}")

    # 5. Match Lost & Found Items
    elif ch == "5":
        print("\n--- MATCHING RESULTS ---")
        match_done = False

        # Compare every lost item with every found item
        for l in lost:
            for f in found:
                if l["item"].lower() == f["item"].lower():
                    print(f"\nMatch Found for: {l['item']}")
                    print(f"Lost at: {l['place']}  |  Found at: {f['place']}")
                    print(f"Owner: {l['person']}  |  Finder: {f['finder']}")
                    match_done = True

        if not match_done:
            print("No matching items yet.")


    # 6. Exit the program
    elif ch == "6":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")