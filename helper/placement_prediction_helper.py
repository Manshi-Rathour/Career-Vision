import numpy as np
import pickle
import json
import os


def get_model_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, '..', 'model', filename)
    return model_dir


# Load the model from pickle file
model_path = get_model_path('placement_prediction_model.pickle')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load columns information from JSON file
columns_path = get_model_path('columns_placement_prediction.json')
with open(columns_path, 'r') as f:
    columns = json.load(f)['data_columns']


def predict_placement(college, attendee, cgpa, speaking_skill, ml_knowledge):
    # Check if the college exists in the columns
    if college.lower() in columns:
        loc_index = columns.index(college.lower())  # Get the index of the college column
    else:
        raise ValueError(f"College '{college}' not found in columns.")

    # Prepare input data with named features
    x_ = np.zeros(len(columns))  # Create an array x_
    x_[0] = attendee
    x_[1] = cgpa
    x_[2] = speaking_skill
    x_[3] = ml_knowledge

    if loc_index >= 0:
        x_[loc_index] = 1  # Set the college column to 1

    # Make prediction
    prediction = model.predict([x_])[0]  # The output is in the form of an array so we take only the first element

    return prediction


if __name__ == "__main__":
    try:
        result = predict_placement('wilson college', 1, 8, 5, 5)
        print(f"Placement Prediction: {result}")
        result2 = predict_placement('GOVERNMENT POLYTECHNIC GANDHINAGAR', 1, 8, 5, 4)
        print(f"Placement Prediction2: {result2}")
        result3 = predict_placement('a. c. patil college of engineering', 1, 5, 3, 5)
        print(f"Placement Prediction3: {result3}")

    except ValueError as e:
        print(e)
