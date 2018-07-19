# timer-cm
A Python context manager for measuring execution time. Useful in conjunction with [Python's profilers](https://docs.python.org/3.5/library/profile.html), or on its own.

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
    with timer.child('large step'):
        sleep(1)
    for _ in range(5):
        with timer.child('small step'):
            sleep(.5)
```

Output:

```
Long task: 3.506s
  5x small step: 2.503s (71%)
  1x large step: 1.001s (28%)
```

To measure times throughout the entire run of your application and report total running times at the end:

```python
from timer_cm import Timer

_TIMER = Timer('my_fn')

def my_fn():
	# Suppose this function is called throughout your application.
	with _TIMER.child('step 1'):
		...
	with _TIMER.child('step 2'):
		...
	...

import atexit
atexit.register(_TIMER.print_results)

```