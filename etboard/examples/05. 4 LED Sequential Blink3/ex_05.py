# ********************************************************************************
# FileName : ex_05
# Description : 4개의 LED를 5회 켰다 껏다 반복하는 예제
# Author : 이인정
# Created Date : 2021.05.31
# Reference :
# Modified : 2021.06.01 : LIJ : 헤더수정
# ********************************************************************************

# import
from ETboard.lib.pin_define import *
from machine import Pin
import time

# global definition
count = 0                     # 4개의 LED를 5회만 켜고 끄기를 위한 변수
i = 5                         # 5번 반복을 위한 변수


# setup
PinD2 = Pin(D2, Pin.OUT)      # D2를 LED 출력모드 설정하기
PinD3 = Pin(D3, Pin.OUT)      # D3를 LED 출력모드 설정하기
PinD4 = Pin(D4, Pin.OUT)      # D4를 LED 출력모드 설정하기
PinD5 = Pin(D5, Pin.OUT)      # D5를 LED 출력모드 설정하기


# main loop
while count < 1:
    for i in range(i):      
        time.sleep(1)         # 1초 기다리기
        PinD2.value(HIGH)     # 빨강 LED 켜기
        PinD3.value(HIGH)     # 파랑 LED 켜기
        PinD4.value(HIGH)     # 초록 LED 켜기
        PinD5.value(HIGH)     # 노랑 LED 켜기

        time.sleep(1)         # 1초기다리기
        PinD2.value(LOW)      # 빨강 LED 끄기
        PinD3.value(LOW)      # 파랑 LED 끄기
        PinD4.value(LOW)      # 초록 LED 끄기
        PinD5.value(LOW)      # 노랑 LED 끄기
        
    count = 1                 # LED를 제어하지 않기 위해 count 변수를 1로 변경

# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr│
# │                                           │
# └───────────────────────────────────────────┘
