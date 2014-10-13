import sys
import os
import dircache
import string
import stat

proto_dir = 'src/examples/example_prototype/'
target_dir = 'src/examples/'

def make_example(src_dir, dest_dir, projname):
  print("make", src_dir, dest_dir)
  try:
    os.mkdir(dest_dir)
  except:
    pass
  for fname in dircache.listdir(src_dir):
    mode = os.stat(src_dir + fname).st_mode
    if 'prototype' in fname:
      dest_name = string.replace(fname, 'prototype', projname)
    else:
      dest_name = fname
    print("fname", fname)
    if stat.S_ISDIR(mode):
      make_example(src_dir + fname + '/', dest_dir + '/' + dest_name + '/', projname)
    else:
      print(dest_dir + '/' + dest_name)
      try:
        test = open(dest_dir + '/' + dest_name, "rb")
        test.close()
      except:
        out = open(dest_dir + '/' + dest_name, "wb")
        for line in open(src_dir + fname):
          line = string.replace(line, 'prototype', projname)
          out.write(line)


num_args = len(sys.argv)

if num_args == 1 or "--help" in sys.argv:
  print("\nmakes or updates a new octet project in src/examples")
  print("\nusage: packaging\make_example.py projectname")
  exit()

for i in range(1,num_args):
  arg = sys.argv[i];
  if arg[0] != '-':
    make_example(proto_dir, target_dir + arg, arg)
  else:
    print("unrecognised option " + arg)
    exit()
