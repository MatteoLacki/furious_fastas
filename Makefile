ipython:
	python -m IPython
run_tests:
	mkdir test_download
	update_fastas test_download data/uniprot.txt
clean:
	rm -rf test_download
