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
