"""
1. top k hosts
You are building an alert processing service for an AI-powered security platform.
Each alert has:


{
    "timestamp": int,
    "host": str,
    "alert_type": str,
    "severity": int
}

Implement a class:


class AlertAggregator:
    def __init__(self, window_size: int):
        ...
    
    def add_alert(self, alert: dict) -> None:
        ...
    
    def get_top_k_hosts(self, k: int) -> list[str]:
        ...

Requirements

Only consider alerts within the last window_size seconds relative to the latest processed timestamp.

A host’s score is the sum of severity of its active alerts in the window.
get_top_k_hosts(k) returns the k hosts with highest scores, in descending order.

If two hosts have the same score, sort by host name ascending.

Assume alerts are added in non-decreasing timestamp order.
Example

agg = AlertAggregator(window_size=10)

agg.add_alert({"timestamp": 1, "host": "a", "alert_type": "malware", "severity": 5})
agg.add_alert({"timestamp": 2, "host": "b", "alert_type": "phishing", "severity": 7})
agg.add_alert({"timestamp": 8, "host": "a", "alert_type": "c2", "severity": 4})

agg.get_top_k_hosts(2)   # ["a", "b"]

agg.add_alert({"timestamp": 15, "host": "c", "alert_type": "ransomware", "severity": 10})
# active window is [5, 15]
# host a => 4, b => 0, c => 10

agg.get_top_k_hosts(2)   # ["c", "a"]

"""
from collections import defaultdict, deque
import heapq
from platform import node

class AlertAggregator:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.alerts = deque()
        self.scores = defaultdict(int)
        self.latest_timestamp = 0
    
    def _cleanup(self, timestamp: int) -> None:
        expiry_time = timestamp - self.window_size
        while self.alerts and self.alerts[0][0] < expiry_time:
            _, host, sev = self.alerts.popleft() # evict left old alerts
            # update scores for the host
            self.scores[host] -= sev # safe for nonexisting host
            #delete entry if score <= 0
            if self.scores[host] <= 0:
                del self.scores[host]

    def add_alert(self, alert: dict)-> None:
        """
        1. add alert to deque, evict old ones
        2. update scores for the host
        3. clean up alerts and scores for evicted alerts
        """
        self.latest_timestamp = max(self.latest_timestamp, alert["timestamp"])
        host, sev = alert["host"], alert["severity"]
        self.alerts.append((alert["timestamp"], host, sev))
        self.scores[host] += sev

        # we need to evict old alerts
        self._cleanup(self.latest_timestamp)

    def get_top_k_hosts(self, k: int) -> list[str]: 
        # heap for all hosts and then read the top k
        # we need customized comparator for score and host name
        class HeapItem:
            def __init__(self, host: str, score: int):
                self.host = host
                self.score = score
            def __lt__(self, other: "HeapItem"): 
                if self.score == other.score:
                    return self.host < other.host
                return self.score > other.score # max heap 
            
        heap = []
        # scan all score items
        for host, score in self.scores.items(): 
                # build item
                item = HeapItem(host,score)
                # we only keep k items in the heap
                if len(heap) < k:
                    heapq.heappush(heap, item)
                else:
                    # we only push item if it is better
                    if item > heap[0]:
                        heapq.heapreplace(heap, item)

        # extract hosts from the heap
        result = []
        while heap:
            result.append(heapq.heappop(heap).host)

        return result

agg = AlertAggregator(window_size=10)

agg.add_alert({"timestamp": 1, "host": "a", "alert_type": "malware", "severity": 5})
agg.add_alert({"timestamp": 2, "host": "b", "alert_type":
    "phishing", "severity": 7})
agg.add_alert({"timestamp": 8, "host": "a", "alert_type": "c2", "severity": 4})


print(agg.get_top_k_hosts(2))  # ["a", "b"]

