count = int(input())
names = []
for _ in range(count):
    names.append(input())

names = [name.split(" ")[1:] for name in names]
# names = [["Maria", "Douglas"], ["Ozzy", "Levi", "Carpenter"], ["Quentin", "Aaron", "Potter"], ["Christy", "Iglesias"], ["Mo", "Mansur"], ["Sam", "Marlon", "Scully"]]

def check_next_names(i, previous_name_index, list_of_names):
    if i < len(names):
        previous_name = list(names[i - 1][previous_name_index])
        
        for name in names[i]:
            current_name = list(name)
            broken = False
            found_next = False
            # print(f"Comparing {previous_name} with {current_name}")
            for j in range(min(len(current_name), len(previous_name))):
                if previous_name[j] < current_name[j]:
                    # print(f"Character {previous_name[j]} is less than {current_name[j]}")
                    found_next = True
                    break
                elif previous_name[j] == current_name[j]:
                    continue
                else:
                    # print(f"Character {previous_name[j]} is greater than {current_name[j]}")
                    broken = True
                    break
            if not broken:
                if len(previous_name) <= len(current_name):
                    found_next = True
            if found_next:
                # print(f"Found next name: {name}")
                next_list = list_of_names.copy()
                next_list.append(name)
                next_path = check_next_names(i + 1, names[i].index(name), next_list)
                if next_path:
                    return next_path
        # print(f"No valid next name found after {previous_name}")
        return False
    else:
        return list_of_names 

possible_names = []
possible_names_found = False
for name_index in range(len(names[0])):
    possible_names = check_next_names(1, name_index, [names[0][name_index]])
    if possible_names:
        possible_names_found = True
        print("\n".join(possible_names))
        break

if not possible_names_found:
    print("impossible")
