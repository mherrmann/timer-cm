# timer-cm
A Python context manager for measuring execution time.

## Installation

```
pip install timer_cm
```

## Usage
First, import the `Timer` class:

```python
from timer_cm import Timer
```

Then use it as a context manager. In this example we use Python's `sleep(...)` function to pause execution for one second:

```python
with Timer('Simple task'):
    sleep(1)
```

This produces the following output:

```
Simple task: 1.005s
```

Often you want to know where a long running code block spends its time. Use `timer.child(name)` to track individual steps:

```python
with Timer('Long task') as timer:
    with timer.child('First step'):
        sleep(1)
    for _ in range(5):
        with timer.child('Many small steps'):
            sleep(.5)
```

Output:

```
Long task: 3.520s
  Many small steps: 2.518s (71%)
  First step: 1.001s (28%)
```