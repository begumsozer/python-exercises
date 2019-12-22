def oldest(people):
	oldest = people[person]
	oldest_name = person
	for person in people:
		if people[person] > oldest:
			oldest = people[person]
			oldest_name = person
	return oldest_name
