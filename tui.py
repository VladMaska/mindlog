from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, Button
from textual.scroll_view import ScrollView
from mindlog import add_entry, load_entries


class MindLogApp(App):
    CSS_PATH = None
    TITLE = "Mindlog TUI"
    SUB_TITLE = "Log your thoughts and mood"

    def compose(self) -> ComposeResult:
        yield Header()

        yield Static("What's on your mind?")
        self.thought_input = Input(placeholder="Type your thoughts here...")
        yield self.thought_input

        yield Static("How's your mood? (1-10)")
        self.mood_input = Input(placeholder="Mood level from 1 to 10")
        yield self.mood_input

        self.status = Static("")
        yield Button("Submit", id="submit_button")
        yield self.status

        yield Static("Previous entries:")
        self.entries_display = ScrollView()
        yield self.entries_display

        yield Footer()

    def on_mount(self):
        self.refresh_entries()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit_button":
            thought = self.thought_input.value.strip()
            mood = self.mood_input.value.strip()

            try:
                mood_int = int(mood)
                if not 1 <= mood_int <= 10:
                    raise ValueError
            except ValueError:
                self.status.update("[red]Invalid mood. Enter a number from 1 to 10.")
                return

            if not thought:
                self.status.update("[red]Thought cannot be empty.")
                return

            add_entry(thought, mood_int)
            self.status.update("[green]Entry saved.")
            self.thought_input.value = ""
            self.mood_input.value = ""

            self.refresh_entries()

    def refresh_entries(self):
        entries = load_entries()
        self.entries_display.remove_children()
        if not entries:
            self.entries_display.mount(Static("No entries yet."))
        else:
            text = "\n".join(
                f"[{e['timestamp']}] ({e['mood']}/10): {e['thought']}"
                for e in reversed(entries[-10:])
            )
            self.entries_display.mount(Static(text))


if __name__ == "__main__":
    app = MindLogApp()
    app.run()
