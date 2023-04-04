users_file = open(r"kullanicilar.txt","r")

Lines = users_file.readlines()



count = 0

for line in Lines:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))

print(f"Tekilleştirmeden önceki kullanıcı sayısı: {count}")

count = 0

Lines = list(dict.fromkeys(Lines))

for line in Lines:
    count += 1
    # print("Line{}: {}".format(count, line.strip()))

print(f"Tekilleştirdikten sonraki kullanıcı sayısı: {count}")

users_file.close()
Lines.sort()
fp = open("tekilleştirilmiş_kullanıcılar.txt", "w")

for line in Lines:
    fp.write("%s" % line)
print("Done")

fp.close()