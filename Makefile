TORONTO_URL := "https://s3.amazonaws.com/tomslee-airbnb-data-2/toronto.zip"
CHICAGO_URL := "https://s3.amazonaws.com/tomslee-airbnb-data-2/chicago.zip"
YEAR := "2017"

.PHONY: all
all: figs/chicago.png figs/toronto.png figs/chicago-toronto.png

.SECONDARY:

data/raw data/merged data/out figs: 
	mkdir -p data/raw
	mkdir -p data/merged
	mkdir -p data/out
	mkdir -p figs

data/raw/toronto.zip data/raw/toronto: | data/raw
	curl -o data/raw/toronto.zip $(TORONTO_URL)
	cd data/raw \
		&& unzip toronto.zip \
		&& mv s3_files/toronto . \
		&& rmdir s3_files

data/merged/toronto.csv: data/raw/toronto src/merge_and_clean.py
	./src/merge_and_clean.py data/raw/toronto -y $(YEAR) -o data/merged/toronto.csv

data/out/toronto_price_per_bedroom.csv: data/merged/toronto.csv src/price_per_bedroom.py
	./src/price_per_bedroom.py data/merged/toronto.csv -o data/out/toronto_price_per_bedroom.csv

figs/toronto.png: data/out/toronto_price_per_bedroom.csv src/density_plot.py
	./src/density_plot.py data/out/toronto_price_per_bedroom.csv -o figs/toronto.png

data/raw/chicago.zip data/raw/chicago: | data/raw
	curl -o data/raw/chicago.zip $(CHICAGO_URL)
	cd data/raw \
		&& unzip chicago.zip \
		&& mv s3_files/chicago . \
		&& rmdir s3_files

data/merged/chicago.csv: data/raw/chicago src/merge_and_clean.py
	./src/merge_and_clean.py data/raw/chicago -y $(YEAR) -o data/merged/chicago.csv

data/out/chicago_price_per_bedroom.csv: data/merged/chicago.csv src/price_per_bedroom.py
	./src/price_per_bedroom.py data/merged/chicago.csv -o data/out/chicago_price_per_bedroom.csv

figs/chicago.png: data/out/chicago_price_per_bedroom.csv src/density_plot.py
	./src/density_plot.py data/out/chicago_price_per_bedroom.csv -o figs/chicago.png

figs/chicago-toronto.png: data/out/chicago_price_per_bedroom.csv data/out/toronto_price_per_bedroom.csv src/density_plot.py
	./src/density_plot.py data/out/chicago_price_per_bedroom.csv data/out/toronto_price_per_bedroom.csv -o figs/chicago-toronto.png

.PHONY: clean
clean:
	rm -f data/merged/toronto.csv
	rm -f data/merged/chicago.csv
	rm -f data/out/toronto_price_per_bedroom.csv
	rm -f data/out/chicago_price_per_bedroom.csv
	rm -f figs/toronto.png
	rm -f figs/chicago.png
	rm -f figs/toronto-chicago.png
