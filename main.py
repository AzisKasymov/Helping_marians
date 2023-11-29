import random


def generate_cargo_location():  # Dist from spaceship to city 7 km
    return random.sample(range(1, 8), 3)


def check_cargo_location(locations, kilometers):
    if len(locations) != len(kilometers):
        return False
    for i in range(3):
        if locations[i] != kilometers[i]:
            return False
    return True


def main():
    weights = [245, 268, 200]
    while True:
        cargo_location = generate_cargo_location()  # array of locations of 3 boxes
        kilometers = []  # array of distances from martians
        for i in range(3):
            klm_of_box = int(input(f'Enter the kilometer mark for box {i + 1}, number from 1 to 7: '))
            kilometers.append(klm_of_box)
        cargo_found = check_cargo_location(cargo_location, kilometers)     
        if cargo_found:
            print('Congratulations! You found all the cargo locations!')
            break
        else:
            print(
                'Fail, the cargoes were not found. Cargoes have changed their location,enter new kilometer marks.')


main()
