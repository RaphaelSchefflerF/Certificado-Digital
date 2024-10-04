from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# Carregar a chave privada com senha
senha = b'teste' #Coloque a senha da chave privada

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=senha
    )

# Carregar o documento para assinar
with open("teste.pdf", "rb") as doc_file:
#Caso queira trocar o documento susbtitua teste.pdf pelo nome do seu documento 
    documento = doc_file.read()

# Assinar o documento com a chave privada
assinatura = private_key.sign(
    documento,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Salvar a assinatura em um arquivo
#Caso queira trocar o nome do arquivo substitua teste_assinado.pdf pelo nome que deseja
with open("teste_assinado.pdf", "wb") as sign_file:
    sign_file.write(assinatura)

print("Documento assinado e assinatura salva em 'teste_assinado.pdf'.")
