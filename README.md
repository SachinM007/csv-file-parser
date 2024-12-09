
This project provides a CSV file parser that reads data from a CSV file and processes it in a meaningful way. The main functionality is to parse the file, handle errors, and provide results in a structured format. It also includes automated tests to ensure proper functionality.

## Features

- Parse CSV files with a flexible and efficient approach.
- Handle different types of data (strings, integers, floats).
- Handle CSV formatting errors gracefully (missing fields, malformed rows).
- Provide clear error messages for incorrect files.
- Test-driven development (TDD) approach with automated unit tests.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- `pip` for installing Python packages.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/csv-file-parser.git
   cd csv-file-parser
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   Install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the CSV file parser, follow these steps:

1. Prepare a CSV file to parse. The file should be structured with headers in the first row and data below it.

   Example `data.csv`:

   ```csv
   Name, Age, Salary
   John, 30, 50000
   Jane, 25, 55000
   ```

2. Use the following Python script to run the parser:

   ```bash
   python csv_parser.py path/to/your/csv-file.csv
   ```

   This command will read the CSV file, parse the contents, and print the parsed data in a structured format.

## Testing

The project includes automated tests to ensure the parser works as expected.

1. To run unit tests with pytest:

   ```bash
   pytest
   ```

2. To generate a coverage report:

   ```bash
   pytest --cov=csv_parser
   ```

3. To run mutation testing using `mutmut`:

   ```bash
   mutmut run --paths-to-mutate csv_parser.py
   ```

   After mutation testing, you can see the results with:

   ```bash
   mutmut results
   ```
