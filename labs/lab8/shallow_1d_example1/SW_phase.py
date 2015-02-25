
import numpy as np

#g = 1.  # gravitational constant used in book
g = 9.81

def integral_curve(h, hstar, hustar, wave_family):
    """
    Return hu as a function of h for integral curves through 
    (hstar, hustar).
    """

    ustar = hustar / hstar
    if wave_family == 1:
        hu = h*ustar + 2*h*(np.sqrt(g*hstar) - np.sqrt(g*h))
    else:
        hu = h*ustar - 2*h*(np.sqrt(g*hstar) - np.sqrt(g*h))
    return hu


def hugoniot_locus(h, hstar, hustar, wave_family):
    """
    Return hu as a function of h for the Hugoniot locus through 
    (hstar, hustar).
    """
    ustar = hustar / hstar
    alpha = h - hstar
    d = np.sqrt(g*hstar*(1 + alpha/hstar)*(1 + alpha/(2*hstar)))
    if wave_family == 1:
        hu = hustar + alpha*(ustar - d)
    else: 
        hu = hustar + alpha*(ustar + d)
    return hu

    
def phase_plane_curves(hstar, hustar, state, wave_family='both'):
    """
    Plot the curves of points in the h - hu phase plane that can be connected to (hstar,hustar).
    state = 'qleft' or 'qright' indicates whether the specified state is ql or qr. 
    wave_family = 1, 2, or 'both' indicates whether 1-waves or 2-waves should be plotted.
    Colors in the plots indicate whether the states can be connected via a shock or rarefaction.
    """
    import matplotlib.pyplot as plt
    
    h = np.linspace(0, hstar, 200)

    if wave_family in [1,'both']:
        if state == 'qleft':
            hu = integral_curve(h, hstar, hustar, 1)
            plt.plot(h,hu,'b', label='1-rarefactions')
        else:
            hu = hugoniot_locus(h, hstar, hustar, 1)
            plt.plot(h,hu,'r', label='1-shocks')
    
    if wave_family in [2,'both']:
        if state == 'qleft':
            hu = hugoniot_locus(h, hstar, hustar, 2)
            plt.plot(h,hu,'g', label='2-shocks')
        else:
            hu = integral_curve(h, hstar, hustar, 2)
            plt.plot(h,hu,'m', label='2-rarefactions')

    h = np.linspace(hstar, 5, 200)

    if wave_family in [1,'both']:
        if state == 'qright':
            hu = integral_curve(h, hstar, hustar, 1)
            plt.plot(h,hu,'b', label='1-rarefactions')
        else:
            hu = hugoniot_locus(h, hstar, hustar, 1)
            plt.plot(h,hu,'r', label='1-shocks')
    
    if wave_family in [2,'both']:
        if state == 'qright':
            hu = hugoniot_locus(h, hstar, hustar, 2)
            plt.plot(h,hu,'g', label='2-shocks')
        else:
            hu = integral_curve(h, hstar, hustar, 2)
            plt.plot(h,hu,'m', label='2-rarefactions')  
            
    # plot and label the point (hstar, hustar)
    plt.plot([hstar],[hustar],'ko',markersize=5)
    plt.text(hstar + 0.1, hustar - 0.2, state, fontsize=13)

        
def make_axes_and_label(x1=-.5, x2=6., y1=-2.5, y2=2.5):
    import matplotlib.pyplot as plt
    plt.plot([x1,x2],[0,0],'k')
    plt.plot([0,0],[y1,y2],'k')
    plt.axis([x1,x2,y1,y2])
    plt.legend()
    plt.xlabel("h = depth",fontsize=15)
    ylabel("hu = momentum",fontsize=15)
