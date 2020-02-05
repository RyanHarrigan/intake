# pull official base image
FROM amazoncorretto:8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PROJECT_DIR=/usr/src/app
# ENV PYTHON_SRC=/root/python_src
ENV LIB_SRC=/root/lib_src

# making directories that will eventually be used
RUN mkdir -p $LIB_SRC

# set work directory
WORKDIR $PROJECT_DIR

# set locale (preventing bug issue when installing project dependencies)
# RUN yum -y install glibc-locale-source glibc-langpack-en && \
#     localedef -f UTF-8 -i en_US en_US.UTF-8 && \
#     export LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
RUN export LC_ALL=C

# adding build dependencies
RUN yum -y update && \
    yum -y install perl-core gcc zlib-devel libjpeg-devel musl-devel openssl-devel tar xz gzip make

# Installing openssl-devel alone seems to result in SSL errors in pip (see https://medium.com/@moreless/pip-complains-there-is-no-ssl-support-in-python-edbdce548852)
# Need to install OpenSSL also to avoid these errors
RUN curl -OL https://github.com/openssl/openssl/archive/OpenSSL_1_0_2l.tar.gz && \
    tar -zxvf OpenSSL_1_0_2l.tar.gz && \
    cd openssl-OpenSSL_1_0_2l/ && \
    ./config shared && \
    make && \
    make install && \
    export LD_LIBRARY_PATH=/usr/local/ssl/lib/ && \
    cd $PROJECT_DIR

# Install python 3.6
RUN cd $LIB_SRC && \
    curl -OL https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tar.xz && \
    tar -xJf Python-3.6.0.tar.xz && \
    cd Python-3.6.0 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm Python-3.6.0.tar.xz && \
    rm -rf Python-3.6.0 && \    
    cd $PROJECT_DIR

# # building python from source
# RUN mkdir -p $PYTHON_SRC
# ADD ./python_source $PYTHON_SRC

# # install python 
# RUN yum -y install python3 && \
#     yum -y install python-pip python3-devel

# install postgres
RUN yum install -y postgresql

# install nodejs
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash - && \
    yum -y install nodejs 

# copy project
COPY . .

# install dependencies
RUN cd $PROJECT_DIR && \
    pip3 install --upgrade pip && \
    npm install -g sass && \
    npm install && \
    make install

# collect pre-baked static media
RUN python3 manage.py collectstatic --noinput