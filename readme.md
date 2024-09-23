# Apartment Building Management System

This Python program manages different aspects of apartment buildings in a city, including tracking the number of units, occupancy status, and facilities. It allows the management to add new buildings, update occupancy, and list available units and facilities in each building.

## Features

- Add new apartment buildings
- Update occupancy status of units
- List available units in each building
- Calculate the occupancy rate of each building
- Shared facilities like gym and pool

## Class Structure

### `ApartmentBuilding`

- **Attributes:**
  - `name`: Name of the building
  - `total_units`: Total number of units in the building
  - `occupied_units`: Number of occupied units
  - `units`: List of boolean values representing occupancy status of each unit
  - `shared_facilities`: Class variable representing shared facilities

- **Methods:**
  - `update_occupancy(unit_number, status)`: Updates the occupancy status of a unit
  - `available_units()`: Returns a list of available units
  - `occupancy_rate()`: Calculates and returns the occupancy rate
  - `__str__()`: Returns a string representation of the building details

## Usage

1. **Add New Building:**
   - Enter the building name and total number of units.

2. **Update Occupancy:**
   - Enter the building name, unit number, and occupancy status (occupied/vacant).

3. **List All Buildings:**
   - Displays the details of all buildings, including available units and occupancy rate.

## Exception Handling

- Ensures input errors are managed effectively, such as invalid unit numbers.

## Example

```python
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
