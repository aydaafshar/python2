def check_temperature(temp_str):
    try:
        temperature = int(temp_str)

        if temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
            return None
        if temperature < 0:
            print(f"Error:{temperature}°C is too cold for plants (min 0°C)")
            return None
        return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"\nTesting temperature: {test}")
        result = check_temperature(test)

        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
