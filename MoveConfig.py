#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
##import easygui


dic={}
Sourcepath="D:\ZDProduction\C_CMEDMA_T"
TargetDirs=["D:\ZDProduction"]
s_target=""
s_product=""
Path=[]
"""
def get_Targetcfg(txt):
    reg1=re.compile(r'<add key="TargetProduct" value="(.*)" />')

    return re.findall(reg1,txt)

def get_Productcfg(txt):
    reg2 = re.compile(r'<add key="Products" value="(.*)" />')
    return reg2.findall(txt)
"""

def ScanPath(targtpath):
    splitroot=targtpath.split('\\')
    filename=splitroot[len(splitroot)-1]
    filescan=filename.split('_')
    return filescan


def ScanDir(targetdir):
    for dir in targetdir:
        os.chdir(dir)
        for newroot, newdirs, newfiles in os.walk(dir, topdown=False):
            root=ScanPath(newroot)
            if len(root)>=2:
                if root[0]=="C"  and root[1]=="CMEDMA" and newroot != Sourcepath:
                    Path.append(newroot)
                    """
                    for newname in newfiles:
                        if newname == "CMEMarketAdapter.exe" and newroot != Sourcepath:
                            Path.append(newroot)
                    """
                        

with open(Sourcepath+"\\CMEMarketAdapter.exe.config", encoding='utf8') as f:
    a=f.readlines()
    for str1 in a:
        if str1.__contains__("TargetProduct"):
            s_target = str1
        elif str1.__contains__("Products"):
            s_product = str1
        elif (s_target != "") & (s_product != ""):
            break
ScanDir(TargetDirs)
for targetdir in Path:
    f1=open(targetdir+"\\CMEMarketAdapter.exe.config", 'r+', encoding='utf8')
    b = f1.readlines()
    f1.seek(0)
    f1.truncate()
    f1.close()
    f2=open(targetdir+"\\CMEMarketAdapter.exe.config", 'r+', encoding='utf8')
    for str2 in b:
        if str2.__contains__("TargetProduct"):

            f2.write(s_target)
            continue
        elif str2.__contains__("Products"):

            f2.write(s_product)
            continue
        else:
            f2.write(str2)
    f2.close()
##easygui.msgbox("完成！")














