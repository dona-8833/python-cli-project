from action import auth,bank_menu


status,authentication = auth()
while True:
    if status:
        print(f"logged in accoount number {authentication.acc_num}")
        bank_menu(authentication)
        break
    else:
        print(authentication)
        break