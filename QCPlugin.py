#!/usr/bin/env python2

import sys
import argparse
import os
import subprocess
import glob

# Get a array of fastq file paths in provided directory
# Exits if none are found
def getFastqFiles(dir_path):
	# Get array of files to quality control
	fasta_files = glob.glob(
		os.path.join(dir_path, "*.fastq.gz"))

	if len(fasta_files) == 0:
		print("No fasta.gz files in directory")
		sys.exit(2)
	# print fasta_files
	return fasta_files


# Argument parser
#parser = argparse.ArgumentParser(
#	description="""
#		Performs quality control of fastq.gz files using the program fastq.
#		Creates reports in QC folder in provided directory.
#		""")

#parser.add_argument(
#	"dir",  # positional argument
#	help="Root data directory. Defaults to invoked working directory.",
#	default=os.getcwd(),  # parent working dir
#	nargs="?")  # optional number of arguments

#args = parser.parse_args()

class QCPlugin:
 def input(self, inputfile):
   self.fasta_files = getFastqFiles(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
  qc_dir = outputfile  

  cmd = ["fastqc"] + self.fasta_files + ["-t", "8", "-o", qc_dir]
  print(cmd)
  # blocking system execution
  subprocess.call(cmd)

