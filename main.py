def find_cargo_location():
    total_weight = 713
    box_weights = [200, 300, 213]
    cargo_locations = [0, 0, 0]

    while True:
        print("Enter kilometer mark:")
        for i in range(3):
            cargo_locations[i] = int(input(f"Box {i + 1}: "))
            print("Error! Please enter a valid integer.")
            return

            cargo_locations[i] += i + 1

        print("Boxes have been moved. Checking the result...")

        if sum(box_weights) == total_weight:
            print("congratulation")
            break
        else:
            print("Error! The total weight of the boxes is not 713 kg. Please re-enter.")

find_cargo_location()
