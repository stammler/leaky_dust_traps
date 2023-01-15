from dustpy import Simulation
import dustpy.constants as c
from functions.alpha import alpha
from functions.grid import refinegrid
from functions.probabilities import bouncing
from functions.planet import Mp_fast
import numpy as np
import parameters as pars

# Creating DustPy object
s = Simulation()

# Setting initial conditions

# Grid
s.ini.grid.mmin = pars.mmin
s.ini.grid.mmax = pars.mmax
s.ini.grid.Nmbpd = pars.Nmbpd
s.ini.grid.rmin = pars.rmin
s.ini.grid.rmax = pars.rmax
s.ini.grid.Nr = pars.Nr

# Gas
s.ini.gas.alpha = pars.alpha
s.ini.gas.Mdisk = pars.Mdisk
s.ini.gas.SigmaRc = pars.Rc

# Dust
s.ini.dust.aIniMax = pars.aIniMax
s.ini.dust.vfrag = pars.vfrag
s.ini.dust.dust2gasRatio = pars.d2g

# Star
s.ini.star.M = pars.Ms
s.ini.star.R = pars.Rs
s.ini.star.T = pars.Ts

# Allow drift-limited particles. This is necessary due to the large initial particle sizes
s.ini.dust.allowDriftingParticles = False

# Adding planets
s.addgroup("planets")
for i in range(len(pars.Mp)):
    name = "p"+str(i).zfill(2)
    s.planets.addgroup(name, description="Planet {}".format(name))
    s.planets.__dict__[name].addfield("M", pars.Mp[i], description="Mass [g]")
    s.planets.p00.M.updater = Mp_fast
    s.planets.__dict__[name].addfield(
        "a", pars.ap[i], description="Semi-major axis [cm]")
# Adding update order
s.planets.p00.updater = ["M"]
s.planets.updater = ["p00"]
s.updater = ["planets"] + s.updateorder

# Making refined grid
if pars.refine:
    ri = np.logspace(np.log10(pars.rmin), np.log10(pars.rmax), pars.Nr+1)
    for i in range(len(pars.Mp)):
        ri = refinegrid(ri, pars.ap[i], num=3)
    s.grid.ri = ri

# Initializing
s.initialize()

# Snapshots
log_tf = np.log10(pars.tFirst)
log_tl = np.log10(pars.tLast)
Nt = int(pars.Nspd * (log_tl-log_tf))
s.t.snapshots = np.logspace(log_tf, log_tl, Nt+1)

# Adding viscosity profile
s.gas.alpha.updater = alpha
s.gas.alpha.update()

# Modifying delta
s.dust.delta.rad[...] = pars.deltar
s.dust.delta.turb[...] = pars.deltat
s.dust.delta.vert[...] = pars.deltaz

# Modifying surface densities
# Gas
s.gas.Sigma *= s.ini.gas.alpha/s.gas.alpha[...]
# Dust
s.dust.Sigma *= s.ini.gas.alpha/s.gas.alpha[..., None]

# Turning off fragmentation and turning on bouncing
s.dust.p.frag[...] = 0.
s.dust.p.frag.updater = None
s.dust.p.stick.updater = bouncing

# Update simulation object
s.update()

# Enforce floor value
s.dust.Sigma = np.where(s.dust.Sigma > s.dust.SigmaFloor,
                        s.dust.Sigma,
                        0.1*s.dust.SigmaFloor)

# Run the model
s.run()
