"""
Testing algorithms
"""
import time
from random import randint
from typing import Generator
import pandas as pd
import matplotlib.pyplot as plt

from sorter_strategy import (
    BubbleSort,
    InsertionSort,
    SelectionSort,
    MergeSort,
    HeapSort,
    QuickSort,
    CountingSort,
    RadixSort,
    StalinSort,
    SortStrategy,
)

class Runner:
    def __init__(self, strategies: list[SortStrategy] | None = None):
        self.strategies: list[SortStrategy] = strategies or [
            BubbleSort(),
            InsertionSort(),
            MergeSort(),
            HeapSort(),
            QuickSort(),
            SelectionSort(),
            CountingSort(),
            RadixSort(),
            StalinSort(),
        ]
        self.results: list[dict] = []
        self.df_results: pd.DataFrame = pd.DataFrame()

    def generator(
        self, start: int, end: int, growth_factor: float, min_val: int = -10_000, max_val: int = 10_000
    ) -> Generator[tuple[int, list[int]], None, None]:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end sizes must be integers.")
        if not isinstance(growth_factor, (float, int)):
            raise TypeError("Growth factor must be a float or int.")
        if not (0 < growth_factor <= 1):
            raise ValueError("Growth factor must be in range (0; 1].")

        current_size = start
        while current_size <= end:
            arr = [randint(min_val, max_val) for _ in range(current_size)]
            yield current_size, arr

            next_size = int(current_size * (1 + growth_factor))
            if next_size <= current_size:
                next_size = current_size + 1
            current_size = next_size

    def is_sorted(self, arr:list[int]) -> bool:
        return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

    def run(self, start: int = 1_000, end: int = 10_000, growth_factor: float = 0.5, save: bool = False) -> pd.DataFrame:
        self.results.clear()

        SLOW_ALGOS = {"Bubble Sort", "Insertion Sort", "Selection Sort"}
        MAX_SLOW_SIZE = 20_000

        for size, base_arr in self.generator(start, end, growth_factor):
            print(f"\n=== Testing size: {size} ===")

            for strategy in self.strategies:
                if strategy.name in SLOW_ALGOS and size > MAX_SLOW_SIZE:
                    print(f"Skipping {strategy.name} for size {size} (too slow)")
                    continue

                start_time = time.perf_counter()
                sorted_arr = strategy.sort(base_arr)
                elapsed_ms = (time.perf_counter() - start_time) * 1000

                is_ok = self.is_sorted(sorted_arr)

                self.results.append({
                    "Size": size,
                    "Algorithm": strategy.name,
                    "Time (ms)": elapsed_ms,
                    "Is Sorted": is_ok,
                    "Elements": len(sorted_arr),
                })
                print(f"{strategy.name:20s} | {elapsed_ms:8.2f} ms")

        self.df_results = pd.DataFrame(self.results)
        if save:
            data_name = "results.csv"
            self.df_results.to_csv(data_name)
            print(f"Results saved as `{data_name}`")

        return self.df_results

    def visualize(self, save_path: str | None = None, show: bool = True):
        if self.df_results.empty:
            print("No data to visualize. Please call run() first.")
            return

        plt.figure(figsize=(12, 7))

        for strategy in self.strategies:
            sub = self.df_results[self.df_results["Algorithm"] == strategy.name]
            if not sub.empty:
                plt.plot(sub["Size"], sub["Time (ms)"], marker="o", linewidth=2, label=strategy.name)

        plt.xlabel("Array size", fontsize=11)
        plt.ylabel("Time (ms)", fontsize=11)
        plt.title("Sorting Algorithms Performance Comparison", fontsize=13, fontweight="bold")
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300)
            print(f"Plot saved to {save_path}")

        if show:
            plt.show()

