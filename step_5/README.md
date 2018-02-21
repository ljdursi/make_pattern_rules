# Step 5

Comparing all data we've downloaded so far

## Using directory updates to include all data

We can't make special rules tha twill match two cities, but 
while we're discussing directories and updates, we can add
ta rule to incorporate all data we have, and have the rule re
build when we add new data

```
figs/all.png: data/out src/density_plot.py 
	./src/density_plot.py $</*.csv -o $@
```

This depends on the figures directory, and it works as expected
so far:

```
make figs/all.png
```

But if we update the data directory:

```
make figs/montreal.png figs/philadelphia.png
```

Now this rule will update `figs/all.png` because the data/out directory
has had data added to it:

```
make figs/all.png
```

And we have our four-city pictures.
