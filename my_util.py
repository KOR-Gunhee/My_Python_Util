import threading
import sys
import time
import datetime
import copy
import inspect
import pprint as pp
import os
import binascii

def crc8Calculate(data):
    crc = 0
    
    for i in range(data.__len__()):
        crc += data[i]
    
    # debug("crc8Calculate : ", hex(crc & 0xFF))
    
    return crc & 0xFF

def crc16Calculate(data):
    crc = 0
    
    for i in range(data.__len__()):
        crc += data[i]
    
    # debug("crc16Calculate : ", hex(crc))
    return crc
    
def debug(*args):
    cf = inspect.currentframe()
    linenumber = cf.f_back.f_lineno
    filename = os.path.basename(cf.f_back.f_code.co_filename)
    print("[DEBUG][",filename,"][",linenumber,"]", end=' ')
    
    cs = []
    for c in args:
        cs.append(c)
        
    pp.pprint(cs) 

def debugHex(name, *args):
    cf = inspect.currentframe()
    linenumber = cf.f_back.f_lineno
    filename = os.path.basename(cf.f_back.f_code.co_filename)
    data = name + " : " + "[" + str.join(", ", (hex(i) for i in args[0])) + "]"
    print("[DEBUG][",filename,"][",linenumber,"]", end=' ')
    pp.pprint(data)
    # pp.pprint(args)
    
    
def intergerToTwoBytes(data) :
    return [data >> 8 & 0xFF, data & 0xFF]

def myCopy(data):
    return copy.deepcopy(data)

def bitCheck(data, cnt):    
    # 비트 결과를 저장할 리스트
    bit_values = []

    # 0번 비트부터 31번 비트까지 순서대로 검사
    for i in range(cnt):
        # i번째 비트를 오른쪽으로 시프트하고 & 연산으로 확인
        bit = (data >> i) & 1
        bit_values.append(bit)

    # debug("bit_values", bit_values)
    
    return bit_values

def intergerToByteList(data):
    if data > 0xffffff :
        return [data >> 24 & 0xFF, data >> 16 & 0xFF, data >> 8 & 0xFF, data & 0xFF]
    elif data >0xffff :
        return [data >> 16 & 0xFF, data >> 8 & 0xFF, data & 0xFF]
    elif data > 0xff :
        return [data >> 8 & 0xFF, data & 0xFF]
    else :
        return [data & 0xFF]
    
def delay_ms(ms):
    time.sleep(ms / 1000)
    
def getCurrentTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def hexStringToHexint(data):
    validChars = "0123456789abcdefABCDEF"  # 16진수에 허용되는 문자
    
    for char in data:
        if char not in validChars:
            return int("0", 16)

    return int(data, 16)