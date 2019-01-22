
import urllib.request

lines = open('urls.txt').readlines()

for line in lines:
	print("Downloading: images/{} {}".format(line.split('/')[-1].strip(), line))
	urllib.request.urlretrieve(line, "images/{}".format(line.split('/')[-1].strip()))