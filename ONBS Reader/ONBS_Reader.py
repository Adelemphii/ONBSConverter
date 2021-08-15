import pynbs


demo_song = pynbs.read('demo_song.nbs')

list = []

previous_tick = 0

for tick, chord in demo_song:
	if tick == 0:
		list.append([note.key for note in chord])

	elif tick - previous_tick >= 20:
		list.append(25)
		list.append([note.key for note in chord])
		previous_tick = tick

	else:
		list.append([note.key for note in chord])
		previous_tick = tick
	print(tick, [note.key for note in chord])

print()
print('All Notes:', list)

print()
print()
print(demo_song.layers[0])
print(demo_song.instruments[0])