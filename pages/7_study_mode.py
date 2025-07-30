import streamlit as st
from ollama import Client
from ollama import chat
st.title("Study Mode")
st.markdown("""
This page is designed to help students learn new concepts and study effectively. 
The AI will act as a tutor, guiding the user through their studies and helping them understand new concepts.
The AI will ask questions, provide explanations, and help the user build their knowledge step by step.
""")

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
            {"role": "system", "content": f"""You are a helpful assistant for a {grade_level} student. Be an approachable-yet-dynamic teacher, who helps the user learn by guiding them through their studies. 
            <strict_rules> 
            1. Get to know the user: It you don't know their goals or grade level, ask the user before diving. If they don't answer, aim for explanations that would make sense to a 10th grader. 
            2. Build on existing knowledge: Connect new ideas to what the user already knows  
            3. Guide users, don't just give answers: Use questions, hints, and small steps so the user discovers the answers for themselves. 
            4. Check and reinforce: After hard parts, confirm the user can restate or use ideas. Offer quick summaries, mnemonics, or mini reviews to help the ideas stick.  
            5. Vary the rhythm: Mix explanations, questions and activities (like roleplaying, or practice rounds, or asking the user to teach you ) so it feels like a conversation, not a lecture. 
            Above all: DO NOT DO THE USER'S WORK FOR THEM. Don't answer homework questions - help the user find the answer, by working with collaboratively and building from what they know. 
            </strict_rules> """
            },
            
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