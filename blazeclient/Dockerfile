# Dockerfile
# IPython Notebook on Anaconda with Blaze
FROM ubuntu:14.04

MAINTAINER Dan Gisolfi <dan.gisolfi@gmail.com>

RUN apt-get update
RUN apt-get install -y wget git-core
# Install Anaconda
RUN mkdir -p /tmp/anaconda
RUN cd /tmp/anaconda;wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.1.0-Linux-x86_64.sh
RUN chmod 750 /tmp/anaconda/Anaconda-2.1.0-Linux-x86_64.sh
RUN /tmp/anaconda/Anaconda-2.1.0-Linux-x86_64.sh -b
# Setup Environment
ENV ANACONDA /root/anaconda/bin
ENV PATH ${ANACONDA}:${PATH}
# Install Blaze
RUN conda install -c blaze blaze=0.6.6
RUN conda install --yes pip
RUN pip install git+https://github.com/ContinuumIO/datashape.git --upgrade
RUN pip install toolz cytoolz multipledispatch  --upgrade
RUN git clone https://github.com/ContinuumIO/blaze.git
RUN cd blaze;python setup.py install
RUN python -c 'import blaze; blaze.test()' i
# Setup IPython Notebook
RUN ipython profile create nbconfig
RUN mkdir -p /home/notebooks
WORKDIR /home/notebooks
EXPOSE 8888
CMD ["ipython","notebook","/root/.ipython/profile_nbconfig/ipython_notebook_config.py"]
