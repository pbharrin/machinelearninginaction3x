Machine Learning in Action 3.X
==========================

This is the source code to go with "Machine Learning in Action"
by Peter Harrington published by Manning Inc, for Python 3.X.
The official page for this book can be found here: http://manning.com/pharrington/

Help is needed to convert these code examples from Python 2.X to Python 3.X.  Contributors will be thanked in the second edition of the book, unless they opt out.

The source code is getting cleaned up at the same time.  For example in the original code everything was imported from NumPy with: `from numpy import *`.  I did that to save space in the source code, however it sacrificed readability.  People didn't know if a method I was using came from NumPy or Python builtin function.  A better approach would have been to use the statement `import numpy as np`.  This adds three characters to every NumPy funciton but at least people will know where this function is coming from.

Converting Python 2.X to 3.X https://docs.python.org/2/library/2to3.html
Setting up a virtual env with Python 3 http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html

You will need numpy to run the examples in this book.  To install NumPy do the following:
`pip3 install numpy`.  Pip3 and Pip may be the same (they are the same in my Virtual env, so you may only need to run `pip install numpy`.  Check the paths of with `which pip` and `which pip3`.

Chapters currently working with Python 3.X:
 - ch2   done by YoungSeon.Ahn
 - ch3   done by YoungSeon.Ahn
 - ch4   done by Angel Ortega
 - ch5   done by Adam Yang
 - ch6   done by shenyyi
 - ch7   done by shenyyi
 - ch8   done by shenyyi
 - ch9   done by shenyyi
 - ch10   done by shenyyi
 - ch11   done by shenyyi
 - ch12   done by shenyyi
 - ch13   done by shenyyi
 - ch14   done by shenyyi
