#! /bin/bash

export PIP_INDEX_URL="http://192.168.124.1:3141/root/pypi"
export PIP_TRUSTED_HOST="192.168.124.1"
export http_proxy="http://192.168.124.1:3128/"
export https_proxy="$http_proxy"
export no_proxy="localhost,127.0.0.1,192.168.124.1,github.com"
export always_trust_ssl="true"
