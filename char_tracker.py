from char_builder import CharSpawn

def stats_check(map_size=0, char_list=[]):
    char_1_name = input("Who are you: ")
    x, y = input("Where would you like to start: ").split()
    player_1 = CharSpawn(char_1_name, x, y)
    char_list.append(player_1)
    print(char_list)

stats_check()