from operator import itemgetter

if __name__ == '__main__':
    names = ['Andreea', 'Emanuel', 'Cristi', 'Diab','Bob']
    scores = ['90', '55.2', '33.4', '70', '55.2']
    records =list()
    lowest_score = 100
    for _ in range(5):
        name = names[_]
        score = float(scores[_])
        if score < lowest_score:
            lowest_score = score
        records.append([name, score])
    y = sorted([x for x in records if x[1] != lowest_score],
               key=itemgetter((1)))
    second_lowest = y[0][1]
    scnd_lowest_names = list()
    for x in records:
        if x[1] == second_lowest:
            scnd_lowest_names.append(x[0])
    scnd_lowest_names.sort()
    print(scnd_lowest_names)

