
.. _lab5:

Lab 5: Friday, Feb. 6, 2015
=============================


The directory `$AM574/labs/lab5/burgers` contains sample code to solve Burgers'
equation.  

Copy this directory to some other location so that you can edit file and play
around with it.

Some notes
----------

- For help with plotting, see the `VisClaw documentation
  <http://www.clawpack.org/contents.html#visclaw-plotting-and-visualization-tools>`_

- The command::

      $ make .plots

  should create a subdirectory `_plots` containing png and html files.
  This checks dependencies, so it may first compile and run the code.

- On SMC, to view the html files, see :ref:`smc_view_html`.

- Alternatively you can step through the frames from an IPython shell, see
  `Interactive plotting with Iplotclaw 
  <http://www.clawpack.org/plotting_python.html#interactive-plotting-with-iplotclaw>`_
    
- The file `qinit.f` contains the initial conditions.  This is in 
  old-style fixed format fortran, which means that executable
  statments must start in column 7 or greater and anything after
  column 72 is ignored!  A 'c' in the first column indicates a
  comment. A character in column 6 indicates a continuation line.
  Labels must be in columns 2 through 5.  This format dates from the 
  days of `punch cards
  <http://faculty.washington.edu/rjl/classes/am583s2014/notes/punchcard.html#punchcard>`_.

- The file `rp1_burgers.f90` contains the Riemann solver, including an "entropy
  fix" when `efix = .true.`.  This is in modern Fortran style (indicated by the
  `.f90` rather than `.f`).  There are fewer restrictions on what columns must
  be used.  The `!` character must be used for comments.  A `&` character at
  the end of a line indicates the next line is a continuation.

- The parameter `beta` used in defining the initial conditions follows a
  convoluted path:

  - The value is assigned in `setrun.py`
  - Doing `make .data` takes the input in `setrun.py` and creates data files
    `*.data`.  The `setprob.data` file contains the problem-dependent parameter
    `beta`.  (Doing `make .output` checks dependencies so if you changed
    `setrun.py` it will automatically also remake the `*.data` files.)
  - Doing `make .output` runs the fortran code.  The subroutine `setprob`
    is called before `qinit` is called.  The code in `setprob.f` reads
    `beta` from `setprob.data` and stores it in a "common block" named
    `comic`.  (This is the old-style Fortran way of declaring a global
    variable.)  
  - The subroutine `qinit` also has a line declaring this same common block
    and so the value of `beta` is available for use.



Try the following:
------------------

- Experiment with the input and see how the solution changes.  Some things you
  might try:

  - Change the number of grid points,
  - Go out to a later time
  - Try different methods, e.g. upwind or Lax-Wendroff by adjusting
    `clawdata.order` or `clawdata.limiter` in `setrun.py`.

- Change the initial conditions by adding a line::

     q(1,i) = q(1,i) - 0.5d0

  to `qinit.f` just before the `150 continue` statement.
  Run the code and observe the solution.  (You will have to adjust 
  `plotaxes.ylimits` in `setplot.py`).

- Now try the same problem after setting::

    efix = .false.

  in `rp1_burgers.f90`.  What do you observe?

- You might also try shifting the initial data by `0.3d0` rather than `0.5d0`.


