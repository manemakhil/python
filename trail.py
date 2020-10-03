if __name__ == '__main__':
    scores = []
    scorserSet = set()
    def s(e):
        return e[1]

    for _ in range(int(input())):
        name = input()
        score = float(input())

        scores.append([name, score])
        scorserSet.add(score)

    scores.sort(key=s)
    scorserSet.remove(scores[0][1])

    def sort(a):        
        a.sort()
        return a

    for n in sort([i[0] for i in scores if(i[1] == min(scorserSet))]):
        print(n)

    