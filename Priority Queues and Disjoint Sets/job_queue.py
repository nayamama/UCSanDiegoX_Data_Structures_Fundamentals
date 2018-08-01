# python3
import heapq


class JobQueue:
    class Worker:
        """
        The workers are priority queue using their release time. If some workers are available
        at the same time, they are sorted by their id ascendingly.
        """

        def __init__(self, id, release_time=0):
            self.id = id
            self.release_time = release_time

        def __lt__(self, other):
            if self.release_time == other.release_time:
                return self.id < other.id
            return self.release_time < other.release_time

        def __gt__(self, other):
            if self.release_time == other.release_time:
                return self.id > other.id
            return self.release_time > other.release_time
    """
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.n = len(self.jobs)
        assert m == len(self.jobs)
    """

    def read_data(self):
        f = open("job_queue_question.txt", "r")
        lines = f.readlines()
        f.close()

        self.num_workers, m = map(int, lines[0].split())
        self.jobs = list(map(int, lines[1].split()))
        self.n = len(self.jobs)
        assert m == len(self.jobs)

    def write_response(self):
        for id, t in self.assigned_workers:
            print(id, t, end=" ")

    """
    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])
    """
    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        """
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]
        """

        """
        construct a heapq of workers (the workers pop out and push in queue in cycles)
        """
        self.assigned_workers = []
        self.workers = [self.Worker(i) for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(self.workers)
            self.assigned_workers.append((worker.id, worker.release_time))

            worker.release_time += job
            heapq.heappush(self.workers, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
