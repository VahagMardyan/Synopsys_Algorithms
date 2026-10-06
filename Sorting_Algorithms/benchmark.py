"""
Test Bench
"""
from runner import Runner

if __name__ == "__main__":
    rn = Runner()
    rn.run(start=1000, end=1200, growth_factor=0.1 ,save=False)
    rn.visualize(show=True)

