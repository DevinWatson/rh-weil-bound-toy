import sys, ctypes
ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
import fitz
d=fitz.open(sys.argv[1]); out=open(sys.argv[2],'w',encoding='utf8')
for i,p in enumerate(d):
    out.write(f"\n=====PAGE {i+1}=====\n"); out.write(p.get_text())
print(len(d))
