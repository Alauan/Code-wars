def codewar_result(codewarrior, opponent):
    codewarrior.sort(reverse=True)
    opponent.sort(reverse=True)
    points = 0

    while len(codewarrior) != 0:
        for Opp_armySize in opponent:
            if codewarrior[0] > Opp_armySize:
                points += 1
                result = 'victory'
                break
            elif codewarrior[0] == Opp_armySize:
                result = 'draw'
            else:
                result = 'defeat'
        if result == 'defeat':
            points -= 1
        codewarrior.remove(codewarrior[0])
        opponent.remove(Opp_armySize)

    if points > 0:
        return 'Victory'
    elif points == 0:
        return 'Stalemate'
    else:
        return 'Defeat'


print(codewar_result([2, 4, 3, 1], [4, 5, 1, 2]))