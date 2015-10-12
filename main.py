#    flifcrush - tries to reduce FLIF files in size
#    Copyright (C) 2015  Matthias Krüger

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 1, or (at your option)
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA  02110-1301 USA


import subprocess
import sys
import os

__author__ = 'Matthias "matthiaskrgr" Krüger'

#print(os.environ['FLIF'])


INFILE="/home/matthias/vcs/git/freedroid/graphics/obstacles/obstacles_atlas1.png"

for N in list(range(30)):
	proc = subprocess.Popen(['/home/matthias/vcs/github/FLIF/flif','-r', str(N), INFILE, '/dev/stdout'], stdout=subprocess.PIPE)
	if (N == 0): #first run, initialize
		N_best=0
		output_best = proc.stdout.read()
		size_best = sys.getsizeof(output_best)
		print("run {run}, size {size} b".format(run=N, size=size_best))
		continue

	output = proc.stdout.read()
	size = sys.getsizeof(output)

	if (size_best > size): # new file is smaller
		output_best = output
		print("run {run}, size {size} b, better than {run_best} ({size_best} b; -{size_change} b)".format(run=N, size=size, run_best=N_best, size_best=size_best, size_change=size_best-size))
		N_best = N
		size_best = size

	else:
		print("run {run}, size {size} b".format(run=N, size=size))
		#break  //determine whether it is save to break out of loop here





# write final best file
file = open("/tmp/out_final.flif", "wb")
file.write(output)
file.close()
