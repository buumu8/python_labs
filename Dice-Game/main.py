from itertools import combinations


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    # write your code here

    for d1 in dice1:
        for d2 in dice2:
            if d1 > d2:
                dice1_wins += 1
            elif d2 > d1:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    # write your code here
    # use your implementation of count_wins method if necessary
    max_win = -1
    winner = -1
    comb = combinations(range(len(dices)), 2)

    for d1, d2 in comb:
        d1_wins, d2_wins = count_wins(dices[d1], dices[d2])
        # print(d1,d2,d1_wins,d2_wins,max_win,winner)
        if d1_wins > d2_wins and d1_wins > max_win:
            max_win = d1_wins
            winner = d1
        elif d2_wins > d1_wins and d2_wins > max_win:
            max_win = d2_wins
            winner = d2
        elif d1_wins == max_win or d2_wins == max_win:
            winner = -1

    return winner


dices = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
print(find_the_best_dice(dices))
