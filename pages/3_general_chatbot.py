import streamlit as st
from ollama import Client
from ollama import chat
st.title("General Q&A chatbot")


####################################################################
# Model selector
####################################################################
model_options = {
    "gemma3n:e4b": "gemma3n:e4b",
    "gemma3n:e2b": "gemma3n:e2b"

}
selected_model = st.sidebar.selectbox(
    "Select a model",
    options=list(model_options.keys()),
    index=0,
    key="model_selector",
)
model_id = model_options[selected_model]
print(f"Selected model: {model_id}")
####################################################################
# Add a grade level selector to the sidebar
####################################################################
grade_levels = {
    "1st Grade": "1st Grade",
    "2nd Grade": "2nd Grade",
    "3rd Grade": "3rd Grade",
    "4th Grade": "4th Grade",
    "5th Grade": "5th Grade",
    "6th Grade": "6th Grade",
    "7th Grade": "7th Grade",
    "8th Grade": "8th Grade",
    "9th Grade": "9th Grade",
    "10th Grade": "10th Grade",
    "11th Grade": "11th Grade",
    "12th Grade": "12th Grade"
}
selected_grade = st.sidebar.selectbox(
    "Select a grade level",
    options=list(grade_levels.keys()),
    index=0,
    key="grade_selector",
)
grade_level = grade_levels[selected_grade]
print(f"Selected grade level: {grade_level}")


#####################################################################
# New chat session button 
#####################################################################
if st.sidebar.button("Start a new chat"):
    st.session_state.messages = []
    st.session_state["ollama_model"] = model_id



if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = model_id

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Initialize the system prompt with the selected grade level
        messages = [
            {"role": "system", "content": f"You are a helpful assistant for a {grade_level} student."},
            
        ]
        messages.extend({"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages)
        stream = chat(
            model=model_id,
            messages= messages,
            stream=True,
        )
        def content_generator():
            for chunk in stream:
                yield chunk['message']['content']
        response = st.write_stream(content_generator())

    st.session_state.messages.append({"role": "assistant", "content": response})