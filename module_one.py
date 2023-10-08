def HammingSimilarities(s1, s2):
    score = 0
    l = len(s1)
    for i in range(l):
        if s1[i] == s2[i]:
            score += 1
    return score

hc = 'CGATGCTTAGCAT'
ch = 'TTCGTGCCTTA'

rearrangment = 0

dict = {}

hcl = len(hc)
chl = len(ch)

if hcl > chl:
    l = chl//4
else:
    l = hcl//4
hct = []
cht = []


for k in range(3, 12, 1):
    score = {}
    for i in range(chl - k + 1):
        for j in range(hcl - k + 1):
            s = HammingSimilarities(ch[i:i+k], hc[j:j+k]) / k
            score[ch[i:i+k], hc[j:j+k]] = s
            #print(ch[i:i+k], hc[j:j+k])
    m = max(score.values())
    for key, v in score.items():
        if v == m and v > 0:
            dict[key] = v

print(dict)
x_copy = dict.copy()
for key, value in dict.items():
    if any(key != k and key[1] in k[1] and value < v for k, v in dict.items()):
        del x_copy[key]

dict = x_copy
print("FINAL", dict)
ld = {}
dl = {}
for key, v in dict.items():
    d = hc.find(key[1])
    ld[key[1]] = d
    dd = ch.find(key[0])
    dl[key[0]] = dd

print(ld)
print(dl)
print(ch)




