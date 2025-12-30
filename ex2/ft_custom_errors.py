# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 19:08:57 by ayda              #+#    #+#              #
#    Updated: 2025/12/30 19:27:58 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass
class WaterError(GardenError):
    pass

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
        
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")



if __name__ == "__main__":
    test_custom_errors()