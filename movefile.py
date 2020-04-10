#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import shutil

SourceFile="D:\OrderGateWay\DAUS_DMA_S10"
TargetDir=["D:\\OrderGateway"]
Path=[]
File=[]

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

def ScanFile(sourcefile):
    alllist = os.listdir(sourcefile + "\\config")
    for i in alllist:
        if i in ("ZD_secdef.dat", "ZD_secdef_option.dat", "ZD_secdef_sp.dat"):
            File.append(sourcefile + "\\config\\" + i)

def CopyFile(path,file):
    for p in path:
        for f in file:
            shutil.copy(f,p+"\\config")



print("开始执行CME合约拷贝脚本")
try:
    ScanDir(TargetDir)
except:
    print("ScanDir方法出错啦")
else:
    try:
        ScanFile(SourceFile)
    except:
        print("ScanFile方法出错啦")
    else:
        try:
            CopyFile(Path, File)
        except:
            print("CopyFile方法出错啦")
        else:
            print("脚本执行完毕")






