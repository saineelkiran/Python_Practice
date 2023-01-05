def top10():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


vals = top10()

for i in vals:
    print(i)
