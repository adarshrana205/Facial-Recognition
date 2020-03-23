# Single user with a picture
import face_recognition

# Load the jpg file
image1 = face_recognition.load_image_file("/home/adarshrana205/Desktop/known_people/Adarsh.jpeg")

# Find all the faces that appear in a picture:
# face_locations=face_recognition.face_locations(image)

# manipulate facial features in pictures
# face_landmarks_list = face_recognition.face_landmarks(image)

# Encode the face parameters
image1_face_encoding = face_recognition.face_encodings(image1)[0]

# Load the image
image2 = face_recognition.load_image_file("/home/adarshrana205/Desktop/unknown_people/Adarsh1.jpeg")
# Encode the face parameters
image2_face_encoding = face_recognition.face_encodings(image2)[0]

# Create a list of known face encodings and their names
known_face_encodings = [image1_face_encoding,image2_face_encoding]

# Create list of the name matching with the position of the known_face_encodings
known_face_names = ["User One","User Two"]
