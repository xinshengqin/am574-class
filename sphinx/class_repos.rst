
.. _class_repos:

Class GitHub Repository
=======================

All of the files that you may need to access for this class will be pushed
to the GitHub repository `amath574w2015/am574-class 
<https://github.com/amath574w2015/am574-class>`_.

To clone this repository::

    git clone https://github.com/amath574w2015/am574-class.git

This will create a directory `am574-class`.  


To update
---------

If new files have been added to the class repository, you can get them by
doing::

    cd am574-class  # or you may need to give the full path
    git pull


To avoid having to worry about
conflicts if you change a file and the same file changes in the repository,
I suggest that you never modify the files in this directory.  Instead, copy
any files you need to some other place before working with them, e.g. ::

    cp -r am574-class/homeworks/hw1  /someplace/else

will recursively copy the directory `hw1` to someplace else (you'll need a
valid path here).

Then modify the files in the new `hw1` directory.

Stayed tuned for instructions on pushing your results back to GitHub.


