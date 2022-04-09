<p align="center">
    <img src="./assets/icds_logo.png">
</p>

<h1 align="center">
Introduction to High-Performance Computing Workshop - HackPSU 2022
</h1>

Interested in learning how to wrangle big data, accelerate your scientific research, or build your own data pipelines? The Introduction to High-Performance Computing workshop will teach you the foundations of HPC, how to work with supercomputers, and some popular frameworks used by scientists today. You will get hands on experience with open-source technologies such as OpenMPI and Numba. All that is required is some working knowledge of Python and the command line!

## Table of Contents

* [Setting up your environment](#setting-up-your-environment)
* [Exercises](#exercises)
* [Authors](#authors)
* [Copyright and License](#copyright-and-license)
* [Troubleshooting](#troubleshooting)

## Setting up your environment

### Install Docker

To run the HPC container I have set up, you will need to have Docker installed on your system. Please install Docker according to the installation instructions for your operating system:

* [Windows](https://docs.docker.com/desktop/windows/install/)
  * [To enable WSL2 backend](https://docs.microsoft.com/en-us/windows/wsl/install)
* [Mac](https://docs.docker.com/desktop/mac/install/)
* Linux
  * [Debian/Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  * [Fedora](https://docs.docker.com/engine/install/fedora/)

### Pull and run container

Once you have installed Docker on your system, using the following command to pull the container for this workshop from Docker Hub:

```
docker pull nucci/hpcintroworkshop:hackpsu-2022
```

After the container has finished downloading, use the following command to launch an interactive bash shell inside the container:

```
docker run -it nucci/hpcintroworkshop:hackpsu-2022
```

### Download examples

Once inside the container, use `git` to download the examples from this repository:

```
git clone https://github.com/NucciTheBoss/intro_to_hpc_hackpsu.git
```

You can use the `micro` text editor to edit files inside the container.

## Exercises

### Exercise 1 - mpi4py

The mpi4py exercise is located in `src/example-1`

### Exercise 2 - numba

The Numba exercise is located in `src/example-2`

### Exercise 3 - Dask

The Dask exercise is located in `src/example-3`

## Authors

* Jason C. Nucciarone - Penn State ICDS - HPC Software Engineer
  * [LinkedIn](https://www.linkedin.com/in/jasonnucci/)

## Copyright and License

Code, documentation, and workshop copyright &copy; 2022 Jason C. Nucciarone, The Pennsylvania State University Institute for Computational and Data Sciences. Repository content is released under the [GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). Authors of third-party images, libraries, and packages maintain their respective copyright.

## Troubleshooting

If you encounter any issues while working with, building, or modifying anything stored in this repository, please open an issue on this repository or email me at nucci.programming@gmail.com. In that issue/email, please describe the issue that you are having, and please explain what you are trying to do with this repository's content.
