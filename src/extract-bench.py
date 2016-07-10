import os
import sys

def PrintUsage():
  print """
Usage:
  python extract-bench.py <source-directory>

  or

  python extract-bench.py <source-directory> <bench-directory>
"""
  exit(1)

def extract(source, bench):
	TYPE_JSDOC = '@type'
	log_path = '/home/aliu/Research/More/Projects/js-infer/log/bench.log'
	log = open(log_path, 'a+')
	for root, _, files in os.walk(source):
		for f in files:
			fname = os.path.join(root, f)
			if fname.endswith('.js'):
				source_file = open(fname, 'r')
				code = source_file.read()
				num = code.count(TYPE_JSDOC)
				if num > 0:
					record = fname + "    " + str(num) + '\n'
					log.write(record)
				source_file.close()
				print fname + "    " + str(num)
	log.close()

if __name__ == '__main__':
	if len(sys.argv) is 3:
		extract(sys.argv[1], sys.argv[2])
	else:
		PrintUsage()