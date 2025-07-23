# random chance of money pucks (-2, 2, 3)
# enter 's' of 'g' as single key input for each shot
# choose shots per period
# chose num periods

import random

# function to print game
# def printSummary()

# [['v', 1], ['v', 1], ['h', 2], ['h', 2], ['v', 1], ['h', 2], ['h', 2], ['h', 2], ['h', 2], ['v', 1], ['h', 2], ['h', 2], ['v', 1], ['h', 2], ['v', 1], ['v', 1], ['v', 1], ['h', 2], ['h', 2], ['v', 1], ['v', 1], ['v', 1], ['h', 2], ['v', 1]]
    
# list of results
num_shots = 12
num_goals = 3
results = ([1] * num_goals ) + [0] * (num_shots - num_goals)
random.shuffle(results)

if __name__ == '__main__':
    # Options
    shotsPerPeriod = int(len(results)/6)
    boolMoneyPucks = True
    moneypucks = [-2, 1, 1, 1, 1, 1, 2, 3]

    # create list of [team, moneypuck] then shuffle order
    plays = [['h', random.choice(moneypucks)], ['v', random.choice(moneypucks)]] * shotsPerPeriod * 3
    random.shuffle(plays)

    hScore = 0
    vScore = 0

    hScoreR = 0
    vScoreR = 0

    for i in range(len(plays)):
        if plays[i][0] == 'v':

            if plays[i][1] * results[i] + vScore >= 0:
                vScore += plays[i][1] * results[i]
            else: vScore = 0

            if plays[i][1] * results[i] + vScoreR >= 0:
                vScoreR += results[i]
            else: vScoreR = 0

        elif plays[i][0] == 'h':
            if plays[i][1] * results[i] + hScore >= 0:
                hScore += plays[i][1] * results[i]
            else: hScore = 0

            if plays[i][1] * results[i] + hScoreR >= 0:
                hScoreR += results[i]
            else: hScoreR = 0

    # print(plays)

    print('\n', '-' * 12, 'MP', '-' * 12)
    print('{:<8}: {:>4}\n{:<8}: {:>4}\n'.format('HOME',hScore,'VISITOR', vScore))


    print('-' * 12, 'REG', '-' * 12)
    print('{:<8}: {:>4}\n{:<8}: {:>4}\n\n'.format('HOME',hScoreR,'VISITOR', vScoreR))