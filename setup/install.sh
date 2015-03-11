#!/usr/bin/env bash

set -e

cd "/setup"

_install() {
  apt-get update
  # Install thumbor requirements
  apt-get install \
    --no-install-recommends --ignore-missing --fix-broken -y \
      $(cat requirements | grep -v "#")

  # Install build dependencies
  apt-get install \
    --no-install-recommends --ignore-missing --fix-broken -y \
    python-pip
}

if [ -e "requirements" ]; then
  _install
  cd "thumbor"
else
  cd "thumbor"
  _install
fi

## Install thumbor
pip install .

# Clean up APT when done
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

cd ".."
rm -rf "thumbor"
