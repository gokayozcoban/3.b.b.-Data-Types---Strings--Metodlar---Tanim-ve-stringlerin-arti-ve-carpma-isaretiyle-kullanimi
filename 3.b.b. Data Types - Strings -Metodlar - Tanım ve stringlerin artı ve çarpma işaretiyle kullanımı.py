
# DATA TYPES (VERİ TİPLERİ)

# STRINGS - METODLAR
# Her şeyin metodu dir() fonksiyonu ile yazdırılabilir:
print(dir(str))

# Metodlardan önce stringlerin matematik işaretleriyle de kullanılabilinirliği
# hakkında bir iki örnek yazayım:
print("gökay" + "özçoban")
gökayözçoban
# "gökay" ve "özçoban" strinlerinin arasına + işareti koyunca Python bunu bir-
# biriyle toplayarak yazdı.
# Bu şekilde birleşik kelimelere/cümlelere de ihtiyaç olabilir ama illa ayrı ya-
# zılmak isteniyorsa boşluğun gelmesi istenilen yere bir boşluk koyularak ayrı
# da yazılabilir:
print("gökay " + "özçoban")
gökay özçoban
# veya:
print("gökay" + " özçoban")
gökay özçoban

# Aynı zamanda stringlerde * işareti de kullanabiliriz:
print("gökay"*3,"özçoban")
gökaygökaygökay özçoban
print("gökay"*3," özçoban")
gökaygökaygökay  özçoban
print("gökay "*3," özçoban")
gökay gökay gökay   özçoban

# METODLAR

# Metodlar fonksiyonlara benzerdir ama onlar gibi çalışmaz, çalışma prensibi
# farklıdır. Metodlar stringten sonra . (nokta) ile başlar.
