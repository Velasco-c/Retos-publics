import json
resources = []

def read_json(name):
    import json

def read_json(name):
    try:
        with open(name, "r") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print("Error: The file does not contain valid JSON.")
        return []
    
def write_json(name,content):
    with open(name,"w") as file:
        json.dump(content,file,indent=False,ensure_ascii=False)
        
def load_data(name):
    resources.clear()
    resources.extend(read_json(name))
    return resources

def save_load(name):
    write_json(name,resources)
