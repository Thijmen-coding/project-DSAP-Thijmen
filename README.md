# DSAP25 – The Decay of Predictive Trading Signals  
Author: Thijmen de Rooij  
Course: Data Science and Advanced Programming (2025)  
Repository: project-DSAP-thijmen  

---

## Project Overview
This project studies how quickly the predictive power of short-term trading signals decays once released.  
Financial markets absorb information over time; execution delays can erode profitability.  
The project simulates how average returns change when a momentum-based signal is executed with delays of 0, 1, 2, and 5 days.  

---

## Folder Structure
```
project-DSAP-Thijmen/
├── data/                     # Folder for raw and processed datasets (e.g., stock prices)
│
├── notebooks/                # Jupyter notebooks for running and visualizing experiments
│   └── analysis.ipynb
│
├── sourcecode/               # Python source code implementing the signal decay logic
│   └── signal_decay.py
│
├── tests/                    # Unit tests to verify code correctness
│   └── test_signal.py
│
├── .gitignore                # Git configuration file to ignore unnecessary files
├── main.py                   # Entry point script to run the full analysis
├── README.md                 # Project documentation
└── requirements.txt          # List of dependencies required to run the project
```
