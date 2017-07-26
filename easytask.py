import math
from collections import defaultdict

testcases = int(input())
first = False
for _ in range(0, testcases):
	if first:
		print("")
	first = True
	submissions = input()
	submissions = int(input())

	team_submissions_rejected = defaultdict(defaultdict)
	team_submissions_accepted = defaultdict(defaultdict)
	time_to_solve = {}
	time_to_solve = defaultdict(lambda: 0, time_to_solve)
	submissions_amount = {}
	submissions_amount = defaultdict(lambda: 0, submissions_amount)
	accepted = {}
	accepted = defaultdict(lambda: 0, accepted)
	count_time_to_solve = {}
	count_time_to_solve = defaultdict(lambda: 0, count_time_to_solve)


	for _ in range(0,submissions):
		time, team, problem, status = input().split();
		time = int(time)

		if not team in team_submissions_rejected[problem]:
			team_submissions_rejected[problem][team] = 0

		if(status == 'R' and not team in team_submissions_accepted[problem]):
			team_submissions_rejected[problem][team] += 1

		else:
			
			if team_submissions_rejected[problem][team] >= 0 and team not in team_submissions_accepted[problem]:
				submissions_amount[problem] += team_submissions_rejected[problem][team] + 1
				accepted[problem] += 1
				time_to_solve[problem] += time
				count_time_to_solve[problem] += 1

			team_submissions_accepted[problem][team] = True

			

	for problem in [chr(i) for i in range(ord('A'),ord('I')+1)]:

		if(submissions_amount[problem]):
			print("{} {} {:0.2f} {:0.2f}".format(problem, accepted[problem], round(submissions_amount[problem]*1.0/accepted[problem],2), round(time_to_solve[problem]*1.0/count_time_to_solve[problem],2)))
		else:
			print("{:s} 0".format(problem))


