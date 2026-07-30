# sdeSheet

My personal collection of Data Structures & Algorithms solutions, written while preparing for SDE / coding interviews.

## What this is

A growing archive of solved problems from LeetCode and popular interview "SDE sheet" style problem sets. Most solutions come straight from my LeetCode submissions (the numbered folders are auto-synced from my account), with additional problems grouped by topic and by practice week as I worked through them. The `week-*` folders in particular follow the early progression of a Striver-style SDE Sheet (array warm-ups like Set Matrix Zeroes, Pascal's Triangle, Next Permutation, Dutch National Flag, then greedy problems like N Meetings in One Room, Job Sequencing, and Minimum Platforms).

This is a study/practice repo, not a library or application — each file is a self-contained solution to one problem.

## Languages

- **Python** — the primary language (~490 files)
- **C++** — a handful of solutions (mostly under `stack/`, `Recursion/`, and `week-1/`)

## How it's organized

- **`NNNN-problem-name/`** — one folder per LeetCode problem (auto-synced), e.g. `0001-two-sum/`. Each contains:
  - the solution file (`NNNN-problem-name.py`)
  - `README.md` — the LeetCode problem statement
  - `NOTES.md` — space for my own notes
  There are ~380 of these numbered problem folders.
- **Topic folders** — problems grouped by subject: `Dynamic Programming/`, `Graphs/`, `Backtracking/`, `Binary Search/`, `Recursion/`, `Linkedlist/`, `tree/`, `stack/`, `array/`, `slidingWindow/`, and more.
- **`week-1/`, `week-100/`** — problems tackled during specific practice sessions, following an SDE-sheet-style day/week progression.
- A few standalone solution files live at the repository root.

## Notes

- Solutions reflect my thinking at the time I solved each problem; they are not all optimal or uniform in style.
- A small number of files under the topic and `week-*` folders are work-in-progress or scratch attempts.

## Credits

Problem statements belong to [LeetCode](https://leetcode.com/). The interview-prep problem selection is inspired by the widely used Striver SDE Sheet ([takeUforward](https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/)).
