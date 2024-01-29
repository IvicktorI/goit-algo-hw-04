import pathlib

path='salary.txt'

def total_salary(path):

    try:
        with open(path, "r") as f:
            employees=[el.strip() for el in f.readlines()]
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return (f"Error: {e}")
    

total_salary(path)