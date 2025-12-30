# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 18:36:03 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 19:07:17 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations():
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError: invalid literal for int()")
        
    print("\nTesting ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: division by zero")
    
    print("\nTesting FileNotFoundError...")
    try:
        with open("missing.txt","r") as f:
             _=f.read()
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        plants = {"tomato" : 5, "carrot" : 4}
        _=plants["missing\_plant"]
    except KeyError as e:
        print("Caught KeyError: 'missing\\_plant'")
    
    print("\nTesting multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print("Caught an error, but program continues!")

def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
    