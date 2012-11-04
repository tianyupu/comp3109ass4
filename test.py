#!/usr/bin/python

import subprocess
import sys, os
from pipes import quote

# Configurations

# The directory containing the test programs
TEST_DIR = './tests'
# The extension for the test programs
PROG_EXT = '.jmp'
# The extension for checking the output of compile programs
TEST_EXT = '.out'

# Script for checking output of compiled program
OUTPUT_TEST_SCRIPT = './run.sh %(test)s | diff -b - %(test)s'+TEST_EXT

# Set to true to true for all tests
# Set to false for specified subset
ALL_TESTS = False
# Subset of tests
TESTS = [
  'basic.jmp',
  'basic2.jmp',
  'basic3.jmp',
  'basic4.jmp',
  'basic5.jmp',
  'changingVars.jmp',
  'complex.jmp',
  'complex2.jmp',
  'complex3.jmp',
  'complex4.jmp',
  'complex5.jmp',
  'complex6.jmp',
  'dead.jmp',
  'dead2.jmp',
  'dead3.jmp',
  'example.jmp',
  'extended_example.jmp',
  'manyJumps.jmp',
  'simpleJumps.jmp',
  'simpleJumps2.jmp',
  'simpleJumps3.jmp',
  'simpleJumps4.jmp',
  'simple_unreachable.jmp',
  'simple_unreachable2.jmp',
  'unreachable.jmp',
]


# Output to shell
class echo():
	def write(self, string):
		subprocess.call("echo -ne %s" % quote(string), shell=True)

sys.stdout = echo()

# Colour output
def blue(string):
	return "\e[1;34m"+string+"\e[0m"

def red(string):
	return "\e[1;31m"+string+"\e[0m"

def green(string):
	return "\e[1;32m"+string+"\e[0m"

# Test function
def run_tests(command, tests, mode="stderr", name="Test"):
  # Print the name of the tests
  print blue('\t'+name)
  
  # Get the width of the longest command
  width = len(command) + command.count('%(test)s')*max(map(len, tests))
  
  # Do the tests
  passed = 0
  for test in tests:
    call = command % {'test': test}
    print ('  $ %s' % call).ljust(width+10),
    
    # Run compilation and read for errors
    stdin, stdout, stderr = os.popen3(call)
    stderr = stderr.read()
    stdout = stdout.read()
    
    # Check results
    if ("stderr" in mode and stderr and "error" not in test) \
      or ("stderr" in mode and not stderr and "error" in test) \
      or ("stdout" in mode and stdout):
      print red("failed")
      
      if "stderr" in mode:
        print red(stderr)
      if "stdout" in mode:
        print stdout
    else:
      print green("passed")
      passed += 1
    
  print

  # Overall test results
  result = "  Passed %d of %d tests" % (passed, len(tests))
  if passed == len(tests):
    print green(result)
  else:
    print red(result)
  
  print

# Begin tests...
print blue('Testing Jump grammar')

# Get a list of the test programs
if ALL_TESTS:
  tests = [os.path.join(TEST_DIR, f[:-4]) for f in os.listdir(TEST_DIR) if f[-4:]==PROG_EXT]
else:
	tests = [os.path.join(TEST_DIR, f) for f in TESTS]

# Output tests
run_tests(OUTPUT_TEST_SCRIPT, tests, ["stderr", "stdout"], "Output tests")

