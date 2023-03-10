import hashlib

def io():
    # ENTRADA DE DADOS
    user = input("USUARIO: ")
    password = input("SENHA: ")
    return user, password
    
def security(user, password):
    string = user + password # CONCATENA O USUARIO E SENHA
    hash_value = hashlib.sha256(string.encode()).hexdigest() #  ENCRIPTA EM sha256 A CONCATENAÇÃO DE USUARIO E SENHA
    user_hash = hashlib.sha256(user.encode()).hexdigest() # ENCRIPTA EM sha256 O USUARIO
    password_hash = hashlib.sha256(password.encode()).hexdigest() # ENCRIPT EM sha256 A SENHA
    return hash_value, user_hash, password_hash # RETORNA AS HASH DAS CRIPTOGRAFIA

def login():
    user, password = io()
    hash, user_hash, password_hash = security(user, password)

    concat = hash + user_hash + password_hash # CONCATENA TODAS AS HASH
    tena = hashlib.sha256(concat.encode()).hexdigest() # ENCRIPTA EM sha256 O RESULTADO DE TODAS AS HASH CONCATENADAS


    if hash == '4c006c647316bd2eff7a6cb09757f0c2ca2bba09de4d562a773ef0c3f3693039' and user_hash == '3cdea1b06e8f4c08213ca4cbd702a27871914c971ee226cf9debf88b8435c375' and password_hash == '3f81f4b399e3527b428d0770aa8ef491ff5b1c706a3c0b83d4eb893ab1881abf' and tena == '7056a36ab294b3400c70ff63d14eb01449c660883e4008c806795bbaa9a507e9':
        return True #FAZ A COMPARAÇÃO DOS VALORES ENCRIPTADOS QUE ENTRARAM NA FUNCÇÃO IO COM AS HASH PREDEFINIDAS DE USUARIO E SENHA PADÃO
    else:
        return False