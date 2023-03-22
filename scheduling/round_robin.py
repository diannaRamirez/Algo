"""
Round Robin is a scheduling algorithm.
In Round Robin each process is assigned a fixed time slot in a cyclic way.
https://en.wikipedia.org/wiki/Round-robin_scheduling
"""
from __future__ import annotations

from statistics import mean
import time
from itertools import cycle as cy
from shutil import get_terminal_size as gts
from threading import Thread as th

class Loading:

    def __init__(self, desc="processing..", points="Done..", timeout=0.2):

        self.desc = desc
        self.end = points
        self.timeout = timeout

        self.starting = th(target=self.animation_start)
        self.steps = ["⢿","....", "⣻","....", "⣽","....", "⣾","....", "⣷","....", "⣯","....", "⣟","....", "⡿","...."]
        self.done = False

    def start(self):
        self.starting.start()
        return self

    def animation_start(self):
        for i in cy(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {i}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = gts((70, 30)).columns
        print("\r " + "  " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, tb, exc_value, exc_type):
        self.stop()
        
if __name__ == "__main__":
    with Loading("Loading..."):
        for k in range(3):
            time.sleep(0.25)

    processing = Loading("Please wait, Processing..", "oohhh!!, That was too fast!", 0.05).start()
    for load_time in range(3):
        time.sleep(0.25)

    processing.stop()



def calculate_waiting_times(burst_times: list[int]) -> list[int]:
    """
    Calculate the waiting times of a list of processes that have a specified duration.

    Return: The waiting time for each process.
    >>> calculate_waiting_times([10, 5, 8])
    [13, 10, 13]
    >>> calculate_waiting_times([4, 6, 3, 1])
    [5, 8, 9, 6]
    >>> calculate_waiting_times([12, 2, 10])
    [12, 2, 12]
    """
    quantum = 2
    rem_burst_times = list(burst_times)
    waiting_times = [0] * len(burst_times)
    t = 0
    while True:
        done = True
        for i, burst_time in enumerate(burst_times):
            if rem_burst_times[i] > 0:
                done = False
                if rem_burst_times[i] > quantum:
                    t += quantum
                    rem_burst_times[i] -= quantum
                else:
                    t += rem_burst_times[i]
                    waiting_times[i] = t - burst_time
                    rem_burst_times[i] = 0
        if done is True:
            return waiting_times


def calculate_turn_around_times(
    burst_times: list[int], waiting_times: list[int]
) -> list[int]:
    """
    >>> calculate_turn_around_times([1, 2, 3, 4], [0, 1, 3])
    [1, 3, 6]
    >>> calculate_turn_around_times([10, 3, 7], [10, 6, 11])
    [20, 9, 18]
    """
    return [burst + waiting for burst, waiting in zip(burst_times, waiting_times)]


if __name__ == "__main__":
    burst_times = [3, 5, 7]
    waiting_times = calculate_waiting_times(burst_times)
    turn_around_times = calculate_turn_around_times(burst_times, waiting_times)
    print("Process ID \tBurst Time \tWaiting Time \tTurnaround Time")
    for i, burst_time in enumerate(burst_times):
        print(
            f"  {i + 1}\t\t  {burst_time}\t\t  {waiting_times[i]}\t\t  "
            f"{turn_around_times[i]}"
        )
    print(f"\nAverage waiting time = {mean(waiting_times):.5f}")
    print(f"Average turn around time = {mean(turn_around_times):.5f}")
