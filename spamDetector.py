import streamlit as st
import pickle

model = pickle.load(open('C:/Users/91749/OneDrive/Desktop/AICTE_SPAM_pro 11/AICTE_SPAM_pro/spam.pkl','rb'))
cv = pickle.load(open('C:/Users/91749/OneDrive/Desktop/AICTE_SPAM_pro 11/AICTE_SPAM_pro/vec.pkl','rb'))

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
                st.success("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")
        else:
            st.write("Please enter an email to classify")
main()
