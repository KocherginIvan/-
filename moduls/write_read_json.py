import json
def create_json(dictionary, name):
    with open(f'{name}.json', 'w', encoding='utf-8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)

def read_data_json(name):
    with open(f'{name}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

