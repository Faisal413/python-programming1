<!--- Copied from https://github.com/GalvanizeDataScience/python-essentials-1/blob/master/1-using-conda.md (which not all students will have access to) -->
# Using Conda Environments


With conda, you can create, export, list, remove, and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file.

To see a list of environments, type `conda env list`. The `*` next to the name indicates the current environment.

```sh
$ conda env list

# conda environments:
#
base                  *  /home/chyld/.local/miniconda3
```

To create a new environment, use the `create` parameter. You need to specify the name of the environment as well as the version of python you would like to use. Here I am naming the environment `alpha` and will be using `python 3.5`.

```sh
$ conda create -n alpha python=3.5

#
# To activate this environment, use
#
#     $ conda activate alpha
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

To revert to the `base` environment, use `conda deactivate`. If you want to switch to the newly created environment, then use `conda activate <env name>`. After you `activate`, you are now inside the environment and can install any python package and version that you would like.

```sh
$ conda activate alpha
$ conda env list

# conda environments:
#
base                     /home/chyld/.local/miniconda3
alpha                 *  /home/chyld/.local/miniconda3/envs/alpha
```

I have switched to the `alpha` environment, and now am installing `numpy`. If I were to switch to another environment, `numpy` would only be there if it was explicitly installed. You can get a list of the packages in a conda environment by typing `pip list`. You can also use `conda list`.

```sh
$ pip install numpy
$ pip list

Package    Version
---------- ---------
numpy      1.18.5
```

You can have as many environments as you like. Below I am creating a new environment called `beta` that has a newer version of python, version `3.8`. I will then switch to that environment using `activate` and then install the `pandas` library. Finally we can do a `pip list` to ensure that `pandas` has been successfully installed into this new conda environment.

```sh
$ conda create -n beta python=3.8
$ conda activate beta
$ pip install pandas
$ pip list

Package         Version
--------------- -------------------
pandas          1.1.0
```

After creating the `beta` environment, I will create a third environment called `gamma` that is using `python 3.7`. In `gamma` I will install both numpy and pandas. And as you can see, when we perform a `pip list`, that indeed both packages have been successfully installed.

```sh
$ conda create -n gamma python=3.7
$ conda activate gamma
$ pip install numpy pandas
$ pip list

Package         Version
--------------- -------------------
numpy           1.19.1
pandas          1.1.0
```

Finally, to get a good look at all the environments we have created today, remember to use the `conda env list` command. As you notice there are four environments below, the default `base`, plus the three that we authored, `alpha`, `beta`, and `gamma`.

```sh
$ conda env list

# conda environments:
#
base                     /home/chyld/.local/miniconda3
alpha                    /home/chyld/.local/miniconda3/envs/alpha
beta                     /home/chyld/.local/miniconda3/envs/beta
gamma                 *  /home/chyld/.local/miniconda3/envs/gamma
```

To go back to the `base` environment, remember to use `conda deactivate`.
