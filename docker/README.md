## Docker Container Specification

### Installed software

* Base OS image: `Ubuntu 20.04.04 - Focal Fossa`
* Python version: `3.10.3`
  * Compile options: `--enable-shared --enable-optimizations --prefix=/opt/python-3.10.3-gcc`
* OpenMPI version: `4.1.3`
  * Compile options: `--enable-static --enable-shared --enable-mpi-cxx --enable-mpi-fortran --without-cuda --prefix=/opt/openmpi-4.1.3-gcc`
* Lua version: `5.3.3`
  * Installed from pre-built binary
* Lmod version: `8.6.6`
  * Compile options: `--prefix=/opt/apps`
* Text editor: `micro`

### How to run container

This container is meant to be run as an interactive shell similar to how users interact with high-performance computing clusters. Use the following command to launch a shell session inside the Docker container as user **hackpsu**:

```
docker run -it nucci/hpcintroworkshop:hackpsu-2022
```

### How to access Python 3.10.3 and OpenMPI 4.1.3

This container comes with the Lmod module system installed, so Python 3.10.3 and OpenMPI 4.1.3 are distributed as Lua module files. You can load them with the following commands:

```
module load python/3.10.3
module load openmpi/4.1.3
```

### How to build the container yourself

To build the container from the Dockerfile yourself, use the following command:

```
docker build -t <name>:<tag> .
```

**Important:** Make sure that the Lua module files `python-3.10.3.lua` and `openmpi-4.1.3.lua` are located in the same directory as the Dockerfile.