YEAR := "2017"

.PHONY: all
all: figs/chicago.png figs/toronto.png figs/chicago-toronto.png

.SECONDARY:

data/raw data/merged data/out figs: 
	mkdir -p $@

data/raw/%.zip data/raw/%: | data/raw
	curl -o data/raw/$*.zip "https://s3.amazonaws.com/tomslee-airbnb-data-2/$*.zip"
	cd data/raw %* \
		&& unzip $*.zip \
		&& mv s3_files/$* . \
		&& rmdir s3_files

data/merged/%.csv: data/raw/% src/merge_and_clean.py | data/merged
	./src/merge_and_clean.py $< -y $(YEAR) -o $@

data/out/%_price_per_bedroom.csv: data/merged/%.csv src/price_per_bedroom.py | data/out
	./src/price_per_bedroom.py $< -o $@

figs/%.png: data/out/%_price_per_bedroom.csv src/density_plot.py | figs
	./src/density_plot.py $< -o $@

figs/chicago-toronto.png: data/out/chicago_price_per_bedroom.csv data/out/toronto_price_per_bedroom.csv src/density_plot.py | figs
	./src/density_plot.py data/out/chicago_price_per_bedroom.csv data/out/toronto_price_per_bedroom.csv -o $@

figs/all.png: data/out src/density_plot.py
	./src/density_plot.py data/out/*.csv -o $@

.PHONY: clean
clean:
	rm -f data/merged/toronto.csv
	rm -f data/merged/chicago.csv
	rm -f data/out/toronto_price_per_bedroom.csv
	rm -f data/out/chicago_price_per_bedroom.csv
	rm -f figs/toronto.png
	rm -f figs/chicago.png
	rm -f figs/toronto-chicago.png
	rm -f figs/all.png
