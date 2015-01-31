
.. _project_topics:

Possible project topics
-----------------------

See :ref:`projects` for general information about the course project.

There are many possible topics.  I suggest using the 
`Piazza discussion board <https://piazza.com/class/i4iq2zhewm74u9>`_
to suggest topics if you are looking for someone to work with.  Label your
post with the `project` tag.

Ideally a project will require 
reading at least one paper from the literature
and presenting a synopsis of the problem and solution, combined with some
computations to support this.  You are not expected to do original research
as part of the project, but it should involve ideas, algorithms, and/or
applications that go beyond what was covered in lectures and homeworks in 
some substantial way.  It could focus on exploring a different class of
algorithms and comparing to the wave-propagation algorithms we focused for
some set of test problems, or applying the Clawpack software to some novel
application (i.e. different than what's in the Clawpack examples and apps,
and that might require writing a new Riemann solver, for example). 

There are several chapters of the book we aren't covering in class, some of
these could form the basis for a project.

Below are a few ideas, with some references.  In many cases I've
referred to my own papers since these tend to use similar notation
and algorithms to what we will study in class, so these may be most
accessible, particularly for students who are new to this field.
But it would be great to explore the literature more broadly and
work through papers by other authors.  I've also given a couple
examples of papers where interesting problems are solved with other
methods and I think it would be interesting to compare with Clawpack.
There are countless other such papers of this nature, so feel free
to come up with papers on a different topic that you are interested
in --- you do not need to pick something from this list.

- Variable coefficient linear equations, e.g. acoustics or elasticity
  (perhaps in two space dimensions).  Chapter 9 could be used as a starting
  point.

- Nonlinear equations with spatially varying fluxes :math:`f(q,x)`.
  We will briefly discuss the "f-wave method" in class, but not in much
  detail and there are many things that could be tried.  
  Layered nonlinear media is one interesting example where the reflections
  at interfaces give rise to dispersion, which couples with the 
  nonlinearity to give solitary waves.
  Some references:

  - `<http://faculty.washington.edu/rjl/pubs/vcflux/index.html>`_
  - `<http://faculty.washington.edu/rjl/pubs/solitary/index.html>`_
  - `<http://faculty.washington.edu/rjl/pubs/layered2011/index.html>`_


- Compare different approximate Riemann solvers for gas dynamics, e.g.
  "exact", Roe, HLLE, perhaps consider other equations of state.

- Euler equations with "two-dimensional Riemann problem" data consisting
  of four constant states in the four quadrants of the plane.  `One such
  example <http://www.clawpack.org/gallery/gallery_classic_amrclaw.html#dimensional-euler-equations>`_ 
  is in the Clawpack gallery, but it would be nice to experiment with the
  numerous other examples presented in this paper:
  
  - `<http://epubs.siam.org/doi/abs/10.1137/0914082>`_.

- Adaptive mesh refinement (AMR) in one space dimension:  The amrclaw
  package includes 2d and 3d AMR but there is no 1d code.  Working on
  developing a simplified version in 1d would be a good way to really 
  understand how AMR works.

- Explore the accuracy and efficiency of dimensional splitting vs.
  unsplit wave-propatation algorithms, both of which will be discussed
  to some extent in class.  This is particularly interesting in
  three space dimensions where the unsplit algorithms are very
  expensive compared to dimensional splitting.

- The wave-propagation methods we are studying are at most second order
  accurate.  If higher-order polynomial reconstructions are used from the 
  cell averages at each step, together with suitable limiters, 
  it is possible to derive higher order shock-capturing methods, such as the
  class of WENO methods (Weighted Essentially Non-Oscillatory).  There's a
  big literature on these methods.  One implementation is incorporated in 
  PyClaw, but you might want to do your own to really understand these methods. 

  - See Chapter 9 for a brief introduction
  - `<http://faculty.washington.edu/rjl/pubs/sharpclaw2011/index.html>`_

- The Buckley-Leverett equation discussed briefly in Chapter 16 is a
  nonconvex scalar equation.  Explore multi-dimensional versions of this 
  used in modeling multiphase flow in porous media (e.g. a subsurface oil
  reservoir).

- Chapter 16 contains some other nonclassical systems and might give
  you some ideas.

- A one-dimensional model of shock wave chaos, exploring the equation
  proposed in 
  `<http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.104104>`_.

- Exploring some more complicated models of traffic flow, for example:

  - `<http://epubs.siam.org/doi/abs/10.1137/S0036139997332099>`_
  - `<http://faculty.washington.edu/rjl/pubs/traffic/index.html>`_

- Well-balanced methods for quasi-steady problems with source terms.
  This will be only briefly discussed in class.

  - `<http://faculty.washington.edu/rjl/pubs/wbfwave10/index.html>`_

- The chemotaxis problem in which bacteria move up the gradient of a 
  nutrient. This is an advection-reaction-diffusion equation and might
  involve using a fractional step approach,  e.g. 

  - `http://faculty.washington.edu/rjl/pubs/chemotaxis/index.html>`_

- The kitchen sink -- Figure 13.3 shows a "cartoon" of a stationary radial
  shock wave in the shallow water equations.  Properly solve this problem with
  radially symmetric 1d and/or full 2d equations.
  
  

