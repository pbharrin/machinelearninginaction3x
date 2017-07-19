Some guidelines to help install dependencies.

# Unix Installation
```
# Install pip3 for Python3
sudo apt-get install python3-pip

# Virtualenv installation (Optional, but recommended)
sudo apt-get install virtualenv
```

# Running virtualenv
```
virtualenv -p python3.5 env --no-site-packages

# activate virtualenv
source env/bin/activate

# deactivate virtualenv
deactivate
```

# Package Installation:
## Option 1: Using virtualenv to install packages locally to our directory (Recommended).
Instead of installing our packages globally, we can install our packages locally with virtualenv.

```
# Virtual env
source env/bin/activate
pip3 install numpy
pip3 install matplotlib
```

We can verify the package installation by checking our virtual directory named 'env'.
```
# Verify for numpy package installation
find './env/lib/python3.5/site-packages/' -name 'numpy'
# Verify for matplotlib package installation
find './env/lib/python3.5/site-packages/' -name 'matplotlib'

# Our output should look something like this:
# ./env/lib/python3.5/site-packages/numpy
# ./env/lib/python3.5/site-packages/numpy/core/include/numpy

# ./env/lib/python3.5/site-packages/matplotlib
```

Install Tkinter to resolve a dependency for matplotlib.

```
# Required for `import matplotlib.pyplot as plt`
sudo apt-get install python3-tk
```

# Option 2: Installing our packages globally (Required if virtualenv is not installed).
Alternatively, we could install our packages globally.

```
sudo pip3 install numpy
sudo pip3 install matplotlib
```

Install Tkinter to resolve a dependency for matplotlib.

```
# Required for `import matplotlib.pyplot as plt`
sudo apt-get install python3-tk
```


# Sample run
We shoud be good to run application code.
Here's an sample code execution:
```
cd Ch04/
unzip email
python3 ./Ch04/bayes.py
```

Congrats, we've got everything all setup!

----------------------
Notes on Chapter Installations:
* Chapter 04  may alternatively use pip3 to install feedparser: `pip3 install feedparser`
