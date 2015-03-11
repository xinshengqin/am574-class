
.. _project_presentations:

Course Project Presentations
============================

Students will present :ref:`projects` in two sessions:

Wednesday, March 11, 4:00 - 5:00pm 
----------------------------------

In JHN 026

**4:00 - 4:20:** Krithika Manohar and Tommaso Buvoli

- TITLE: Introduction to WENO Methods
- ABSTRACT: Essentially non-oscillatory or ENO methods have historically
  proven successful at capturing shock discontinuities by choosing the
  smoothest interpolating polynomial at several neighboring stencils. Weighted
  ENO or WENO methods use a convex combination of the interpolating polynomial
  at all stencils and hence preserve both the high-resolution for shocks and
  high-order accuracy for smooth data.
  
  We implement and test these schemes on one-dimensional hyperbolic equations
  such as the advection and burgers equations with shocks. We will also
  include comparisons with \verb+clawpack+'s results for non-WENO schemes. We
  also plan to investigate the benefits of using Total Variation Diminishing
  (TVD) Runge-Kutta schemes versus traditional non-TVD integrators.

**4:20 - 4:40:** Qi Guo and Peng Zheng

- TITLE: Models of Traffic Flow with Discontinuous and Non-convex Flux
- ABSTRACT: 
  In this project, we investigate two models of traffic flow based on
  Lighthill-Whitham-Richards model. In the first part, we look into the
  model of traffic flow on freeway, where the flux function is discontinuous
  and piecewise linear. We utilize the method of mollification to smooth out
  the discontinuity, and construct the convex hull to solve the problem.
  Additionally, a numerical PDE solver in CLAWPACK and a ODE solver of
  car-following model are designed to simulate the results. In the second
  part, the car-following model of night-time driving is explored. With or
  without perturbing the velocities, we could observe the instability and
  clustering of cars with uniform initial density.

**4:40 - 5:00:** Kelsey Maass and Brisa Davis

- TITLE: Comparison of Two Second Order Traffic Flow Models
- ABSTRACT: 
  While the Lighthill-Whitham-Richards traffic flow model behaves well
  macroscopically, it does not accurately describe how vehicles travel
  through shocks. We compare two second order models, the Payne-Whitman
  model and the Aw-Rascle model, that attempt to improve the first order LWR
  model. Specifically, we demonstrate that the PW model's representation of
  traffic as a fluid ignores the anisotropic nature of cars, which leads to
  unrealistic results. Next we consider the AR model, which utilizes a
  convective derivative to resolve the problem of negative velocities
  present in the PW model. Through this talk we hope to highlight the fact
  that introducing higher order relations does not automatically improve the
  accuracy of modeling a given physical system, illustrating the importance
  of validation in modeling.
  



Friday, March 13, 3:30 - 5:30pm 
----------------------------------

In OUG 141 (Odegaard Library)

**3:30 - 3:50:** Saumya Sinha and Kenneth Roche

- TITLE: Adaptive Mesh Refinement for 1D Hyperbolic PDEs
- ABSTRACT: 
  We describe an adaptive mesh refinement algorithm that extends high
  resolution wave-progpagation techniques to hyperbolic systems in
  non-conservative form. The algorithm was implemented and tested for simple
  1D problems. Results are compared to static mesh solutions for the same
  problems.

**3:50 - 4:10:** Devin Light and Scott Moe

- TITLE: A p-Adaptive Discontinuous Galerkin Method for Hyperbolic Conservation
  Laws in 1D
