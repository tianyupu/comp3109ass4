# COMP3109 Assignment 4
============

## Resources
* [Graphviz user manual](http://www.graphviz.org/Documentation/dotguide.pdf)

## Compiling
Currently, to compile, use `run.sh` and the name of the example file.
```shell
  $ ./run.sh example.jmp
```

## Testing
Run the following command:
```shell
  $ ./test.py
```
This tests all of the files in tests

## Where stuff is
Unreachable code is removed within the `CFGraph/cfgraph.py` file within the function `remove_unreachable`

Jump elimination is also performed within the `CFGraph/cfgraph.py` file within the function `remove_jump`

Dead code elimination is performed in `CFGraph/deadcode.py` this is called in the `CFGraph/cfgraph.py` file with the function remove_dead.
