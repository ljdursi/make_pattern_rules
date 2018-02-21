# Step 4

There's only really one rule we haven't touched yet, the rule setting up 
our directories.  Let's get to that:

## Multiple targets and our first debugging

```
data/raw data/merged data/out figs: 
	mkdir -p $@
```

This rule will now create whatever directory is required by the rule.  Let's
delete our non-raw data directories and figures directory and give things a
try:

```
rm -rf data/merged data/out figs
make
```

Well, that didn't get far.  What went wrong?  It looks like one of the
directories didn't get made.

Let's see what's going on in that directory creating rule, 

```
data/raw data/merged data/out figs: 
	$(warning mkdir rule called with [$@ $< $^])
	mkdir -p $@
```

and try again.  This is how we call Make functions in Gnu make; this prints
a warning message (and lets us do a little print-debugging).   We'll print
the target and prerequistes (of course there aren't any prerequisites for this
rule, so those should be blank).  This'll let us see what is going on:

```
rm -rf data/merged data/out figs
make
```

Ah ha!  The rule is only ever explicitly being called for data/merged; we never
added data/out or figs dependencies explicitly.  This isn't uncommon to see;
as our rules get more complex (or we do builds in parallel), we sometimes discover
that our Makefile has been working without us having specified all the dependencies
we need.  Let's add those dependencies where they're needed - again, they're going
to be order-only dependencies, since they only need to be created; we don't need
to update the target when they become newer:

```
data/out/%_price_per_bedroom.csv: data/merged/%.csv src/price_per_bedroom.py | data/out

figs/%.png: data/out/%_price_per_bedroom.csv src/density_plot.py | figs

figs/chicago-toronto.png: data/out/chicago_price_per_bedroom.csv data/out/chicago_price_per_bedroom.csv src/density_plot.py | figs
```

There - done.  Works nicely
