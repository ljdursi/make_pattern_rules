# Step 1

We have a working Makefile, with canonical "all" and "clean" targets, that
will do incremental builds as necessary.  Great!

## Adding our first pattern rule

Discuss the current repetition of rules between Chicago and Toronto, and
how that limits expandability (large amounts of code have to be 
copied-and-pasted-and-edited to add Montreal or Philadelphia), and
maintainability (any change you make has to be made multiple places).

One of the reasons for moving towards automation is to let the computer
do the bookkepping, not for us to make sure that the equivalent rule in
2 or 4 places is updated the same way...

In a programming language like Python or R, or even a shell script, we would
write a function to handle this.  Make is a different sort of language - 
"declarative" - and it handles these situations by using pattern matching.

Introduce "%" for patterns and "$*" for the matched stem, and replace
the single-city figure rules with a single rule:

figs/%.png: data/out/%_price_per_bedroom.csv src/density_plot.py
	./src/density_plot.py data/out/$*_price_per_bedroom.csv -o figs/$*.png
