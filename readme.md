# Expense Calculator

A simple and efficient Python-based command-line interface (CLI) tool designed to help you track, manage, and visualize your daily expenses. Data is securely stored using a local SQLite database, ensuring your records persist between sessions.

## Features

- **Add Expenses**: Quickly record new expenses with amount, category, and date.
- **View All Expenses**: Display a list of all recorded transactions directly in the terminal.
- **Data Persistence**: Uses `sqlite3` to store data locally in `expenses.db`.
- **Export to CSV**: Easily export your expense data to a CSV file (`expenses.csv`) for use in Excel or other tools.
- **Visualization**: Generate bar charts to visualize total expenses by category using `matplotlib`.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Matplotlib**: A plotting library for Python.

## Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone <repository-url>
   cd expence_calculator
   ```

2. **Install dependencies**:
   This project requires `matplotlib` for the graphing feature.
   ```bash
   pip install matplotlib
   ```

   *Note: `sqlite3` and `csv` are part of the Python standard library and do not require separate installation.*

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Interact with the Menu**:
   Once running, you will see the following options:

   ```
   1. Add Expense
   2. Show Expenses
   3. Export to CSV
   4. Plot Expenses by Category
   5. Exit
   ```

   - **Add Expense**: Enter the numeric amount, text category (e.g., Food, Travel), and date (YYYY-MM-DD).
   - **Show Expenses**: Prints all records from the database.
   - **Export to CSV**: Saves all database records to `expenses.csv` in the current directory.
   - **Plot Expenses**: Opens a popup window displaying a bar chart of expenses aggregated by category.

## Project Structure

- `main.py`: The core application logic, database handling, and CLI interface.
- `expenses.db`: (Auto-generated) SQLite database file storing your data.
- `expenses.csv`: (Auto-generated) output file when exporting data.
- `readme.md`: Project documentation.

## Database Schema

Table Name: `expenses`

| Column   | Type    | Description |
| :------- | :------ | :---------- |
| id       | INTEGER | Primary Key |
| amount   | REAL    | Cost value  |
| category | TEXT    | Type of expense |
| date     | TEXT    | Date of transaction |

## License

This project is open-source and available for personal use and modification.
