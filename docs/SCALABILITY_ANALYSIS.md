# Large-Scale Quiz Performance Analysis

## 1. Purpose

This document addresses NEITO criterion 16.
It evaluates performance, memory consumption,
search cost, bottlenecks, and scalability.

## 2. Actual Benchmark Environment

- Measurement time: 2026-11-15T00:18:40
- Python: 3.12.10
- OS: Windows 11
- Architecture: AMD64
- Processor: AMD64 Family 25 Model 117 Stepping 2, AuthenticAMD
- Logical CPU count: 16
- Total benchmark time: 16.000 seconds

## 3. Reproduction Method

Source: [benchmark_scalability.py](../benchmarks/benchmark_scalability.py)

Run from the project root:

    python -u benchmarks/benchmark_scalability.py

The benchmark uses the actual Quiz, QuizGame,
and QuizStorage classes.

Synthetic questions are generated from one
default question template with unique IDs
and unique question text.

Question counts: 20, 100, 1000, and 10000.

Each case measures a single execution of
object creation, game initialization, listing,
random session creation, saving, and loading.

Search time is the median of 100 linear
searches for the final question ID in a
previously obtained question list.

The search is a benchmark helper, not a claim
that the console has an ID-search menu.

Memory is measured separately using tracemalloc
during question-object creation only.

The random session contains ten questions.
The random seed is 20261115.

All state files are written to temporary
directories. The real state.json is not used.

## 4. Actual Measured Processing Times

All values are milliseconds (ms).

| Questions | Create | Initialize | List | Search | Random | Save | Load |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | 0.098000 | 0.120300 | 0.040600 | 0.000800 | 0.100200 | 3.276600 | 0.456600 |
| 100 | 0.244700 | 0.852900 | 0.203100 | 0.002300 | 0.238100 | 4.751500 | 2.189500 |
| 1000 | 2.611900 | 58.887000 | 1.919700 | 0.019300 | 2.453600 | 88.154700 | 67.151400 |
| 10000 | 30.088600 | 5224.001400 | 19.401400 | 0.181450 | 19.899300 | 5125.183700 | 5145.995700 |

## 5. Actual Memory and File Size

| Questions | Object creation peak (MiB) | JSON size (KiB) |
|---:|---:|---:|
| 20 | 0.009926 | 12.114258 |
| 100 | 0.039551 | 60.240234 |
| 1000 | 0.318733 | 602.526367 |
| 10000 | 3.155266 | 6034.167969 |

## 6. Measured Scaling from 1000 to 10000

The number of questions increased tenfold.

| Metric | Measured growth factor |
|---|---:|
| Game initialization | 88.712x |
| Question listing | 10.106x |
| Linear search | 9.402x |
| Random session | 8.110x |
| JSON save | 58.139x |
| JSON load | 76.633x |
| Object creation memory | 9.899x |
| JSON file size | 10.015x |

## 7. Observed Bottleneck

At 10000 questions, Game initialization had the
largest measured time among the listed
operations in this benchmark:
5224.001400 ms.

The measured timings are observations from
this machine, not universal guarantees.

## 8. Algorithmic Complexity

N is the number of questions.
K is the number of selected questions.

Assumptions: bounded question text length
and bounded play-history size.

| Operation | Current expected complexity |
|---|---|
| Create N Quiz objects | O(N) |
| Add one question with duplicate checks | O(N) |
| Sequential initialization | O(N^2) |
| List and copy questions | O(N) |
| Linear ID search | O(N) |
| Random session preparation | O(N + K) |
| JSON save with repeated validation | O(N^2) |
| JSON load with repeated validation | O(N^2) |
| Question storage memory | O(N) |

The QuizGame constructor repeatedly calls
add_quiz(), which checks existing questions.

A simple sequential duplicate-check model
has N * (N - 1) / 2 comparisons.

At N = 10000 this model yields 49995000
comparisons. This is a theoretical model,
not an instrumented comparison count.

JSON serialization itself is linear in the
serialized data size. Repeated application
validation can increase the overall cost.

## 9. Proposed Scalability Improvements

| Bottleneck | Proposed improvement |
|---|---|
| Repeated ID checks | Maintain a dictionary indexed by ID |
| Repeated text checks | Maintain a normalized question set |
| Linear lookup | Use a dictionary or database index |
| Repeated validation | Validate once during bulk loading |
| Full JSON rewrites | Consider SQLite transactions |
| Large console lists | Pagination and filtering |
| Large object collections | Lazy loading where appropriate |

Dictionary and set membership have average
O(1) lookup complexity under normal hashing
conditions, rather than a full linear scan.

An indexed bulk initialization strategy
could reduce repeated duplicate checking
from quadratic to approximately linear time.

Indexes require additional memory and must
remain consistent after insertion and deletion.

SQLite can provide indexed queries and
transactional updates for larger datasets.

These are proposed future improvements.
They are not implemented or benchmarked
as part of this revision.

## 10. Validation and Data Integrity

- PASS: 20 question round trip
- PASS: 100 question round trip
- PASS: 1000 question round trip
- PASS: 10000 question round trip

Each case verified question count, ID lookup,
session startup, save and reload, all question
data, and best-score preservation.

## 11. Limitations

- Most timings are single-run observations.
- Search is measured using 100 repetitions.
- Synthetic questions have similar lengths.
- The benchmark does not simulate concurrent users.
- Memory is traced Python object allocation only.
- It is not total process memory or peak game memory.
- Timing runs do not enable tracemalloc.
- Disk caching and background tasks can affect results.
- No production latency requirement was specified.
- Results do not establish a maximum supported size.

## 12. Conclusion

The benchmark provides measured evidence for
20, 100, 1000, and 10000 questions.

The application can be evaluated beyond its
original twenty-question educational dataset.

Repeated duplicate validation is a potential
scalability bottleneck. Indexed lookup and
bulk validation are recommended before
deploying much larger question banks.

NEITO criterion 16 is addressed through actual
performance measurements, memory measurements,
search analysis, complexity analysis, and
explicit future scalability strategies.
