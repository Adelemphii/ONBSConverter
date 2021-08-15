import pynbs


demo_song = pynbs.read('demo_song.nbs')

note_list = []
chars = ['[', ']']

previous_tick = 0

for tick, chord in demo_song:
	if tick == 0:
		note_list.append([note.key for note in chord])

	elif tick - previous_tick >= 20:
		if tick - previous_tick >= 40:
			note_list.append(25)
			note_list.append(25)
			if tick-previous_tick >= 60:
				note_list.append(25)
				note_list.append(25)
				note_list.append(25)
		note_list.append(25)
		note_list.append([note.key for note in chord])
		previous_tick = tick

	else:
		note_list.append([note.key for note in chord])
		previous_tick = tick
	print(tick, [note.key for note in chord])

print()
print('All Notes:', note_list)

print()

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
note_list = flatten(note_list)
formatted_note_list = []
# 33 is lowest - 0
# 57 is highest - 24
for note_num in note_list:
    formatted_note_list.append(define_numbers(note_num))
    print(define_numbers(note_num))
    print(note_num)


with open('file.txt', 'w') as f:
	for item in formatted_note_list:
		f.write("%s," % item)