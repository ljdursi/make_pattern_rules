# Step 3

We've nearly halved the size of our Makefile, making it more extensible
and maintainable!  Let's tackle one of the last rules now and see how
extensible the result is:

## Tackling the data download rule

The only remaining step involved in the actual data processing pipeline
is the data download; let's tackle that:

```
data/raw/%.zip data/raw/%: | data/raw
	curl -o data/raw/$*.zip "https://s3.amazonaws.com/tomslee-airbnb-data-2/$*.zip"
	cd data/raw %* \
		&& unzip $*.zip \
		&& mv s3_files/$* . \
```

It doesn't really give us any scope to use any of the automatic variables, but 
there isn't much repetition here.

We're lucky here in that the URLs for the data are easy to infer given the name
of the city; if it wasn't, we'd need to try to use some additional functionaity
we'll learn in later lessons.

Now let's say we wanted to look at the same plot for Montreal, or Philadelphia,
two other similarly sized cities on either side of the border:

```
make figs/montreal.png
````

It works!  Can we tackle the chicago-toronto figure too, so we can automatically
make a philadelphia-montreal figure in the same way?

(try it)

No - we can only have one pattern per rule.  This is actually a strong limitation
of Make; it will execute rules or not based only on filenames, but there can
only be one pattern per name (in this case it might not be too bad, but the very
general patterns Make allows means multiple patterns per name quickly become 
intractibly difficult)
