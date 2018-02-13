class Endpoint:
    datacenter_latency = 0
    def __init__(self, id, datacenter_latency):
        self.id = id
        self.requests = {}  # Key: VideoID, Value: no. of requests
        self.caches = {}   # Key: ChacheID, Value: Saved latency
        self.datacenter_latency = datacenter_latency

    def add_request(self, video_id, no_requests):
        self.requests[video_id] = no_requests

    def add_cache(self, cache_id, latency):
        self.caches[cache_id] = latency
