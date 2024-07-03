import numpy as np
import pickle
import json


# Load the model from pickle file
with open('../model/placement_prediction_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load columns information from JSON file
with open('../model/columns_placement_prediction.json', 'r') as f:
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
