
import numpy as np
from scipy.optimize import fsolve


def exact_riemann_solution(q_l, q_r, grav=9.81):
    """Return the exact solution to the Riemann problem with initial states q_l, q_r.
       The solution is given in terms of a list of states, a list of speeds (each of which
       may be a pair in case of a rarefaction fan), and a function reval(xi) that gives the
       solution at a point xi=x/t.
       
       The input and output vectors are the conserved quantities.
    """
    h_l = q_l[0]
    hu_l = q_l[1]
    u_l = hu_l / h_l  # assumes h_l != 0

    h_r = q_r[0]
    hu_r = q_r[1]
    u_r = hu_r / h_r  # assumes h_r != 0

    # Compute left and right state sound speeds
    c_l = np.sqrt(grav*h_l)
    c_r = np.sqrt(grav*h_r)
    
    
    # Define the integral curves and hugoniot loci
    integral_curve_1   = lambda h : h*u_l + \
            2*h*(np.sqrt(grav*h_l) - np.sqrt(grav*h))
    integral_curve_2   = lambda h : h*u_r - \
            2*h*(np.sqrt(grav*h_r) - np.sqrt(grav*h))
    hugoniot_locus_1 = lambda h : h_l*u_l + (h-h_l)*(u_l - \
            np.sqrt(grav*h_l*(1 + (h-h_l)/h_l) * (1 + (h-h_l)/(2*h_l))))
    hugoniot_locus_2 = lambda h : h_r*u_r + (h-h_r)*(u_r + \
            np.sqrt(grav*h_r*(1 + (h-h_r)/h_r) * (1 + (h-h_r)/(2*h_r))))
    
    # Check whether the 1-wave is a shock or rarefaction
    def phi_l(h):        
        if h>=h_l: return hugoniot_locus_1(h)
        else: return integral_curve_1(h)
    
    # Check whether the 2-wave is a shock or rarefaction
    def phi_r(h):
        if h>=h_r: return hugoniot_locus_2(h)
        else: return integral_curve_2(h)
        
    phi = lambda h : phi_l(h)-phi_r(h)

    # Compute middle state h, hu by finding curve intersection
    h_m,info, ier, msg = fsolve(phi, (h_l+h_r)/2.,full_output=True,xtol=1.e-14)
    # For strong rarefactions, sometimes fsolve needs help
    if ier!=1:
        h_m,info, ier, msg = fsolve(phi, (h_l+h_r)/2.,full_output=True,factor=0.1,xtol=1.e-10)
        # This should not happen:
        if ier!=1: 
            print 'Warning: fsolve did not converge.'
            print msg

    hu_m = phi_l(h_m)
    u_m = hu_m / h_m
    
        
    # compute the wave speeds
    ws = np.zeros(4)
    
    # Find shock and rarefaction speeds
    if h_m>h_l: 
        ws[0] = (hu_l - hu_m) / (h_l - h_m)
        ws[1] = ws[0]
    else:
        c_m = np.sqrt(grav * h_m)
        ws[0] = u_l - c_l
        ws[1] = u_m - c_m

    if h_m>h_r: 
        ws[2] = (hu_r - hu_m) / (h_r - h_m)
        ws[3] = ws[2]
    else:
        c_m = np.sqrt(grav * h_m)
        ws[2] = u_m + c_m
        ws[3] = u_r + c_r
                
    # Find solution inside rarefaction fans (in primitive variables)
    def raref1(xi):
        RiemannInvariant = u_l + 2*np.sqrt(grav*h_l)
        h = (RiemannInvariant - xi)**2 / (9*grav)
        u = xi + np.sqrt(grav*h)
        hu = h*u
        return h, hu
        
    def raref2(xi):
        RiemannInvariant = u_r - 2*np.sqrt(grav*h_r)
        h = (RiemannInvariant - xi)**2 / (9*grav)
        u = xi - np.sqrt(grav*h)
        hu = h*u
        return h, hu

    q_m = np.squeeze(np.array((h_m, hu_m)))
    
    states = np.column_stack([q_l,q_m,q_r])
    speeds = [(ws[0],ws[1]),(ws[2],ws[3])]

    def reval(xi):
        rar1 = raref1(xi)
        rar2 = raref2(xi)
        h_out = (xi<=speeds[0][0])*h_l + \
            (xi>speeds[0][0])*(xi<=speeds[0][1])*rar1[0] + \
            (xi>speeds[0][1])*(xi<=speeds[1][0])*h_m +  \
            (xi>speeds[1][0])*(xi<=speeds[1][1])*rar2[0] +  \
            (xi>speeds[1][1])*h_r
        hu_out = (xi<=speeds[0][0])*hu_l + \
            (xi>speeds[0][0])*(xi<=speeds[0][1])*rar1[1] + \
            (xi>speeds[0][1])*(xi<=speeds[1][0])*hu_m +  \
            (xi>speeds[1][0])*(xi<=speeds[1][1])*rar2[1] +  \
            (xi>speeds[1][1])*hu_r
        return h_out, hu_out

    return states, speeds, reval
