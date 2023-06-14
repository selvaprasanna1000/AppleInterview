# AppleInterview

**What Python versions do this code support?**
I use 'defaultdict' to auto initialize the lists in dictionary which is supported only in Python3.7 or later versions.
Other than this, I simply use the basic math libraries which is available in Python standard library. 

If we want to use Python2.x, simply replace the 'defaultdict' to use regular dictionary and initialize the list manually.

Replace the line:

    graph = defaultdict(list)

To:

    graph = {}
    [graph.setdefault(i, []) for i in range(circle_count)]


