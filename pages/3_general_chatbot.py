import streamlit as st
from ollama import Client
from ollama import chat
st.title("General QA chatbot")


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
        # stream = client.chat.completions.create(
        #     model=st.session_state["ollama_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # )
        stream = chat(
            model=model_id,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        def content_generator():
            for chunk in stream:
                yield chunk['message']['content']
        response = st.write_stream(content_generator())

    st.session_state.messages.append({"role": "assistant", "content": response})