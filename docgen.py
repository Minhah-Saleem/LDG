#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import openai

st.title("LDG using ChatGPT")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to generate legal documents with 
       the OpenAI API's implementation of the ChatGPT model.
       Click on a document type button to generate the document. Once the document type 
       is selected, provide the necessary information in the text boxes to generate the document.
       '''
    )

model_engine = "text-davinci-003"
openai.api_key = "Your API key"

document_types = {
    "Last Will and Testament Template": {
        "Your Name": "[Your Name]",
        "Your Address": "[Your Address]",
        "Distribution of Assets": "[Distribution of Assets]",
        "Appointment of Guardians": "[Appointment of Guardians]",
        "Date": "[Date]"
    },
    "Trust Agreement Template": {
        "Your Name": "[Your Name]",
        "Your Address": "[Your Address]",
        "Trustee Name": "[Trustee Name]",
        "Trust Property": "[Trust Property]",
        "Terms and Conditions": "[Terms and Conditions]",
        "Date": "[Date]"
    },
    "Contract Template": {
        "Party1 Name": "[Party1 Name]",
        "Party1 Address": "[Party1 Address]",
        "Party2 Name": "[Party2 Name]",
        "Party2 Address": "[Party2 Address]",
        "Contract Terms": "[Contract Terms]",
        "Date": "[Date]"
    },
    "Power of Attorney Template": {
        "Principal Name": "[Principal Name]",
        "Principal Address": "[Principal Address]",
        "Attorney Name": "[Attorney Name]",
        "Attorney Address": "[Attorney Address]",
        "Powers Granted": "[Powers Granted]",
        "Limitations": "[Limitations]",
        "Start Date": "[Start Date]",
        "End Date": "[End Date]",
        "Successor Agent Name": "[Successor Agent Name]",
        "Jurisdiction": "[Jurisdiction]",
        "Date": "[Date]"
    },
    "Real Estate Purchase Agreement Template": {
        "Buyer Name": "[Buyer Name]",
        "Seller Name": "[Seller Name]",
        "Property Address": "[Property Address]",
        "Purchase Price": "[Purchase Price]",
        "Date": "[Date]"
    },
    "Employment Agreement Template": {
        "Employer Name": "[Employer Name]",
        "Employer Address": "[Employer Address]",
        "Employee Name": "[Employee Name]",
        "Employee Address": "[Employee Address]",
        "Employment Terms": "[Employment Terms]",
        "Salary": "[Salary]",
        "Benefits": "[Benefits]",
        "Date": "[Date]"
    },
    "Articles of Incorporation Template": {
        "Company Name": "[Company Name]",
        "Company Address": "[Company Address]",
        "Shareholders": "[Shareholders]",
        "Directors": "[Directors]",
        "Purpose of the Company": "[Purpose of the Company]",
        "Date": "[Date]"
    },
    "Intellectual Property Assignment Agreement Template": {
        "Assignor Name": "[Assignor Name]",
        "Assignor Address": "[Assignor Address]",
        "Assignee Name": "[Assignee Name]",
        "Assignee Address": "[Assignee Address]",
        "Intellectual Property Description": "[Intellectual Property Description]",
        "Effective Date": "[Effective Date]",
        "Jurisdiction": "[Jurisdiction]",
        "Date": "[Date]"
    },
    "Divorce Settlement Agreement Template": {
        "Husband Name": "[Husband Name]",
        "Husband Address": "[Husband Address]",
        "Wife Name": "[Wife Name]",
        "Wife Address": "[Wife Address]",
        "Property Division": "[Property Division]",
        "Child Custody": "[Child Custody]",
        "Visitation Rights": "[Visitation Rights]",
        "Spousal Support": "[Spousal Support]",
        "Date": "[Date]"
    },
    "Legal Complaint Template": {
        "Plaintiff Name": "[Plaintiff Name]",
        "Plaintiff Address": "[Plaintiff Address]",
        "Defendant Name": "[Defendant Name]",
        "Defendant Address": "[Defendant Address]",
        "Claims": "[Claims]",
        "Legal Arguments": "[Legal Arguments]",
        "Relief Sought": "[Relief Sought]",
        "Jurisdiction": "[Jurisdiction]",
        "Date": "[Date]"
    },
    "Other":{
        "user_query": "Enter query here:"
    }
    # Add more document types and their corresponding required information here
}
countries = {
    "Afghanistan": "Afghanistan",
    "Albania": "Albania",
    "Algeria": "Algeria",
    "Argentina": "Argentina",
    "Australia": "Australia",
    "Austria": "Austria",
    "Belgium": "Belgium",
    "Brazil": "Brazil",
    "Canada": "Canada",
    "China": "China",
    "Colombia": "Colombia",
    "Croatia": "Croatia",
    "Cuba": "Cuba",
    "Czech Republic": "Czech Republic",
    "Denmark": "Denmark",
    "Egypt": "Egypt",
    "Finland": "Finland",
    "France": "France",
    "Germany": "Germany",
    "Greece": "Greece",
    "Hungary": "Hungary",
    "India": "India",
    "Indonesia": "Indonesia",
    "Iran": "Iran",
    "Italy": "Italy",
    "Japan": "Japan",
    "South Korea": "South Korea",
    "Malaysia": "Malaysia",
    "Mexico": "Mexico",
    "Morocco": "Morocco",
    "Netherlands": "Netherlands",
    "New Zealand": "New Zealand",
    "Norway": "Norway",
    "Pakistan": "Pakistan",
    "Philippines": "Philippines",
    "Poland": "Poland",
    "Portugal": "Portugal",
    "Romania": "Romania",
    "Russia": "Russia",
    "Saudi Arabia": "Saudi Arabia",
    "Serbia": "Serbia",
    "Singapore": "Singapore",
    "South Africa": "South Africa",
    "Spain": "Spain",
    "Sweden": "Sweden",
    "Switzerland": "Switzerland",
    "Turkey": "Turkey",
    "Ukraine": "Ukraine",
    "United Arab Emirates": "United Arab Emirates",
    "United Kingdom": "United Kingdom",
    "United States": "United States"
}

language_options = {
    "Pashto": "Pashto",
    "Albanian": "Albanian",
    "Arabic": "Arabic",
    "Spanish": "Spanish",
    "English": "English",
    "German": "German",
    "Dutch": "Dutch",
    "Portuguese": "Portuguese",
    "Chinese (Mandarin)": "Chinese (Mandarin)",
    "Croatian": "Croatian",
    "Czech": "Czech",
    "Danish": "Danish",
    "Finnish": "Finnish",
    "French": "French",
    "Greek": "Greek",
    "Hungarian": "Hungarian",
    "Hindi": "Hindi",
    "Indonesian": "Indonesian",
    "Persian": "Persian",
    "Italian": "Italian",
    "Japanese": "Japanese",
    "Korean": "Korean",
    "Malay": "Malay",
    "Norwegian": "Norwegian",
    "Urdu": "Urdu",
    "Filipino": "Filipino",
    "Polish": "Polish",
    "Romanian": "Romanian",
    "Russian": "Russian",
    "Serbian": "Serbian",
    "Swedish": "Swedish",
    "Turkish": "Turkish",
    "Ukrainian": "Ukrainian"
}


def main():
    document_type = st.sidebar.radio("Select a document type:", list(document_types.keys()))
    if document_type != "Other":
        generate_document(document_types[document_type],document_type)
    else:
        user_query = st.text_input("Enter query here:", "")
        if user_query:
            response = ChatGPT(user_query)
            st.subheader("Generated Document")
            st.write(response)
            f_name = st.text_input("Enter file name to save the document:", "")
            if f_name != "":
                save_response_as_file(response, f_name)


def ChatGPT(user_query):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_query,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response


def generate_document(required_info, document_type):
    st.subheader("Document Information")
    document_info = {}
    for info_name, info_label in required_info.items():
        document_info[info_name] = st.text_input(info_label, "")
    
    country = st.selectbox("Select country:", list(countries.keys()))
    language = st.selectbox("Select language:", list(language_options.keys()))
    
    if all(document_info.values()):
        if country and language:
            # Generate the document using the provided information and selected language
            document = generate_legal_document(document_type, document_info, language_options[language], countries[country])
            response = ChatGPT(document)
            st.subheader("Generated Document")
            st.write(response)
            f_name = st.text_input("Enter file name to save the document:", "")
            if f_name != "":
                save_response_as_file(response, f_name)


def generate_legal_document(document_type, info, language, country):
    # Generate the legal document using the provided information and selected language
    # You can write your logic here to generate the document
    # This is just a placeholder implementation
    document = f"Generate {document_type} according to the laws of {country} in {language}:\n\n{info}"
    return document


def save_response_as_file(response, file_name):
    with open(file_name, "w") as f:
        f.write(response)
    st.write(f"Response saved as file: {file_name}")


if __name__ == "__main__":
    main()


# In[ ]:




