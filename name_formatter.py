f = open("n_raw.txt", "r", encoding="utf8")
w = open("no.txt",'w', encoding="utf8")
for x in f:
    w.write(x[:x.find('|')]+'\n')
    