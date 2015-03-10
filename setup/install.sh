#!/usr/bin/env bash

set -e
set -x

echo "hello"

_install() {
  local pkg="thumbor" ver=$1

  if [ -e "requirements" ]; then
    apt-get update && apt-get install \
      --no-install-recommends --ignore-missing --fix-broken -y \
        $(cat requirements) && \
  fi

  # Temporary install unzip
  apt-get install unzip

  # Download the snapshot
  curl https://github.com/thumbor/$pkg/archive/${ver}.zip && \
    unzip ${ver}.zip >/dev/null && rm -f ${ver}.zip

  cd "$pkg-${ver}"

  python setup.py install

  # Remove unzip
  apt-get purge unzip

  # Clean up APT when done
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

  cd ".."
  rm -rf "/$pkg-${ver}"
}

_install thumbor $THUMBOR_VERSION
