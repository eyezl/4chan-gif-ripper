# 4chan /gif/ Ripper
Short-form porn collector.

## Disclaimer
This doesn't _really_ respect the API rules (read: one [1] request per second).
But it also doesn't seem to bother them. In any case, just don't be a bigger
asshole than me, okay?

## Usage
1. Clone the repo.
2. `python3 main.py`
3. Look at the list, input your choices, and press enter.

There will be folders created for each of the threads *at the root of where
you ran the script*. Files are named using the filename used at upload; if a
name wasn't given, then a timestamp is used instead. A re-rip of a thread will
efficiently skip over matching files already found in the directory.
