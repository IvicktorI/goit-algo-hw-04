from pathlib import Path
from colorama import Fore

def show_all(directories,n=0):
    path = Path(directories)
    if path.exists():
        if path.is_dir():
            print(('  ')*n,end='')
            print(Fore.YELLOW+path.name)
            temp_list=path.glob('*')
            n+=1
            for el in temp_list:
                show_all(el.resolve(),n)
        if path.is_file():
            print(('  ')*n,end='')
            print(Fore.GREEN+path.name)
    else:
        print('Directories not found')
    

show_all('C:\python\go-it\goit-algo-hw-04')