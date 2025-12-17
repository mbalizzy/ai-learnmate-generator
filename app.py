import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")

templates = {
    "Quiz Generator": (
        "Create 5 multiple-choice questions about {topic} for {level} learners.\n"
        "Each question must have options A), B), C), D).\n"
        "Mark the correct answer by appending ' **' at the end of that option.\n"
        "Use only real, accurate facts. No explanations."
    ),
    "Lesson Summary": (
        "Write a clear summary of {topic} for {level} learners using bullet points."
    ),
    "Explain with Analogy": (
        "Explain {topic} to a {level} learner using a simple analogy, then give a short technical explanation."
    )
}

topic_options = [
    "Artificial Intelligence", "Machine Learning", "Deep Learning",
    "Neural Networks", "Natural Language Processing", "Computer Vision",
    "AI Ethics", "Large Language Models"
]

def generate(topic, level, template_name):
    if not topic:
        return "Please select a topic."

    prompt = templates[template_name].format(topic=topic, level=level.lower().capitalize())
    result = generator(prompt, max_length=512, do_sample=False)[0]["generated_text"]
    return result

with gr.Blocks(title="AI LearnMate Content Generator") as demo:
    gr.Markdown("# 🤖 AI LearnMate Content Generator")
    gr.Markdown("Generate quizzes, summaries, and analogies without pasting context.")

    with gr.Row():
        topic = gr.Dropdown(topic_options, label="Topic", value="Natural Language Processing")
        level = gr.Dropdown(["Beginner", "Intermediate", "Advanced"], label="Level", value="Beginner")
        template_choice = gr.Dropdown(list(templates.keys()), label="Template", value="Quiz Generator")

    generate_btn = gr.Button("Generate Content", variant="primary")
    output = gr.Textbox(label="Generated Content", lines=20)

    generate_btn.click(generate, inputs=[topic, level, template_choice], outputs=output)

demo.launch()
