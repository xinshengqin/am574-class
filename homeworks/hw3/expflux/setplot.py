
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

def qtrue(x,t):
    """
    Evaluate and return the true solution.  
    x is a numpy array,  
    t is the scalar time
    """
    from numpy import exp, log, zeros, where, logical_and
    
    ts = 2./(exp(2.)+1)  # time rarefaction catches shock
    q = zeros(x.shape)
    q = where(x<t, q, log(x/t))  # rarefaction for x>t, ignoring shock
    if t<ts:
        q = where(x<exp(2)*t, q, 2.) # flat top
        q = where(x < 1+t*(exp(2)-1)/2., q, 0.)  # cut off at shock
    else:
        # cut off at shock, avoiding evaluating log at invalid arguments:
        q = where(logical_and(x>0, x*log(x/t) - x + t > 2), 0., q)
    return q


#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    plotdata.clearfigures()  # clear any old figures,axes,items data



    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='q[0]', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes(name='Solution')
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = [-0.1, 2.1]
    plotaxes.title = 'q[0]'

    def plot_qtrue(current_data):
        from pylab import linspace, plot, legend
        x = current_data.x  # computational grid
        xx = linspace(x.min(), x.max(), 1000)  # fine grid for plotting
        t = current_data.t  # time for this plot
        qq = qtrue(xx,t)
        plot(xx,qq,'r')
        legend(['computed','true'])  # clawpack solution plotted first
    plotaxes.afteraxes = plot_qtrue

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(name='solution', plot_type='1d')
    plotitem.plot_var = 0
    plotitem.plotstyle = '-o'
    plotitem.color = 'b'

    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?
    
    return plotdata

