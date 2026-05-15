# ==================== AKILLI ADAPTIF ÖĞRENİM SİSTEMİ: 7. SINIF MATEMATİK ====================
# Python + Tkinter
# Tamamen adaptif seviye ilerleme sistemi ile modern arayüz

import tkinter as tk
from tkinter import messagebox, ttk
import time
import random
from dataclasses import dataclass
from typing import List, Dict

# ==================== VERİ MODELLERI ====================

@dataclass
class Soru:
    """Soru veri modeli"""
    soru: str
    secenekler: List[str]
    dogru: str
    aciklama: str

@dataclass
class SeviyeSonucu:
    """Seviye sonuç modeli"""
    seviye: str
    dogru_sayisi: int
    yanlis_sayisi: int
    sure: float
    basari_yuzde: float
    
    def gec_mi(self, hedef_yuzde: float) -> bool:
        """Belirtilen yüzdeyi geçtiyse True döndür"""
        return self.basari_yuzde >= hedef_yuzde

# ==================== SORU BANKASI ====================

SORU_BANKASI = {
    "ÜNİTE 1: TAM SAYILARLA İŞLEMLER": {
        "temel": [
            Soru(
                soru="(-8) + 15 = ?",
                secenekler=["7", "-7", "23", "-23"],
                dogru="7",
                aciklama="Negatif ve pozitif sayıları toplarken mutlak değeri büyük olanın işareti sonuca yazılır."
            ),
            Soru(
                soru="6 - 11 = ?",
                secenekler=["-5", "5", "17", "-17"],
                dogru="-5",
                aciklama="6'dan 11 çıkarsa 5 eksik kalır. Yani -5 olur."
            ),
            Soru(
                soru="(-3) + (-7) = ?",
                secenekler=["-10", "10", "-4", "4"],
                dogru="-10",
                aciklama="Aynı işaretli sayılar toplanırken mutlak değerleri toplanır ve ortak işaret yazılır."
            ),
            Soru(
                soru="15 - (-5) = ?",
                secenekler=["20", "10", "-20", "-10"],
                dogru="20",
                aciklama="Çıkarma işleminde, çıkan sayının işareti değiştirilip toplama yapılır: 15 + 5 = 20"
            ),
            Soru(
                soru="(-5) × 6 = ?",
                secenekler=["-30", "30", "-1", "11"],
                dogru="-30",
                aciklama="Farklı işaretli sayılar çarpılırsa sonuç negatif olur."
            ),
            Soru(
                soru="9 - 4 = ?",
                secenekler=["5", "-5", "13", "3"],
                dogru="5",
                aciklama="9'dan 4'ü çıkarsak 5 kalır."
            ),
            Soru(
                soru="(-2) + 8 = ?",
                secenekler=["6", "-6", "10", "-10"],
                dogru="6",
                aciklama="-2 ile 8 toplanırsa 6 olur."
            ),
        ],
        "orta": [
            Soru(
                soru="(-20) + (-10) + 15 = ?",
                secenekler=["-15", "15", "-5", "5"],
                dogru="-15",
                aciklama="(-20) + (-10) = -30, sonra -30 + 15 = -15"
            ),
            Soru(
                soru="(-15) + 10 - (-5) = ?",
                secenekler=["0", "10", "-10", "20"],
                dogru="0",
                aciklama="(-15) + 10 = -5, sonra -5 - (-5) = -5 + 5 = 0"
            ),
            Soru(
                soru="7 + (-14) + 9 = ?",
                secenekler=["2", "-2", "30", "-30"],
                dogru="2",
                aciklama="7 - 14 = -7, sonra -7 + 9 = 2"
            ),
            Soru(
                soru="(-2) × 5 × (-3) = ?",
                secenekler=["30", "-30", "10", "-10"],
                dogru="30",
                aciklama="(-2) × 5 = -10, sonra (-10) × (-3) = 30"
            ),
            Soru(
                soru="20 ÷ (-4) × 2 = ?",
                secenekler=["-10", "10", "-5", "5"],
                dogru="-10",
                aciklama="Soldan sağa: 20 ÷ (-4) = -5, sonra -5 × 2 = -10"
            ),
            Soru(
                soru="3 + (-8) = ?",
                secenekler=["-5", "5", "11", "-11"],
                dogru="-5",
                aciklama="3 + (-8) = 3 - 8 = -5"
            ),
            Soru(
                soru="(-4) × 2 = ?",
                secenekler=["-8", "8", "-2", "2"],
                dogru="-8",
                aciklama="Negatif ve pozitif çarpılırsa sonuç negatif olur."
            ),
        ],
        "zor": [
            Soru(
                soru="(-4) × (-3) = ?",
                secenekler=["12", "-12", "7", "-7"],
                dogru="12",
                aciklama="Aynı işaretli sayılar çarpılırsa sonuç pozitif olur."
            ),
            Soru(
                soru="(-48) ÷ (-8) = ?",
                secenekler=["6", "-6", "8", "-8"],
                dogru="6",
                aciklama="Aynı işaretler bölünürse sonuç pozitif olur."
            ),
            Soru(
                soru="(-25) + 30 - 8 = ?",
                secenekler=["-3", "3", "-13", "13"],
                dogru="-3",
                aciklama="Soldan sağa işlem: (-25) + 30 = 5, sonra 5 - 8 = -3"
            ),
            Soru(
                soru="18 - 24 + (-6) = ?",
                secenekler=["-12", "12", "-6", "6"],
                dogru="-12",
                aciklama="18 - 24 = -6, sonra -6 + (-6) = -12"
            ),
            Soru(
                soru="(-12) × 3 + 6 = ?",
                secenekler=["-30", "30", "-42", "42"],
                dogru="-30",
                aciklama="Önce çarpma: (-12) × 3 = -36, sonra toplama: -36 + 6 = -30"
            ),
            Soru(
                soru="(-5) × (-2) × 3 = ?",
                secenekler=["30", "-30", "15", "-15"],
                dogru="30",
                aciklama="(-5) × (-2) = 10, sonra 10 × 3 = 30"
            ),
            Soru(
                soru="100 ÷ (-5) = ?",
                secenekler=["-20", "20", "-5", "5"],
                dogru="-20",
                aciklama="100 ÷ (-5) = -20"
            ),
        ],
    },

    "ÜNİTE 2: RASYONEL SAYILAR": {
        "temel": [
            Soru(
                soru="1/2 + 1/4 = ?",
                secenekler=["3/4", "2/6", "1/6", "5/4"],
                dogru="3/4",
                aciklama="Paydaları eşitle: 2/4 + 1/4 = 3/4"
            ),
            Soru(
                soru="3/5 - 1/5 = ?",
                secenekler=["2/5", "4/5", "2/0", "1/0"],
                dogru="2/5",
                aciklama="Paydası aynı olan kesirler çıkarılır: (3-1)/5 = 2/5"
            ),
            Soru(
                soru="2/3 × 3/4 = ?",
                secenekler=["1/2", "5/7", "6/12", "3/4"],
                dogru="1/2",
                aciklama="Paylar çarpılır, paydalar çarpılır: 6/12 = 1/2"
            ),
            Soru(
                soru="4/5 ÷ 2/5 = ?",
                secenekler=["2", "1", "8/25", "4/2"],
                dogru="2",
                aciklama="Bölünen kesir aynen yazılır, bölen kesir ters çevrilip çarpılır: 4/5 × 5/2 = 2"
            ),
            Soru(
                soru="0,5 = ?",
                secenekler=["1/2", "1/4", "2/3", "3/4"],
                dogru="1/2",
                aciklama="Ondalık kesir rasyonel sayıya çevrilir."
            ),
            Soru(
                soru="1/3 + 1/3 = ?",
                secenekler=["2/3", "1/6", "2/6", "1/3"],
                dogru="2/3",
                aciklama="Paydası aynı olan kesirler: (1+1)/3 = 2/3"
            ),
            Soru(
                soru="5/6 - 1/6 = ?",
                secenekler=["4/6", "5/12", "1/6", "2/3"],
                dogru="4/6",
                aciklama="(5-1)/6 = 4/6"
            ),
        ],
        "orta": [
            Soru(
                soru="1/2 + 1/3 + 1/6 = ?",
                secenekler=["1", "2/3", "1/2", "4/6"],
                dogru="1",
                aciklama="Paydaları eşitle: 3/6 + 2/6 + 1/6 = 6/6 = 1"
            ),
            Soru(
                soru="7/8 - 1/4 = ?",
                secenekler=["5/8", "6/8", "1/2", "3/4"],
                dogru="5/8",
                aciklama="Paydaları eşitle: 7/8 - 2/8 = 5/8"
            ),
            Soru(
                soru="(-3/4) + 1/2 = ?",
                secenekler=["-1/4", "1/4", "-1/2", "1/2"],
                dogru="-1/4",
                aciklama="-3/4 + 2/4 = -1/4"
            ),
            Soru(
                soru="0,75 - 1/4 = ?",
                secenekler=["1/2", "1/4", "1/3", "2/3"],
                dogru="1/2",
                aciklama="0,75 = 3/4, sonra 3/4 - 1/4 = 2/4 = 1/2"
            ),
            Soru(
                soru="2/5 × 10/3 = ?",
                secenekler=["4/3", "3/4", "20/15", "1/2"],
                dogru="4/3",
                aciklama="20/15 = 4/3"
            ),
            Soru(
                soru="1/2 × 2/3 = ?",
                secenekler=["1/3", "2/6", "3/6", "1/6"],
                dogru="1/3",
                aciklama="2/6 = 1/3"
            ),
            Soru(
                soru="3/4 + 1/4 = ?",
                secenekler=["1", "4/8", "2/4", "3/8"],
                dogru="1",
                aciklama="3/4 + 1/4 = 4/4 = 1"
            ),
        ],
        "zor": [
            Soru(
                soru="1/3 + 2/5 = ?",
                secenekler=["11/15", "3/8", "2/8", "3/15"],
                dogru="11/15",
                aciklama="Paydaları eşitle: 5/15 + 6/15 = 11/15"
            ),
            Soru(
                soru="5/6 - 1/3 = ?",
                secenekler=["1/2", "4/6", "2/3", "1/3"],
                dogru="1/2",
                aciklama="5/6 - 2/6 = 3/6 = 1/2"
            ),
            Soru(
                soru="3/4 × 2/5 = ?",
                secenekler=["3/10", "6/20", "5/9", "1/2"],
                dogru="3/10",
                aciklama="6/20 = 3/10"
            ),
            Soru(
                soru="5/9 ÷ 1/3 = ?",
                secenekler=["5/3", "3/5", "5/27", "1/3"],
                dogru="5/3",
                aciklama="5/9 × 3/1 = 15/9 = 5/3"
            ),
            Soru(
                soru="(-1/2) + (-1/3) = ?",
                secenekler=["-5/6", "-1/6", "-3/5", "-2/5"],
                dogru="-5/6",
                aciklama="-3/6 - 2/6 = -5/6"
            ),
            Soru(
                soru="2/3 + 3/4 = ?",
                secenekler=["17/12", "5/7", "5/12", "6/12"],
                dogru="17/12",
                aciklama="Paydaları eşitle: 8/12 + 9/12 = 17/12"
            ),
            Soru(
                soru="7/8 × 4/7 = ?",
                secenekler=["1/2", "4/8", "28/56", "7/8"],
                dogru="1/2",
                aciklama="28/56 = 1/2"
            ),
        ],
    },

    "ÜNİTE 3: CEBİRSEL İFADELER": {
        "temel": [
            Soru(
                soru="3x + 5 + 2x = ?",
                secenekler=["5x + 5", "5x", "6x + 5", "x + 5"],
                dogru="5x + 5",
                aciklama="Benzer terimler toplanır: 3x + 2x = 5x"
            ),
            Soru(
                soru="2a + 3b - a + b = ?",
                secenekler=["a + 4b", "a + 3b", "3a + 4b", "a + 2b"],
                dogru="a + 4b",
                aciklama="2a - a = a, 3b + b = 4b"
            ),
            Soru(
                soru="x + 7 = 12 ise x kaçtır?",
                secenekler=["5", "19", "-5", "12"],
                dogru="5",
                aciklama="x = 12 - 7 = 5"
            ),
            Soru(
                soru="2x + 3 = 11 ise x kaçtır?",
                secenekler=["4", "5", "6", "8"],
                dogru="4",
                aciklama="2x = 8, x = 4"
            ),
            Soru(
                soru="3(x + 2) = 15 ise x kaçtır?",
                secenekler=["3", "5", "2", "4"],
                dogru="3",
                aciklama="3x + 6 = 15, 3x = 9, x = 3"
            ),
            Soru(
                soru="x - 3 = 7 ise x kaçtır?",
                secenekler=["10", "4", "-4", "3"],
                dogru="10",
                aciklama="x = 7 + 3 = 10"
            ),
            Soru(
                soru="4x - x = ?",
                secenekler=["3x", "5x", "-3x", "x"],
                dogru="3x",
                aciklama="4x - x = 3x"
            ),
        ],
        "orta": [
            Soru(
                soru="4x - 2 + x + 8 = ?",
                secenekler=["5x + 6", "5x", "5x - 6", "4x + 6"],
                dogru="5x + 6",
                aciklama="4x + x = 5x, -2 + 8 = 6"
            ),
            Soru(
                soru="x - 5 = 12 ise x kaçtır?",
                secenekler=["17", "7", "-7", "12"],
                dogru="17",
                aciklama="x = 12 + 5 = 17"
            ),
            Soru(
                soru="3x = 24 ise x kaçtır?",
                secenekler=["8", "24", "6", "12"],
                dogru="8",
                aciklama="x = 24 ÷ 3 = 8"
            ),
            Soru(
                soru="x/2 = 10 ise x kaçtır?",
                secenekler=["20", "5", "10", "2"],
                dogru="20",
                aciklama="x = 10 × 2 = 20"
            ),
            Soru(
                soru="2x + 1 = 9 ise x kaçtır?",
                secenekler=["4", "5", "8", "3"],
                dogru="4",
                aciklama="2x = 8, x = 4"
            ),
            Soru(
                soru="5x + 2x = ?",
                secenekler=["7x", "3x", "10x", "x"],
                dogru="7x",
                aciklama="5x + 2x = 7x"
            ),
            Soru(
                soru="2(x + 3) = 14 ise x kaçtır?",
                secenekler=["4", "3", "7", "5"],
                dogru="4",
                aciklama="2x + 6 = 14, 2x = 8, x = 4"
            ),
        ],
        "zor": [
            Soru(
                soru="(x + 2)(x - 3) = ?",
                secenekler=["x² - x - 6", "x² + x - 6", "x² - 6", "x² - 5x - 6"],
                dogru="x² - x - 6",
                aciklama="Dağıtma özelliği: x² - 3x + 2x - 6 = x² - x - 6"
            ),
            Soru(
                soru="2x + 5 = 3x - 2 ise x kaçtır?",
                secenekler=["7", "5", "3", "2"],
                dogru="7",
                aciklama="5 + 2 = 3x - 2x, x = 7"
            ),
            Soru(
                soru="5(2x - 1) = 35 ise x kaçtır?",
                secenekler=["4", "5", "3", "6"],
                dogru="4",
                aciklama="10x - 5 = 35, 10x = 40, x = 4"
            ),
            Soru(
                soru="3x + 2y = 12 ve x = 2 ise y kaçtır?",
                secenekler=["3", "4", "5", "6"],
                dogru="3",
                aciklama="3(2) + 2y = 12, 6 + 2y = 12, y = 3"
            ),
            Soru(
                soru="3x - 5 = 16 ise x kaçtır?",
                secenekler=["7", "5", "6", "8"],
                dogru="7",
                aciklama="3x = 21, x = 7"
            ),
            Soru(
                soru="(x + 1)(x + 2) = ?",
                secenekler=["x² + 3x + 2", "x² + 2x + 1", "x² + 3x + 1", "x² + x + 2"],
                dogru="x² + 3x + 2",
                aciklama="x² + 2x + x + 2 = x² + 3x + 2"
            ),
            Soru(
                soru="4x - 3x = ?",
                secenekler=["x", "7x", "-x", "12x"],
                dogru="x",
                aciklama="4x - 3x = x"
            ),
        ],
    },

    "ÜNİTE 4: ORAN - ORANTІ VE YÜZDELER": {
        "temel": [
            Soru(
                soru="Bir gömlek 80 TL'dir. %25 indirim yapılırsa, yeni fiyatı kaç TL'dir?",
                secenekler=["60", "70", "55", "65"],
                dogru="60",
                aciklama="80 × 25/100 = 20 indirim, 80 - 20 = 60 TL"
            ),
            Soru(
                soru="300'ün %10'u kaçtır?",
                secenekler=["30", "50", "20", "40"],
                dogru="30",
                aciklama="300 × 10/100 = 30"
            ),
            Soru(
                soru="Bir sınıfta 40 öğrenci vardır. %50'si erkek ise, kaç erkek vardır?",
                secenekler=["20", "25", "30", "15"],
                dogru="20",
                aciklama="40 × 50/100 = 20"
            ),
            Soru(
                soru="120 TL'nin %20 fazlası kaç TL'dir?",
                secenekler=["144", "140", "150", "160"],
                dogru="144",
                aciklama="120 × 20/100 = 24 artış, 120 + 24 = 144 TL"
            ),
            Soru(
                soru="2:4 oranını sadeleştirin.",
                secenekler=["1:2", "2:3", "1:3", "2:5"],
                dogru="1:2",
                aciklama="Her iki taraf 2'ye bölünür."
            ),
            Soru(
                soru="50'nin %20'si kaçtır?",
                secenekler=["10", "20", "5", "25"],
                dogru="10",
                aciklama="50 × 20/100 = 10"
            ),
            Soru(
                soru="200'ün %5'i kaçtır?",
                secenekler=["10", "20", "15", "5"],
                dogru="10",
                aciklama="200 × 5/100 = 10"
            ),
        ],
        "orta": [
            Soru(
                soru="Bir kitap 50 TL'dir. %30 indirimliyse kaç TL'ye satılır?",
                secenekler=["35", "40", "30", "45"],
                dogru="35",
                aciklama="50 × 30/100 = 15 indirim, 50 - 15 = 35 TL"
            ),
            Soru(
                soru="50 sayısı 200 sayısının yüzde kaçıdır?",
                secenekler=["25", "20", "30", "15"],
                dogru="25",
                aciklama="50/200 × 100 = 25%"
            ),
            Soru(
                soru="Bir ürünün fiyatı 100 TL'den 150 TL'ye çıktı. Yüzde kaç artış oldu?",
                secenekler=["50", "40", "60", "30"],
                dogru="50",
                aciklama="(150-100)/100 × 100 = 50%"
            ),
            Soru(
                soru="3:5 oranında A:B vardır. Toplam 80 ise B kaçtır?",
                secenekler=["50", "40", "30", "60"],
                dogru="50",
                aciklama="3x + 5x = 80, 8x = 80, x = 10, B = 50"
            ),
            Soru(
                soru="200'ün %150'si kaçtır?",
                secenekler=["300", "250", "350", "400"],
                dogru="300",
                aciklama="200 × 150/100 = 300"
            ),
            Soru(
                soru="100'ün %25'i kaçtır?",
                secenekler=["25", "50", "20", "75"],
                dogru="25",
                aciklama="100 × 25/100 = 25"
            ),
            Soru(
                soru="Bir malın fiyatı 80 TL'den 96 TL'ye çıktı. Yüzde kaç artış?",
                secenekler=["20", "25", "15", "30"],
                dogru="20",
                aciklama="(96-80)/80 × 100 = 20%"
            ),
        ],
        "zor": [
            Soru(
                soru="600'ün %35'i kaçtır?",
                secenekler=["210", "200", "220", "230"],
                dogru="210",
                aciklama="600 × 35/100 = 210"
            ),
            Soru(
                soru="Bir öğrenci 400 TL'den 480 TL'ye birikinti yaptı. Yüzde kaç artış?",
                secenekler=["20", "25", "15", "30"],
                dogru="20",
                aciklama="(480-400)/400 × 100 = 20%"
            ),
            Soru(
                soru="Bir mal %40 kâr ile 140 TL'ye satılıyor. Maliyet kaç TL?",
                secenekler=["100", "120", "110", "130"],
                dogru="100",
                aciklama="100 + 100×40/100 = 100 + 40 = 140"
            ),
            Soru(
                soru="2:3:5 oranında A:B:C vardır. Toplam 100 ise B kaçtır?",
                secenekler=["30", "25", "20", "40"],
                dogru="30",
                aciklama="2x + 3x + 5x = 100, 10x = 100, x = 10, B = 30"
            ),
            Soru(
                soru="Bir harita 1:1000 ölçekte yapılmıştır. 5 cm'lik harita uzunluğu gerçekte kaç metredir?",
                secenekler=["50", "40", "60", "30"],
                dogru="50",
                aciklama="5 cm × 1000 = 5000 cm = 50 m"
            ),
            Soru(
                soru="Bir ürünün fiyatı %10 düşürüldü. Yeni fiyat 90 TL ise eski fiyat kaçtır?",
                secenekler=["100", "110", "120", "80"],
                dogru="100",
                aciklama="x × 90/100 = 90, x = 100"
            ),
            Soru(
                soru="4:6 oranını sadeleştirin.",
                secenekler=["2:3", "1:2", "2:4", "3:4"],
                dogru="2:3",
                aciklama="Her iki taraf 2'ye bölünür."
            ),
        ],
    },

    "ÜNİTE 5: DOĞRULAR VE AÇILAR": {
        "temel": [
            Soru(
                soru="Bir açı 45° ise, tümleyeni kaç derecedir?",
                secenekler=["45", "90", "135", "180"],
                dogru="45",
                aciklama="Tümleyen açı: 90° - 45° = 45°"
            ),
            Soru(
                soru="Bir açı 60° ise, bütünleyeni kaç derecedir?",
                secenekler=["120", "90", "60", "180"],
                dogru="120",
                aciklama="Bütünleyen açı: 180° - 60° = 120°"
            ),
            Soru(
                soru="Ters açılar eşit midir?",
                secenekler=["Evet", "Hayır", "Bazen", "Belki"],
                dogru="Evet",
                aciklama="Ters açılar her zaman eşittir."
            ),
            Soru(
                soru="Dik açı kaç derecedir?",
                secenekler=["90", "180", "45", "60"],
                dogru="90",
                aciklama="Dik açı 90°'dir."
            ),
            Soru(
                soru="Bir kare kaç kenarı vardır?",
                secenekler=["4", "3", "5", "6"],
                dogru="4",
                aciklama="Karenin 4 eşit kenarı vardır."
            ),
            Soru(
                soru="Doğru açı kaç derecedir?",
                secenekler=["180", "90", "45", "270"],
                dogru="180",
                aciklama="Doğru açı 180°'dir."
            ),
            Soru(
                soru="Dar açı kaç derecedir?",
                secenekler=["0° ile 90° arasında", "90°", "90° ile 180° arasında", "180° ile 360° arasında"],
                dogru="0° ile 90° arasında",
                aciklama="Dar açı 0° ile 90° arasındadır."
            ),
        ],
        "orta": [
            Soru(
                soru="Dairenin çevresi formülü nedir?",
                secenekler=["C = 2πr", "C = πr²", "C = πr", "C = π²r"],
                dogru="C = 2πr",
                aciklama="Çevre = 2 × π × Yarıçap"
            ),
            Soru(
                soru="Dairenin alanı formülü nedir?",
                secenekler=["A = πr²", "A = 2πr", "A = πr", "A = πd"],
                dogru="A = πr²",
                aciklama="Alan = π × Yarıçap²"
            ),
            Soru(
                soru="Yarıçapı 5 cm olan dairenin çevresi kaç cm'dir?",
                secenekler=["10π", "5π", "25π", "2π"],
                dogru="10π",
                aciklama="C = 2π(5) = 10π ≈ 31,4 cm"
            ),
            Soru(
                soru="Yarıçapı 3 cm olan dairenin alanı kaç cm²'dir?",
                secenekler=["9π", "6π", "3π", "18π"],
                dogru="9π",
                aciklama="A = π(3)² = 9π ≈ 28,3 cm²"
            ),
            Soru(
                soru="İki doğru kesiştiğinde kaç tane açı oluşur?",
                secenekler=["4", "2", "6", "8"],
                dogru="4",
                aciklama="4 açı oluşur."
            ),
            Soru(
                soru="Bir açı 35° ise tümleyeni kaçtır?",
                secenekler=["55", "145", "65", "25"],
                dogru="55",
                aciklama="90° - 35° = 55°"
            ),
            Soru(
                soru="Bir açı 75° ise bütünleyeni kaçtır?",
                secenekler=["105", "15", "90", "165"],
                dogru="105",
                aciklama="180° - 75° = 105°"
            ),
        ],
        "zor": [
            Soru(
                soru="Bir üçgenin iç açılarının toplamı kaç derecedir?",
                secenekler=["180", "90", "270", "360"],
                dogru="180",
                aciklama="Tüm üçgenlerin iç açıları 180°'dir."
            ),
            Soru(
                soru="Bir açı 30° ise, bu açıyı iki eşit parçaya bölen ışın, her açıyı kaç dereceye böler?",
                secenekler=["15", "30", "60", "10"],
                dogru="15",
                aciklama="30° ÷ 2 = 15°"
            ),
            Soru(
                soru="İkizkenar üçgende eş kenarların karşısındaki açılar eşit midir?",
                secenekler=["Evet", "Hayır", "Bazen", "Belki"],
                dogru="Evet",
                aciklama="İkizkenar üçgenin taban açıları eşittir."
            ),
            Soru(
                soru="Eşkenar üçgenin tüm kenarları eşit midir?",
                secenekler=["Evet", "Hayır", "Bazen", "Belki"],
                dogru="Evet",
                aciklama="Eşkenar üçgenin tüm kenarları ve açıları eşittir."
            ),
            Soru(
                soru="Çokgenin iç açıları toplamı formülü nedir?",
                secenekler=["(n-2) × 180", "n × 180", "(n-1) × 180", "n × 90"],
                dogru="(n-2) × 180",
                aciklama="n kenar sayısıdır."
            ),
            Soru(
                soru="Bir dordörtgenin iç açıları toplamı kaç derecedir?",
                secenekler=["360", "180", "540", "720"],
                dogru="360",
                aciklama="(4-2) × 180 = 360°"
            ),
            Soru(
                soru="Eşkenar üçgenin her bir açısı kaç derecedir?",
                secenekler=["60", "90", "45", "30"],
                dogru="60",
                aciklama="180° ÷ 3 = 60°"
            ),
        ],
    },

    "ÜNİTE 6: VERİ ANALİZİ VE ÖLÇÜMLER": {
        "temel": [
            Soru(
                soru="Aritmetik ortalama nasıl bulunur?",
                secenekler=["Tüm değerlerin toplamını veri sayısına böl", "En büyük değerden en küçüğü çıkar", "En çok tekrarlanan değer bul", "Ortadaki değeri seç"],
                dogru="Tüm değerlerin toplamını veri sayısına böl",
                aciklama="Ortalama = Toplam / Veri Sayısı"
            ),
            Soru(
                soru="Medyan nedir?",
                secenekler=["Sıralanmış verinin ortasındaki değer", "En çok tekrarlanan değer", "Tüm değerlerin toplamı", "En büyük ve en küçük fark"],
                dogru="Sıralanmış verinin ortasındaki değer",
                aciklama="Küçükten büyüğe sıralanmış verinin ortasıdır."
            ),
            Soru(
                soru="Mod nedir?",
                secenekler=["En sık tekrarlanan değer", "Ortadaki değer", "Başlangıç değeri", "Son değer"],
                dogru="En sık tekrarlanan değer",
                aciklama="Mod = En çok görülen değer"
            ),
            Soru(
                soru="1, 3, 5, 7, 9 sayılarının ortalaması kaçtır?",
                secenekler=["5", "6", "7", "4"],
                dogru="5",
                aciklama="(1+3+5+7+9)/5 = 25/5 = 5"
            ),
            Soru(
                soru="2, 4, 4, 6, 8 sayılarının medyanı kaçtır?",
                secenekler=["4", "5", "6", "3"],
                dogru="4",
                aciklama="Sıralı: 2,4,4,6,8 → Ortadaki = 4"
            ),
            Soru(
                soru="3, 3, 5, 5, 5, 7 sayılarının modunu bulunuz.",
                secenekler=["5", "3", "7", "4"],
                dogru="5",
                aciklama="5 en sık (3 kez) tekrarlanan sayıdır."
            ),
            Soru(
                soru="10, 20, 30 sayılarının ortalaması kaçtır?",
                secenekler=["20", "15", "25", "30"],
                dogru="20",
                aciklama="(10+20+30)/3 = 60/3 = 20"
            ),
        ],
        "orta": [
            Soru(
                soru="Küpün farklı görünümlerinin sayısı kaçtır?",
                secenekler=["6", "4", "8", "12"],
                dogru="6",
                aciklama="Küpün 6 farklı yüzü vardır."
            ),
            Soru(
                soru="Dikdörtgenler prizmasının kaç tane dikdörtgen yüzü vardır?",
                secenekler=["6", "4", "8", "12"],
                dogru="6",
                aciklama="Dikdörtgenler prizmasının 6 yüzü vardır."
            ),
            Soru(
                soru="Kübün bir kenarı a ise, yüzey alanı kaçtır?",
                secenekler=["6a²", "a²", "4a²", "8a²"],
                dogru="6a²",
                aciklama="6 × (a × a) = 6a²"
            ),
            Soru(
                soru="Prizmanın hacmi formülü nedir?",
                secenekler=["V = Taban Alanı × Yükseklik", "V = πr²h", "V = bh/3", "V = 2bh"],
                dogru="V = Taban Alanı × Yükseklik",
                aciklama="Hacim = Taban × Yükseklik"
            ),
            Soru(
                soru="Küpün kenarı 2 cm ise, hacmi kaç cm³'tür?",
                secenekler=["8", "4", "6", "12"],
                dogru="8",
                aciklama="V = 2³ = 8 cm³"
            ),
            Soru(
                soru="Dikdörtgenler prizmasının kenarları 2, 3, 4 cm ise hacmi kaç cm³?",
                secenekler=["24", "12", "18", "36"],
                dogru="24",
                aciklama="V = 2 × 3 × 4 = 24 cm³"
            ),
            Soru(
                soru="Küpün kenarı 3 cm ise yüzey alanı kaçtır?",
                secenekler=["54", "27", "36", "45"],
                dogru="54",
                aciklama="6 × 3² = 6 × 9 = 54 cm²"
            ),
        ],
        "zor": [
            Soru(
                soru="10, 20, 30, 40, 50 sayılarının modunu bulunuz.",
                secenekler=["Mod yok", "30", "40", "50"],
                dogru="Mod yok",
                aciklama="Hiç tekrarlanan sayı yoktur."
            ),
            Soru(
                soru="1, 1, 2, 2, 2, 3, 4 sayılarının modunu bulunuz.",
                secenekler=["2", "1", "3", "4"],
                dogru="2",
                aciklama="2 en sık (3 kez) tekrarlanan sayıdır."
            ),
            Soru(
                soru="İstatistikte açıklık (range) nedir?",
                secenekler=["En büyük - En küçük değer", "Ortalama", "Medyan", "Mod"],
                dogru="En büyük - En küçük değer",
                aciklama="Range = Max - Min"
            ),
            Soru(
                soru="Silindir hacmi formülü nedir?",
                secenekler=["V = πr²h", "V = 2πr²h", "V = πrh", "V = πr³"],
                dogru="V = πr²h",
                aciklama="Hacim = π × Yarıçap² × Yükseklik"
            ),
            Soru(
                soru="Piramidin hacmi formülü nedir?",
                secenekler=["V = (Taban Alanı × Yükseklik) / 3", "V = Taban Alanı × Yükseklik", "V = πr²h / 3", "V = 2bh/3"],
                dogru="V = (Taban Alanı × Yükseklik) / 3",
                aciklama="Hacim = (Taban × h) / 3"
            ),
            Soru(
                soru="Kürenin hacmi formülü nedir?",
                secenekler=["V = (4/3)πr³", "V = πr²h", "V = 4πr²", "V = πr³"],
                dogru="V = (4/3)πr³",
                aciklama="Kürenin hacmi = (4/3) × π × r³"
            ),
            Soru(
                soru="Kürenin yüzey alanı formülü nedir?",
                secenekler=["A = 4πr²", "A = πr²", "A = 2πr²", "A = 4πr"],
                dogru="A = 4πr²",
                aciklama="Kürenin yüzey alanı = 4 × π × r²"
            ),
        ],
    },
}

