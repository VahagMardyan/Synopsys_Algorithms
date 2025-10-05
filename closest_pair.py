import math, random, time
import matplotlib.pyplot as plt

def distance(p1:list, p2:list) -> float:
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# # brute force
def brute_force(points:list) -> tuple:
    min_dist = float('inf')
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                p1 = points[i]
                p2 = points[j]
    return (p1, p2, min_dist)

# # Divide and conquer
def rec(xsorted:list, ysorted:list) -> tuple:
    n = len(xsorted)
    if n <= 3:
        return brute_force(xsorted)
    else:
        midpoint = xsorted[n//2]
        xsorted_left = xsorted[:n//2]
        xsorted_right = xsorted[n//2:]
        ysorted_left = []
        ysorted_right = []
        for point in ysorted:
            ysorted_left.append(point) if (point[0] <= midpoint[0]) else ysorted_right.append(point)
        (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
        (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
        (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right, delta_right)
        in_band = [ point for point in ysorted if midpoint[0] - delta < point[0] < midpoint[0] + delta ]
        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = distance(in_band[i], in_band[j])
                if d < delta:
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta

def closest(points:list) -> tuple:
    xsorted = sorted(points, key=lambda point : point[0])
    ysorted = sorted(points, key=lambda point : point[1])
    return rec(xsorted, ysorted)

class Test:
    def __init__(self):
        self.algorithms = {
            "Divide and concuer O(nlog(n))" : lambda point : closest(point),
            "Brute-force O(n²)" :  lambda point :  brute_force(point)
        }
        self.results = {
            "Divide and concuer O(nlog(n))": [],
            "Brute-force O(n²)": [],
        }
        self.sizes = []
    
    def generate_points(self, size:int) -> list:
        points = set()
        while len(points) < size:
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
            points.add((x,y))
        return list(points)
    
    def timer(self, size:int):
        points = self.generate_points(size)
        print(f"\npoints' amount: {len(points)}")
        results = {}
        for name, func in  self.algorithms.items():
            if name == "Brute-force O(n²)" and size > 5000:
                print(f"{name}: skipped (too slow)")
                self.results[name].append(float('inf'))
                continue
            start = time.perf_counter()
            res = func(points)
            end = time.perf_counter()
            spent_time = (end - start) * 1000
            print(f"{name}: result={res}, time={spent_time:.4f} ms")
            results[name] = res
            self.results[name].append(spent_time)

        self.sizes.append(size)

        if len(results) > 1 and len({r[2] for r in results.values()}) > 1:
            print("Warning: mismatch between algorithms!")

    def plot_results(self):
        for name, times in self.results.items():
            plt.plot(self.sizes, times, marker="o", label = name)
        plt.xlabel("Points' amount")
        plt.ylabel("Execution time (ms)")
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
        plt.show()

t = Test()
i = 10.0
while i <= 10_000:
    t.timer(int(i))
    i *= 1.02

t.plot_results()
