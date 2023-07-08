import streamlit as st
from streamlit_chat import message
from bardapi import Bard


#function to generate the output

# token is not to be shared 
token = 'xxxx'
st.session_state.something=''

def generate_response(prompt):
  bard=Bard(token=token)
  response =bard.get_answer(prompt)['content']
  return response


#Function to recieve user queries 
def get_text():
    input_text=st.text_input('Tutor Bot',placeholder="Write your text..",key='input' )
    return input_text

# with open('credentials.json', 'r') as f:
#     file = json.load(f)
#     token = file['token']

#This is title for the app
st.title('Personal Tutoring Bot 🤖')



#<div class="appview-container css-1wrcr25 e1g8pov66" data-testid="stAppViewContainer" data-layout="narrow">flex
#data-testid="stAppViewContainer"



st.markdown(
  '''

<style>

[data-testid="stAppViewContainer"]
{
    background-image:url('https://eskipaper.com/images/white-wallpaper-10.jpg');
    background-size:cover;
}

iframe > body, iframe,div.esravye2, .css-97ja1j , .e13qjvis2  {
        background-color: transparent !important;
}
.stTextInput{
  position:sticky;
  bottom:0;
}



</style>
'''

  , unsafe_allow_html=True)


if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

#Accepting user input 
user_input=get_text()
if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range (len(st.session_state['generated'])):
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True);
        message(st.session_state['generated'][i], key=str(i));

