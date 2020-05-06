'''
def findPeak():
    num_checkpoints = input()
    if int(num_checkpoints) < 3:
        return 0
    checkpoints = input().split()
    peaks = 0
    for j in range(1, int(num_checkpoints) - 1):
        #print(checkpoints[j])
        if checkpoints[j] > checkpoints[j - 1] and checkpoints[j] > checkpoints[j + 1]:
            peaks += 1
    return peaks

num_tests = input()

for i in range(int(num_tests)):
    print(findPeak())

'''
def findPeak():
    num_checkpoints = input()
    if int(num_checkpoints) < 3:
        return 0
    checkpoints = input().split()
    peaks = 0
    for j in range(1, int(num_checkpoints) - 1):
        if int(checkpoints[j]) > int(checkpoints[j - 1]) and int(checkpoints[j]) > int(checkpoints[j + 1]):
            peaks += 1
    return peaks


num_tests = input()
results = []
for i in range(int(num_tests)):
    results.append("Case #" + str(i + 1) + ": " + str(findPeak()))
for i in results:
    print(i)
