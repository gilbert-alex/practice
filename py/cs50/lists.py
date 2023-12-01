'''
lists are a data structure
lists have built in methods - .append
lists have built in functions = sum(), len()
'''

# averages three numbers using a list and for loop
# get scores
scores_0 = []
for i in range(3):
    score = int(input("Score: "))
    scores_0.append(score)

# print average
average = sum(scores_0) / len(scores_0)
print(f"Average: {average}")

# another syntax option
scores_1 = []
for j in range(3):
    score = int(input("Score: "))
    scores_1 += [score]

average = sum(scores_1) / len(scores_1)
print(f"Average: {average}")