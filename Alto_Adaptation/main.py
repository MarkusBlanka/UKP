import math

user_input = input()
n_of_notes, low, high = user_input.split(" ")
n_notes = int(n_of_notes)
low = int(low)
high = int(high)


notes = input().split(" ")
notes = [int(note) for note in notes]

# notes = [40, 41, 52, 44, 40]
# n_notes = len(notes)
# low = 20
# high = 40

# notes = [22, 29, 32, 19, 21, 23]
# n_notes = len(notes)
# low = 20
# high = 42

# notes = [42] * 6
# n_notes = len(notes)
# low = 40
# high = 64

# notes = [15, 19, 18, 40, 42, 44, 26, 29, 28, 4, 2]
# n_notes = len(notes)
# low = 12
# high = 23

# notes = [40, 41, 54, 52]
# n_notes = len(notes)
# low = 20
# high = 40


octave = 12
smallest_range_count = 120
previous_range = []
previous_range_count = 0
current_range = []
octaves_needed = 0
i = 0
while i < len(notes):
    note = notes[i]
    if note >= low and note <= high:
        current_range.append(i)
        i += 1
        continue

    if note < low:
        previous_range = current_range
        current_range = [i]
        difference = low - note
        octaves_needed = math.floor((difference / 13)) + 1
        if i > 0:
            for j in reversed(range(0, i)):
                previous_note = notes[j]
                if previous_note >= low - (octaves_needed * 12) and previous_note <= high - (octaves_needed * 12):
                    current_range.append(j)
                else:
                    break
        if i < len(notes):
            for k in range(i + 1, len(notes)):
                next_note = notes[k]
                if next_note >= low - (octaves_needed * 12) and next_note <= high - (octaves_needed * 12):
                    current_range.append(k)
                    i = k
                else:
                    i = k
                    break
        overlap = set(previous_range) & set(current_range)
        if overlap:
            middle = int((min(previous_range) + max(current_range)) / 2)
            if middle in previous_range and current_range:
                previous_range = [x for x in previous_range if x < middle]
                current_range = [x for x in current_range if x >= middle]
                smallest_range_count = min(smallest_range_count, min(len(previous_range), len(current_range)))
            elif middle in previous_range:
                previous_range = [x for x in previous_range if x not in current_range]
                smallest_range_count = min(smallest_range_count, len(previous_range), len(current_range))
            elif middle in current_range:
                current_range = [x for x in current_range if x not in previous_range]
                smallest_range_count = min(smallest_range_count, len(previous_range), len(current_range))
        else:
            smallest_range_count = min(smallest_range_count,len(current_range))
    if note > high:
        previous_range = current_range
        current_range = [i]
        difference = high - note
        octaves_needed = math.ceil((difference / 13)) - 1
        if i > 0: 
            for j in reversed(range(0, i)):
                previous_note = notes[j]
                if previous_note >= low - (octaves_needed * 12) and previous_note <= high - (octaves_needed * 12):
                    current_range.append(j)
                else:
                    break
        if i < len(notes):
            for k in range(i + 1, len(notes)):
                next_note = notes[k]
                if next_note >= low - (octaves_needed * 12) and next_note <= high - (octaves_needed * 12):
                    current_range.append(k)
                    i = k
                else:
                    i = k
                    break
        # check if there is overlap between previous and current range
        overlap = set(previous_range) & set(current_range)
        if overlap:
            if all(x in previous_range for x in current_range) or all(x in current_range for x in previous_range):
                smallest_range_count = max(len(previous_range), len(current_range))
                break
            previous_range_new_count = len([x for x in previous_range if x not in current_range])
            middle = int((min(previous_range) + max(current_range)) / 2)
            if middle in previous_range and current_range:
                previous_range = [x for x in previous_range if x < middle]
                current_range = [x for x in current_range if x >= middle]
                smallest_range_count = min(smallest_range_count, min(len(previous_range), len(current_range)))
            elif middle in previous_range:
                previous_range = [x for x in previous_range if x not in current_range]
                smallest_range_count = min(smallest_range_count, len(previous_range), len(current_range))
            elif middle in current_range:
                current_range = [x for x in current_range if x not in previous_range]
                smallest_range_count = min(smallest_range_count, len(previous_range), len(current_range))
        else:
            smallest_range_count = min(smallest_range_count,len(current_range))
    i += 1
print(f"{min(smallest_range_count, len(current_range))}")