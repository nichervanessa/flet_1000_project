#pip install langdetect
#pip install flet

from flet import *
from langdetect import detect


def main(page:Page):
    page.window.width=350
    page.window.height=650
    page.window.left=930

    page.window.title_bar_hidden=True
    page.bgcolor=Colors.AMBER
    page.appbar=AppBar(
        title=Text("Language Detections App"),
        center_title=True,
        bgcolor="green",
        leading=Icon(Icons.LANGUAGE)
    )
    #########################################
    text_input=TextField(label="Enter Text",multiline=True,bgcolor="white")
    text_output=Text("",size=16)
    #####################
    def result_function(e):
        try:
            detect_lang=detect(text_input.value)
            text_output.value=f"Detected Languages is:{detect_lang}"
        except:
            text_output.value="Could not detect the language"
        page.update()
    text_btn=FilledButton("SHow Language",width=300,color="white",bgcolor="black",height=45,on_click=result_function)

    page.add(
        Column(
            controls=[
                text_input,
                text_btn,
                text_output
            ],alignment=MainAxisAlignment.CENTER
        )
    )
    page.update()

app(target=main,view=AppView.FLET_APP)