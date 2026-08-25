import gradio as gr

from app.sql_service import ask_database


def main():
    with gr.Blocks() as demo:
        gr.Markdown("# Mini AI SQL Assistant")
        question = gr.Textbox(
            label="Ask in plain English",
            placeholder="Example: What are the top customers by revenue?"
        )
        button = gr.Button("Run")
        status = gr.Markdown()
        sql = gr.Code(label="SQL", language="sql")
        results = gr.Dataframe(label="Results")
        answer = gr.Markdown(label="Answer")

        button.click(
            fn=ask_database,
            inputs=question,
            outputs=[status, sql, results, answer],
        )

    demo.launch()


if __name__ == "__main__":
    main()
