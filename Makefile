install:
	pip uninstall scrapy_rclone -y
	python setup.py install

clear:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
