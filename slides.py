import pptx 
import os

presentation = pptx.Presentation(os.path.join("slide", "template.pptx"))

def list_text_boxes(presentation, slide_num):
    slide = presentation.slides[slide_num - 1]
    text_boxes = []
    for shape in slide.shapes:
        if shape.has_text_frame and shape.text:
            text_boxes.append(shape.text)
    return text_boxes

def update_text_of_textbox(presentation, slide_num, textbox_id, new_text):
    slide = presentation.slides[(slide_num - 1)]
    count = 0
    for shape in slide.shapes:
        if shape.has_text_frame and shape.text:
            count += 1
            if count == textbox_id:
                text_frame = shape.text_frame
                first_paragraph = text_frame.paragraphs[0]
                first_run = first_paragraph.runs[0] if first_paragraph.runs else first_paragraph.add_run()

                # Preserve formatting of first run
                font = first_run.font
                font_name = font.name
                font_size = font.size
                font_bold = font.bold
                font_italic = font.italic
                font_underline = font.underline
                font_colour = font.color.rgb

                # Clear existing text in frame and apply new text with preserved formatting
                text_frame.clear()
                new_run = text_frame.paragraphs[0].add_run()
                new_run.text = new_text

                new_run.font.name = font_name
                new_run.font.size = font_size
                new_run.font.bold = font_bold
                new_run.font.italic = font_italic
                new_run.font.underline = font_underline
                new_run.font.color.rgb = font_colour
                return


for idx, text in enumerate(list_text_boxes(presentation=presentation, slide_num=1), 1):
    print(f"Text Box {idx}: {text}")

title = "The History of Porsche"
subheading = "A course that goes into the history of Porsche and how it was founded"



update_text_of_textbox(presentation=presentation, slide_num=1, textbox_id=1, new_text=subheading)

output_path = "new" + "_template.pptx"
presentation.save(output_path)