import streamlit as st
from helper.calculating_graduation_year_helper import calGraduationYear
from helper.placement_prediction_helper import predict_placement
import json
import os


def get_model_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(current_dir, 'model', filename)
    return model_dir


def main():
    st.title('Graduation Year Prediction')

    # Input fields
    current_year = st.number_input('Enter Current Year', min_value=2000, max_value=2100, step=1)
    academic_year = st.selectbox('Select Course Duration (in Years)', [1, 2, 3, 4])
    current_ay = st.selectbox('Select Current Year in Course', [1, 2, 3, 4])

    # Calculate graduation year
    if st.button('Predict Graduation Year'):
        graduation_year = calGraduationYear(current_year, academic_year, current_ay)
        st.success(f'Predicted Graduation Year: {graduation_year}')

    # Input fields for placement prediction
    st.header('Placement Prediction')

    # Load college names from JSON file
    college_names_path = get_model_path('college_names.json')
    if os.path.exists(college_names_path):
        with open(college_names_path, 'r') as f:
            college_names = json.load(f)['college_names']
    else:
        st.error(f"College names JSON file '{college_names_path}' not found.")
        return

    # Dropdown for selecting college name
    college_name = st.selectbox('Select College Name', college_names)

    attending = st.radio('Are you attending college?', ('No', 'Yes'))
    attendee = 1 if attending == 'Yes' else 0
    cgpa = st.number_input('CGPA', min_value=1.0, max_value=10.0, step=0.1, format="%.1f")
    speaking_skill = st.select_slider('Speaking Skill Level', options=[1, 2, 3, 4, 5])
    ml_knowledge = st.select_slider('ML Knowledge Level', options=[1, 2, 3, 4, 5])

    # Make placement prediction
    if st.button('Predict Placement'):
        try:
            prediction = predict_placement(college_name, attendee, cgpa, speaking_skill, ml_knowledge)
            if prediction == 1:
                st.success('Placement Prediction: Placed')
            elif prediction == 0:
                st.markdown('<p style="background-color:red;color:white;padding:10px;border-radius:7px;">Placement Prediction: Not Placed</p>', unsafe_allow_html=True)
        except ValueError as e:
            st.error(str(e))


if __name__ == "__main__":
    main()
