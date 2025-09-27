player_1 = [int(x) for x in list(input())]
player_2 = [int(x) for x in list(input())]
player_3 = [int(x) for x in list(input())]

win_sequence = []
i = 0
j = 0
k = 0
while i < len(player_1) or j < len(player_2) or k < len(player_3):
    input_player_1 = player_1[i] if i < len(player_1) else None
    input_player_2 = player_2[j] if j < len(player_2) else None
    input_player_3 = player_3[k] if k < len(player_3) else None
    numbers = [input_player_1, input_player_2, input_player_3]
    if numbers[0] == numbers[1]:
        win_sequence.append(player_1[i])
        i += 1
        j += 1
    elif numbers[0] == numbers[2]:
        win_sequence.append(player_1[i])
        i += 1
        k += 1
    elif numbers[1] == numbers[2]:
        win_sequence.append(player_2[j])
        j += 1
        k += 1
    else:
        break


print("".join(map(str, win_sequence)))