# Importing required packages
import streamlit as st
import openai

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "sk-z012321345656p['lk;lhkuhkyukgytjtkaeHfghghASDADSF" 

# Define a function to handle the translation process
def translate_text(text, target_language):
    # Define the prompt for the ChatGPT model
    prompt = f"You are a world reknown language translator with 70 years of experience in translating all languages. Translate '{text}' to {target_language}"
    
    # Generate the translated text using ChatGPT
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Extract the translated text from the response
    translated_text = response.choices[0].text.strip()
    
    return translated_text


# Define the main function that sets up the Streamlit UI and handles the translation process
def main():
    # Set up the Streamlit UI
    st.sidebar.header('Language Translation App')
    st.sidebar.write('Enter text to translate and select the target language:')
    
    # Create a text input for the user to enter the text to be translated
    text_input = st.text_input('Enter text')
    
    # Create a selectbox for the user to select the target language
    target_language = st.selectbox('Select language', ['Arabic', 'English', 'Spanish', 'French', 'German', 'Japanese', 'Italian', 'Korean', 'Russian', 'Yoruba', 'Igbo', "Medumba"])
    
    # Create a button that the user can click to initiate the translation process
    translate_button = st.button('Translate')
    
    # Create a placeholder where the translated text will be displayed
    translated_text = st.empty()
    
    # Handle the translation process when the user clicks the translate button
    if translate_button:
        translated_text.text('Translating...')
        translated_text.info(translate_text(text_input, target_language))
        

# Call the main function
if __name__ == '__main__':
    main()