# ==================== SEVİYE YÖNETİCİSİ ====================

class SeviyeYoneticisi:
    """Adaptif seviye ilerleme yöneticisi"""
    SEVIYELER = ["temel", "orta", "zor"]
    HEDEF_YUZDE = {
        "temel": 60.0,
        "orta": 80.0,
        "zor": 0.0  # Final seviye hedefi yok
    }
    
    def __init__(self):
        self.mevcut_seviye_index = 0
        self.sonuclar_gecmisi: List[SeviyeSonucu] = []
    
    def mevcut_seviye(self) -> str:
        """Mevcut seviyeyi döndür"""
        return self.SEVIYELER[self.mevcut_seviye_index]
    
    def seviye_tamamlandi(self, sonuc: SeviyeSonucu) -> tuple[bool, str]:
        """
        Seviye tamamlandığında sonuç olup olmadığını kontrol et
        Returns: (başarılı_mı, sonraki_adım_mesajı)
        """
        self.sonuclar_gecmisi.append(sonuc)
        hedef = self.HEDEF_YUZDE[sonuc.seviye]
        
        if sonuc.gec_mi(hedef):  # Hedef yüzdeyi geçtiyse
            if self.mevcut_seviye_index < len(self.SEVIYELER) - 1:
                self.mevcut_seviye_index += 1
                sonraki_seviye = self.mevcut_seviye().upper()
                return True, f"🎉 Harika başarı! {sonuc.seviye.upper()} seviyesini geçtiniz.\n\nŞimdi {sonraki_seviye} seviyesine geçiyorsunuz."
            else:
                return True, f"🏆 Tebrikler! Tüm seviyeleri başarıyla tamamladınız!\n\nFinal başarı oranı: %{sonuc.basari_yuzde:.1f}"
        else:
            return False, f"⚠️ {sonuc.seviye.upper()} seviyesini tekrar çözmek gerekiyor.\nBaşarı oranınız: %{sonuc.basari_yuzde:.1f}\n\nHedef: %{hedef}\n\nBiraz daha pratik yap!"
    
    def sifirla(self):
        """Başlangıç haline getir"""
        self.mevcut_seviye_index = 0
        self.sonuclar_gecmisi.clear()

