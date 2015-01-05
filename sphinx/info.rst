
.. _info:

=============================================================
Course information
=============================================================


Instructor
---------------

* `Prof. Randall LeVeque <http://faculty.washington.edu/rjl>`_

  * Office: Lewis 328 
  * netid for email: rjl
  * Office hours: TBA


Class meeting times
-------------------

* MW 3:30 - 4:20 pm in Johnson 026 for lectures.
* F 3:30-4:20 pm in Odegaard Library OUG 141 (This is an 
  `Active Learning Classroom <http://www.lib.washington.edu/ougl/learning-spaces/active-learning-classrooms>`_
  where we will work on computing projects.)


Discussion board
----------------

Registered students should be able to access the `Piazza discussion board 
<https://piazza.com/class/i4iq2zhewm74u9>`_.

Grading
-------

* Homework: 50%, midterm: 20%, final project: 25%, peer review activities: 5%
* See :ref:`homeworks` for more information and due dates.

.. _syllabus:

Recommended Background
----------------------

**Prerequisite:** Either AMATH 586 or permission of instructor.
Applied Math 585-6 or similar background is strongly recommended, i.e.
experience in numerical methods for differential equations, along with basic
understanding of partial differential equations.

Programming experience is also expected. Experience in Fortran and Python
would be most valuable but not required.

Experience with using git and GitHub would also be useful, but not required.

Textbook
--------

- R. J. LeVeque 
  `Finite Volume Methods for Hyperbolic Problems
  <http://faculty.washington.edu/rjl/book.html>`_, 
  Cambridge University Press, 2002.

- The `Clawpack Documentation <http://www.clawpack.org/>`_
  will also be very useful since we will be using
  this software extensively.

Goals
-----

- Master the basic theory of hyperbolic PDEs and nonlinear conservations
  laws, 
- Understand the development of high-resolution shock-capturing finite
  volume methods for solving these equations, 
- Learn about some applications of hyperbolic problems,
- Gain experience in using the Clawpack software for solving these
  equations, including how to set up a new problem,
- Learn the basics of Python programming and use of IPython notebooks,
- Become comfortable using Git and GitHub and learn about the development
  paradigm used for Clawpack and many other open source scientific codes.

Topics
--------

Some of the topics to be covered are listed below.
See also :ref:`outline`.

- Mathematical theory of linear and nonlinear systems of hyperbolic 
  PDEs and conservation laws.
    - Eigenstructure of Jacobian matrix.
    - Shock and rarefaction waves, contact discontinuities.
    - Phase plane analysis -- Hugoniot loci and integral curves.
    - Solution to the Riemann problem for linear and 
      nonlinear systems of equations.
    - Entropy functions and admissibility criteria.

- Theory of finite volume methods.
    - Upwind method, Godunov's method, use of true and approximate Riemann solvers.
    - High-resolution methods with limiters, TVD methods.
    - Review concepts from AMath 586 such as dissipation, dispersion, 
      Lax-Wendroff method, stability, CFL condition, etc.
    - Multi-dimensional finite volume methods on Cartesian and mapped grids
    - Adaptive Mesh Refinement (AMR)

- Use of Clawpack software
    - Setting up a problem, defining a Riemann solver.
    - Plotting solutions.
    - Experimenting with different methods.

- Applications such as
    - Linear advection, acoustics, and elasticity,
    - Nonlinear Burgers' equation, traffic flow,
    - Shallow water equations,
    - Euler equations of compressible gas dynamics.