- ABSTRACT: 
  Discontinuous Galerkin (DG) methods are becoming increasingly popular
  tools for the numerical integration of hyperbolic conservation laws. DG
  methods provide a natural extension of finite volume methods to higher
  orders while maintaining a compact stencil and exhibit a number of
  desirable computational features. However, as problems of larger and
  larger scopes are considered it is increasingly necessary to implement an
  adaptive method which devotes the finite degrees of freedom to where they
  are most needed in the domain. To that end we propose a novel p-adaptive
  DG scheme which uses a hierarchical basis and allows the degree of the
  local polynomial approximation to vary between cells. This method either
  adds or removes degrees of freedom for the next step in the integration
  based on the behavior of the coefficient of the highest degree polynomial
  basis present in the current approximation. The efficiency and accuracy
  performance of the proposed method will be measured against a non-adapting
  scheme on several standard tests.

**4:10 - 4:30:** Hai Zhu and Xin Yang

- TITLE: The f-wave method for nonlinear conservation laws with spatially varying flux
- ABSTRACT: 
  The wave-propagation form has been shown to be a nice way to implement the
  finite volume method for hyperbolic conservation laws. In this project we
  study one generalization of the standard wave-propagation method which
  decomposes the flux into waves of the eigenvectors of the Jacobian matrix
  rather than decomposing the conserved quantities. Computational
  experiments using the f-wave method are performed for 1D heterogeneous
  nonlinear elastic wave model.

**4:30 - 4:50:** Chris Uyeda and Alex Li

- TITLE: Convergence of Several Fixed Geometry Nozzles Using the Pseudo-1D
  Euler Equations

- ABSTRACT: 
  The pseudo-1D Euler equations will be used to simulate several different
  converging-diverging nozzle geometries and test each nozzles’ ability to
  converge to a steady state with a shock in the diverging section of the
  nozzle. Each simulation will use a fixed pressure ratio starting from a
  pressure reservoir and exhausting to the ambient environment. The location
  of the shock from simulations will be compared to the analytical quasi-1D
  solution derived from isentropic and shock relations in the nozzle. In
  addition to tracking the shock location, the flow property distribution
  will also be analyzed to ensure the expected physics of flow in a
  converging-diverging nozzle is satisfied.

**4:50 - 5:10:** Jacob Ortega-Gingrich and Chen Xin

- TITLE: Augmented approximate Riemann solvers for the shallow water equations with
  variable bathymetry
- ABSTRACT: 
  We describe an augmented Riemann solver for the one-dimensional shallow
  water equations with variable topography suggested by David George which
  addresses a number of the needs of applications involving flooding and
  small perturbations of delicate steady states. Fluid flows over varying
  topography, for example add a source term which the numerical method must
  balance with jumps in momentum and depth in order to preserve delicate
  steady states, such as an ocean at rest. Furthermore, applications
  involving flooding, such as the modeling of tsunami inundation, require a
  Riemann solver that can handle dry cells and preserve depth
  non-negativity. The augmented solver herein discussed satisfies these
  properties by amalgamating various aspects of existing solvers such as the
  HLLE solvers and f-wave approaches and the addition of a stationary steady
  state wave to account for the source term. Additionally, we discuss some
  specific techniques which may be use to handle various challenging
  situations which may arise in a model such as the handling of steep
  shorelines. Finally, we discuss an implementation of this augmented
  Riemann solver for the one-dimensional shallow water equations and present
  a few numerical demonstrations.


**5:10 - 5:30:** Kaspar Mueller and Shawn Qin

- TITLE: Hydraulic bore interaction with a column - A comparison between the
  solution of the shallow equation and experimental results
- ABSTRACT: 
  In this paper we compare the solution of the shallow water equations with
  experimental results. The experiment simulates the interaction between an
  incident bore and a free-standing coastal structure. The shallow water
  equations are solved using the CLAWPACK software. Three different cases
  are simulated and compared. In the first case, the column is removed. This
  is a simple dambreak problem and history of wave height and velocity at
  where column center should be are measured and compared. In the second
  case, a square column is set and wave height at some locations ahead the
  column are measured and compared. For the third case, the square column is
  replaced with a cylinder with the same data measured and compared. The
  discrepancy between geoclaw simulation and experiment results are also
  discussed and analyzed in a deep manner.
