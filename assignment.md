# Python Programming 1 Assignment

### Part 1: Fill in functions

Fill in the functions in [src/functions.py](./src/functions.py) according to their docstrings.

To try out your code and see if it works, import the functions you want to run inside of `main.py`. Then just execute your file by using `python main.py`.

**Note on docstrings:** Writing a docstring for each function you write is a best practice you should get in the habit of following. Docstrings are important for helping users (including your future self) understand what your functions do, *but* writing it **before** you start coding can also help you get clear about how you things will fit together. Think of this as an intermediate step in the process: an idea in your head, *task written in English*, and your final Python code.

The docstrings in functions.py are written in the style of NumPy docstrings, this format is a good one to emulate (though employers often have their own style guides for this.)

### Part 2: Importing code locally

As you start to build up your personal code base, you will want to use your functions and classes across different files. You do so by using `import`. Sometimes people run into errors when importing across files in different directories. So let's walk through that process.

Start by creating an empty folder on your desktop called 'python-programming'. Within that create two empty directories, one called 'scripts' and the other  'pkgs'. Within the 'scripts' directory, create a file named 'example.py'. In the 'pkgs' directory create another directory called 'example_pkg' and in there you need two files: '\_\_init\_\_.py' (which is an empty file that Python looks for when accessing modules within packages), and 'functions.py' from Part 1.

Here is the layout of your files:

- `python-programming`
    - `pkgs`
        - `example_pkg`
            - `__init__.py`
            - `functions.py`
    - `scripts`
        - `example.py`

Now we’re done with creating our package. We have a module `functions` in our package `example_pkg`. See this [tutorial](https://docs.python.org/3/tutorial/modules.html#packages) for more details on this structure.

We want to use this module in our new script in 'example.py'. To do so, add this code 'example.py':

```python
from example_pkg import functions


if __name__ == "__main__":
    print(functions.lowercase_text('ADVANCED PYTHON PROGRAMMING'))
    print(functions.remove_punctuation('ADVANCED_PYTHON_PROGRAMMING!!!!'))
    print(functions.most_common_letters('advanced python programming'))
    print(functions.merge_dictionaries({"python": 6, "programming": 11}, {"python": 12, "programming": 22}))
```

Now our program is complete and let’s try running 'example.py' from the 'python-programming' directory.

$ `python scripts/example.py`

As expected, we get an error because Python is unable to locate the module that we’re trying to import. This is a common problem that occurs when trying to access packages stored in different directories and locations.

#### Use PYTHONPATH to set the path to our packages

The most straight-forward solution is to use the PYTHONPATH environment variable and set it equal to the path to our packages. This will allow us to create and save all of our packages in one location, and import them directly into our projects.
To do this, we just have to set the environment variable.

**Windows**: search 'env' and click 'Edit the system environment variables' option. Next, click 'Environment Variables':

Under 'User variables' click 'New'. Variable name is equal to `PYTHONPATH` and variable value will be equal to the path to our packages, for example, 'C:\Users\username\Desktop\python-programming\pkgs'.

**Linux/Mac**: the easiest is to update the '.bashrc' or '.zshrc' (depending if you are running bash or zsh) file in your home directory to add the path. For example:

$ `nano ~/.bashrc`

will open this file using the light-weight, in-terminal text editor 'nano'. Then anywhere in that file (feel free to use the text editor of your choice), write:
`export PYTHONPATH='/Users/username/Desktop/python-programming/pkgs'`

Again, replacing above with the path to your packages and the username with our username. Then save and quit with `ctrl+x`, `y`, `enter`.

Last, to activate the new changes in `~/.bashrc`, do the following

$ `source ~/.bash_profile`

#### Run example.py

Before running example.py’ again, we have to close and reopen whatever command line we’re using, so that our environment gets updated. Then, run the file again:

$ `python scripts/example.py`

Everything should run as expected this time. From here, we can create and add any additional packages or modules filled with methods, classes, or variables and import them into any file we are working from in any directory with a simple import statement.

We can also change the path for `PYTHONPATH` if we chose to move everything to a different location or rename the directory to something else.


### Part 3: Install and use python modules

In addition to writing our own packages and modules, we will want to make use of the wide range to tools written by others.

Hopefully you are working with an Anaconda or Miniconda installation of Python and one of the main benefits of doing so is that it can help you manage these libraries. For example, an Anaconda installation comes with a large number of libraries that are relevant to doing data science with Python.

Inevitably however, you will want to use a library that is not already installed on your machine and it is important to be consistent with how you install these so you avoid problems like the path issues we saw in Part 2.

The main way to install libraries to your Anaconda installation is with `conda install`. You can search for packages that are available to install at [anaconda.org](https://anaconda.org/).

[SciPy](https://docs.scipy.org/doc/scipy/reference/api.html) is a large library with many different modules useful to data scientists. For practice installing/importing/using libraries, we'll use SciPy's stats module.

1. Install SciPy with `conda install scipy` in your terminal. (Your computer may already have SciPy installed, in this case running this command will cause it to check for any updates to the library and its dependencies.)

2. When starting to familiarize yourself with a new library you will usually want to run Python interactively, so open a jupyter notebook and import the stats module as follows: `from scipy import stats`. This imports the `stats` module, rather than the entire library. It is good practice to only import the modules you will be using from a library, especially when they are big like SciPy.

3. In order to generate some data to use in statistics calculations, let's use the [`random`](https://docs.python.org/3/library/random.html) library (which is part of the Python Standard Library, so does not need to be installed separately). Import `random` and use the `uniform` function to generate a random number between 1 and 10. (You may want to look at its docstring, recall that typing Shift-Tab after the function name should bring this up in a notebook.)

4. Put 100 random numbers from `uniform` into a list.

5. Call `stats.describe` on your list. Do you understand what this function has returned? Are the results what you would expect? Again, you may want to look at this function's docstring.

#### `conda` versus `pip`

If you have installed Python packages before, you may have used `pip` to do so. Generally, if a package is available with `conda` it will make your life easier to stick with it, and thousands of the most popular packages in data science are available. However, *hundreds of thousands* of packages are installable with `pip`, so sometimes you will need to use it instead. When packages are installed from different sources, they don't always communicate properly (more details [here](https://www.anaconda.com/blog/understanding-conda-and-pip)).

Probably the most important practice to follow when using package(s) that you installed with `pip` is to create and develop your code in a separate conda environment (more on best practices [here](https://www.anaconda.com/blog/using-pip-in-a-conda-environment)).

6. Choose a package to install with `pip`. You can find everything that's available at [PyPI.org](https://pypi.org/). BEFORE INSTALLING, create a new conda environment. You should name your environment in a way that is relevant to the package you're going to install. If you need a refresher on how to do this, refer to [these notes](./conda-notes.md).

7. Connect to your new environment and then `pip` install your chosen package.

8. Write a script that makes use of this new package with `import`. Bonus points: also import functions that you created yourself, following the flow from Part 2.

9. Deactivate this new conda environment.
