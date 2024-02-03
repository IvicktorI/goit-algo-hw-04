from pathlib import Path
from colorama import Fore
import sys

def show_all(directories,n=0):
    path = Path(directories)
    if path.exists():
        if path.is_dir():
            print(('  ')*n,end='')
            print(Fore.YELLOW+path.name+Fore.WHITE)
            temp_list=path.glob('*')
            n+=1
            for el in temp_list:
                show_all(el.resolve(),n)
        if path.is_file():
            print(('  ')*n,end='')
            print(Fore.GREEN+path.name+Fore.WHITE)
    else:
        print('Directories not found')

def main():
    try:
        path=sys.argv[1]
        show_all(path)
    except Exception:
        print('Incorect path')
    
if __name__ == "__main__":
    main()
