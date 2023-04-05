users_file = open(r"tekilleştirilmiş_kullanıcılar.txt","r",encoding="utf8")

usernameLines = users_file.readlines()
count = 0

for line in usernameLines:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))

print(f"Eşleştirmeden önceki kullanıcı sayısı: {count}")

users_file.close()

sam_file = open(r"admanager.txt","r",encoding="utf8")

samLines = sam_file.readlines()

count = 0

for userLine in usernameLines:
    for samLine in samLines:
        if samLine.find(userLine) == -1:
            # userline = userLine +" bulunamadı."
            # print(userLine)
            continue
        else:
            # userline == samLine
            print(samLine)
            count += 1
            break


print(f"contain line count = {count}")
# print("userLines = ")
# print("\n".join(usernameLines))

sam_file.close()