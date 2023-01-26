# + respostas / qnt players * 0.8

def welcome():
    return "You are welcome to the divination game"


def collect_ansewrs(players):
    players_dictionary = {}
    total = 0
    for player in range(players):
        player_name = input("Coloque seu nome: ")
        player_ansewrs = int(input("Esconlha um número entre 1 e 100: "))
        players_dictionary[player_name] = player_ansewrs
        total += player_ansewrs
    print(players)
    total = total / players * 0.8
    ansewr_list = [players_dictionary, total]
    return ansewr_list


def winner(ansewr_list):
    welcome()
    total = ansewr_list[1]
    error = 100
    winner_player = ""
    for player in ansewr_list[0]:
        if abs(ansewr_list[0][player] - total) <= error:
            error = abs(ansewr_list[0][player] - total)
            winner_player = player
            print(total)
    print(winner_player)
    return winner_player


winner(collect_ansewrs(3))
