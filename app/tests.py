from utils.security import hash_password, verify_password

# hashed_pass = "$2b$12$P2vzfz2QLnuhoPReMqlHB.AUvdZYsUF9NmCA3att0OcfT/tRce8n2"
#
# console_prefix = ">"
# while True:
#     action = input(f"вибери дію {console_prefix}")
#     if action == "login":
#         console_prefix = ">"
#         password = input(f"введыть пароль {console_prefix}")
#         if hashed_pass:
#             if verify_password(password, hashed_pass):
#                 print(f"pass is correct")
#             else:
#                 print("passwort in nor correct")
#                 action = "register"
#         else:
#             print("паролю нема но його можна добавити командою register")
#
#     elif action == "register":
#         console_prefix = "<"
#         new_pass = input(f"введи новий пароль {console_prefix}")
#         hashed_pass = hash_password(new_pass)
#         print(f"успышно зареэстровано \n новийхеш: {hashed_pass}")
#         console_prefix = ">"

new_pass = "" #awefersfg34
print(f"{new_pass} -> {hash_password(new_pass)} -> {verify_password(new_pass, hash_password(new_pass))}")