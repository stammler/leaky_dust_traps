from setuptools import find_packages
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

package_name = "leaky_dust_traps"

ext_prob = Extension(
    name="functions.probabilities_f",
    sources=[
        "functions/probabilities.f90"]
)
extensions = [ext_prob]

setup(
    name=package_name,

    description="Leaky Dust Traps: How Fragmentation impacts Filtering by Planets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="numerical,simulation,science,physics,astrophysics,astronomy",

    url="https://github.com/stammler/leaky_dust_traps/",
    project_urls={"Source Code": "https://github.com/stammler/leaky_dust_traps/"
                  },

    author="Sebastian Markus Stammler, Tim Lichtenberg, Joanna Drążkowska, Til Birnstiel",
    author_email="sebastian.stammler@gmail.com",
    maintainer="Sebastian Stammler",

    version="1.0.0",
    license="BSD",

    ext_modules=extensions,

    packages=find_packages(),
    install_requires=["dustpy==1.0.1", "matplotlib", "numpy", "scipy"],
    include_package_data=True,
    zip_safe=False,
)
