class ApartmentBuilding:
    shared_facilities = ["Gym", "Pool"]

    def __init__(self, name, total_units):
        self.name = name
        self.total_units = total_units
        self.occupied_units = 0
        self.units = [False] * total_units  # False means the unit is vacant

    def update_occupancy(self, unit_number, status):
        if 0 <= unit_number < self.total_units:
            self.units[unit_number] = status
            self.occupied_units = sum(self.units)
        else:
            raise ValueError("Invalid unit number")

    def available_units(self):
        return [i for i, occupied in enumerate(self.units) if not occupied]

    def occupancy_rate(self):
        return (self.occupied_units / self.total_units) * 100

    def __str__(self):
        facilities = ", ".join(self.shared_facilities)
        return (f"Building: {self.name}\n"
                f"Total Units: {self.total_units}\n"
                f"Occupied Units: {self.occupied_units}\n"
                f"Occupancy Rate: {self.occupancy_rate():.2f}%\n"
                f"Available Units: {self.available_units()}\n"
                f"Facilities: {facilities}\n")


def main():
    buildings = []

    while True:
        print("\n1. Add new building")
        print("\n2. Update occupancy")
        print("\n3. List all buildings")
        print("\n4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter building name: ")
            total_units = int(input("Enter total number of units: "))
            buildings.append(ApartmentBuilding(name, total_units))

        elif choice == '2':
            building_name = input("Enter building name: ")
            unit_number = int(input("Enter unit number: "))
            status = input("Enter status (occupied/vacant): ").lower() == "occupied"

            for building in buildings:
                if building.name == building_name:
                    try:
                        building.update_occupancy(unit_number, status)
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Building not found")

        elif choice == '3':
            for building in buildings:
                print(building)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
