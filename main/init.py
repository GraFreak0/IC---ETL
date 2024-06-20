import os
import time
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, write
from nbformat.reader import NotJSONError

def execute_notebook(notebook_path):
    try:
        # Load the notebook
        with open(notebook_path, 'r') as f:
            nb = read(f, as_version=4)

        # Execute the notebook
        ep = ExecutePreprocessor(timeout=None, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

        # Save the executed notebook
        with open(notebook_path, 'w') as f:
            write(nb, f)
          
    except FileNotFoundError:
        print(f"Error: Notebook file '{notebook_path}' not found.")
    except NotJSONError as e:
        print(f"Error: Notebook file '{notebook_path}' does not appear to be JSON: {str(e)}")
    except Exception as e:
        print(f"Error executing notebook '{notebook_path}': {str(e)}")

def monitor_execution(notebook_name):
    base_dir = r'C:\Users\ijohnson\OneDrive - Ecobank Group\persona\PROJECTS\IC - NIP\main'
    notebook_path = os.path.join(base_dir, f'{notebook_name}.ipynb')
    execute_notebook(notebook_path)
    print(f'Execution of {notebook_name} notebook complete.')

if __name__ == '__main__':
    notebooks_to_run = ['inwardSuccessful', 'outwardSuccessful', 'finals']
    
    for notebook in notebooks_to_run:
        monitor_execution(notebook)
        print('Waiting for the next notebook to complete...')
        time.sleep(5)
    
    print('All notebooks executed successfully.')