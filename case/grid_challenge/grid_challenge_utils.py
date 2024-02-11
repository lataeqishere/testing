def gridChallenge(grid):
    # Write your code here
    orderedGrid = [sorted(x) for x in grid]
    for i, string in enumerate(orderedGrid):
        if (i) != len(string):
            newString = ''.join([x[i] for x in orderedGrid])
            if newString!=''.join(sorted(newString)):
                return 'NO'
    return 'YES'