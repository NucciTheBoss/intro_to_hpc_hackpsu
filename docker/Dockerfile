# syntax=docker/dockerfile:1.4
FROM ubuntu:focal-20220404

LABEL author="Jason C. Nucciarone" \
maintainer="Jason C. Nucciarone" \
owner="Jason C. Nucciarone" \
version="v1.0"

SHELL ["/usr/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN <<EOF
apt-get update
apt-get upgrade
apt-get install -y bash build-essential git libbz2-dev libffi-dev libssl-dev lua5.3 lua-bit32:amd64 lua-posix:amd64 lua-posix-dev liblua5.3-0:amd64 liblua5.3-dev:amd64 tcl tcl-dev tcl8.6 tcl8.6-dev:amd64 libtcl8.6:amd64 wget zlib1g-dev gfortran libtbb-dev liblzma-dev liblapack-dev libopenblas-dev libhdf5-dev
wget https://github.com/zyedidia/micro/releases/download/v2.0.10/micro-2.0.10-linux64-static.tar.gz
tar -xzf micro-2.0.10-linux64-static.tar.gz
mv micro-2.0.10/micro /usr/bin
rm -rf *.tar.gz
EOF

# Install Python
RUN <<EOF
mkdir -p /opt
cd /opt
wget https://www.python.org/ftp/python/3.10.3/Python-3.10.3.tgz
tar -xzf Python-3.10.3.tgz
rm -rf *.tgz
cd Python-3.10.3
./configure --enable-shared --enable-optimizations --prefix=/opt/python-3.10.3-gcc
make
make install
ln -s /opt/python-3.10.3-gcc/bin/python3.10 /opt/python-3.10.3-gcc/bin/python
ln -s /opt/python-3.10.3-gcc/bin/pip3.10 /opt/python-3.10.3-gcc/bin/pip
mkdir -p /opt/modulefiles/python
EOF

# Install OpenMPI
RUN <<EOF
cd /opt
wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.3.tar.gz
tar -xzf openmpi-4.1.3.tar.gz
rm -rf *.tar.gz
cd openmpi-4.1.3
./configure --enable-static --enable-shared --enable-mpi-cxx --enable-mpi-fortran --without-cuda --prefix=/opt/openmpi-4.1.3-gcc
make
make install
mkdir -p /opt/modulefiles/openmpi
EOF

# Install Python packages mpi4py, numba, and dask
RUN <<EOF
export PATH=/opt/python-3.10.3-gcc/bin:/opt/openmpi-4.1.3-gcc/bin:$PATH
export LD_LIBRARY_PATH=/opt/python-3.10.3-gcc/lib:/opt/openmpi-4.1.3-gcc/lib:$LD_LIBRARY_PATH
python -m pip install mpi4py
python -m pip install numba
python -m pip install "dask[complete]"
EOF

# Install Lmod
RUN <<EOF
mkdir -p /opt/apps
cd /opt/apps
wget https://github.com/TACC/Lmod/archive/refs/tags/8.6.6.tar.gz
tar -xzf 8.6.6.tar.gz
cd Lmod-8.6.6
./configure --prefix=/opt/apps
make install
ln -s /opt/apps/lmod/lmod/init/profile /etc/profile.d/modules.sh
ln -s /opt/apps/lmod/lmod/init/cshrc /etc/profile.d/modules.csh
EOF

# Create default user
RUN <<EOF
mkdir -p /home/hackpsu
useradd -d /home/hackpsu -s /usr/bin/bash -c "HackPSU 2022" -p "$(openssl passwd -1 hackpsu)" hackpsu
chown hackpsu /home/hackpsu
EOF

# Configure Lmod to run in bash shell session
RUN cat <<EOF > /home/hackpsu/.bashrc
if ! shopt -q login_shell; then
  if [ -d /etc/profile.d ]; then
    for i in /etc/profile.d/*.sh; do
      if [ -r \$i ]; then
        . \$i
      fi
    done
  fi
fi
EOF

# Copy in Lua modulefiles for Python and OpenMPI and add to MODULEPATH
COPY python-3.10.3.lua /opt/modulefiles/python/3.10.3.lua
COPY openmpi-4.1.3.lua /opt/modulefiles/openmpi/4.1.3.lua
ENV MODULEPATH=/opt/modulefiles:$MODULEPATH

# Clean up /opt
RUN <<EOF
rm -rf /opt/Python-3.10.3 /opt/openmpi-4.1.3
EOF

# Set up interactive environment
USER hackpsu
WORKDIR /home/hackpsu

