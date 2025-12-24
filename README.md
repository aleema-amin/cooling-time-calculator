## 🌡️ Cooling Time Calculator  
*A Python tool for modelling real‑world cooling using Newton’s Law of Cooling*

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📘 Overview

This project is a command‑line Python application that calculates how long it takes for an object to cool in a given environment. It uses Newton’s Law of Cooling, allows users to estimate the cooling constant k, provides material presets, logs results to a file, and includes a full help/“About” menu explaining the physics behind the calculations.

This tool is designed for students, engineers, and anyone exploring thermodynamics in a practical, interactive way.

## ✨ Features

- **Cooling Time Calculator** — Computes cooling time using Newton's Law of Cooling  

- **Estimate Cooling Constant (k)** using material presets or custom values for:  
  - mass  
  - surface area  
  - specific heat capacity  
  - convective heat transfer coefficient  

- **About Menu** — Includes explanations of:  
  - Newton's Law of Cooling  
  - Typical values of *h*, *A*, *m*, *c*  
  - How to estimate the cooling constant *k*  

- **Material Presets** — Choose from steel, aluminium, water, wood, or enter custom values  

- **Logging System** — Saves each calculation with:  
  - inputs  
  - results  
  - timestamps  

- **Clear Log Option** — Reset the saved results file from the menu  

- **Coloured CLI Interface** — Clean, readable, user‑friendly terminal output  

## 🧩 Technical Highlights

- Implements exponential decay modelling  
- Uses rearranged Newton’s Law of Cooling to solve for time  
- Includes physics‑based estimation of the cooling constant *k*  
- Uses file I/O for persistent logging with timestamps  
- Includes robust input validation and error handling  
- Menu‑driven CLI with clean, readable formatting  

## 📊 Program Flowchart
```
+-----------------------------+
|          START              |
+--------------+--------------+
               |
               v
+-----------------------------+
|   Display Main Menu         |
|   (1–7 options)             |
+--------------+--------------+
               |
               v
+-----------------------------+
|  Get user choice (1–7)      |
+--------------+--------------+
               |
               v
        +------+------+
        |             |
        v             v
 +----------------+  +----------------------+
 |  Choice == 1   |  |  Choice == 2–6      |
 |  Calculate     |  |  Other menu options |
 |  Cooling Time  |  |  (Learn, Estimate k,|
 +-------+--------+  |  Open/Clear Log,    |
         |           |  About)             |
         |           +----------+----------+
         |                      |
         |                      v
         |           +-----------------------------+
         |           | Perform selected action     |
         |           | (show info / compute /     |
         |           | open file / clear log)     |
         |           +-------------+--------------+
         |                         |
         |                         v
         |              +------------------------+
         |              | Return to Main Menu    |
         |              +-----------+------------+
         |                          ^
         |                          |
         v                          |
+-----------------------------+     |
|  Cooling Time Workflow      |     |
+-----------------------------+     |
|  • Ask for inputs OR        |     |
|    use real-world preset    |     |
|  • Validate inputs          |     |
|  • Compute cooling time     |     |
|  • Let user choose units    |     |
|    (minutes/seconds/hours)  |     |
|  • Ask: show graph (y/n)?   |     |
|  • If yes: plot graph       |     |
|  • Log inputs + results     |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Return to Main Menu        |
+-------------+---------------+
              ^
              |
      +-------+--------+
      | Choice == 7    |
      | Exit Program   |
      +-------+--------+
              |
              v
+-----------------------------+
|            END              |
+-----------------------------+
```
## 🖥️ Demo Output

```
+------------------------------+
|          MAIN MENU           |
+------------------------------+

1. Calculate Estimated Cooling Time
2. Learn Cooling Time Equation
3. Estimate k from Material and Size
4. Open Saved Results File
5. Clear Log File
6. About Menu
7. Exit Program

Choose an option (1-7):
```

## 📸 Screenshots

### Main Menu
![Main Menu Screenshot](Main_Menu.png)

### Cooling Time Calculation Example
![Cooling Time Calculation Example](Cooling_Time_Example.png)

### Estimate k from Material and Size Example
![Estimate k from Material and Size Example](Estimating_k_from_Material_and_Size_Example.png)

## 🌍 Why This Project Matters

Understanding cooling behaviour is essential in engineering fields such as:

- aerospace (thermal protection systems)  
- materials science  
- food safety  
- electronics cooling  
- environmental modelling  

This tool provides a simple, interactive way to explore real thermodynamic behaviour and understand how objects cool in real‑world environments.

## 🧠 The Science Behind It

This tool uses **Newton's Law of Cooling**, which models how an object cools relative to the temperature difference between the object and its surroundings.

### Core Equation

T(t) = T_env + (T_0 - T_env)e^-kt

Where:  
- T(t) = temperature at time t 
- T_0 = initial temperature  
- T_env = ambient temperature  
- k = cooling constant  
- t = time  

The program rearranges this equation to solve for time.

### Estimating the Cooling Constant

k = hA / mc

Where:  
- h = convective heat transfer coefficient  
- A = surface area  
- m = mass  
- c = specific heat capacity  

## ▶️ How to Run This Calculator

1. Install Python 3  
2. Download the `.py` file from this repository  
3. Open a terminal and run:  
   ```
   python cooling_time_calculator.py
   ```  
4. Use the menu to navigate through the program  

## 🔧 Future Improvements

- Add graphing of temperature vs. time  
- Add GUI version using Tkinter or PyQt  
- Add more material presets  
- Add unit conversion options  
- Add error bars or uncertainty estimation  

## 📂 Repository Structure

```
cooling-time-calculator/
│
├── cooling_time_calculator.py   # Main program
├── .gitignore                   # Python ignore rules
├── LICENSE                      # MIT License
└── README.md                    # Project documentation
```

## 👤 Author

Created by **Aleema Amin**  
High Wycombe, UK

## 📄 License

This project is licensed under the **MIT License**, allowing free use, modification, and distribution with attribution.
