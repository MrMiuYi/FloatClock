import tkinter as tk
import time
import winsound  # For playing system sounds (Windows)
from tkinter import messagebox  # Import messagebox for confirmation dialog
import keyboard  # 导入 keyboard 库

class FloatingTimer:
    def __init__(self, master, font_color="black", outline_color="white"):
        self.master = master
        master.overrideredirect(True)
        master.attributes('-topmost', True)
        master.geometry("+200+200")

        # 初始化计时器变量
        self.is_running = True
        self.start_time = time.time()
        self.time_elapsed = 0

        # 设置背景透明
        master.attributes('-transparentcolor', 'lightgray')

        # 使用 Canvas
        self.canvas = tk.Canvas(master, bg="lightgray", highlightthickness=0)
        self.canvas.pack()

        self.font_family = "Helvetica"
        self.font_size = 48
        self.font_weight = "bold"
        self.text_color = font_color
        self.outline_color = outline_color

        self.timer_text_id = None

        # 按钮框架
        self.button_frame = tk.Frame(master, bg="lightgray")
        self.button_frame.pack(pady=5)
        self.button_frame.pack_forget()

        self.pause_button = tk.Button(self.button_frame, text="暂停", command=self.toggle_pause, padx=5, pady=2)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.button_frame, text="重新计时", command=self.reset_timer, padx=5, pady=2)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # 退出按钮
        self.exit_button = tk.Button(self.button_frame, text="退出", command=self.confirm_exit, padx=5, pady=2)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

        # 鼠标进入/离开事件
        master.bind("<Enter>", self.show_buttons)
        master.bind("<Leave>", self.hide_buttons)
        self.button_frame.bind("<Enter>", self.show_buttons)
        self.button_frame.bind("<Leave>", self.hide_buttons)

        # 添加全局快捷键 - 修改为 Win+Alt+Space 和 Win+Alt+R
        keyboard.add_hotkey('win+alt+s', self.toggle_pause)  # Win+Alt+S 暂停/继续
        keyboard.add_hotkey('win+alt+a', self.reset_timer)      # Win+Alt+A 重新计时

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

            self.canvas.delete("timer_text")
            self.draw_outlined_text(time_str, self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2)

        self.master.after(100, self.update_timer)

    def draw_outlined_text(self, text, x, y):
        """绘制带轮廓的文本."""
        font = (self.font_family, self.font_size, self.font_weight)
        outline_offset = 2

        # 绘制轮廓
        for dx in range(-outline_offset, outline_offset + 1):
            for dy in range(-outline_offset, outline_offset + 1):
                if dx == 0 and dy == 0: continue
                self.canvas.create_text(x + dx, y + dy, text=text, font=font, fill=self.outline_color, tags="timer_text")

        # 绘制主文本
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
        self.update_timer()

    def confirm_exit(self):
        """退出确认对话框."""
        if messagebox.askyesno("退出确认", "确定要退出FloatClock吗?"):
            self.exit_app()

    def exit_app(self):
        """关闭应用."""
        self.master.destroy()

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
timer_app = FloatingTimer(root, font_color="red", outline_color="white")

# 保持程序运行，直到窗口关闭，以便全局快捷键监听器继续工作
root.mainloop()
