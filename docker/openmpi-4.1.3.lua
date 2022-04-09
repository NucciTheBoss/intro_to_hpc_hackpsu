help([[The Open MPI Project is an open source Message Passing Interface implementation 
that is developed and maintained by a consortium of academic, research, and industry 
partners. Open MPI is therefore able to combine the expertise, technologies, and resources 
from all across the High Performance Computing community in order to build the best MPI library 
available. Open MPI offers advantages for system and software vendors, application developers 
and computer science researchers.]])

-- General information
whatis("Description: The Open MPI Project is an open source Message Passing Interface implementation that is developed and maintained by a consortium of academic, research, and industry partners.")
whatis("OpenMPI Version: 4.1.3")
whatis("Compiler Suite: GCC")
whatis("Compile Options: --enable-static --enable-shared --enable-mpi-cxx --enable-mpi-fortran --without-cuda --prefix=/opt/openmpi-4.1.3-gcc")

-- Concatenate paths with OpenMPI 4.1.3 root folder
local root = "/opt/openmpi-4.1.3-gcc"

local mpibin = pathJoin(root, "bin")
local mpilib = pathJoin(root, "lib")
local mpiman = pathJoin(root, "share/man")
local mpiinclude = pathJoin(root, "include")
local mpipkgconfig = pathJoin(root, "lib/pkgconfig")
local mpiccpath = pathJoin(mpibin, "mpicc")
local mpicxxpath = pathJoin(mpibin, "mpic++")
local mpif77path = pathJoin(mpibin, "mpif77")
local mpif90path = pathJoin(mpibin, "mpif90")

-- Prepend paths
prepend_path("LD_LIBRARY_PATH", mpilib)
prepend_path("LIBRARY_PATH", mpilib)
prepend_path("PATH", mpibin)
prepend_path("MANPATH", mpiman)
prepend_path("C_INCLUDE_PATH", mpiinclude)
prepend_path("CPLUS_INCLUDE_PATH", mpiinclude)
prepend_path("INCLUDE", mpiinclude)
prepend_path("PKG_CONFIG_PATH", mpipkgconfig)
prepend_path("CMAKE_PREFIX_PATH", root)
setenv("MPICC", mpiccpath)
setenv("MPICXX", mpicxxpath)
setenv("MPIF77", mpif77path)
setenv("MPIF90", mpif90path)
