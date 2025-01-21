import torch
import gradio as gr
from transformers import pipeline

# If The model is not downloaded local machine use this.
# Path to the locally downloaded model
model_path = "../models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"

# Initialize the pipeline using the local model path
# text_summery = pipeline("summarization", model=model_path, torch_dtype=torch.bfloat16)

# If The model is not downloaded yet use this.
text_summery = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", torch_dtype=torch.bfloat16)


# Input text for summarization

# text = (
#     "Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman and political figure known "
#     "for his key roles in the space company SpaceX and the automotive company Tesla, Inc. who since "
#     "January 2025 has served as Administrator of the Department of Government Efficiency, under the "
#     "second Trump presidency. He is also known for his ownership of X Corp. (the company that operates "
#     "the social media platform X, formerly Twitter), and his role in the founding of the Boring Company, "
#     "xAI, Neuralink, and OpenAI. Musk is the wealthiest individual in the world; as of January 2025, Forbes "
#     "estimates his net worth to be US$421 billion."
# )

# Generate the summary
# summary = text_summery(text)
# print(summary)

def summery(input):
    output = text_summery(input)
    return output[0]['summary_text']

gr.close_all()

demo = gr.Interface(fn=summery,
                    inputs=[gr.Textbox(label="Input text to summarize", lines=6)],
                    outputs=[gr.Textbox(label="Summarized text", lines=4)],
                    title="@GenAIProject: Text Summarization",
                    description="Summarizes text using GenAI model")

demo.launch(share=True)