# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
# During his last hike he took exactly steps. For every step he took, he noted if it was an uphill or a downhill, step.
# Gary's hikes start and end at sea level and each step up or down represents a

# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of
# valleys Gary traversed.

# countingValleys has the following parameter(s):
# n: the number of steps Gary takes
# s: a string describing his path

# Complete the countingValleys function below.


def countingValleys(n, s):
    v = 0
    lvl = 0
    for i in range(n):
        if s[i] == 'D':
            lvl += 1
        if s[i] == 'U':
            lvl -= 1

        if lvl == 0 and s[i] == 'U':
            v += 1
    return v
