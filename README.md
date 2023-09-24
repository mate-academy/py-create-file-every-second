# Create a file every second

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Write an app that will create 1 file every 1 second in current directory (where the script is located).

- File name must be in the following format: `app-{hours}_{minutes}_{seconds}.log`.
- File content must be a timestamp of this operation (example: 2007-06-29 13:49:40.059821).
- The app must print to console timestamp and newly created file name when it completes file creation successfully.
- The app must run forever until you terminate the process.

It can be relevant here to use:
- `datetime.now()` from module `datetime`
- `sleep()` from module `time`

Example:
```python
# Output: 
# ...
# 2020-01-01 14:10:07.057405 app-14_10_7.log
# 2020-01-01 14:10:08.062182 app-14_10_8.log
# 2020-01-01 14:10:09.067101 app-14_10_9.log
# ...

with open("app-14_10_7.log", "r") as f:
    print(f.read())
# 2020-01-01 14:10:07.057405
```

**Important**: to import datetime use the following syntax: 
```python
from datetime import datetime
```
Do not use this notation:
```python
import datetime
```