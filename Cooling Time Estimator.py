"""
Cooling Time Calculator Program
--------------------------------

This program models the cooling of an object using Newton's Law of Cooling.
It allows the user to input initial temperature, ambient temperature, and
cooling constant, then predicts the time required to reach a target temperature.

Features:
- Input validation
- Logging of results to file
- Optional experimental data comparison
- Graph-ready output format

This tool is designed for use in a STEM investigation to compare theoretical
predictions with real experimental cooling data.
"""

import math
from datetime import datetime
import os
import time

# Colour codes

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def startup_banner():
    """
    Displays the program's startup banner with colour formatting.
    """

VERSION = '1.0'

print(CYAN + f"""
+----------------------------------------+
|      COOLING TIME CALCULATOR v{VERSION}      |
|        Newton's Law of Cooling         |
|         Engineered by Aleema *         |
+----------------------------------------+
""" + RESET)
time.sleep(0.5)

def convert_input(prompt):
    """
    Converts user input into a float value.
    Accepts either plain numbers (e.g. '500') or values with units (e.g. '500 g', '0.2 kg').
    Returns None if the format is invalid.
    """
    raw = input(prompt).strip().lower()

    # If the user enters only a number, return it directly
    try:
        return float(raw)
    except ValueError:
        pass  # Continue to unit parsing

    # Split number + unit
    parts = raw.split()
    if len(parts) != 2:
        print(RED + "Invalid format. Example: '500 g' or '0.2 kg'." + RESET)
        return None

    value_str, unit = parts

    # Normalise unit formatting

    unit = unit.replace("²", "2")
    unit = unit.replace(" ", "")

    try:
        value = float(value_str)
    except ValueError:
        print(RED + "Invalid number." + RESET)
        return None

    # Mass units

    if unit == "kg":
        return value
    if unit == "g":
        return value / 1000

    # Area units

    if unit in ["m2", "m²"]:
        return value
    if unit in ["cm2", "cm²"]:
        return value / 10000

    # Specific heat capacity units

    if unit == "j/kgk":
        return value
    if unit == "j/gk":
        return value * 1000

    # Heat transfer coefficient units

    if unit in ["w/m2k", "w/m²k"]:
        return value
    if unit in ["w/cm2k", "w/cm²k"]:
        return value * 10000  # cm² → m²
    if unit == "kw/m2k":
        return value * 1000   # kW → W

    print(RED + f"Unknown unit '{unit}'." + RESET)
    return None

# Create log file if it doesn't exist

if not os.path.exists("cooling_log.txt"):
    with open("cooling_log.txt", "w") as file:
        file.write("=== COOLING LOG FILE ===\n\n")

def menu():
    """
        Display the main menu for the Cooling Time Calculator program.

    Returns:
        str: The user's menu selection as a string.
    """
    while True:
        print(CYAN + '\n+------------------------------+' + RESET)
        print(CYAN + '|          MAIN MENU           |' + RESET)
        print(CYAN + '+------------------------------+\n' + RESET)
        print(CYAN + '1. Calculate Estimated Cooling Time' + RESET)
        print(CYAN + '2. Learn Cooling Time Equation' + RESET)
        print(CYAN + '3. Estimate k from Material and Size' + RESET)
        print(CYAN + '4. Open Saved Results File' + RESET)
        print(CYAN + '5. Clear Log File' + RESET)
        print(CYAN + '6. About Menu' + RESET)
        print(CYAN + '7. Exit Program' + RESET)

        choice = input(CYAN + '\nChoose an option (1-7): ' + RESET).strip()

        # Validation

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return choice

        print(RED + 'Invalid choice. Please enter a number between 1 and 7.' + RESET)

