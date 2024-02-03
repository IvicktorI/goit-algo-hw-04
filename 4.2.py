path='cats.txt'

def get_cats_info(path):

    try:
        with open(path, "r", encoding='utf-8') as f:
            cats=[el.strip() for el in f.readlines()]
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return (f"Error: {e}")
    
    cats_info=[]
    try:
        for i in cats:
            temp=[]
            temp=i.split(',')
            cats_info.append({'id':temp[0],'name':temp[1],'age':temp[2]})
        return  cats_info
    except Exception:
        return 'File is empty'

print(get_cats_info(path))
    