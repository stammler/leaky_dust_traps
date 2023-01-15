[![arXiv](https://img.shields.io/badge/arXiv-10.48550/arXiv.2301.#####-blue)](https://doi.org/10.48550/arXiv.2301.#####) [![GitHub](https://img.shields.io/github/license/stammler/leaky_dust_traps)](https://github.com/stammler/leaky_dust_traps/blob/master/LICENSE)

# Leaky Dust Traps

This repository contains the [DustPy](https://stammler.github.io/dustpy/) setups and a [notebook](https://github.com/stammler/leaky_dust_traps/blob/main/notebooks/plots.ipynb) producing the figures of the publication [Leaky Dust Traps: How Fragmentation impacts Dust Filtering by Planets]().

## Installation

The models contain Fortran modules that need to be compiled first. To do so clone the repository and run the setup script.  
A Fotran compiler is required.

```
git clone git@github.com:stammler/leaky_dust_traps.git
cd leaky_dust_traps
pip install .
```

## Running Models

To run a model change to the respective directory and run the model script

```
cd models/toy_saturn/
python start.py
```

Please note, that some models will take several days to run.  
For more details, please have a look at the [DustPy documentation](https://stammler.github.io/dustpy/).

## Models

The following model setups are available in the repository

| Name                                                                                                                         | Planet mass       | Description                                                        |
|:-----------------------------------------------------------------------------------------------------------------------------|------------------:|:-------------------------------------------------------------------|
| [`toy_saturn`](https://github.com/stammler/leaky_dust_traps/tree/main/models/toy_saturn)                                     | $M_\mathrm{sat}$  | Toy model, Saturn mass planet                                      |
| [`toy_noPlanet`](https://github.com/stammler/leaky_dust_traps/tree/main/models/toy_noPlanet)                                 | –                 | Toy model, without planet                                          |
| [`toy_saturn_noFrag`](https://github.com/stammler/leaky_dust_traps/tree/main/models/toy_saturn_noFrag)                       | $M_\mathrm{sat}$  | Toy model, Saturn mass planet, no fragmentation                    |
| [`toy_saturn_bouncing`](https://github.com/stammler/leaky_dust_traps/tree/main/models/toy_saturn_bouncing)                   | $M_\mathrm{sat}$  | Toy model, Saturn mass planet, bouncing                            |
| [`toy_saturn_vFrag100`](https://github.com/stammler/leaky_dust_traps/tree/main/models/toy_saturn_vFrag100)              | $M_\mathrm{sat}$  | Toy model, Saturn mass planet, $v_\mathrm{frag}=1$ m/s             |
| [`full_noPlanet`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_noPlanet)                               | –                 | Full model, without planet                                         |
| [`full_30Me`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_30Me)                                      | $30\,M_\oplus$    | Full model, 30 Earth mass planet                                   |
| [`full_50Me`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_50Me)                                       | $50\,M_\oplus$    | Full model, 50 Earth mass planet                                   |
| [`full_saturn_deltar2`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_saturn_deltar2)                   | $M_\mathrm{sat}$  | Full model, Saturn Earth mass planet, $\delta_r = 10^{-2}$         |
| [`full_saturn`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_saturn)                                   | $M_\mathrm{sat}$  | Full model, without planet                                         |
| [`full_saturn_deltar4`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_saturn_deltar4)                   | $M_\mathrm{sat}$  | Full model, Saturn Earth mass planet, $\delta_r = 10^{-4}$         |
| [`full_saturn_deltar5`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_saturn_deltar5)                   | $M_\mathrm{sat}$  | Full model, Saturn Earth mass planet, $\delta_r = 10^{-5}$         |
| [`full_200Me`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_200Me)                                     | $200\,M_\oplus$   | Full model, 200 Earth mass planet                                  |
| [`full_jupiter`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_jupiter)                                 | $M_\mathrm{jup}$  | Full model, Jupiter mass planet                                    |
| [`full_MtSlow`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtSlow)                                   | $M\left(t\right)$ | Full model, slowly growing planet                                  |
| [`full_MtSlow_deltar4`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtSlow_deltar4)                   | $M\left(t\right)$ | Full model, slowly growing planet, $\delta_r = 10^{-4}$            |
| [`full_MtSlow_deltar5`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtSlow_deltar5)                   | $M\left(t\right)$ | Full model, slowly growing planet, $\delta_r = 10^{-5}$            |
| [`full_MtSlow_bouncing`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtSlow_bouncing)                 | $M\left(t\right)$ | Full model, slowly growing planet, bouncing                        |
| [`full_MtSlow_bouncing_deltas5`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtSlow_bouncing_deltas5) | $M\left(t\right)$ | Full model, slowly growing planet, bouncing, $\delta_i = 10^{-5}$  |
| [`full_MtFast_bouncing_deltas5`](https://github.com/stammler/leaky_dust_traps/tree/main/models/full_MtFast_bouncing_deltas5) | $M\left(t\right)$ | Full model, rapidly growing planet, bouncing, $\delta_i = 10^{-5}$ |

## Acknowledgements

This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme under grant agreement No 714769. This project has received funding by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) through grants FOR 2634/1 and 361140270. This research was supported by the Munich Institute for Astro-, Particle and BioPhysics (MIAPbP) which is funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany’s Excellence Strategy – EXC-2094 – 390783311. JD was funded by the European Union under the European Union’s Horizon Europe Research & Innovation Programme 101040037 (PLANETOIDS). Views and opinions expressed are however those of the authors only and do not necessarily reflect those of the European Union or the European Research Council. Neither the European Union nor the granting authority can be held responsible for them. TL was supported by grants from the Simons Foundation (SCOL Award No. 611576) and the Branco Weiss Foundation.