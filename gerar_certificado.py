from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import serialization, hashes
from datetime import datetime, timedelta

senha = b'teste' #Coloque a mesma senha que você usou para criar a chave privada

# Carregar a chave privada
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=senha
    )

# Geração do nome do certificado (subject e issuer)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"BR"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"TO"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Palmas"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"FC Solutions"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"Raphael Henrique Scheffler Ferreira"), #Coloque o seu nome entre as aspas
])

# Construção do certificado
certificate_builder = x509.CertificateBuilder()

certificate_builder = certificate_builder.subject_name(subject)
certificate_builder = certificate_builder.issuer_name(issuer)
certificate_builder = certificate_builder.public_key(private_key.public_key())
certificate_builder = certificate_builder.serial_number(x509.random_serial_number())
certificate_builder = certificate_builder.not_valid_before(datetime.utcnow())
certificate_builder = certificate_builder.not_valid_after(
    datetime.utcnow() + timedelta(days=365)
)
certificate_builder = certificate_builder.add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False
)

# Assinar o certificado com a chave privada
certificate = certificate_builder.sign(
    private_key=private_key,
    algorithm=hashes.SHA256()
)

# Salvar o certificado em um arquivo PEM
with open("certificado.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

print("Certificado criado e salvo em 'certificado.pem'.")
