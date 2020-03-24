# Compare with a picture

import face_recognition
import numpy as np
from face_recognizer1 import *
# Load a image
face_picture=face_recognition.load_image_file("/home/adarshrana205/Desktop/known_people/Adarsh.jpeg")
# Find all the faces that appear in a picture:
face_locations=face_recognition.face_locations(face_picture)
# Encode the faces
face_encodings=face_recognition.face_encodings(face_picture,face_locations)

# loop in all detected faces
for face_encoding in face_encodings:
    # if the face is a match for the known face
    matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
    # we will give name  unknown if the employee is not in the system
    name = "Unknown"
    # check the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    name = "Unknown"
    # check the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    # take the best one
    best_match_index = np.argmin(face_distances)
    # if we have a match:
    if matches[best_match_index]:
        # Give the detected face the name of the employee that match
        name = known_face_names[best_match_index]


