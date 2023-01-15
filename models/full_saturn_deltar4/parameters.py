from dustpy import constants as c
import numpy as np

##### SIMULATION #####
tFirst = 1.e3 * c.year  # First snapshot
tLast = 1.e7 * c.year   # Last snapshot
Nspd = 20               # Number of snapshots per decade


##### GRID #####

rmin = 1. * c.au        # Inner grid boundary
rmax = 1000. * c.au     # Outer grid boundary
Nr = 100                # Number of radial grid cells


##### DUST #####

mmin = 1.e-12           # Maximum mass
mmax = 1.e9             # Minimum mass
Nmbpd = 7               # Number of mass bins per decade
aIniMax = 1.e-4         # Maximum initial particle size
d2g = 1.e-2             # dust-to-gas ratio
deltar = 1.e-4          # Radial delta parameter
deltat = 1.e-3          # Turbulent delta parameter
deltaz = 1.e-3          # Vertical delta parameter
vfrag = 1000.           # Fragmentation velocity
Rcav = 0. * c.au        # Cavity radius


##### GAS #####

Mdisk = 0.05 * c.M_sun  # Disk mass
Rc = 30. * c.au         # Critical cut-off radius
alpha = 1.e-3           # alpha viscosity parameter


##### STAR #####
Ms = 1. * c.M_sun       # Mass
Rs = 2. * c.R_sun       # Radius
Ts = 5772.              # Effective temperature


##### PLANETS #####

Mp = np.array([         # Mass
    95.159
]) * c.M_earth
ap = np.array([         # Semi-major axis
    5.
]) * c.au
