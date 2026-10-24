import gradio as gr
gr.close_all()

def greet(name, age, preference ,hobbies):
  return f"Name;{name}\nAge:{age}\nSubject Preference: {preference}\n Hobbies: {[h for h in hobbies]}"

demo=gr.Interaface(
  fn=getDetails,
  inputs=[gr.Textbox(label="Name:")],
  gr.Slider(label="Age: "),
  gr.Radio(label="Subject Prefernce: ", choices=['C','C#','Java','Python']),
  gr.Checkboxgroup(label='Hobbies:',choices=['Painting','Singing','Reading','Gaming' ])
  ],
  outputs=[gr.Textbox()],
)
demo.launch()
