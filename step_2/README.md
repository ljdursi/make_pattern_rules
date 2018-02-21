# Step 2

That worked well!  We replaced two rules with one.  Let's tackle
the rest!

## Other automatic variables

Before we get started though - there's still a lot of repetition in
the updated rule:

```
figs/%.png: data/out/%_price_per_bedroom.csv src/density_plot.py
	./src/density_plot.py data/out/$*_price_per_bedroom.csv -o figs/$*.png
```

eg, `data/out/...price_per_bedroom.csv` is typed twice, as is the target
of the rule, `figs/$*.png` - introducing places where things can go wrong.

Again, why should we need to remember these things - let make deal with it!

Introduce the idea of automatic variables, and `$@` for the target
(in the case of multiple targets for a rule, it's the one that caused the
rule to be triggered) and `$<` for the first dependency.  Go through
the other common ones (in automatic_variables.txt) and explain that they
are, in fact, kind of hard to remember - if we were writing Make from scratch
today we'd use longer variable names.

With that, update the figure rule, but also the data processing rules:

```
data/merged/%.csv: data/raw/% src/merge_and_clean.py
	./src/merge_and_clean.py $< -y $(YEAR) -o $@

data/out/%_price_per_bedroom.csv: data/merged/%.csv src/price_per_bedroom.py
	./src/price_per_bedroom.py $< -o $@

figs/%.png: data/out/%_price_per_bedroom.csv src/density_plot.py
 	./src/density_plot.py $< -o $@
```