def calculate_cooling_time():
    """
        Calculate the estimated cooling time of an object using Newton's Law of Cooling.

    This function:
        - Prompts the user for initial temperature, environment temperature,
          cooling constant k, and target temperature.
        - Validates numeric input.
        - Computes cooling time in minutes.
        - Allows the user to choose output units (minutes, seconds, hours).
        - Displays the final cooling time.
        - Logs all calculation details to 'cooling_log.txt'.

    Returns:
        None
    """

    print(CYAN + '\n--- COOLING TIME CALCULATOR ---\n' + RESET)

    # Initial temperature

    while True:
        initial_temp = convert_input("Initial temperature of object (°C): ")
        if initial_temp is not None:
            break

    # Environment temperature

    while True:
        environment_temp = convert_input("Environment temperature (°C): ")
        if environment_temp is not None:
            break

    # Cooling constant k

    while True:
        cooling_constant = convert_input("Cooling constant k (1/min): ")
        if cooling_constant is not None:
            break

    # Target temperature

    while True:
        target_temperature = convert_input("Target temperature you want to reach (°C): ")
        if target_temperature is not None:
            break

    if target_temperature < environment_temp:
        print(YELLOW + "Warning: Target temperature is below environment temperature. This implies heating, not cooling." + RESET)
        return
    elif target_temperature == environment_temp:
        estimated_cooling_time = 0
        print(GREEN + "Target temperature equals environment temperature. Cooling time is zero." + RESET)
    else:
        estimated_cooling_time = (-1 / cooling_constant) * math.log((target_temperature - environment_temp) / (initial_temp - environment_temp))

    print(CYAN + "\nChoose output units:" + RESET)
    print(CYAN +"1. Minutes" + RESET)
    print(CYAN + "2. Seconds" + RESET)
    print(CYAN + "3. Hours" + RESET)

    unit_choice = input("Select an option (1-3): ")

    if unit_choice == "1":
        final_time = estimated_cooling_time
        unit_label = "minutes"
    elif unit_choice == "2":
        final_time = estimated_cooling_time * 60
        unit_label = "seconds"
    elif unit_choice == "3":
        final_time = estimated_cooling_time / 60
        unit_label = "hours"
    else:
        print(RED + "Invalid choice. Defaulting to minutes." + RESET)
        final_time = estimated_cooling_time
        unit_label = "minutes"

    for i in range(3):
        print('Calculating' + '.' * (i + 1))
        time.sleep(0.3)

    time.sleep(0.2)

    print(GREEN + f'The estimated cooling time of your object is {final_time:.2f} {unit_label}.' + RESET)

    input(CYAN + '\nPress Enter to return to the menu...' + RESET)

    # Save calculation details to log file
    with open("cooling_log.txt", "a") as file:
        file.write("=====================================\n")
        file.write(" COOLING CALCULATION LOG ENTRY\n")
        file.write("=====================================\n")
        file.write(f"Timestamp:                 {datetime.now()}\n")
        file.write(f"Initial Temperature:       {initial_temp} °C\n")
        file.write(f"Environment Temperature:   {environment_temp} °C\n")
        file.write(f"Cooling Constant k:        {cooling_constant} 1/min\n")
        file.write(f"Target Temperature:        {target_temperature} °C\n")
        file.write(f"Estimated Cooling Time:    {final_time:.2f} {unit_label}\n")
        file.write("-------------------------------------\n\n")

def explain_equation():
    """
       Displays a detailed explanation of Newton's Law of Cooling.

       This includes:
           - The mathematical form of the equation.
           - Definitions of each variable.
           - A step-by-step example calculation.
           - A conceptual explanation of how cooling slows over time.

       Returns:
           None
    """

    print(CYAN + '''
------------------------------
   Newton's Law of Cooling:
------------------------------

''' + RESET + GREEN +

'''\nT(t)= T_env + (T0 - T_env) * e^(-k * t)

''' + RESET + CYAN + '''

Where:

T(t) = Temperature of object at time t (what we want to calculate)
T_env = Temperature of the environment (object will eventually cool to this temp)
T0 = Initial temperature
math.exp(-k * t) = This means that at the start, when t = 0, 
cooling is fast, but as time increases, cooling slows down

''' + RESET + CYAN + '''

What this equation is basically saying:
An object cools down faster when it’s very hot, and cools down slower 
as it gets closer to the room temperature.

''' + RESET + CYAN + '''

This equation gives temperature at time t, but in engineering, we usually
want the opposite: How long until an object cools to a certain temperature?

''' + RESET + GREEN + '''

So, we rearrange the equation to solve for t instead:

t = -(1 / k) * ln((T_target - T_env) / (T0 - T_env))

''' + RESET + CYAN + '''

For example:

- A metal block starts at 150°C
- The room is 25°C
- The cooling constant is k = 0.1
- Your target temperature is 50°C

All you would have to do is substitute these values in the equation.
''' + RESET + GREEN + '''

So, the equation would be:

t = -(1 / 0.1) * ln((50 - 25) / (150 - 25))
  = -(1 / 0.1) * ln(25 / 125)
  = -(1 / 0.1) * ln(0.2)
  = -10 * -1.609
  = 16.09

''' + RESET + CYAN + '''

So, your object would take approximately 16 minutes to cool down from 150°C
down to 50°C in a 25°C environment with k = 0.1.''' + RESET)

