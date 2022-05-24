#!/bin/sh

HOSTNAME=$1
PORT=$2

TRUST_CERT_FILE_LOC=/home/tpcp/Desktop/AI/deep_learning_with_python/venv/lib/python3.8/site-packages/certifi/cacert.pem

sudo bash -c "echo -n | openssl s_client -showcerts -connect ${HOSTNAME}:${PORT} \
2>/dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' \
>> ${TRUST_CERT_FILE_LOC}"