agg.add_alert({"timestamp": 15, "host": "c", "alert_type": "ransomware", "severity": 10})
# active window is [5, 15]
# host a => 4, b => 0, c => 10              
print(agg.get_top_k_hosts(2))  # ["c", "a"] 


"""
Comment: since this is a dynamic k, we rebuild heap every call
"""

"""
2. You are building an AI agent platform.
Each task may depend on other tasks finishing first.

Implement:

class TaskScheduler:
    def __init__(self, tasks: list[dict]):
        ...
    
    def get_execution_order(self) -> list[str]:
        ...

Each task looks like:

{"id": "A", "deps": []}
{"id": "B", "deps": ["A"]}
{"id": "C", "deps": ["A"]}
{"id": "D", "deps": ["B", "C"]}
Requirements
Return a valid execution order.
If there is a cycle, raise an exception or return [].
If multiple tasks are ready at the same time, return them in lexicographical order.
Example
tasks = [
    {"id": "A", "deps": []},
    {"id": "B", "deps": ["A"]},
    {"id": "C", "deps": ["A"]},
    {"id": "D", "deps": ["B", "C"]},
]

Valid output:

["A", "B", "C", "D"]

because after A, both B and C are ready, and lexicographical order picks B first.
"""
from collections import defaultdict
import heapq

class TaskScheduler:
    def __init__(self, tasks: list[dict]):
        self.tasks = tasks

    def get_execution_order(self) -> list[str]:
        # build graphs and indegree list
        graph = defaultdict(list)
        indegree = defaultdict(int)
        all_tasks = set()

        for task in self.tasks:
            task_id = task["id"]
            for dep in task["deps"]:
                if dep not in indegree:
                    indegree[dep] = 0
                    all_tasks.add(dep)
                
                graph[dep].append(task_id) # dep -> task 
                indegree[task_id] += 1
        # do BFS, since it requires lexicographical order, we need min heap
        heap = []
        for task in all_tasks:
            if indegree[task] == 0:
                heapq.heappush(heap, task)  
        
        result = []

        while heap:
            task = heapq.heappop(heap)
            result.append(task)

            for next_task in graph[task]:
                indegree[next_task] -= 1
                if indegree[next_task] == 0:
                    heapq.heappush(heap, next_task)

        # check if we have a cycle
        if len(result) != len(all_tasks):
            raise Exception("Cycle detected")
        
        return result

"""
tasks = [   {"id": "A", "deps": []},
    {"id": "B", "deps": ["A"]},
    {"id": "C", "deps": ["A"]},
    {"id": "D", "deps": ["B", "C"]},
]
scheduler = TaskScheduler(tasks)
print(scheduler.get_execution_order())  # ["A", "B", "C", "D"]  

# cycle case test
tasks = [   {"id": "A", "deps": ["D"]},
    {"id": "B", "deps": ["A"]},
    {"id": "C", "deps": ["A"]},     
    {"id": "D", "deps": ["B", "C"]},
]
scheduler = TaskScheduler(tasks)
try:
    print(scheduler.get_execution_order())
except Exception as e:
    print(e)  # Cycle detected          
"""

"""
3. Each task has:

an id
a list of deps
a duration

You have k workers.

A task can start only when:

all dependencies are finished
a worker is free

If multiple tasks are ready at the same time, pick lexicographically smaller task IDs first.

Implement:

def min_completion_time(tasks: list[dict], k: int) -> int:
    ...
Example
tasks = [
    {"id": "A", "deps": [], "duration": 3},
    {"id": "B", "deps": ["A"], "duration": 2},
    {"id": "C", "deps": ["A"], "duration": 4},
    {"id": "D", "deps": ["B", "C"], "duration": 1},
]
k = 2
Expected
A runs first: time 0 -> 3
then B and C run in parallel: 3 -> 5 and 3 -> 7
then D: 7 -> 8

Answer:

8
"""

import heapq
from collections import defaultdict

