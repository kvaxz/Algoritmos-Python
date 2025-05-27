while True:
    user = input("Informe o nome de usuario: ")
    password = input("Informe a senha: ")
    repeat_password = input("Repita a senha: ")

    if password != repeat_password or password == user:
        print("As senhas estão diferentes ou iguais ao nome de usuario!")
    else:
        print(f"Conta criada com sucesso! =) ")
        break