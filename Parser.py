import sys
from Video import Video
from Cache import Cache
from Endpoint import Endpoint

num_videos = 0
num_endpoints = 0
num_req_descriptions = 0
num_caches = 0
cache_mb_size = 0

videos = []
endpoints = []
caches = []

def parse_file(file_name):
    with open(file_name) as f:
        parse_header(f.readline())
        parse_videos(f.readline())
        init_caches()
        parse_endpoints(f)
        parse_requests(f)
    return videos, endpoints, caches

def parse_endpoints(file_stream):
    global num_endpoints, caches, endpoints
    for i in range(num_endpoints):
        endpoint_header = file_stream.readline().split(" ")
        datacenter_latency = int(endpoint_header[0])
        num_caches = int(endpoint_header[1])
        e = Endpoint(i, datacenter_latency)
        for j in range(num_caches):
            endpoint_cache_line = file_stream.readline().split(" ")
            cache_id = int(endpoint_cache_line[0])
            latency = int(endpoint_cache_line[1])
            e.add_cache(cache_id, latency)
            caches[cache_id].add_endpoint(e)
        endpoints.append(e)
    assert len(endpoints), num_endpoints

def parse_requests(file_stream):
    global num_req_descriptions, endpoints
    for i in range(num_req_descriptions):
        request_line = file_stream.readline().split(" ")
        video_id = int(request_line[0])
        endpoint_id = int(request_line[1])
        num_reqs = int(request_line[2])
        endpoints[endpoint_id].add_request(video_id, num_reqs)

def parse_videos(line):
    global num_videos, videos
    video_sizes = line.split(" ")
    assert len(video_sizes) == num_videos
    for i in range(0,num_videos):
        videos.append(Video(i, int(video_sizes[i])))

def parse_header(line):
    global num_videos, num_endpoints, num_req_descriptions, num_caches, cache_mb_size
    header_items = line.split(" ")
    num_videos = int(header_items[0])
    num_endpoints = int(header_items[1])
    num_req_descriptions = int(header_items[2])
    num_caches = int(header_items[3])
    cache_mb_size = int(header_items[4])

def init_caches():
    global cache_mb_size, num_caches, caches
    for i in range(num_caches):
        c = Cache()
        c.set_max_capacity(cache_mb_size)
        caches.append(c)
if __name__ == "__main__":
    videos, endpoints, caches = parse_file("streaming/me_at_the_zoo.in")