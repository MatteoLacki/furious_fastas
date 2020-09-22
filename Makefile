ipython:
	python -m IPython
run_tests:
	rm -rf test_download
	mkdir -p test_download
	update_fastas test_download data/uniprot.txt
clean:
	rm -rf test_download

