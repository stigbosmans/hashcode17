import Parser
import numpy as np
videos, endpoints, caches = Parser.parse_file("streaming/me_at_the_zoo.in")
num_caches = len(caches)
num_endpoints = len(endpoints)
num_videos = len(videos)
video_matrix = np.zeros((num_videos))
for v in range(num_videos):
    video_matrix[v] = videos[v].size

print("num caches", num_caches)
for c in range(num_caches):
    ends = caches[c].endpoints
    cost_matrix = np.ones((num_endpoints, num_videos))
    for e in ends:
        reqs = e.requests
        for video_id, num_reqs in reqs.items():
            video = videos[video_id]
            cost_matrix[e.id][video_id] = e.datacenter_latency - (num_reqs * e.caches[c])
    print(cost_matrix)