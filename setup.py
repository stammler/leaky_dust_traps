from setuptools import find_packages
import sys
try:
    from numpy.distutils.core import Extension
    from numpy.distutils.core import setup
except ImportError as exc:  # We do not have our build deps installed
    msg = "Error: {} must be installed before running the build.".format(
        exc.name)
    msg += "\nPlease install {} first. You can do this with `pip install {}`.".format(
        exc.name, exc.name)
    print(msg)
    sys.exit(1)

package_name = "leaky_dust_traps"

ext_prob = Extension(
    name="leaky_functions.probabilities_f",
    sources=[
        "leaky_functions/probabilities.f90"]
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
    install_requires=["charset_normalizer",
                      "dustpy==1.0.1", "matplotlib", "numpy", "scipy"],
    include_package_data=True,
    zip_safe=False,
)
