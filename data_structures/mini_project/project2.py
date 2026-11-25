import sys

sports_score_sheet = [2,3,6,6,5]

sports_score_sheet.sort(reverse=True)

print(sports_score_sheet)

maximum_score = max(sports_score_sheet)
runner_score = 0
for score in sports_score_sheet:
    if score >= maximum_score:
        continue
    else:
        runner_score = score
        print("The runner score is:", score)
        break
