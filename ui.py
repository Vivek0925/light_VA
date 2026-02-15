import tkinter as tk
import threading
import os
from main import main


class FloatingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Light")
        self.root.geometry("100x100+1200+600")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.config(bg="#000000")

        # Canvas for circular orb
        self.canvas = tk.Canvas(
            root,
            width=100,
            height=100,
            bg="#000000",
            highlightthickness=0
        )
        self.canvas.pack()

        # Draw circular orb
        self.orb = self.canvas.create_oval(
            10, 10, 90, 90,
            fill="#4a6cff",
            outline=""
        )

        # Status text
        self.text = self.canvas.create_text(
            50, 50,
            text="Light",
            fill="white",
            font=("Arial", 12, "bold")
        )

        # Click to start assistant
        self.canvas.tag_bind(self.orb, "<Button-1>", self.start_assistant)
        self.canvas.tag_bind(self.text, "<Button-1>", self.start_assistant)

        # Dragging
        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

        # Right-click to close
        self.canvas.bind("<Button-3>", self.close_app)

        # Hover effects
        self.canvas.bind("<Enter>", self.on_hover)
        self.canvas.bind("<Leave>", self.on_leave)

        self.assistant_running = False

    def start_assistant(self, event=None):
        if not self.assistant_running:
            self.canvas.itemconfig(self.orb, fill="#00c8ff")
            self.canvas.itemconfig(self.text, text="Listening")
            self.assistant_running = True

            thread = threading.Thread(target=main, daemon=True)
            thread.start()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.root.winfo_pointerx() - self.x
        y = self.root.winfo_pointery() - self.y
        self.root.geometry(f"+{x}+{y}")

    def on_hover(self, event):
        self.canvas.itemconfig(self.orb, fill="#6f8cff")

    def on_leave(self, event):
        if self.assistant_running:
            self.canvas.itemconfig(self.orb, fill="#00c8ff")
        else:
            self.canvas.itemconfig(self.orb, fill="#4a6cff")

    def close_app(self, event=None):
        # Fully stop Light and exit program
        os._exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    app = FloatingAssistant(root)
    root.mainloop()