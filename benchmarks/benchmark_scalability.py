"""Measure scalability of the actual quiz application."""

import argparse
import gc
import json
import os
import platform
import random
import statistics
import sys
import tempfile
import time
import tracemalloc

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))

from quiz import Quiz
from quiz_game import QuizGame
from storage import QuizStorage


SIZES = (20, 100, 1000, 10000)
SESSION_SIZE = 10
SEARCH_REPEATS = 100
SEED = 20261115

DEFAULT_PATH = ROOT / "data/default_quizzes.json"

DOCUMENT_PATH = (
    ROOT / "docs/SCALABILITY_ANALYSIS.md"
)


def timed(function, *args, **kwargs):

    start = time.perf_counter()

    result = function(
        *args,
        **kwargs
    )

    elapsed = (
        time.perf_counter() - start
    ) * 1000

    return result, elapsed


def create_quizzes(count, template):

    quizzes = []

    for index in range(1, count + 1):

        item = dict(template)

        item["id"] = index

        item["question"] = (
            f"Benchmark question {index:06d}"
        )

        item["choices"] = list(
            template["choices"]
        )

        quizzes.append(
            Quiz.from_dict(item)
        )

    return quizzes


def search_by_id(quizzes, target):

    return next(
        (
            quiz
            for quiz in quizzes
            if quiz.id == target
        ),
        None
    )


def measure_search(quizzes, target):

    measurements = []

    for _ in range(SEARCH_REPEATS):

        found, elapsed = timed(
            search_by_id,
            quizzes,
            target
        )

        assert found is not None
        assert found.id == target

        measurements.append(elapsed)

    return statistics.median(
        measurements
    )


def measure_object_memory(count, template):

    gc.collect()

    tracemalloc.start()

    try:

        quizzes = create_quizzes(
            count,
            template
        )

        assert len(quizzes) == count

        current, peak = (
            tracemalloc.get_traced_memory()
        )

        return peak / (1024 ** 2)

    finally:

        tracemalloc.stop()


def run_case(count, template):

    print(
        f"\nCASE: {count} QUESTIONS",
        flush=True
    )

    random.seed(SEED)

    gc.collect()

    quizzes, create_ms = timed(
        create_quizzes,
        count,
        template
    )

    assert len(quizzes) == count

    print(
        f"CREATE OBJECTS: {create_ms:.6f} ms",
        flush=True
    )

    game, init_ms = timed(
        QuizGame,
        quizzes
    )

    print(
        f"INITIALIZE GAME: {init_ms:.6f} ms",
        flush=True
    )

    listed, list_ms = timed(
        game.list_quizzes
    )

    assert len(listed) == count

    print(
        f"LIST QUESTIONS: {list_ms:.6f} ms",
        flush=True
    )

    search_ms = measure_search(
        listed,
        count
    )

    print(
        f"SEARCH LAST ID: {search_ms:.6f} ms",
        flush=True
    )

    _, random_ms = timed(
        game.start_game,
        count=SESSION_SIZE
    )

    assert game.is_active

    assert game.current_quiz is not None

    print(
        f"RANDOM SESSION: {random_ms:.6f} ms",
        flush=True
    )

    game.cancel_game()

    assert not game.is_active

    with tempfile.TemporaryDirectory() as directory:

        path = (
            Path(directory)
            / "state.json"
        )

        storage = QuizStorage(
            path=path
        )

        _, save_ms = timed(
            storage.save,
            game
        )

        assert path.is_file()

        size_kib = (
            path.stat().st_size / 1024
        )

        print(
            f"JSON SAVE: {save_ms:.6f} ms",
            flush=True
        )

        restored, load_ms = timed(
            storage.load
        )

        print(
            f"JSON LOAD: {load_ms:.6f} ms",
            flush=True
        )

        restored_quizzes = (
            restored.list_quizzes()
        )

        assert len(restored_quizzes) == count

        expected = [
            quiz.to_dict()
            for quiz in listed
        ]

        actual = [
            quiz.to_dict()
            for quiz in restored_quizzes
        ]

        assert actual == expected

        assert (
            restored.best_score
            == game.best_score
        )

        assert not path.with_name(
            "state.json.tmp"
        ).exists()

    memory_mib = measure_object_memory(
        count,
        template
    )

    print(
        f"OBJECT MEMORY PEAK: {memory_mib:.6f} MiB",
        flush=True
    )

    print(
        f"JSON FILE SIZE: {size_kib:.6f} KiB",
        flush=True
    )

    print(
        f"PASS: {count} question round trip",
        flush=True
    )

    return {
        "count": count,
        "create_ms": create_ms,
        "init_ms": init_ms,
        "list_ms": list_ms,
        "search_ms": search_ms,
        "random_ms": random_ms,
        "save_ms": save_ms,
        "load_ms": load_ms,
        "memory_mib": memory_mib,
        "size_kib": size_kib,
    }


