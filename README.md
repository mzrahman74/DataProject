# Data Project with Python & Pandas

This project demonstrates data analysis and data manipulation using Python and the Pandas library.

## Prerequisites

- Python 3.14 or later
- pip

## Project Structure

```
dataProject/
│
├── .venv/              # Python virtual environment
├── data/               # Input datasets
├── output/             # Generated files
├── src                 # Main application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install Pandas manually:

```bash
pip install pandas
```

Then generate the requirements file:

```bash
pip freeze > requirements.txt
```

## Run the Project

```bash
python main.py
```

## Example

```python
import pandas as pd

df = pd.read_csv("data/sample.csv")

print(df.head())
print(df.describe())
```

## Common Pandas Operations

- Read CSV and Excel files
- Filter rows
- Select columns
- Handle missing values
- Group and aggregate data
- Merge DataFrames
- Sort data
- Export results to CSV or Excel

## Useful Commands

Check installed packages:

```bash
pip list
```

Deactivate the virtual environment:

```bash
deactivate
```

## Dependencies

- Python
- Pandas
- Matplotlib

Install additional libraries as needed:

```bash
pip install numpy openpyxl
```

## License

This project is for learning and educational purposes.
