import os
import sys
import json
import asyncio
from pathlib import Path

# Kivy framework imports for native Android UI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

# Native Android hardware access via Plyer
try:
    from plyer import tts
except ImportError:
    tts = None


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent


BASE_DIR = get_base_dir()
API_CONFIG_PATH = BASE_DIR / "config" / "api_keys.json"


def load_api_key() -> str:
    if API_CONFIG_PATH.exists():
        try:
            with open(API_CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f).get("gemini_api_key", "")
        except Exception as e:
            print(f"[Config Error] Failed to read api_keys.json: {e}")
    return os.environ.get("GEMINI_API_KEY", "")


class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JarvisUI, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10

        # Title Header
        self.header = Label(
            text="[b]J.A.R.V.I.S  MOBILE[/b]",
            markup=True,
            font_size="22sp",
            size_hint_y=None,
            height=40,
            color=(0, 0.8, 1, 1),
        )
        self.add_widget(self.header)

        # Output / Log Area
        self.scroll = ScrollView(size_hint=(1, 1))
        self.log_label = Label(
            text="J.A.R.V.I.S initialized and online...\n",
            font_size="15sp",
            size_hint_y=None,
            color=(0.9, 0.9, 0.9, 1),
            text_size=(Window.width - 40, None),
            halign="left",
            valign="top",
        )
        self.log_label.bind(
            texture_size=lambda instance, value: setattr(instance, "height", value[1])
        )
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)

        # Input Area
        self.input_box = BoxLayout(
            orientation="horizontal", size_hint_y=None, height=50, spacing=10
        )
        self.user_input = TextInput(
            hint_text="Type command here...",
            multiline=False,
            font_size="16sp",
            background_color=(0.15, 0.2, 0.25, 1),
            foreground_color=(1, 1, 1, 1),
        )
        self.user_input.bind(on_text_validate=self.on_send_command)

        self.send_btn = Button(
            text="SEND",
            size_hint_x=None,
            width=90,
            background_color=(0, 0.6, 0.9, 1),
        )
        self.send_btn.bind(on_release=self.on_send_command)

        self.input_box.add_widget(self.user_input)
        self.input_box.add_widget(self.send_btn)
        self.add_widget(self.input_box)

    def append_log(self, text: str):
        def _update(dt):
            self.log_label.text += f"\n{text}"
        Clock.schedule_once(_update)

    def on_send_command(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return

        self.append_log(f"You: {query}")
        self.user_input.text = ""

        # Process message asynchronously
        asyncio.create_task(self.process_query(query))

    async def process_query(self, query: str):
        # Placeholder response handling
        response = f"Received command: '{query}'"
        self.append_log(f"JARVIS: {response}")

        # Text-To-Speech output via Plyer
        if tts:
            try:
                tts.speak(response)
            except Exception as e:
                print(f"[TTS Exception] {e}")


class JarvisApp(App):
    def build(self):
        self.title = "J.A.R.V.I.S"
        return JarvisUI()


if __name__ == "__main__":
    JarvisApp().run()
