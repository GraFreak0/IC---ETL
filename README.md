# IC - ETL: Automated Data Processing
## Overview
This program semi-automates a manual process that normally takes an estimated 5 hours to complete, reducing the processing time to under 6 minutes.

## Process Overview
The program is divided into two stages:

### Stage 1: Data Ingestion and Preparation
In this stage, the program:

- Loads/Extracts multiple CSV files
- Resolves encoding errors in the files
- Cleans and transforms the data
- Loads/Writes the files into categorized .csv files labeled as 'Inward' and 'Outward'

### Stage 2: Data Categorization
In this stage, the program:

- Loads the previously exported Inward and Outward .csv files
- Further breaks down the data into sub-categories for easier user understanding

## Getting Started
[Insert instructions on how to run the program, any dependencies required, and any other relevant information]

## Modules/Libraries utilized
- io
- os
- glob
- pandas
- pandasql
- datetime
- nbformat
- nbconvert

To install these Python modules, you can use the `pip` package manager. Open your terminal or command prompt and run the following commands:
```bash
pip install pandas pandasql nbformat nbconvert
```
For the other modules (`io`, `os`, `glob`, and `datetime`), they are part of the Python standard library, so you don't need to install them separately. You can directly import them in your Python scripts or Jupyter notebooks.
If you encounter any issues during installation or need further assistance, feel free to ask! 😊
