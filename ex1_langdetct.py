# Install necessary libraries (you can uncomment to install them)
# pip install langdetect
# pip install flet

from flet import *  # Import all Flet components to create the UI
from langdetect import detect  # Import the langdetect library for detecting languages

def main(page: Page):  # The main function that defines the page setup
    # Set window properties
    page.window.width = 350  # Set the width of the window to 350 pixels
    page.window.height = 650  # Set the height of the window to 650 pixels
    page.window.left = 930  # Position the window 930 pixels from the left side of the screen

    page.window.title_bar_hidden = True  # Hide the window's title bar
    page.bgcolor = Colors.AMBER  # Set the background color of the page to amber

    # Create an AppBar at the top of the window with a title and an icon
    page.appbar = AppBar(
        title=Text("Language Detections App"),  # Set the title of the app in the app bar
        center_title=True,  # Center the title in the app bar
        bgcolor="green",  # Set the app bar's background color to green
        leading=Icon(Icons.LANGUAGE)  # Add a language icon to the left side of the app bar
    )

    #########################################
    # Create a TextField for user input (multiline for longer text)
    text_input = TextField(label="Enter Text", multiline=True, bgcolor="white")

    # Create a Text element to display the result of language detection
    text_output = Text("", size=16)  # Initially empty, will be updated with detected language

    #####################
    # Define the function that is triggered when the button is clicked
    def result_function(e):
        try:
            # Attempt to detect the language of the input text using langdetect
            detect_lang = detect(text_input.value)  # Detect the language from the input
            # If language is detected, display the result in the output field
            text_output.value = f"Detected Language is: {detect_lang}"
        except:
            # If the language detection fails, show an error message
            text_output.value = "Could not detect the language"
        page.update()  # Update the page to reflect the changes in the UI

    # Create a button to trigger the language detection
    text_btn = FilledButton(
        "Show Language",  # Button label
        width=300,  # Set button width
        color="white",  # Set button text color
        bgcolor="black",  # Set button background color
        height=45,  # Set button height
        on_click=result_function  # Link the button's click event to the result_function
    )

    # Add the components to the page in a Column layout (centering them)
    page.add(
        Column(
            controls=[
                text_input,  # Add the text input field to the layout
                text_btn,  # Add the button for triggering the language detection
                text_output  # Add the text output element to display the result
            ],
            alignment=MainAxisAlignment.CENTER  # Align all components to the center
        )
    )

    page.update()  # Update the page to ensure all elements are displayed

# Run the app with the main function as the entry point
app(target=main, view=AppView.FLET_APP)  # Launch the Flet app using the main function
