import platform as _platform
import sys as _sys
import os
import asyncio
import re
import threading
import time
import json
import traceback
from datetime import datetime
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

# Kivy imports for Android UI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from plyer import tts

# Make stdout/stderr UTF-8 tolerant
for _stream in (_sys.stdout, _sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

def get_base_dir():
    if getattr(_sys, "frozen", False):
        return Path(_sys.executable).parent
    return Path(__file__).resolve().parent

BASE_DIR = get_base_dir()
API_CONFIG_PATH = BASE_DIR / "config" / "api_keys.json"
PROMPT_PATH = BASE_DIR / "core" / "prompt.txt"

def _get_api_key() -> str:
    try:
        with open(API_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)["gemini_api_key"]
    except Exception:
        return os.environ.get("GEMINI_API_KEY", "")

def _load_system_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8")
    except Exception:
        return (
            "You are JARVIS, Tony Stark's AI assistant. "
            "Be concise, direct, and always use the provided tools to complete tasks."
        )

# Optional imports with fallbacks for Android environment
try:
    from memory.memory_manager import (
        load_memory, update_memory, format_memory_for_prompt,
        save_session_summary, pop_last_session,
    )
except ImportError:
    load_memory = lambda: {}
    update_memory = lambda x: None
    format_memory_for_prompt = lambda x: ""
    save_session_summary = lambda x, y: None
    pop_last_session = lambda: None

try:
    from actions.weather_report import weather_action
except ImportError:
    weather_action = lambda parameters, player: "Weather unavailable"

try:
    from actions.web_search import web_search as web_search_action, _news as _fetch_news_sync
except ImportError:
    web_search_action = lambda parameters, player: "Web search unavailable"
    _fetch_news_sync = lambda query: "News unavailable"


class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super(JarvisUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10

        self.header = Label(
            text="[b]J.A.R.V.I.S  SYSTEM[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=40,
            color=(0, 0.8, 1, 1)
        )
        self.add_widget(self.header)

        self.scroll = ScrollView(size_hint=(1, 1))
        self.log_label = Label(
            text="J.A.R.V.I.S initialized and ready...\n",
            font_size='15sp',
            size_hint_y=None,
            color=(0.9, 0.9, 0.9, 1),
            text_size=(Window.width - 40, None),
            halign='left',
            valign='top'
        )
        self.log_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)

        self.input_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.user_input = TextInput(
            hint_text="Type command here...",
            multiline=False,
            font_size='16sp',
            background_color=(0.15, 0.2, 0.25, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.user_input.bind(on_text_validate=self.process_command)

        self.send_btn = Button(
            text="SEND",
            size_hint_x=None,
            width=90,
            background_color=(0, 0.6, 0.9, 1)
        )
        self.send_btn.bind(on_release=self.process_command)

        self.input_box.add_widget(self.user_input)
        self.input_box.add_widget(self.send_btn)
        self.add_widget(self.input_box)

        self.muted = False
        self.current_file = None

    def write_log(self, text):
        self.log_label.text += f"\n{text}"

    def set_state(self, state):
        print(f"[State] {state}")

    def show_content(self, title, content):
        self.write_log(f"\n--- {title} ---\n{content}\n----------------")

    def process_command(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return

        self.write_log(f"User: {query}")
        self.user_input.text = ""
        
        # Speak response using Plyer Text-To-Speech for Android
        response = f"Processing command: {query}"
        self.write_log(f"JARVIS: {response}")
        try:
            tts.speak(response)
        except Exception as e:
            print(f"[TTS Error] {e}")


class JarvisApp(App):
    def build(self):
        self.title = "J.A.R.V.I.S"
        return JarvisUI()


if __name__ == "__main__":
    JarvisApp().run()
