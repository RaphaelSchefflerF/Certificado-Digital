from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Carregar o certificado
with open("certificado.pem", "rb") as cert_file:
    certificado = x509.load_pem_x509_certificate(cert_file.read())

# Extrair a chave pública do certificado
public_key = certificado.public_key()

# Carregar o documento original
with open("teste.pdf", "rb") as doc_file:
    documento = doc_file.read()

# Carregar a assinatura
with open("teste_assinado.pdf", "rb") as sign_file:
    assinatura = sign_file.read()

# Verificar a assinatura
try:
    public_key.verify(
        assinatura,
        documento,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Assinatura verificada com sucesso!")

except Exception as e:
    print(f"Falha na verificação da assinatura: {e}")
