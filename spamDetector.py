import streamlit as st
import pickle

model = pickle.load(open('spam123.pkl','rb '))
cv = pickle.load(open('vac.pkl','rb'))

def main():
    st.title("Email spam classification Aplication")
    st.write("This is a Machine Learning application to classify emails as spam or ham.")
    st.subheader("classification")
    user_input=st.text_area("Enter as email to classify" ,height=150)
    if st.button("classify"):
        if user_input:
            data=[user_input]
            print(data)
            vac=cv.transform(data).toarray()
            result=model.predict(vac)
            if result[0]==0:
                st.succes("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")
        else:
            st.write("Please enter an email to classify")
main()