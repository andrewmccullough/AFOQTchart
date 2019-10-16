import csv
import random

# GENERATE_NEW_TABLE = False
#
# if GENERATE_NEW_TABLE:
# 	f = open("table.csv", "w")
# 	writer = csv.writer(f)
#
# 	# header row
# 	row = [" "]
# 	for c in range(-16, 17):
# 		row.append(c)
#
# 	writer.writerow(row)
#
# 	# remaining rows
# 	for r in range(-16, 17):
# 		row = [r]
# 		for _ in range(-16, 17):
# 			row.append(random.randint(20, 500))
# 		writer.writerow(row)
#
# 	f.close()

source = open("table.csv")
reader = csv.reader(source)

f = open("questions.csv", "w")
writer = csv.writer(f)
writer.writerow([None, "X", "Y", None, "A", "B", "C", "D", "E"])

correct_answers = []

# iterate through number of questions
NUMBER_QUESTIONS = 40
for n in range(NUMBER_QUESTIONS):
	source.seek(0)

	# [1, 33]
	col = random.randint(1, 41)
	row = random.randint(1, 41)

	visible_col = col - 21
	visible_row = -1 * row + 21

	trick_answers = []
	correct_answer = None

	for i, r in enumerate(reader):
		if i == row:
			correct_answer = int(r[col])

	while len(trick_answers) < 4:
		trick_answer = correct_answer + random.randint(-3, 3)
		if 50 <= trick_answer <= 130 and trick_answer != correct_answer and trick_answer not in trick_answers:
			trick_answers.append(trick_answer)

	all_answers = trick_answers + [correct_answer]
	random.shuffle(all_answers)
	correct_letter = ["A", "B", "C", "D", "E"][all_answers.index(correct_answer)]
	correct_answers.append(correct_letter)

	writer.writerow([n + 1, visible_col, visible_row, None, all_answers[0], all_answers[1], all_answers[2], all_answers[3], all_answers[4]])


answers = open("answers.txt", "w")
for i, each in enumerate(correct_answers):
	answers.write(str(i + 1) + ": " + each + "\n")

f.close()
source.close()
answers.close()