def min_completion_time(tasks: list[dict], k: int) -> int:
    if k <= 0:
        raise ValueError("k must be positive")
    if not tasks:
        return 0

    graph = defaultdict(list)
    indegree = defaultdict(int)
    duration = defaultdict(int)
    all_tasks = set()

    for task in tasks:
        task_id = task["id"]
        for dep in task["deps"]:
            if dep not in indegree:
                indegree[dep] = 0
                all_tasks.add(dep)
                duration[dep] = 0  # assume missing tasks have 0 duration   
            graph[dep].append(task_id)
            indegree[task_id] += 1
            duration[task_id] = task["duration"]

    ready = [task_id for task_id in all_tasks if indegree[task_id] == 0]
    heapq.heapify(ready)

    running = []  # (finish_time, task_id)
    time = 0
    completed = 0

    while ready or running:
        while ready and len(running) < k:
            task_id = heapq.heappop(ready)
            finish_time = time + duration[task_id]
            heapq.heappush(running, (finish_time, task_id))

        if not running:
            raise ValueError("Cycle detected")

        time = running[0][0]

        finished = []
        while running and running[0][0] == time:
            _, task_id = heapq.heappop(running)
            finished.append(task_id)
            completed += 1

        for task_id in finished:
            for nxt in graph[task_id]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    heapq.heappush(ready, nxt)

    if completed != len(all_tasks):
        raise ValueError("Cycle detected")

    return time

tasks = [
    {"id": "A", "deps": [], "duration": 3},
    {"id": "B", "deps": ["A"], "duration": 2},                  


    {"id": "C", "deps": ["A"], "duration": 4},
    {"id": "D", "deps": ["B", "C"], "duration": 1},
]
k = 2
print("k")      
# print(min_completion_time(tasks, k))  # 8

"""
4. Implement an LRU cache.

class LRUCache:
    def __init__(self, capacity: int):
        ...
    
    def get(self, key: int) -> int:
        ...
    
    def put(self, key: int, value: int) -> None:
        ...
Requirements
get(key) returns the value if key exists, else -1
put(key, value) inserts or updates the key
when capacity is exceeded, evict the least recently used key
both operations should be O(1) average time
"""
class Node: 
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_front(self, node: Node) -> None:
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node                

    def move_to_front(self, node: Node) -> None:
        if node is self.head:
            return
        # remove node from current position
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node is self.tail:
            self.tail = node.prev

        node.prev = None
        node.next = self.head

        # add to front
        self.add_to_front(node)

    def remove_tail(self) -> Node:
        if not self.tail:
            raise ValueError("Empty list")
        tail_node = self.tail
        if tail_node.prev:
            tail_node.prev.next = None
        self.tail = tail_node.prev
        tail_node.prev = None
        tail_node.next = None
        return tail_node

    def remove(self, node: Node) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.cache = {} # key -> node
        self.dll = DoublyLinkedList()  # track usage order
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # update list
        self.dll.move_to_front(node)
       
        return node.value
       
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dll.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # evict least recently used item
                lru_node = self.dll.remove_tail()
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self.dll.add_to_front(new_node)
            self.cache[key] = new_node

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)      # evicts key 2
print(lru.get(2))  # -1 (not found)
lru.put(4, 4)      # evicts key 3
print(lru.get(3))  # -1 (not found)
print(lru.get(4))  # 4      

"""


5. Given a list of intervals:

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

merge all overlapping intervals.

Expected:

[[1, 6], [8, 10], [15, 18]]
Core idea
sort by start time
keep a result list
compare current interval to the last merged interval
if overlapping, extend the end
otherwise append a new interval


"""
class MergeIntervals:
    def __init__(self):
        pass

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:  # overlap
                last_merged[1] = max(last_merged[1], current[1])  # extend end
            else:
                merged.append(current)  # no overlap, add new interval

        return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] 


merger = MergeIntervals()
print(merger.merge(intervals))  # [[1, 6], [8, 10], [15, 18]]
