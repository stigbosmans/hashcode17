class Cache:
    def __init__(self):
        self.max_capacity = 0
        self.videos = {}   # Key: VideoID, Value: Size
        self.endpoints = []

    def set_max_capacity(self, capacity):
        self.max_capacity = capacity

    def add_video(self, videoID, size):
        self.videos[size] = videoID

    def add_endpoint(self, endpoint):
        self.endpoints.append(endpoint)
