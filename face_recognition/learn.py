import numpy as np
from IPython.display import display
from PIL import Image, ImageDraw

import face_recognition
from list import convert


def learn():
    names, images = convert()

    # This is an example of running face recognition on a single image
    # and drawing a box around each person that was identified.

    """
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("curry.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("james.jpg")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    """

    # Create arrays of known face encodings and their names
    known_face_encodings = []


    for i in range(len(images)):
        image = face_recognition.load_image_file(f'img_learn/{images[i]}')
        image_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_encoding)


    known_face_names = names
    print('Learned encoding for', len(known_face_encodings), 'images.')
    return known_face_encodings, known_face_names