# ==================== ANA UYGULAMA SINIFI ====================

class AdaptifOgrenimSistemi:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Adaptif Öğrenime Sistemi - 7. Sınıf Matematik")
        self.root.geometry("950x750")
        self.root.resizable(True, True)
        
        # Renkler ve stil
        self.RENKLER = {
            "bg": "#f0f4f8",
            "header": "#0f172a",
            "buton": "#3b82f6",
            "dogru": "#10b981",
            "yanlis": "#ef4444",
            "uyari": "#f59e0b",
            "metin": "#1e293b",
            "acik_metin": "#64748b",
        }
        
        self.root.config(bg=self.RENKLER["bg"])
        
        # Durum değişkenleri
        self.seviye_yoneticisi = SeviyeYoneticisi()
        self.secilen_unite = None
        self.sorular_listesi: List[Soru] = []
        self.soru_index = 0
        self.dogru = 0
        self.yanlis = 0
        self.baslangic_zamani = None
        
        self.arayuz_unite_secimi()
    
    # ==================== ARAYÜZ: ÜNİTE SEÇİMİ ====================
    
    def arayuz_unite_secimi(self):
        """Ünite seçim ekranı"""
        self.temizle()
        
        # Header
        header = tk.Frame(self.root, bg=self.RENKLER["header"], height=100)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            header,
            text="📚 7. SINIF MATEMATİK",
            font=("Segoe UI", 26, "bold"),
            bg=self.RENKLER["header"],
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            header,
            text="Adaptif Öğrenime Sistemi",
            font=("Segoe UI", 11),
            bg=self.RENKLER["header"],
            fg="#cbd5e1"
        ).pack()
        
        # İçerik
        icenik = tk.Frame(self.root, bg=self.RENKLER["bg"])
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            icenik,
            text="📖 Çalışmak İstediğiniz Ünitéyi Seçin",
            font=("Segoe UI", 14, "bold"),
            bg=self.RENKLER["bg"],
            fg=self.RENKLER["metin"]
        ).pack(pady=20)
        
        # Scroll frame
        canvas = tk.Canvas(icenik, bg=self.RENKLER["bg"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(icenik, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.RENKLER["bg"])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Üniteler
        for unite in SORU_BANKASI.keys():
            self._olustur_unite_butonu(scrollable_frame, unite)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _olustur_unite_butonu(self, parent, unite: str):
        """Ünite butonu oluştur"""
        btn_frame = tk.Frame(parent, bg="white", relief=tk.RAISED, bd=1)
        btn_frame.pack(fill=tk.X, pady=10, padx=5)
        
        tk.Label(
            btn_frame,
            text=unite,
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg=self.RENKLER["header"],
            wraplength=750,
            justify="left"
        ).pack(anchor="w", padx=15, pady=10)
        
        btn = tk.Button(
            btn_frame,
            text="Başla ▶",
            font=("Segoe UI", 10, "bold"),
            bg=self.RENKLER["buton"],
            fg="white",
            command=lambda u=unite: self.testi_basla(u),
            padx=15,
            pady=5,
            relief=tk.FLAT
        )
        btn.pack(anchor="e", padx=15, pady=(0, 10))
    
    # ==================== TEST BAŞLATMA ====================
    
    def testi_basla(self, unite: str):
        """Test başlat - otomatik temel seviyeden başla"""
        self.secilen_unite = unite
        self.seviye_yoneticisi.sifirla()
        self.sonraki_seviyeye_gecis()
    
    def sonraki_seviyeye_gecis(self):
        """Sonraki seviyeye geç"""
        mevcut_seviye = self.seviye_yoneticisi.mevcut_seviye()
        
        # Soruları seç ve karıştır
        tum_sorular = SORU_BANKASI[self.secilen_unite][mevcut_seviye].copy()
        random.shuffle(tum_sorular)
        self.sorular_listesi = tum_sorular[:5]  # 5 soru seç
        
        self.soru_index = 0
        self.dogru = 0
        self.yanlis = 0
        self.baslangic_zamani = time.time()
        
        self.soru_goster()
    
    # ==================== ARAYÜZ: SORU GÖSTER ====================
    
    def soru_goster(self):
        """Soru göster"""
        if self.soru_index >= len(self.sorular_listesi):
            self.seviye_tamamlandi()
            return
        
        self.temizle()
        soru_data = self.sorular_listesi[self.soru_index]
        mevcut_seviye = self.seviye_yoneticisi.mevcut_seviye()
        
        # Header
        header = tk.Frame(self.root, bg=self.RENKLER["header"], height=130)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        unite_kisa = self.secilen_unite.split(":")[1].strip() if ":" in self.secilen_unite else self.secilen_unite
        tk.Label(
            header,
            text=f"📖 {unite_kisa}",
            font=("Segoe UI", 13, "bold"),
            bg=self.RENKLER["header"],
            fg="white"
        ).pack(pady=10)
        
        seviye_emoji = {"temel": "⭐", "orta": "⭐⭐", "zor": "⭐⭐⭐"}
        ilerleme = self.soru_index + 1
        toplam = len(self.sorular_listesi)
        
        tk.Label(
            header,
            text=f"{seviye_emoji[mevcut_seviye]} {mevcut_seviye.upper()} SEVİYE | "
                 f"Soru {ilerleme}/{toplam}",
            font=("Segoe UI", 10),
            bg=self.RENKLER["header"],
            fg="#cbd5e1"
        ).pack()
        
        tk.Label(
            header,
            text=f"✓ Doğru: {self.dogru} | ✗ Yanlış: {self.yanlis}",
            font=("Segoe UI", 10),
            bg=self.RENKLER["header"],
            fg="#cbd5e1"
        ).pack()
        
        # Progress Bar
        progress_frame = tk.Frame(header, bg="#1e293b", height=8)
        progress_frame.pack(fill=tk.X, padx=0, pady=(10, 0))
        
        progress_width = (ilerleme / toplam) * 950
        progress_bar = tk.Frame(progress_frame, bg=self.RENKLER["buton"], height=8)
        progress_bar.place(width=progress_width, height=8)
        
        # İçerik
        icenik = tk.Frame(self.root, bg=self.RENKLER["bg"])
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Soru
        soru_frame = tk.Frame(icenik, bg="white", relief=tk.RAISED, bd=1)
        soru_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(
            soru_frame,
            text=soru_data.soru,
            font=("Segoe UI", 13, "bold"),
            bg="white",
            fg=self.RENKLER["metin"],
            wraplength=850,
            justify="left"
        ).pack(padx=20, pady=20)
        
        # Seçenekler
        tk.Label(
            icenik,
            text="Doğru cevabı seçin:",
            font=("Segoe UI", 10, "bold"),
            bg=self.RENKLER["bg"],
            fg=self.RENKLER["metin"]
        ).pack(anchor="w", pady=(10, 10))
        
        self.secim_var = tk.StringVar()
        
        for i, secenek in enumerate(soru_data.secenekler):
            frame = tk.Frame(icenik, bg=self.RENKLER["bg"])
            frame.pack(anchor="w", padx=40, pady=5, fill=tk.X)
            
            rb = tk.Radiobutton(
                frame,
                text=secenek,
                variable=self.secim_var,
                value=secenek,
                font=("Segoe UI", 11),
                bg=self.RENKLER["bg"],
                activebackground=self.RENKLER["bg"],
                selectcolor="#e0e0e0",
                fg=self.RENKLER["metin"]
            )
            rb.pack(anchor="w")
        
        # Butonlar
        buton_frame = tk.Frame(icenik, bg=self.RENKLER["bg"])
        buton_frame.pack(pady=20, anchor="center")
        
        tk.Button(
            buton_frame,
            text="✓ Cevabı Kontrol Et",
            font=("Segoe UI", 10, "bold"),
            bg=self.RENKLER["dogru"],
            fg="white",
            command=lambda: self.kontrol_et(soru_data),
            padx=20,
            pady=10,
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            buton_frame,
            text="⊗ Atla",
            font=("Segoe UI", 10, "bold"),
            bg=self.RENKLER["uyari"],
            fg="white",
            command=self.soruyu_atla,
            padx=20,
            pady=10,
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=5)
    
    # ==================== CEVAP KONTROL ====================
    
    def kontrol_et(self, soru_data: Soru):
        """Cevabı kontrol et"""
        cevap = self.secim_var.get()
        
        if not cevap:
            messagebox.showwarning("⚠️ Uyarı", "Lütfen bir seçenek seçin!")
            return
        
        if cevap == soru_data.dogru:
            self.dogru += 1
            motivasyon_mesajlari = [
                "🎉 Mükemmel!",
                "⭐ Harika!",
                "🌟 Çok iyi!",
                "👏 Bravo!",
                "🚀 Süpersin!",
            ]
            motivasyon = random.choice(motivasyon_mesajlari)
            
            messagebox.showinfo(
                f"{motivasyon}",
                f"Doğru cevap: {soru_data.dogru}\n\n"
                f"💡 Açıklama:\n{soru_data.aciklama}"
            )
        else:
            self.yanlis += 1
            messagebox.showerror(
                "❌ Yanlış!",
                f"Sizin cevabınız: {cevap}\n"
                f"Doğru cevap: {soru_data.dogru}\n\n"
                f"📖 Açıklama:\n{soru_data.aciklama}"
            )
        
        self.soru_index += 1
        self.soru_goster()
    
    def soruyu_atla(self):
        """Soruyu atla"""
        self.yanlis += 1
        self.soru_index += 1
        self.soru_goster()
    
    # ==================== SEVİYE SONUCU ====================
    
    def seviye_tamamlandi(self):
        """Seviye tamamlandı ekranı"""
        sure = round(time.time() - self.baslangic_zamani, 1)
        toplam = self.dogru + self.yanlis
        basari_yuzde = (self.dogru / toplam * 100) if toplam > 0 else 0
        
        mevcut_seviye = self.seviye_yoneticisi.mevcut_seviye()
        sonuc = SeviyeSonucu(
            seviye=mevcut_seviye,
            dogru_sayisi=self.dogru,
            yanlis_sayisi=self.yanlis,
            sure=sure,
            basari_yuzde=basari_yuzde
        )
        
        gecis_basarili, mesaj = self.seviye_yoneticisi.seviye_tamamlandi(sonuc)
        
        self.temizle()
        
        # Header
        header = tk.Frame(self.root, bg=self.RENKLER["header"], height=100)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        icon = "✅" if gecis_basarili else "⚠️"
        tk.Label(
            header,
            text=f"{icon} SEVİYE TAMAMLANDI",
            font=("Segoe UI", 24, "bold"),
            bg=self.RENKLER["header"],
            fg="white"
        ).pack(pady=20)
        
        # İçerik
        icenik = tk.Frame(self.root, bg=self.RENKLER["bg"])
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Durum kutusu - başarı durumuna göre renk
        if basari_yuzde >= 80:
            durum_renk = self.RENKLER["dogru"]  # Yeşil
            basari_durumu = "🟢 YÜKSEK BAŞARI"
        elif basari_yuzde >= 60:
            durum_renk = self.RENKLER["uyari"]  # Turuncu
            basari_durumu = "🟠 ORTA BAŞARI"
        else:
            durum_renk = self.RENKLER["yanlis"]  # Kırmızı
            basari_durumu = "🔴 DÜŞÜK BAŞARI"
        
        durum_frame = tk.Frame(icenik, bg=durum_renk, relief=tk.RAISED, bd=2)
        durum_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(
            durum_frame,
            text=basari_durumu,
            font=("Segoe UI", 12, "bold"),
            bg=durum_renk,
            fg="white"
        ).pack(pady=5)
        
        tk.Label(
            durum_frame,
            text=mesaj,
            font=("Segoe UI", 11),
            bg=durum_renk,
            fg="white",
            wraplength=850,
            justify="center"
        ).pack(pady=15)
        
        # İstatistikler
        istatistik_frame = tk.Frame(icenik, bg="white", relief=tk.RAISED, bd=1)
        istatistik_frame.pack(fill=tk.X, pady=15)
        
        # İstatistik satırları
        stats = [
            (f"✓ Doğru Cevaplar", str(self.dogru), self.RENKLER["dogru"]),
            (f"✗ Yanlış Cevaplar", str(self.yanlis), self.RENKLER["yanlis"]),
            (f"📊 Başarı Oranı", f"%{basari_yuzde:.1f}", self.RENKLER["buton"]),
            (f"⏱️ Geçen Süre", f"{sure} saniye", "#8b5cf6"),
        ]
        
        for label, value, renk in stats:
            stat_row = tk.Frame(istatistik_frame, bg="white")
            stat_row.pack(fill=tk.X, padx=20, pady=10)
            
            tk.Label(
                stat_row,
                text=label,
                font=("Segoe UI", 10, "bold"),
                bg="white",
                fg=self.RENKLER["metin"]
            ).pack(anchor="w")
            
            tk.Label(
                stat_row,
                text=value,
                font=("Segoe UI", 14, "bold"),
                bg="white",
                fg=renk
            ).pack(anchor="w", padx=20)
        
        # Butonlar
        buton_frame = tk.Frame(icenik, bg=self.RENKLER["bg"])
        buton_frame.pack(pady=30)
        
        # Devam butonu veya başka ünite seçme
        if gecis_basarili and self.seviye_yoneticisi.mevcut_seviye_index < 3:
            tk.Button(
                buton_frame,
                text="➡️ Sonraki Seviyeye Geç",
                font=("Segoe UI", 11, "bold"),
                bg=self.RENKLER["dogru"],
                fg="white",
                command=self.sonraki_seviyeye_gecis,
                padx=20,
                pady=10,
                relief=tk.FLAT
            ).pack(pady=5)
        
        if not gecis_basarili:
            tk.Button(
                buton_frame,
                text="🔄 Seviyeyi Tekrar Et",
                font=("Segoe UI", 11, "bold"),
                bg=self.RENKLER["uyari"],
                fg="white",
                command=self.sonraki_seviyeye_gecis,
                padx=20,
                pady=10,
                relief=tk.FLAT
            ).pack(pady=5)
        
        tk.Button(
            buton_frame,
            text="📚 Başka Ünitéyi Seç",
            font=("Segoe UI", 11, "bold"),
            bg=self.RENKLER["buton"],
            fg="white",
            command=self.arayuz_unite_secimi,
            padx=20,
            pady=10,
            relief=tk.FLAT
        ).pack(pady=5)
        
        tk.Button(
            buton_frame,
            text="❌ Çıkış",
            font=("Segoe UI", 11, "bold"),
            bg="#64748b",
            fg="white",
            command=self.root.destroy,
            padx=20,
            pady=10,
            relief=tk.FLAT
        ).pack(pady=5)
    
    # ==================== YARDIMCI METODLAR ====================
    
    def temizle(self):
        """Ekranı temizle"""
        for widget in self.root.winfo_children():
            widget.destroy()

# ==================== ÇALIŞTIR ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = AdaptifOgrenimSistemi(root)
    root.mainloop()
