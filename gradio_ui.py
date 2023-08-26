import gradio as gr

from untils import generate_response, set_user_query

def demo_func() -> tuple:
    return '', []

with gr.Blocks() as demo:
    chatbot = gr.components.Chatbot(label='Openai Assistant')
    msg = gr.components.Text(label='Input query')
    clear = gr.components.Button(value='Clear', variant='stop')

    msg.submit(
        fn=set_user_query,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    ).then(
        fn=generate_response,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )

    clear.click(fn=demo_func, inputs=[], outputs=[msg, chatbot])
