FROM phusion/baseimage:0.9.16
MAINTAINER xamfoo

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && \
  apt-get -y install \
    checkinstall=1.6.2-4ubuntu1 \
    python-dev=2.7.5-5ubuntu3 \
    libpng12-dev=1.2.50-1ubuntu2 \
    libtiff5-dev=4.0.3-7ubuntu0.1 \
    libjasper-dev=1.900.1-14ubuntu3.2 \
    libwebp-dev=0.4.0-4 \
    libopencv-dev=2.4.8+dfsg1-2ubuntu1 \
    python-pgmagick=0.5.7-1 \
    libmagick++-dev=8:6.7.7.10-6ubuntu3 \
    graphicsmagick=1.3.18-1ubuntu3 \
    libcurl4-openssl-dev=7.35.0-1ubuntu2.3 \
    python-pip=1.5.4-1 && \
  pip install pycurl numpy thumbor && \
# Add default thumbor configuration
  thumbor-config > /etc/thumbor.conf && \
# Clean up APT when done.
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
