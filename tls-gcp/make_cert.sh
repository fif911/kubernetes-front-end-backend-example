echo "Making k8app private key"
openssl genrsa -out k8s.codes_priv.key 2048

echo "Making certificate signing request"
openssl req -new -sha512 -nodes -key k8s.codes_priv.key -out gcp.k8s.codes.csr -config k8s.codes__csr.conf