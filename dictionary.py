contacts_list = {"greshma" : 1234567,
                 "devnath" : 2345678}
print(contacts_list)

i = input("Do you want to add or delete a contact  ? :")
if i == "yes" :
    j = input("add  or delete ? : ")
    if j == "add" :
        k = input("Name :")
        l = input("Number :")
        contacts_list[k] = l

    elif j == "delete" :
        m = input("Which contact you want to delete ? :")
        if m in contacts_list :
            contacts_list.pop(m)
        else :
            print("contact not found !")


print(contacts_list)