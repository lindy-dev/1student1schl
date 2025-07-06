import streamlit as st
from ollama import chat, ChatResponse

def grade_essay(essay_qtn, essay_text, grade_level):
    grader_prompt = "You are an expert essay grader"
    grader_prompt += f" for {essay_qtn}. "
    grader_prompt += f" Your task is to grade the essay based on the provided question and text"
    grader_prompt += f" the essay text is {essay_text}"
    grader_prompt += f" the grade level is {grade_level}"

    response: ChatResponse = chat(model='gemma3n:e4b', messages=[
    {
        'role': 'user',
        'content': grader_prompt,
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    return response.message.content

st.set_page_config(
    page_title="Essay Feedback",
    page_icon="👋",
)

st.title("Essay Feedback")

# Input fields
essay_question = st.text_input("Essay Question")
essay_text = st.text_area("Essay Text", height=200)
grade_level = st.selectbox("Select Grade Level", ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])

# Submit button
if st.button("Submit"):
    essay_output_grade = grade_essay(essay_qtn=essay_question,essay_text=essay_text, grade_level=grade_level)
    st.success(f"Essay submitted for {grade_level}.")
    # st.text_area("Output", value=essay_output_grade, height=120, disabled=True)
    st.markdown(essay_output_grade, unsafe_allow_html=False)