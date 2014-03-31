import os
from numpy import *
import pylab as pl
 
iterations = 100 # number of iterations
density = 2000 # density of the grid
 
# fractal range
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

x_min, x_max = -0.2738, -0.1923
y_min, y_max = -0.05, 0.05

x_min, x_max = -0.5, 0.5
y_min, y_max = -0.25, 0.25


# x, y are matrices containing the real and imaginary parts 
# of all z values in the grid
x, y = meshgrid(linspace(x_min, x_max, density),
                linspace(y_min, y_max, density))
 
# we define c as c=x+iy, c is a 1000x1000 matrix
c = x + 1j*y
 
# initially, z=c, we copy so that z and c are different objects in memory
z = c.copy()
 
# m is used to plot the fractal
m = zeros((density, density))

# iterations
for n in xrange(iterations):
    print "Completed %d %%" % (100 * float(n)/iterations)
 
    # indices of the numbers c such that |z(c)|<=10, with z = z_n
    indices = (abs(z) <= 10)
 
    # update z
    z[indices] = z[indices]**3 - 2*z[indices] + c[indices]
 
    # we update the values in m
    m[indices] = n
 

# save plot
plot_basename = "mandelbrot"
plot_ext = ".png"

file_names = [f for f in os.listdir('.') if os.path.isfile(f)]
nums = [int(f.split(os.extsep)[1]) for f in file_names if plot_basename in f.split(os.extsep)[0] and len(f.split(os.extsep)) > 2]
plot_name = plot_basename + "." + str(max(nums) + 1) + plot_ext

savefig_args = {'dpi':600,'bbox_inches':'tight','pad_inches':0.1}

fig = pl.figure(figsize=(6,6))
ax = fig.add_subplot(1,1,1)

# we plot log(m)
ax.imshow(log(m), cmap=pl.cm.RdBu,
           extent=(x_min, x_max, y_min, y_max))

ax.set_title('Mandelbrot Set')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')

fig.savefig(plot_name, **savefig_args)