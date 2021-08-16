import pynbs
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Adele's Epic NBS to FRP Converter!")

def find_path():
	global file_path

	file_path = filedialog.askopenfilename()
	value = lbl_value["text"]
	lbl_value["text"] = file_path



def define_numbers(argument):
	return {
		25: 25,
		33: 0,
		34: 1,
		35: 2,
		36: 3,
		37: 4,
		38: 5,
		39: 6,
		40: 7,
		41: 8,
		42: 9,
		43: 10,
		44: 11,
		45: 12,
		46: 13,
		47: 14,
		48: 15,
		49: 16,
		50: 17,
		51: 18,
		52: 19,
		53: 20,
		54: 21,
		55: 22,
		56: 23,
		57: 24
	}[argument]

def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result

def read_file_and_export():

	demo_song = pynbs.read(file_path)

	note_list = []

	previous_tick = 0

	for tick, chord in demo_song:
		if tick == 0:
			note_list.append([note.key for note in chord])

		sub = tick - previous_tick
		while sub >= 20:
			note_list.append(25)
			sub -= 20
		note_list.append([note.key for note in chord])
		previous_tick = tick

		print(tick, [note.key for note in chord])

	print()
	print('All Notes:', note_list)

	print()

	note_list = flatten(note_list)
	formatted_note_list = []
	# 33 is lowest - 0
	# 57 is highest - 24
	for note_num in note_list:
		formatted_note_list.append(define_numbers(note_num))


	if entry.get():
		with open(entry.get() + '.txt', 'w') as f:
			for item in formatted_note_list:
				f.write("%s," % item)
		print(f"File saved to %s" % entry.get(), "from", file_path)
	else:
		with open('notes.txt', 'w') as f:
			for item in formatted_note_list:
				f.write("%s," % item)
		print("File saved to notes.txt from", file_path)


for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

lbl_value = tk.Label(master=window, text="No File Selected")
lbl_value.grid(row=0, column=1)

btn_browse = tk.Button(master=window, text="Browse", command=find_path)
btn_browse.grid(row=0, column=2, sticky="nsew")

entry = tk.Entry()
entry.grid(row=2, column=1, sticky="nsew")

btn_confirm = tk.Button(master=window, text="Confirm", command=read_file_and_export)
btn_confirm.grid(row=1, column=0, sticky='nsew')

lbl_file_name = tk.Label(master=window, text="Save Name")
lbl_file_name.grid(row=1, column=1, sticky="nsew")



window.mainloop()