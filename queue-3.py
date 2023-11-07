from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        while self.requests and t - self.requests[0] > 3000:
            self.requests.popleft()
        
        self.requests.append(t)
        
        return len(self.requests)

recentCounter = RecentCounter()
print(recentCounter.ping(1))  
print(recentCounter.ping(100))  
print(recentCounter.ping(3001))  
print(recentCounter.ping(3002))  
