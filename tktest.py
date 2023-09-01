import tkinter as tk
from functions import *

window = tk.Tk()
window.geometry("900x600")
window.title("Minion's Taiko SV Tool")
window.resizable(False, False)

snap_var = tk.StringVar()
snap_var.set("Select Snap")

function_var = tk.StringVar()
function_var.set("Select Function")

output = ""

#SV generation
def execute():
    p1, p2, p3, p4, p5, p6, p7, p8 = int(time.get()), int(spaces.get()), float(start_sv.get()), float(
        end_sv.get()), int(reps.get()), int(snap_var.get()), function_var.get(), int(bpm.get())
    svout.insert("end-1c", sv(p1, p2, p3, p4, p5, p6, p7, p8))

#simple clear function
def clear():
    svout.delete("1.0", tk.END)

#GUI Elements
text0 = tk.Label(text="Output:", font=("Helvetica", 8))
text0.grid(row=0, column=0, pady=5)

text9 = tk.Label(text="Minion's Taiko SV Tool!", font=("Helvetica", 15), foreground="#FF0000")
text9.grid(row=0, column=1, columnspan=2, pady=5)

text1 = tk.Label(text="Starting Offset", font=("Arial", 8))
text1.grid(row=1, column=1, sticky="s", padx=10)
time = tk.Entry()
time.grid(row=1, column=2, sticky="S", padx=10)

text8 = tk.Label(text="BPM", font=("Arial", 8))
text8.grid(row=2, column=1, sticky="s", padx=10)
bpm = tk.Entry()
bpm.grid(row=2, column=2, sticky="S", padx=10)

text2 = tk.Label(text="No. of Grid Spaces", font=("Arial", 8))
text2.grid(row=3, column=1, sticky="s", padx=10)
spaces = tk.Entry()
spaces.grid(row=3, column=2, sticky="S", padx=10)

start_sv = tk.Entry()
start_sv.grid(row=4, column=2, sticky="S", padx=10)
text3 = tk.Label(text="Starting SV", font=("Arial", 8))
text3.grid(row=4, column=1, sticky="s", padx=10)

end_sv = tk.Entry()
end_sv.grid(row=5, column=2, sticky="S", padx=10)
text4 = tk.Label(text="Ending SV", font=("Arial", 8))
text4.grid(row=5, column=1, sticky="s", padx=10)

reps = tk.Entry()
reps.grid(row=6, column=2, sticky="S", padx=10)
text5 = tk.Label(text="Repetitions", font=("Arial", 8))
text5.grid(row=6, column=1, sticky="s", padx=10)

snap = tk.OptionMenu(window, snap_var, "1", "2", "3", "4", "6", "8", "12", "16")
snap.grid(row=7, column=2, sticky="S", padx=10)
text6 = tk.Label(text="Snap: 1/", font=("Arial", 8))
text6.grid(row=7, column=1, sticky="s", padx=10)

sv_fun = tk.OptionMenu(window, function_var, "Linear", "Wave")
sv_fun.grid(row=8, column=2, sticky="S", padx=10)
text7 = tk.Label(text="Function", font=("Arial", 8))
text7.grid(row=8, column=1, sticky="s", padx=10)

button = tk.Button(text="Execute SV Function", command=execute)
button.grid(row=22, column=0, sticky="news", padx=8, pady=10)

button2 = tk.Button(text="Clear Output", command=clear, width=61)
button2.grid(row=22, column=1, columnspan=2, sticky="news", padx=8, pady=10)

svout = tk.Text(font=("Consolas", 8), width=70, height=40)
svout.grid(row=1, column=0, sticky="S", padx=10, rowspan=20)

if __name__ == "__main__":
    window.mainloop()
