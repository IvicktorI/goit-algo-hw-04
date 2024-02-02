import pathlib, re

path='salry.txt'

def total_salary(path):

    try:
        with open(path, "r") as f:
            employees=[el.strip() for el in f.readlines()]
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return (f"Error: {e}")
    
    salary=[]
    for i in employees:
        salary.append(float(re.search(r'\d+',i).group()))

    try:
        return  (sum(salary),sum(salary)/len(salary))
    except Exception:
        return 'File is empty'
    
print(total_salary(path))
