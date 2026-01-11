def garden_operations():
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            _ = f.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        plants = {"tomato": 5, "carrot": 4}
        _ = plants["missing\\_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except Exception:
        print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
