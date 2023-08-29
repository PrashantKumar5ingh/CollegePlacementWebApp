# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 02:00:32 2023

@author: Lenovo
"""
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('D:/ML Projects/LogisticRegression/CollegePlacementPredictor/model.sav','rb'))

def predictor(input_data):
    
    input_data = np.array(input_data)
    input_data = input_data.reshape((1,-1))
    
    prediction = model.predict(input_data)
    print(prediction)
    if(prediction[0]==1):
        return "Placement: True"
    else:
        return "Placement: False"

def getNumericalForStream(stream):
    if(stream=='ECE'):
        return 2
    elif stream =='CSE':
        return 0
    elif stream =='IT':
        return 1
    elif stream =='CIVIL':
        return 4
    elif stream =='MECH':
        return 5
    else:   
        return 3
    
def getNumericalForGender(gender):
    if(gender=='Male'):
        return 1
    else:
        return 0

def getNumericalFor(x):
    if(x=='Yes'):
        return 1
    else:
        return 0

def main():
    
    st.title('Placement Prediction WebApp')
    #Age,Gender,Stream,Internships,CGPA,HistoryOfBacklogs,PlacedOrNot

    #getting input from user
    age = st.number_input('Age' , min_value=18, max_value=28)
    if age is not None and age < 18 or age > 28:
        st.error("Please enter an age between 18 and 28.")
        
    gender = st.radio("Gender",('Male','Female'))
    
    #with st.expander(label="Gender", expanded=False):
        #st.write("male")
        #st.write("female")'''
        
    stream = st.radio("Stream",('CSE','IT','ECE','EE','CIVIL','MECH'))
    
    
        
    internship = st.radio("Internship",('Yes','No'))
    
    cgpa = st.number_input('CGPA' , min_value=0,max_value=10)
    if cgpa is not None and cgpa < 0 or cgpa > 10:
        st.error("Please enter an age between 0 and 10.")
    
    backlog = st.radio('BackLog',('Yes','No'))
    
    
    # converting text to numerical
    gender = getNumericalForGender(gender)
    stream = getNumericalForStream(stream)
    internship = getNumericalFor(internship)
    backlog = getNumericalFor(backlog)
    
    #code for prediction
    result = ''
    
    #creating a button for prediction
    if st.button('Predict'):
        result = predictor([age,gender,stream,internship,cgpa,backlog])
        
    st.success(result)
    

if __name__ =='__main__':
    main()