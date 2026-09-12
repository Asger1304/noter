'''
    SOCCER TOURNAMENT

    In this problem we consider a soccer tournament among n teams.
    The teams play m games. For each game among two teams A and B, we
    know the number of goals a and b scored by A and B, respectively.
    If the game ends in a draw, i.e. a == b, then both teams receive
    one point. Otherwise, the winning team receives 3 points and the
    loosing team 0 points.

    Input:

        The first line contains two integers n and m, separated by
        space, being the number of teams n and the number of mathes
        played m. Then follows n lines, each with a unique team name
        being a non-empty string only containing characters A-Z and
        _. Each team name has length at most 25. Then follows m lines,
        one for each match, of the form A B a b, where A and B are
        valid distinct team names and a and b are the number of goals
        scored by A and B respectively.

        2 <= n <= 20
        0 <= m <= n * (n - 1)

    Output:

        The output consists of n lines, the final ranking after all m
        games. Each line should contain a team name followed by the
        team's final points, separated by a space. The teams should be
        sorted in decreasing point order. If several teams have the
        same number of points, the teams should appear sorted
        alphabetically. All points and team names are separated by a
        space:

             Team1 point1 Team2 point2 ...

    Example:

      Input:  3 6
              A
              B
              C
              A B 3 1
              A C 1 2
              B C 2 0
              B A 1 0
              C A 2 1
              C B 5 1

      Output: C 9
              B 6
              A 3
'''


n,m=tuple(map(int,input().split()))
d={}
for s in range(n):
    d[input()]=0

for i in range(m):
    A,B,a,b=tuple(input().split())
    a=int(a)
    b=int(b)
    if a==b:
        d[A]+=1
        d[B]+=1
    elif a>b:
        d[A]+=3
    elif b>a:
        d[B]+=3

T=sorted([(f,d[f]) for f in d])
Ts=sorted(T,key=lambda s:-s[1])
for s in Ts:
    print(str(s[0])+" "+str(s[1]))