input(CYAN + '\nPress Enter to return to the menu...' + RESET)

def choose_material():
    print(CYAN + "\n--- MATERIAL PRESETS ---\n" + RESET)
    print("1. Steel (c = 500 J/kg·K)")
    print("2. Aluminium (c = 900 J/kg·K)")
    print("3. Water (c = 4180 J/kg·K)")
    print("4. Wood (c = 1700 J/kg·K)")
    print("5. Custom (you enter everything)")

    choice = input(CYAN + "Choose a material (1-5): " + RESET)

    if choice not in ["1", "2", "3", "4", "5"]:
        print(RED + "Invalid choice. Defaulting to custom." + RESET)
        return None

    materials = {
        "1": 500,    # steel
        "2": 900,    # aluminium
        "3": 4180,   # water
        "4": 1700,   # wood
        "5": None    # custom}
        }

    return materials[choice]

def estimate_k_from_material_and_size():
    """
        Estimate the cooling constant k based on material and geometric properties.

        Prompts the user for:
            - Convective heat transfer coefficient (W/(m^2·K))
            - Surface area (m^2)
            - Mass (kg)
            - Specific heat capacity (J/(kg·K))

        Uses the formula:
            k = (h * A) / (m * c)

        Returns:
            float: The estimated cooling constant k in 1/min.
    """
    print(CYAN + "\n--- ESTIMATE K FROM MATERIAL & SIZE ---\n" + RESET)

    print(CYAN + "Choose a material:\n" + RESET)
    print(CYAN + "1. Steel (c = 500 J/kgK)" + RESET)
    print(CYAN + "2. Aluminium (c = 900 J/kgK)" + RESET)
    print(CYAN + "3. Water (c = 4180 J/kgK)" + RESET)
    print(CYAN + "4. Wood (c = 1700 J/kgK)" + RESET)
    print(CYAN + "5. Custom" + RESET)

    material_choice = input("Select an option (1-5): ")

    # Material presets dictionary

    presets = {
        "1": (500, "Steel"),
        "2": (900, "Aluminium"),
        "3": (4180, "Water"),
        "4": (1700, "Wood")
    }

    if material_choice in presets:
        specific_heat_capacity, material_name = presets[material_choice]
        print(GREEN + f"Using preset: {material_name} ({specific_heat_capacity} J/kgK)" + RESET)

    else:
        # Custom material
        specific_heat_capacity = None
        print(GREEN + "Custom material selected." + RESET)

        while specific_heat_capacity is None:
            specific_heat_capacity = convert_input("Enter specific heat capacity (J/kgK or J/gK): ")

    if material_choice == "1":
        specific_heat_capacity = 500
        print(GREEN + "Using preset: Steel (500 J/kgK)" + RESET)

    elif material_choice == "2":
        specific_heat_capacity = 900
        print(GREEN + "Using preset: Aluminium (900 J/kgK)" + RESET)

    elif material_choice == "3":
        specific_heat_capacity = 4180
        print(GREEN + "Using preset: Water (4180 J/kgK)" + RESET)

    elif material_choice == "4":
        specific_heat_capacity = 1700
        print(GREEN + "Using preset: Wood (1700 J/kgK)" + RESET)

    else:
        print(CYAN + "\nCustom material selected." + RESET)
        specific_heat_capacity = None
        while specific_heat_capacity is None:
            specific_heat_capacity = convert_input(
                "Enter specific heat capacity (J/kgK or J/gK): ")

    convective_heat_transfer = None
    while convective_heat_transfer is None:
        convective_heat_transfer = convert_input(
            "Enter convective heat transfer coefficient h (W/m2K, W/cm2K, or kW/m2K): ")

    surface_area = None
    while surface_area is None:
        surface_area = convert_input("Enter surface area (m2 or cm2): ")

    mass = None
    while mass is None:
        mass = convert_input("Enter mass (kg or g): ")

    if convective_heat_transfer > 5000 or surface_area > 50 or mass > 500:
        print(YELLOW + "\nWarning: One or more values are unusually high." + RESET)
        cont = input("Continue anyway? (y/n): ").lower()
        if cont != "y":
            print(RED + "Calculation cancelled." + RESET)
            return

    k_value = convective_heat_transfer * surface_area / (mass * specific_heat_capacity)

    print(CYAN + "\nCalculating cooling constant k..." + RESET)
    print(GREEN + f"\nEstimated thermal conductivity constant k = {k_value:.5f} 1/min" + RESET)

    input(CYAN + "\nPress Enter to return to the menu..." + RESET)

