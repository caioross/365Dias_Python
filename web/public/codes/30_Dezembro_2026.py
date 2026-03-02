import tkinter as tk
from datetime import datetime, timedelta

def update_time():
    """Atualiza o tempo restante até a virada do ano."""
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    time_left = new_year - now

    days, seconds = time_left.days, time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    time_str = f"{days}d {hours}h {minutes}m {seconds}s"
    label.config(text=time_str)
    root.after(1000, update_time)

def main():
    """Inicializa a janela principal da GUI."""
    global root, label
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    label = tk.Label(root, font=('Helvetica', 48), fg='white', bg='black')
    label.pack(expand=True)

    update_time()
    root.mainloop()

if __name__ == '__main__':
    main()