import json

with open(r'D:/КАНДИДАТСКАЯ ДИССЕРТАЦИЯ/Helpfull Demos/mecano/data/waste/train/coco_annotations.json', 'r') as f:
    json_data = json.load(f)
    
print(json.dumps(json_data, indent=2))