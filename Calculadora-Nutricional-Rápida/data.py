import json
resources = []
def read_json(name):
    try:
        with open(name,"r") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return [] 

def write_json(name,content):
    with open(name,"w") as file:
        json.dump(content,file,indent=4,ensure_ascii=False)
        
def load_data(name):
    resources.clear()
    resources.extend(read_json(name))
    return resources
def save_data(name):
    write_json(name,resources)