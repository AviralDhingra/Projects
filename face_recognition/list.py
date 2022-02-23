import json


def convert():
    with open('faces.json', "r") as f:
        faces = f.read()
    print(faces)
    faces = json.loads(faces)
    names = list(faces.keys())
    images = list(faces.values())
    return names, images
