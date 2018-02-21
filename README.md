# Programming Make, part I: Pattern Rules

A short walk-through of pattern rules in Makefile, targetted at
people who have a little scripting experience.  Notionally, at this
point we have:

- Introduced a motivating problem (comparing AirBnB prices in two similar-sized cities in different countries, Toronto and Chicago)
- Talked about the reasons for wanting reproducibility/automation and Make in particular
- Gone through the process of translating a bash script into Make in two steps (literally, then breaking out each output-file individually) and seen the advantage of incremental rebuilds; this introduces
    - targets
    - dependencies
    - SECONDARY: for keeping intermediate targets
    - Multi-line commands; each line is run in a different shell
- Added some canonical targets (clean and all) and introduced PHONY

Now we're taking that and introducing pattern rules for DRY - maintainability and extensibility.

The worked example uses python, with seaborn and pandas, although
no python experience is necessary; for our purposes, they are just
command line tools we're running.  However, you'll have to make sure
the modules are installed:

```
virtualenv make_pattern
source make_pattern/bin/activate
pip install -r requirements.txt
```

and make sure you have **GNU**, not BSD, Make installed; the precise version shouldn't matter:

```
$ make -v
GNU Make 3.81
...
```
