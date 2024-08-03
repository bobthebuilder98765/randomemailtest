from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
import random

class EmailApp(App):
    def build(self):
        self.email_password_list = [
            "Y3BksnBsM9@gmail.com:Loka0808",
            "OUW4aJ9f2z@gmail.com:Loka0808",
            "qzPJHxyK5l@gmail.com:Loka0808",
            # Add more pairs as needed
        ]

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Press the button to get an email-password pair.", size_hint_y=None, height=44)
        layout.add_widget(self.label)

        self.button = Button(text="Get Random Email:Password", on_press=self.get_random_pair, size_hint_y=None, height=44)
        layout.add_widget(self.button)

        return layout

    def get_random_pair(self, instance):
        if not self.email_password_list:
            self.label.text = "No more email-password pairs left."
            return

        # Select a random email-password pair
        pair = random.choice(self.email_password_list)
        # Remove the selected pair from the list
        self.email_password_list.remove(pair)
        # Copy the pair to the clipboard
        Clipboard.copy(pair)
        # Update the label with the selected pair
        self.label.text = f"Copied to clipboard: {pair}"

if __name__ == '__main__':
    EmailApp().run()
