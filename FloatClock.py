import tkinter as tk
import time
import winsound  # For playing system sounds (Windows)
from tkinter import messagebox  # Import messagebox for confirmation dialog

class FloatingTimer:
    def __init__(self, master, font_color="black", outline_color="white"): # Added outline_color parameter
        self.master = master
        master.overrideredirect(True)  # Remove window decorations
        master.attributes('-topmost', True) # Keep window on top
        master.geometry("+200+200") # Initial position

        # Initialize timer variables
        self.is_running = True
        self.start_time = time.time()
        self.time_elapsed = 0

        # Set background transparency of the ROOT window
        master.attributes('-transparentcolor', 'lightgray') # Set 'lightgray' as transparent color

        # Use Canvas instead of Label
        self.canvas = tk.Canvas(master, bg="lightgray", highlightthickness=0) # highlightthickness=0 removes border
        self.canvas.pack()

        self.font_family = "Helvetica" # You can change font family here
        self.font_size = 48          # You can change font size here
        self.font_weight = "bold"     # You can change font weight here
        self.text_color = font_color   # Main text color
        self.outline_color = outline_color # Outline color

        self.timer_text_id = None # To store the canvas text object id for updating

        # Button frame
        self.button_frame = tk.Frame(master, bg="lightgray") # Button frame background
        self.button_frame.pack(pady=5)
        self.button_frame.pack_forget()

        self.pause_button = tk.Button(self.button_frame, text="暂停", command=self.toggle_pause, padx=5, pady=2)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="重新计时", command=self.reset_timer, padx=5, pady=2)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Add Exit Button
        self.exit_button = tk.Button(self.button_frame, text="退出", command=self.confirm_exit, padx=5, pady=2) # Changed command to confirm_exit
        self.exit_button.pack(side=tk.LEFT, padx=5) # Pack Exit button

        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

        # Bind mouse enter and leave events to canvas now
        master.bind("<Enter>", self.show_buttons)
        master.bind("<Leave>", self.hide_buttons)
        self.button_frame.bind("<Enter>", self.show_buttons)
        self.button_frame.bind("<Leave>", self.hide_buttons)


        self.drag_start_x = 0
        self.drag_start_y = 0

        self.update_timer()

    def update_timer(self):
        if self.is_running:
            self.time_elapsed = time.time() - self.start_time
            hours = int(self.time_elapsed / 3600)
            minutes = int((self.time_elapsed % 3600) / 60)
            seconds = int(self.time_elapsed % 60)
            time_str = "{:02d}:{:02d}".format(minutes, seconds)

            self.canvas.delete("timer_text") # Remove previous text items tagged with "timer_text"
            self.draw_outlined_text(time_str, self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2) # Draw outlined text


        self.master.after(100, self.update_timer)

    def draw_outlined_text(self, text, x, y):
        """Draws text with an outline effect on the canvas."""
        font = (self.font_family, self.font_size, self.font_weight)
        outline_offset = 2 # Adjust for thicker/thinner outline

        # Draw outline in white
        for dx in range(-outline_offset, outline_offset + 1):
            for dy in range(-outline_offset, outline_offset + 1):
                if dx == 0 and dy == 0: continue # Skip the center position
                self.canvas.create_text(x + dx, y + dy, text=text, font=font, fill=self.outline_color, tags="timer_text")

        # Draw main text in the specified color on top
        self.timer_text_id = self.canvas.create_text(x, y, text=text, font=font, fill=self.text_color, tags="timer_text")


    def toggle_pause(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.pause_button.config(text="暂停")
            self.start_time = time.time() - self.time_elapsed
        else:
            self.pause_button.config(text="继续")

    def reset_timer(self):
        self.is_running = True
        self.pause_button.config(text="暂停")
        self.start_time = time.time()
        self.time_elapsed = 0
        self.update_timer() # Directly update to show "00:00:00" immediately

    def confirm_exit(self):
        """Confirms exit with a messagebox."""
        if messagebox.askyesno("退出确认", "确定要退出FloatClock吗?"): # Show confirmation dialog
            self.exit_app()

    def exit_app(self):
        """Closes the application."""
        self.master.destroy() # Destroy the root window to exit

    def start_drag(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_drag(self, event):
        x = self.master.winfo_x() - self.drag_start_x + event.x
        y = self.master.winfo_y() - self.drag_start_y + event.y
        self.master.geometry("+{}+{}".format(x, y))

    def stop_drag(self, event):
        pass

    def show_buttons(self, event):
        self.button_frame.pack(pady=5)

    def hide_buttons(self, event):
        if not self.is_mouse_in_widget(self.master) and not self.is_mouse_in_widget(self.button_frame):
            self.button_frame.pack_forget()

    def is_mouse_in_widget(self, widget):
        try:
            x, y = widget.winfo_pointerxy()
            widget_x = widget.winfo_rootx()
            widget_y = widget.winfo_rooty()
            widget_width = widget.winfo_width()
            widget_height = widget.winfo_height()
            return widget_x <= x <= widget_x + widget_width and widget_y <= y <= widget_y + widget_height
        except tk.TclError:
            return False


root = tk.Tk()
# Example usage with red font and white outline
timer_app = FloatingTimer(root, font_color="red", outline_color="white") # Pass outline_color
root.mainloop()

