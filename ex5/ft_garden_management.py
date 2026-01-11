class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):

        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours > 12:
            raise GardenError(f"Sunlight hours {sunlight_hours} is"
                              f" too high (max 12)")
        if sunlight_hours < 2:
            raise GardenError(f"Sunlight hours {sunlight_hours} is"
                              f" too low (min 2)")
        print(f"{plant_name}: healthy (water: {water_level},"
              f" sun: {sunlight_hours})")


def main():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Caught GardenError: {e}")

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
