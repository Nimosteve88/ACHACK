import tkinter as tk
from datetime import timedelta
import winsound

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.work_duration = timedelta(minutes=25)
        self.break_duration = timedelta(minutes=5)
        self.current_duration = self.work_duration
        self.remaining_time = self.work_duration
        self.is_paused = False

        self.label = tk.Label(self.master, text=self.format_time(self.remaining_time), font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.resume_button = tk.Button(self.master, text="Resume", command=self.resume_timer, state=tk.DISABLED)
        self.resume_button.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)

        self.timer()

    def pause_timer(self):
        self.is_paused = True
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)

    def resume_timer(self):
        self.is_paused = False
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)
        self.timer()

    def reset_timer(self):
        self.is_paused = False
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

        self.remaining_time = self.work_duration
        self.label.config(text=self.format_time(self.remaining_time))

    def timer(self):
        if not self.is_paused:
            if self.remaining_time.total_seconds() <= 0:
                self.timer_complete()
            else:
                self.label.config(text=self.format_time(self.remaining_time))
                self.remaining_time -= timedelta(seconds=1)
                self.master.after(1000, self.timer)

    def timer_complete(self):
        winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
        if self.current_duration == self.work_duration:
            self.current_duration = self.break_duration
        else:
            self.current_duration = self.work_duration

        self.remaining_time = self.current_duration
        self.label.config(text=self.format_time(self.remaining_time))
        self.timer()

    def format_time(self, duration):
        return str(duration).split(".")[0]

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()