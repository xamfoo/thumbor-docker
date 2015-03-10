#!/usr/bin/env bash

set -e

cd "/setup"

_install() {
  apt-get update
  apt-get install \
    --no-install-recommends --ignore-missing --fix-broken -y \
      $(cat requirements | grep -v "#")
  # Clean up APT when done
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
}

if [ -e "requirements" ]; then
  _install
  cd "thumbor"
else
  cd "thumbor"
  _install
fi

python setup.py install

cd ".."
rm -rf "thumbor"
