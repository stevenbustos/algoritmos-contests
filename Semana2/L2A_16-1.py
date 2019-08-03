__author__ = 'Steven Bustos'
w    m = [[]*N for i in range(N)]
    cereza = 0

    for i in xrange(N):
        m[i] = list(sys.stdin.readline().strip())

    for i in xrange(N):
        for j in xrange(N):
            if m[i][j] == "#":
                cereza = cereza + 1
    print cereza