def open_saved_results_file():
    """
       Display the contents of the cooling log file.

       Attempts to open 'cooling_log.txt' and print its contents.
       If the file does not exist, an error message is shown.

       Returns:
           None
    """

    try:
        with open('cooling_log.txt', 'r') as file:
            content = file.read()

            print(CYAN + "\n----- Saved Cooling Log -----\n" + RESET)
            if not content.strip():
                print(YELLOW + 'Log file is empty.' + RESET)
            else:
                print(content)

            print(file.read())
            print(CYAN + "\n-----------------------------\n" + RESET)
    except FileNotFoundError:
        print(RED + "\nNo log file found. Run a calculation first." + RESET)

    input(CYAN + '\nPress Enter to return to the menu...' + RESET)

def clear_log():
        """
            Clear all contents of the cooling log file.

            Overwrites 'cooling_log.txt' with an empty file and confirms the action
            to the user.

            Returns:
                None
        """

        with open('cooling_log.txt', 'w') as file:
            file.write(CYAN + "=== COOLING LOG FILE ===\n\n" + RESET)

        print(GREEN + '\nLog file cleared.' + RESET)

        input(CYAN + '\nPress Enter to return to the menu...' + RESET)

def about_menu():
        print(CYAN + "\n--- ABOUT / HELP MENU ---\n" + RESET)
        print(CYAN + "1. What is the Law of Cooling?" + RESET)
        print(CYAN + "2. Typical values for h, A, m, and c" + RESET)
        print(CYAN + "3. How do you estimate the cooling constant?" + RESET)

        choice = input(CYAN + "\nChoose an option (1-3): " + RESET)
        print()  # spacing

        if choice == "1":
            print(CYAN +

("Newton’s Law of Cooling describes how quickly an object changes temperature\n"
"when placed in an environment with a different temperature.\n\n"
"Key idea:\n"
"The bigger the temperature difference, the faster the object cools (or heats).\n\n"
"The cooling rate is proportional to the difference between:\n"
"- the object's temperature\n"
"- the surrounding temperature\n\n"
"So if something is very hot in a cool room, it cools quickly at first.\n"
"As it approaches room temperature, cooling slows down.") + RESET)

        elif choice == "2":
           print(CYAN +

("""Typical values:
Convective heat transfer coefficient (h):
- Air (natural convection): 5–25 W/(m²·K)
- Air (fan/wind): 10–200 W/(m²·K)
- Water (moving): 50–10000 W/(m²·K)

Surface area (A):
- Small objects: 0.001–0.1 m²
- Medium objects: 0.1–2 m²
- Large objects: 2–10 m²

Mass (m):
- Small objects: 0.01–1 kg
- Medium objects: 1–20 kg
- Large objects: 20–200 kg

Specific heat capacity (c):
- Metals: 400–900 J/(kg·K)
- Plastics: 1000–2000 J/(kg·K)
- Wood: 1500–2500 J/(kg·K)
- Water: 4180 J/(kg·K)""") + RESET)

        elif choice == "3":
            print(CYAN +

"""The cooling constant k tells you how quickly an object cools in a given environment.

Formula:
    k = (h * A) / (m * c)

Where:
- h = convective heat transfer coefficient
- A = surface area
- m = mass
- c = specific heat capacity

Meaning:
- Larger h or A → heat escapes faster → k increases
- Larger m or c → object stores more heat → k decreases

This formula balances:
- how easily heat escapes
- how much heat the object holds
into one constant.""" + RESET)

        else:
            print(RED + "Invalid choice. Returning to menu." + RESET)

        input(CYAN + "\nPress Enter to return to the menu..." + RESET)


startup_banner()

# Main program loop

while True:
    choice = menu()

    if choice == '1':
        calculate_cooling_time()
    elif choice == '2':
        explain_equation()
    elif choice == '3':
        estimate_k_from_material_and_size()
    elif choice == '4':
        open_saved_results_file()
    elif choice == '5':
        clear_log()
    elif choice =='6':
        about_menu()
    elif choice == '7':
        print(CYAN + '\nExiting program . . .' + RESET)
        break
    else:
        print(RED + '\nInvalid option.' + RESET)


