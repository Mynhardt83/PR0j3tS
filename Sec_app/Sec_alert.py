from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

# KV language string defining the UI design
kv = """
ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"
    phone_input: phone_input
    password_input: password_input

    FloatLayout:
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "background.jpg"
        BoxLayout:
            orientation: "vertical"
            size_hint: (0.8, 0.5)
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            spacing: 10
            padding: 10

            TextInput:
                id: phone_input
                hint_text: "Cell Phone Number"
                multiline: False
                size_hint_y: None
                height: "40dp"
                input_filter: "int"
                background_color: (1, 1, 1, 0.8)
            
            TextInput:
                id: password_input
                hint_text: "Password"
                password: True
                multiline: False
                size_hint_y: None
                height: "40dp"
                background_color: (1, 1, 1, 0.8)
            
            Button:
                text: "Login"
                size_hint_y: None
                height: "50dp"
                background_color: (0, 0.5, 1, 1)
                on_press: root.validate_login()

<HomeScreen>:
    name: "home"
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.9, 0.9, 0.9, 1  # Light gray background
            Rectangle:
                pos: self.pos
                size: self.size

        # Large Emergency Button
        Button:
            text: "SEND ALERT"
            font_size: "30sp"
            bold: True
            size_hint: (0.6, 0.2)
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            background_color: (1, 0, 0, 1)  # Red button
            on_press: root.send_alert()

        # Navigation Bar
        BoxLayout:
            size_hint: (1, 0.1)
            pos_hint: {"x": 0, "y": 0}
            spacing: 20
            padding: 10
            orientation: "horizontal"

            Button:
                text: "Home"
                on_press: root.manager.current = "home"
                background_color: (0.2, 0.2, 0.2, 1)
                color: (1, 1, 1, 1)

            Button:
                text: "Alert"
                on_press: root.show_alert_screen()
                background_color: (0.2, 0.2, 0.2, 1)
                color: (1, 1, 1, 1)

            Button:
                text: "Log"
                on_press: root.show_log_screen()
                background_color: (0.2, 0.2, 0.2, 1)
                color: (1, 1, 1, 1)

            Button:
                text: "Settings"
                on_press: root.show_settings_screen()
                background_color: (0.2, 0.2, 0.2, 1)
                color: (1, 1, 1, 1)
"""

# Login Screen Logic
class LoginScreen(Screen):
    phone_input = ObjectProperty(None)
    password_input = ObjectProperty(None)

    def validate_login(self):
        phone = self.phone_input.text.strip()
        password = self.password_input.text.strip()
        if phone and password:
            self.manager.current = "home"  # Redirect to Home after login
        else:
            print("Please enter both a phone number and a password.")

# Home Screen Logic
class HomeScreen(Screen):
    def send_alert(self):
        print("Emergency Alert Sent!")  # Placeholder for alert action

    def show_alert_screen(self):
        print("Navigating to Alert Screen...")

    def show_log_screen(self):
        print("Navigating to Log Screen...")

    def show_settings_screen(self):
        print("Navigating to Settings Screen...")

# Main App Class
class SecurityAlertApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    SecurityAlertApp().run()
