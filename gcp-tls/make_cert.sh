echo "Making k8app private key"
openssl genrsa -out k8s.codes_priv.key 2048

echo "Making certificate signing request"
openssl req -new -sha512 -nodes -key k8s.codes_priv.key -out gcp.k8s.codes.csr -config k8s.codes__csr.conf

#echo "Making k8app certificate"
#openssl x509 -req -sha512 -days 90 -in k8app.csr -CA ca.crt -CAkey ca.key -CAcreateserial -extfile k8app_crt.conf -out k8app.crt