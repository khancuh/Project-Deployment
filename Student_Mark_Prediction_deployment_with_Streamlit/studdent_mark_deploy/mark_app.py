import numpy as np
import pickle
import streamlit as st

# loading the saved model 
model = pickle.load(open("lr_model.pkl",'rb')) 
# creating a function for prediction 
def marks_prediction(input_data):      
    # changing data to numpy array 
    input_data_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped =  input_data_array.reshape(1,-1)
    temp = np.array(input_data_reshaped, dtype=float)
    
    # Main function 
    result = model.predict(temp)
    
    
    strr = "Marks Predicted : "
    temp = [strr]
    temp2 = [result[0][0]]
    
    merged_list = temp + temp2

    # Convert the merged list to a string without brackets and commas
    merged_str = "  ".join(str(item) for item in merged_list)
    
    
    if result[0]>100: 
        return 100
    elif (result[0] >= 0 and result[0]<=100):
        return merged_str
    else:
      return "Invalid Input "
    

def main():
    # giving a title 
    #st.title('')
    st.markdown("<h1 style='text-align: center; color: green;'>Student Marks Prediction </h1>", unsafe_allow_html=True)
    
    # getting the input data from input user
    
    Hours = st.text_input("Enter the number of hour of actually study (range between 1-13 for correct prediction)  ")
    
    
    # code for prediction 
    prediction = '' # null string 
    
    
    # creating a button for prediction 
    if st.button('Result Submit'):  
        prediction = marks_prediction([Hours])
        
    st.success(prediction)
    
    st.markdown("***")
    
    st.markdown("""
    About the data to be filled : 
        
        Hours : As number of hours of study before exams is positively correlated 
        with marks obtained by students so more hours of study genrally gives more 
        marks (exception exists like us 💀) and if you found your marks wrong then 
        go and BLAME your teacher 🙃
        """) 
    st.write(" \n\n\n\n\n\n")
    st.markdown("******")
    
    st.write("Creater : [Imran Khan] ")
if __name__ == '__main__':
    main()
    
    