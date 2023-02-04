echo "Making k8app private key"
openssl genrsa -out k8app_priv.key 4096

echo "Making certificate signing request"
openssl req -new -sha512 -nodes -key k8app_priv.key -out k8app.csr -config k8app_csr.conf

echo "Making k8app certificate"
openssl x509 -req -sha512 -days 90 -in k8app.csr -CA ca.crt -CAkey ca.key -CAcreateserial -extfile k8app_crt.conf -out k8app.crt