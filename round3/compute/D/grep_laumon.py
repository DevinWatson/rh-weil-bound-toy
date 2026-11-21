import re
t=open(r'./round2/compute/LIT/LAU.txt',encoding='utf8',errors='replace').read().split('\n')
for lo,hi,name in [(244,765,'ch1'),(767,1887,'ch2'),(1887,2944,'ch3'),(2944,3130,'ch4')]:
    n=sum(1 for l in t[lo-1:hi] if re.search(r'poids|\bpur|Weil',l,re.I))
    print(name,n)
