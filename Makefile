.PHONY: deb clean

deb:
	dpkg-buildpackage -us -uc -b

clean:
	rm -rf build dist *.egg-info .debbuild
