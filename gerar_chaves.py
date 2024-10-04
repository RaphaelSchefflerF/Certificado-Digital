from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048, #O tamanho da chave deve ser o recomendável de 2048 bits 
)

# Extrair chave pública
public_key = private_key.public_key()
# Definir uma senha para proteger a chave privada
password = b'teste'  # Substitua oque está dentro das aspas pela senha que deseja usar

# Exportar a chave privada para um arquivo, criptografada com a senha
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password)
        )
    )

# Exportar a chave pública para um arquivo
with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Chaves RSA geradas e salvas em 'private_key.pem' e 'public_key.pem'.")
