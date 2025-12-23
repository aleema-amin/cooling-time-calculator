Overview -

This project is a command‑line Python application that calculates how long it takes for 
an object to cool in a given environment. It uses Newton’s Law of Cooling, 
allows users to estimate the cooling constant k, provides material presets, 
logs results to a file, and includes a full help/“About” menu explaining 
the physics behind the calculations.
This tool is designed for students, engineers, and anyone exploring thermodynamics 
in a practical, interactive way.

Features -

- Cooling Time Calculator - Computes cooling time using Newton's Law of Cooling
- Estimate Cooling Constant (k) - Estimate k using material presets or custom values for:
   - mass
   - surface area
   - specific heat capacity
   - convective heat transfer coefficient
- About Menu - Includes explanations of:
   - Newton's Law of Cooling
   - Typical values of h, A, m, c
   - How to estimate the cooling constant k
- Material Presets - Choose from common materials (steel, aluminium, water, and wood) or enter
  custom values.
- Logging System - Saves each calcuation to a text file with:
   - inputs
   - results
   - timestamps
- Clear Log Option - Reset the saved results file from the menu.
- Coloured CLI Interface - Clean, readable, user-friendly terminal output.

The Science Behind It -

This tool uses Newton's Law of Cooling, which models how an object cools relative to the
temperature difference between the object and its surroundings.

The core equation:
                        T(t) = T_env + (T0 - T_env)e^-kt
Where:
- T(t) = temperature at time t
- T0 = initial temperature
- T_env = ambient temperature
- k = cooling constant
- t = time

The program rearranges this equation to solve for time.

You can also estimate k using:
                                    k = hA / mc
Where:
- h = convective heat transfer coefficient
- A = surface area
- m = mass
- c = specific heat capacity

How to Run this Calculator -

- Install Python 3
- Download the .py file from this repository
- Open a terminal and run: python cooling_time_calculator.py
- Use the menu to navigate throught the program

Repository Structure -

cooling-time-calculator/
│
├── cooling_time_calculator.py   # Main program
├── .gitignore                   # Python ignore rules
├── LICENSE                      # MIT License
└── README.md                    # Project documentation

Author -

Created by Aleema Amin
High Wycombe, UK

License -

This project is licensed under the MIT License, allowing free use, modification, and
distribution with attribution.
