"""
You are given a list of (website, userId) pairs that represent users visiting websites.
Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:
[('google.com', 1), ('google.com', 3), ('google.com', 5), ('pets.com', 1), ('pets.com', 3), ('yahoo.com', 6),
('yahoo.com', 2), ('yahoo.com', 3), ('yahoo.com', 4), ('yahoo.com', 5), ('wikipedia.org', 4), ('wikipedia.com', 5),
('wikipedia.com', 6), ('wikipedia.com', 7), ('bing.com', 1), ('bing.com', 3), ('bing.com', 5), ('bing.com', 6)]

To compute the similarity between two websites you should compute the number of users they have in common divided
by the number of users who have visited either site in total. (This is kown as the Jaccard index.)

For example, in this case, we would conclude that google.com and bing.com are the most similar,
with a score of 3/4
"""
import heapq
from collections import defaultdict


def find_top_pair(log, k):
	logger = defaultdict(set)
	
	for site, user_id in log:
 		logger[site].add(user_id)

	heap = []
	sites = list(logger.keys())

	for _ in range(k):
		heapq.heappush(heap, (0, ('', '') ))

	for s_idx in range(len(sites) - 1):
		for s_idy in range(s_idx + 1, len(sites)):
			score = similarity_score(logger, sites[s_idx], sites[s_idy])
			heapq.heappushpop(heap, (score, (sites[s_idx], sites[s_idy]) ))

	return [pair[1] for pair in heap]


def similarity_score(logger, fst_s, snd_s):
	return len(logger[fst_s] & logger[snd_s]) / len(logger[fst_s] | logger[snd_s]) 


if __name__ == '__main__':
	logs = [
		('google.com', 1), ('google.com', 3), ('google.com', 5), ('pets.com', 1), ('pets.com', 3), ('yahoo.com', 6),
		('yahoo.com', 2), ('yahoo.com', 3), ('yahoo.com', 4), ('yahoo.com', 5), ('wikipedia.org', 4), ('wikipedia.com', 5),
		('wikipedia.com', 6), ('wikipedia.com', 7), ('bing.com', 1), ('bing.com', 3), ('bing.com', 5), ('bing.com', 6)
	]

	assert find_top_pair(logs, 1) == [('google.com', 'bing.com')]
	assert find_top_pair(logs, 2) == [('google.com', 'pets.com'), ('google.com', 'bing.com')]
	assert find_top_pair(logs, 0) == []
	