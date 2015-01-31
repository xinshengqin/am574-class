
.. _software_installation:

=============================================================
Downloading and installing software for this class
=============================================================

See :ref:`smc` for some information on using SageMathCloud as an alternative
to installing software on your own computer.

.. _install_git:

Git
---

We will use the Git version control language for various purposes:

- To distribute computer code and other materials through the class
  repository,
- To make sure you have an up-to-date version of Clawpack, which might
  be updated during the quarter. 
- To submit homework.
- To collaborate with other students on a class project.

There are many resources for learning to use Git.  You might start with 
the GitHub `Set Up Git <https://help.github.com/articles/set-up-git/>`_
page, which includes information on how to install it.

See the `Clawpack git
resources page <http://www.clawpack.org/git_resources.html>`_ for more links
to tutorials, etc.

The `Clawpack Developers' Guide <http://www.clawpack.org/developers.html>`_
has some information about our standard development procedure with Git.

See :ref:`class_repos` for information on cloning the class repository.

.. _install_clawpack:

Clawpack
--------

We will use Clawpack extensively in this class.  To insure you have the
latest version and to make it easy to incorporate changes during the
quarter, I suggest installing by cloning the Github repositories, following
the instructions `here
<http://www.clawpack.org/developers.html#setup-dev>`_.

If you already have a version of clawpack installed you might want to give
the version you clone a new name, e.g. *clawpack_am574*.  Here's how you'd
do that::

    # cd to the directory where you want *clawpack_am574* to reside
    git clone git://github.com/clawpack/clawpack.git clawpack_am574
    cd clawpack_am574
    python setup.py git-dev

To run any Fortran codes or use various Python tools, you will need to 
set your environment variables, e.g. for the bash shell::

    export CLAW=/path/to/clawpack_am574
    export PYTHONPATH=$CLAW

or append to your current PYTHONPATH if it's already set, via::

    export PYTHONPATH=$PYTHONPATH:$CLAW

In these notes and the Clawpack documentation, `$CLAW` will be used to
indicate the path to your top level Clawpack diretory.

Note that the "python setup.py git-dev" step above will clone a number of
other repositories under `$CLAW`.

For this class, you should also clone the `Clawpack Applications repository
<http://www.clawpack.org/apps.html>`_,  which in
particular contains codes that go along with the textbook::

    cd $CLAW
    git clone git://github.com/clawpack/apps


Later in the quarter we will discuss how to fork the repositories to your
own account if you want to be able to fix bugs or add new features and then
issue pull requests.

.. _install_fortran_python:

Fortran and Python
------------------

A recent version of `gfortran` or other Fortran compiler should be fine.

We will use Python 2.x (not 3.x).  I recommend the 
`Anaconda distribution <http://continuum.io/downloads>`_
of Python 2.7 since this contains a long 
`list of packages <http://docs.continuum.io/anaconda/pkg-docs.html>`_,
including the latest version of the IPython notebook, matplotlib, etc.



See also:

- `Clawpack Installation Prerequisites
  <http://www.clawpack.org/installing.html#installation-prerequisites>`_

- `Downloading and installing software
  <http://faculty.washington.edu/rjl/classes/am583s2014/notes/software_installation.html>`_
  page from AMath 583 last spring, which has some other tips.


.. _install_test:

Testing your Clawpack installation
----------------------------------

If everything is working properly, you should be able to do the following::

    cd $CLAW/classic/examples/acoustics_1d_example
    make .exe  # should compile the code
    make .output  # should run the code
    make .plots   # should plot the results
    
then you should be able to open the file `_plots/_PlotIndex.html` in a web
browser and view the results.

To test if IPython notebooks are working properly, try the following
example.  

**Note:** The notebook below uses some modifications that are not in the
latest release of Clawpack but are in the *master* branch. 
You should be able to do this to get what's needed::

    cd $CLAW/clawutil
    git checkout master
    git pull  # will probably say it's up to date if you cloned recently

    cd $CLAW/visclaw
    git checkout master
    git pull  # will probably say it's up to date if you cloned recently

The notebook below has not yet been merged into the master branch of the `apps`
repository, so you'll have to check out a different branch::

    cd $CLAW/apps
    git checkout notebook_experiments  

    cd $CLAW/apps/notebooks/classic/advection_1d
    ipython notebook advection_1d.ipynb

You should be able to execute all cells (one at a time by repeatedly hitting
`Shift-Enter`, or all of them by choosing `Run All` from the `Cell` menu at
the top.  

The resulting notebook should look like this:
`view via nbviewer
<http://nbviewer.ipython.org/url/faculty.washington.edu/rjl/notebooks/advection_1d/advection_1d.ipynb>`_