def write_document(results, elapsed):

    timestamp = datetime.now().isoformat(
        timespec="seconds"
    )

    lines = [
        "# Large-Scale Quiz Performance Analysis",
        "",
        "## 1. Purpose",
        "",
        "This document addresses NEITO criterion 16.",
        "It evaluates performance, memory consumption,",
        "search cost, bottlenecks, and scalability.",
        "",
        "## 2. Actual Benchmark Environment",
        "",
        f"- Measurement time: {timestamp}",
        f"- Python: {platform.python_version()}",
        f"- OS: {platform.system()} {platform.release()}",
        f"- Architecture: {platform.machine()}",
        f"- Processor: {platform.processor()}",
        f"- Logical CPU count: {os.cpu_count()}",
        f"- Total benchmark time: {elapsed:.3f} seconds",
        "",
        "## 3. Reproduction Method",
        "",
        "Source: [benchmark_scalability.py]"
        "(../benchmarks/benchmark_scalability.py)",
        "",
        "Run from the project root:",
        "",
        "    python -u benchmarks/benchmark_scalability.py",
        "",
        "The benchmark uses the actual Quiz, QuizGame,",
        "and QuizStorage classes.",
        "",
        "Synthetic questions are generated from one",
        "default question template with unique IDs",
        "and unique question text.",
        "",
        "Question counts: 20, 100, 1000, and 10000.",
        "",
        "Each case measures a single execution of",
        "object creation, game initialization, listing,",
        "random session creation, saving, and loading.",
        "",
        "Search time is the median of 100 linear",
        "searches for the final question ID in a",
        "previously obtained question list.",
        "",
        "The search is a benchmark helper, not a claim",
        "that the console has an ID-search menu.",
        "",
        "Memory is measured separately using tracemalloc",
        "during question-object creation only.",
        "",
        "The random session contains ten questions.",
        f"The random seed is {SEED}.",
        "",
        "All state files are written to temporary",
        "directories. The real state.json is not used.",
        "",
        "## 4. Actual Measured Processing Times",
        "",
        "All values are milliseconds (ms).",
        "",
        "| Questions | Create | Initialize | List | Search | Random | Save | Load |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for row in results:

        lines.append(
            f"| {row['count']} "
            f"| {row['create_ms']:.6f} "
            f"| {row['init_ms']:.6f} "
            f"| {row['list_ms']:.6f} "
            f"| {row['search_ms']:.6f} "
            f"| {row['random_ms']:.6f} "
            f"| {row['save_ms']:.6f} "
            f"| {row['load_ms']:.6f} |"
        )

    lines.extend([
        "",
        "## 5. Actual Memory and File Size",
        "",
        "| Questions | Object creation peak (MiB) | JSON size (KiB) |",
        "|---:|---:|---:|",
    ])

    for row in results:

        lines.append(
            f"| {row['count']} "
            f"| {row['memory_mib']:.6f} "
            f"| {row['size_kib']:.6f} |"
        )

    small = next(
        row for row in results
        if row["count"] == 1000
    )

    large = next(
        row for row in results
        if row["count"] == 10000
    )

    lines.extend([
        "",
        "## 6. Measured Scaling from 1000 to 10000",
        "",
        "The number of questions increased tenfold.",
        "",
        "| Metric | Measured growth factor |",
        "|---|---:|",
    ])

    metrics = (
        ("Game initialization", "init_ms"),
        ("Question listing", "list_ms"),
        ("Linear search", "search_ms"),
        ("Random session", "random_ms"),
        ("JSON save", "save_ms"),
        ("JSON load", "load_ms"),
        ("Object creation memory", "memory_mib"),
        ("JSON file size", "size_kib"),
    )

    for label, key in metrics:

        baseline = small[key]

        if baseline > 0:

            ratio = large[key] / baseline

            lines.append(
                f"| {label} | {ratio:.3f}x |"
            )

        else:

            lines.append(
                f"| {label} | N/A |"
            )

    timing_keys = (
        ("Object creation", "create_ms"),
        ("Game initialization", "init_ms"),
        ("Question listing", "list_ms"),
        ("Linear search", "search_ms"),
        ("Random session", "random_ms"),
        ("JSON save", "save_ms"),
        ("JSON load", "load_ms"),
    )

    label, key = max(
        timing_keys,
        key=lambda item: large[item[1]]
    )

    lines.extend([
        "",
        "## 7. Observed Bottleneck",
        "",
        f"At 10000 questions, {label} had the",
        "largest measured time among the listed",
        "operations in this benchmark:",
        f"{large[key]:.6f} ms.",
        "",
        "The measured timings are observations from",
        "this machine, not universal guarantees.",
        "",
        "## 8. Algorithmic Complexity",
        "",
        "N is the number of questions.",
        "K is the number of selected questions.",
        "",
        "Assumptions: bounded question text length",
        "and bounded play-history size.",
        "",
        "| Operation | Current expected complexity |",
        "|---|---|",
        "| Create N Quiz objects | O(N) |",
        "| Add one question with duplicate checks | O(N) |",
        "| Sequential initialization | O(N^2) |",
        "| List and copy questions | O(N) |",
        "| Linear ID search | O(N) |",
        "| Random session preparation | O(N + K) |",
        "| JSON save with repeated validation | O(N^2) |",
        "| JSON load with repeated validation | O(N^2) |",
        "| Question storage memory | O(N) |",
        "",
        "The QuizGame constructor repeatedly calls",
        "add_quiz(), which checks existing questions.",
        "",
        "A simple sequential duplicate-check model",
        "has N * (N - 1) / 2 comparisons.",
        "",
        "At N = 10000 this model yields 49995000",
        "comparisons. This is a theoretical model,",
        "not an instrumented comparison count.",
        "",
        "JSON serialization itself is linear in the",
        "serialized data size. Repeated application",
        "validation can increase the overall cost.",
        "",
        "## 9. Proposed Scalability Improvements",
        "",
        "| Bottleneck | Proposed improvement |",
        "|---|---|",
        "| Repeated ID checks | Maintain a dictionary indexed by ID |",
        "| Repeated text checks | Maintain a normalized question set |",
        "| Linear lookup | Use a dictionary or database index |",
        "| Repeated validation | Validate once during bulk loading |",
        "| Full JSON rewrites | Consider SQLite transactions |",
        "| Large console lists | Pagination and filtering |",
        "| Large object collections | Lazy loading where appropriate |",
        "",
        "Dictionary and set membership have average",
        "O(1) lookup complexity under normal hashing",
        "conditions, rather than a full linear scan.",
        "",
        "An indexed bulk initialization strategy",
        "could reduce repeated duplicate checking",
        "from quadratic to approximately linear time.",
        "",
        "Indexes require additional memory and must",
        "remain consistent after insertion and deletion.",
        "",
        "SQLite can provide indexed queries and",
        "transactional updates for larger datasets.",
        "",
        "These are proposed future improvements.",
        "They are not implemented or benchmarked",
        "as part of this revision.",
        "",
        "## 10. Validation and Data Integrity",
        "",
    ])

    for row in results:

        lines.append(
            f"- PASS: {row['count']} question round trip"
        )

    lines.extend([
        "",
        "Each case verified question count, ID lookup,",
        "session startup, save and reload, all question",
        "data, and best-score preservation.",
        "",
        "## 11. Limitations",
        "",
        "- Most timings are single-run observations.",
        "- Search is measured using 100 repetitions.",
        "- Synthetic questions have similar lengths.",
        "- The benchmark does not simulate concurrent users.",
        "- Memory is traced Python object allocation only.",
        "- It is not total process memory or peak game memory.",
        "- Timing runs do not enable tracemalloc.",
        "- Disk caching and background tasks can affect results.",
        "- No production latency requirement was specified.",
        "- Results do not establish a maximum supported size.",
        "",
        "## 12. Conclusion",
        "",
        "The benchmark provides measured evidence for",
        "20, 100, 1000, and 10000 questions.",
        "",
        "The application can be evaluated beyond its",
        "original twenty-question educational dataset.",
        "",
        "Repeated duplicate validation is a potential",
        "scalability bottleneck. Indexed lookup and",
        "bulk validation are recommended before",
        "deploying much larger question banks.",
        "",
        "NEITO criterion 16 is addressed through actual",
        "performance measurements, memory measurements,",
        "search analysis, complexity analysis, and",
        "explicit future scalability strategies.",
        "",
    ])

    DOCUMENT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
        newline="\n"
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run only 20 questions without writing a report."
    )

    args = parser.parse_args()

    defaults = json.loads(
        DEFAULT_PATH.read_text(
            encoding="utf-8"
        )
    )

    assert len(defaults) == 20

    template = defaults[0]

    sizes = (
        (20,)
        if args.smoke
        else SIZES
    )

    start = time.perf_counter()

    results = [
        run_case(count, template)
        for count in sizes
    ]

    elapsed = (
        time.perf_counter() - start
    )

    if not args.smoke:

        write_document(
            results,
            elapsed
        )

        print(
            "CREATED:",
            "docs/SCALABILITY_ANALYSIS.md"
        )

    print("\nBENCHMARK SUMMARY")

    for row in results:

        print(
            "RESULT:",
            json.dumps(
                row,
                sort_keys=True
            )
        )

    print("CASES COMPLETED:", len(results))

    print(
        "TOTAL BENCHMARK SECONDS:",
        f"{elapsed:.3f}"
    )

    print(
        "PASS: All benchmark cases verified"
    )


if __name__ == "__main__":
    main()
