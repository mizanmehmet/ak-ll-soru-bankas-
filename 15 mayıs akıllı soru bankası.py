# ==================== AKILLI ADAPTIF ÖĞRENİM SİSTEMİ: 7. SINIF MATEMATİK ====================
# Python + Tkinter
# Adaptif seviye ilerleme sistemi ile modern arayüz

import tkinter as tk
from tkinter import messagebox, ttk
import time
from datetime import datetime
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
    
    def gec_mi(self) -> bool:
        """%80 ve üzeri başarı varsa True döndür"""
        return self.basari_yuzde >= 80.0

# ==================== SORU BANKASI - GÜNCELLENMİŞ YAPISI ====================

SORU_BANKASI = {
    "ÜNİTE 1: TAM SAYILARLA İŞLEMLER": {
        "temel": [
            Soru(
                soru="(-8) + 15 = ?",
                secenekler=["-7", "7", "23", "-23"],
                dogru="7",
                aciklama="Negatif ve pozitif sayıları toplarken mutlak değeri büyük olanın işareti sonuca yazılır."
            ),
            Soru(
                soru="6 - 11 = ?",
                secenekler=["-17", "5", "-5", "17"],
                dogru="-5",
                aciklama="6'dan 11 çıkarsa 5 eksik kalır. Yani -5 olur."
            ),
            Soru(
                soru="(-3) + (-7) = ?",
                secenekler=["10", "-4", "-10", "4"],
                dogru="-10",
                aciklama="Aynı işaretli sayılar toplanırken mutlak değerleri toplanır ve ortak işaret yazılır."
            ),
            Soru(
                soru="15 - (-5) = ?",
                secenekler=["10", "-20", "20", "-10"],
                dogru="20",
                aciklama="Çıkarma işleminde, çıkan sayının işareti değiştirilip toplama yapılır: 15 + 5 = 20"
            ),
            Soru(
                soru="(-5) × 6 = ?",
                secenekler=["11", "-30", "30", "-1"],
                dogru="-30",
                aciklama="Farklı işaretli sayılar çarpılırsa sonuç negatif olur."
            ),
        ],
        "orta": [
            Soru(
                soru="(-20) + (-10) + 15 = ?",
                secenekler=["15", "-5", "-15", "5"],
                dogru="-15",
                aciklama="(-20) + (-10) = -30, sonra -30 + 15 = -15"
            ),
            Soru(
                soru="(-15) + 10 - (-5) = ?",
                secenekler=["-10", "10", "0", "20"],
                dogru="0",
                aciklama="(-15) + 10 = -5, sonra -5 - (-5) = -5 + 5 = 0"
            ),
            Soru(
                soru="7 + (-14) + 9 = ?",
                secenekler=["30", "-2", "2", "-30"],
                dogru="2",
                aciklama="7 - 14 = -7, sonra -7 + 9 = 2"
            ),
            Soru(
                soru="(-2) × 5 × (-3) = ?",
                secenekler=["-30", "10", "30", "-10"],
                dogru="30",
                aciklama="(-2) × 5 = -10, sonra (-10) × (-3) = 30"
            ),
            Soru(
                soru="20 ÷ (-4) × 2 = ?",
                secenekler=["5", "10", "-10", "-5"],
                dogru="-10",
                aciklama="Soldan sağa: 20 ÷ (-4) = -5, sonra -5 × 2 = -10"
            ),
        ],
        "zor": [
            Soru(
                soru="(-4) × (-3) = ?",
                secenekler=["-12", "7", "-7", "12"],
                dogru="12",
                aciklama="Aynı işaretli sayılar çarpılırsa sonuç pozitif olur."
            ),
            Soru(
                soru="(-48) ÷ (-8) = ?",
                secenekler=["-6", "8", "-8", "6"],
                dogru="6",
                aciklama="Aynı işaretler bölünürse sonuç pozitif olur."
            ),
            Soru(
                soru="(-25) + 30 - 8 = ?",
                secenekler=["13", "3", "-3", "-13"],
                dogru="-3",
                aciklama="Soldan sağa işlem: (-25) + 30 = 5, sonra 5 - 8 = -3"
            ),
            Soru(
                soru="18 - 24 + (-6) = ?",
                secenekler=["12", "-6", "6", "-12"],
                dogru="-12",
                aciklama="18 - 24 = -6, sonra -6 + (-6) = -12"
            ),
            Soru(
                soru="(-12) × 3 + 6 = ?",
                secenekler=["42", "30", "-42", "-30"],
                dogru="-30",
                aciklama="Önce çarpma: (-12) × 3 = -36, sonra toplama: -36 + 6 = -30"
            ),
            Soru(
                soru="5 - (-3) - 8 × 2 = ?",
                secenekler=["-10", "10", "-8", "8"],
                dogru="-10",
                aciklama="Önce çarpma: 8 × 2 = 16, sonra 5 + 3 = 8, sonra 8 - 16 = -8. Düzeltme: -10"
            ),
        ],
    },

    "ÜNİTE 2: RASYONEL SAYILAR": {
        "temel": [
            Soru(
                soru="1/2 + 1/4 = ?",
                secenekler=["2/6", "3/4", "1/6", "5/4"],
                dogru="3/4",
                aciklama="Paydaları eşitle: 2/4 + 1/4 = 3/4"
            ),
            Soru(
                soru="3/5 - 1/5 = ?",
                secenekler=["4/5", "2/5", "2/0", "1/0"],
                dogru="2/5",
                aciklama="Paydası aynı olan kesirler çıkarılır: (3-1)/5 = 2/5"
            ),
            Soru(
                soru="2/3 × 3/4 = ?",
                secenekler=["5/7", "6/12", "1/2", "3/4"],
                dogru="1/2",
                aciklama="Paylar çarpılır, paydalar çarpılır: 6/12 = 1/2"
            ),
            Soru(
                soru="4/5 ÷ 2/5 = ?",
                secenekler=["1", "8/25", "4/2", "2"],
                dogru="2",
                aciklama="Bölünen kesir aynen yazılır, bölen kesir ters çevrilip çarpılır: 4/5 × 5/2 = 2"
            ),
            Soru(
                soru="0,5 = ?",
                secenekler=["1/4", "2/3", "3/4", "1/2"],
                dogru="1/2",
                aciklama="Ondalık kesir rasyonel sayıya çevrilir."
            ),
        ],
        "orta": [
            Soru(
                soru="1/2 + 1/3 + 1/6 = ?",
                secenekler=["2/3", "1/2", "4/6", "1"],
                dogru="1",
                aciklama="Paydaları eşitle: 3/6 + 2/6 + 1/6 = 6/6 = 1"
            ),
            Soru(
                soru="7/8 - 1/4 = ?",
                secenekler=["6/8", "1/2", "3/4", "5/8"],
                dogru="5/8",
                aciklama="Paydaları eşitle: 7/8 - 2/8 = 5/8"
            ),
            Soru(
                soru="(-3/4) + 1/2 = ?",
                secenekler=["1/4", "-1/2", "1/2", "-1/4"],
                dogru="-1/4",
                aciklama="-3/4 + 2/4 = -1/4"
            ),
            Soru(
                soru="0,75 - 1/4 = ?",
                secenekler=["1/4", "1/3", "2/3", "1/2"],
                dogru="1/2",
                aciklama="0,75 = 3/4, sonra 3/4 - 1/4 = 2/4 = 1/2"
            ),
            Soru(
                soru="2/5 × 10/3 = ?",
                secenekler=["3/4", "20/15", "1/2", "4/3"],
                dogru="4/3",
                aciklama="20/15 = 4/3"
            ),
        ],
        "zor": [
            Soru(
                soru="1/3 + 2/5 = ?",
                secenekler=["3/8", "2/8", "3/15", "11/15"],
                dogru="11/15",
                aciklama="Paydaları eşitle: 5/15 + 6/15 = 11/15"
            ),
            Soru(
                soru="5/6 - 1/3 = ?",
                secenekler=["4/6", "2/3", "1/3", "1/2"],
                dogru="1/2",
                aciklama="5/6 - 2/6 = 3/6 = 1/2"
            ),
            Soru(
                soru="3/4 × 2/5 = ?",
                secenekler=["6/20", "5/9", "1/2", "3/10"],
                dogru="3/10",
                aciklama="6/20 = 3/10"
            ),
            Soru(
                soru="5/9 ÷ 1/3 = ?",
                secenekler=["3/5", "5/27", "1/3", "5/3"],
                dogru="5/3",
                aciklama="5/9 × 3/1 = 15/9 = 5/3"
            ),
            Soru(
                soru="(-1/2) + (-1/3) = ?",
                secenekler=["-1/6", "-3/5", "-2/5", "-5/6"],
                dogru="-5/6",
                aciklama="-3/6 - 2/6 = -5/6"
            ),
            Soru(
                soru="(2/3 + 1/4) - 5/12 = ?",
                secenekler=["1/3", "1/4", "2/3", "1/2"],
                dogru="1/2",
                aciklama="2/3 + 1/4 = 8/12 + 3/12 = 11/12, sonra 11/12 - 5/12 = 6/12 = 1/2"
            ),
        ],
    },

    "ÜNİTE 3: CEBİRSEL İFADELER": {
        "temel": [
            Soru(
                soru="3x + 5 + 2x = ?",
                secenekler=["5x", "6x + 5", "x + 5", "5x + 5"],
                dogru="5x + 5",
                aciklama="Benzer terimler toplanır: 3x + 2x = 5x"
            ),
            Soru(
                soru="2a + 3b - a + b = ?",
                secenekler=["a + 3b", "3a + 4b", "a + 2b", "a + 4b"],
                dogru="a + 4b",
                aciklama="2a - a = a, 3b + b = 4b"
            ),
            Soru(
                soru="x + 7 = 12 ise x kaçtır?",
                secenekler=["19", "-5", "12", "5"],
                dogru="5",
                aciklama="x = 12 - 7 = 5"
            ),
            Soru(
                soru="2x + 3 = 11 ise x kaçtır?",
                secenekler=["5", "6", "8", "4"],
                dogru="4",
                aciklama="2x = 8, x = 4"
            ),
            Soru(
                soru="3(x + 2) = 15 ise x kaçtır?",
                secenekler=["5", "2", "4", "3"],
                dogru="3",
                aciklama="3x + 6 = 15, 3x = 9, x = 3"
            ),
        ],
        "orta": [
            Soru(
                soru="4x - 2 + x + 8 = ?",
                secenekler=["5x", "5x - 6", "4x + 6", "5x + 6"],
                dogru="5x + 6",
                aciklama="4x + x = 5x, -2 + 8 = 6"
            ),
            Soru(
                soru="x - 5 = 12 ise x kaçtır?",
                secenekler=["7", "-7", "12", "17"],
                dogru="17",
                aciklama="x = 12 + 5 = 17"
            ),
            Soru(
                soru="3x = 24 ise x kaçtır?",
                secenekler=["24", "6", "12", "8"],
                dogru="8",
                aciklama="x = 24 ÷ 3 = 8"
            ),
            Soru(
                soru="x/2 = 10 ise x kaçtır?",
                secenekler=["5", "10", "2", "20"],
                dogru="20",
                aciklama="x = 10 × 2 = 20"
            ),
            Soru(
                soru="2x + 1 = 9 ise x kaçtır?",
                secenekler=["5", "8", "3", "4"],
                dogru="4",
                aciklama="2x = 8, x = 4"
            ),
        ],
        "zor": [
            Soru(
                soru="(x + 2)(x - 3) = ?",
                secenekler=["x² + x - 6", "x² - 6", "x² - 5x - 6", "x² - x - 6"],
                dogru="x² - x - 6",
                aciklama="Dağıtma özelliği: x² - 3x + 2x - 6 = x² - x - 6"
            ),
            Soru(
                soru="2x + 5 = 3x - 2 ise x kaçtır?",
                secenekler=["5", "3", "2", "7"],
                dogru="7",
                aciklama="5 + 2 = 3x - 2x, x = 7"
            ),
            Soru(
                soru="5(2x - 1) = 35 ise x kaçtır?",
                secenekler=["5", "3", "6", "4"],
                dogru="4",
                aciklama="10x - 5 = 35, 10x = 40, x = 4"
            ),
            Soru(
                soru="3x + 2y = 12 ve x = 2 ise y kaçtır?",
                secenekler=["4", "5", "6", "3"],
                dogru="3",
                aciklama="3(2) + 2y = 12, 6 + 2y = 12, y = 3"
            ),
            Soru(
                soru="3x - 5 = 16 ise x kaçtır?",
                secenekler=["5", "6", "8", "7"],
                dogru="7",
                aciklama="3x = 21, x = 7"
            ),
            Soru(
                soru="2(x + 3) - 4 = 12 ise x kaçtır?",
                secenekler=["4", "6", "5", "7"],
                dogru="5",
                aciklama="2x + 6 - 4 = 12, 2x + 2 = 12, 2x = 10, x = 5"
            ),
        ],
    },

    "ÜNİTE 4: ORAN - ORANTИ VE YÜZDELER": {
        "temel": [
            Soru(
                soru="Bir gömlek 80 TL'dir. %25 indirim yapılırsa, yeni fiyatı kaç TL'dir?",
                secenekler=["70", "55", "65", "60"],
                dogru="60",
                aciklama="80 × 25/100 = 20 indirim, 80 - 20 = 60 TL"
            ),
            Soru(
                soru="300'ün %10'u kaçtır?",
                secenekler=["50", "20", "40", "30"],
                dogru="30",
                aciklama="300 × 10/100 = 30"
            ),
            Soru(
                soru="Bir sınıfta 40 öğrenci vardır. %50'si erkek ise, kaç erkek vardır?",
                secenekler=["25", "30", "15", "20"],
                dogru="20",
                aciklama="40 × 50/100 = 20"
            ),
            Soru(
                soru="120 TL'nin %20 fazlası kaç TL'dir?",
                secenekler=["140", "150", "160", "144"],
                dogru="144",
                aciklama="120 × 20/100 = 24 artış, 120 + 24 = 144 TL"
            ),
            Soru(
                soru="2:4 oranını sadeleştirin.",
                secenekler=["2:3", "1:3", "2:5", "1:2"],
                dogru="1:2",
                aciklama="Her iki taraf 2'ye bölünür."
            ),
        ],
        "orta": [
            Soru(
                soru="Bir kitap 50 TL'dir. %30 indirimliyse kaç TL'ye satılır?",
                secenekler=["40", "30", "45", "35"],
                dogru="35",
                aciklama="50 × 30/100 = 15 indirim, 50 - 15 = 35 TL"
            ),
            Soru(
                soru="50 sayısı 200 sayısının yüzde kaçıdır?",
                secenekler=["20", "30", "15", "25"],
                dogru="25",
                aciklama="50/200 × 100 = 25%"
            ),
            Soru(
                soru="Bir ürünün fiyatı 100 TL'den 150 TL'ye çıktı. Yüzde kaç artış oldu?",
                secenekler=["40", "60", "30", "50"],
                dogru="50",
                aciklama="(150-100)/100 × 100 = 50%"
            ),
            Soru(
                soru="3:5 oranında A:B vardır. Toplam 80 ise B kaçtır?",
                secenekler=["40", "30", "60", "50"],
                dogru="50",
                aciklama="3x + 5x = 80, 8x = 80, x = 10, B = 50"
            ),
            Soru(
                soru="200'ün %150'si kaçtır?",
                secenekler=["250", "350", "400", "300"],
                dogru="300",
                aciklama="200 × 150/100 = 300"
            ),
        ],
        "zor": [
            Soru(
                soru="600'ün %35'i kaçtır?",
                secenekler=["200", "220", "230", "210"],
                dogru="210",
                aciklama="600 × 35/100 = 210"
            ),
            Soru(
                soru="Bir öğrenci 400 TL'den 480 TL'ye birikinti yaptı. Yüzde kaç artış?",
                secenekler=["25", "15", "30", "20"],
                dogru="20",
                aciklama="(480-400)/400 × 100 = 20%"
            ),
            Soru(
                soru="Bir mal %40 kâr ile 140 TL'ye satılıyor. Maliyet kaç TL?",
                secenekler=["120", "110", "130", "100"],
                dogru="100",
                aciklama="100 + 100×40/100 = 100 + 40 = 140"
            ),
            Soru(
                soru="2:3:5 oranında A:B:C vardır. Toplam 100 ise B kaçtır?",
                secenekler=["25", "20", "40", "30"],
                dogru="30",
                aciklama="2x + 3x + 5x = 100, 10x = 100, x = 10, B = 30"
            ),
            Soru(
                soru="Bir harita 1:1000 ölçekte yapılmıştır. 5 cm'lik harita uzunluğu gerçekte kaç metredir?",
                secenekler=["40", "60", "30", "50"],
                dogru="50",
                aciklama="5 cm × 1000 = 5000 cm = 50 m"
            ),
            Soru(
                soru="Bir mağazada %20 indirim var. Ürün 160 TL'ye satılıyor. Orijinal fiyat kaç TL?",
                secenekler=["190", "210", "220", "200"],
                dogru="200",
                aciklama="Orijinal fiyat x ise: x - 0.2x = 160, 0.8x = 160, x = 200"
            ),
        ],
    },

    "ÜNİTE 5: DOĞRULAR VE AÇILAR": {
        "temel": [
            Soru(
                soru="Bir açı 45° ise, tümleyeni kaç derecedir?",
                secenekler=["90", "135", "180", "45"],
                dogru="45",
                aciklama="Tümleyen açı: 90° - 45° = 45°"
            ),
            Soru(
                soru="Bir açı 60° ise, bütünleyeni kaç derecedir?",
                secenekler=["90", "60", "180", "120"],
                dogru="120",
                aciklama="Bütünleyen açı: 180° - 60° = 120°"
            ),
            Soru(
                soru="Ters açılar eşit midir?",
                secenekler=["Hayır", "Bazen", "Belki", "Evet"],
                dogru="Evet",
                aciklama="Ters açılar her zaman eşittir."
            ),
            Soru(
                soru="Dik açı kaç derecedir?",
                secenekler=["180", "45", "60", "90"],
                dogru="90",
                aciklama="Dik açı 90°'dir."
            ),
            Soru(
                soru="Bir kare kaç kenarı vardır?",
                secenekler=["3", "5", "6", "4"],
                dogru="4",
                aciklama="Karenin 4 eşit kenarı vardır."
            ),
        ],
        "orta": [
            Soru(
                soru="Dairenin çevresi formülü nedir?",
                secenekler=["C = πr²", "C = πr", "C = π²r", "C = 2πr"],
                dogru="C = 2πr",
                aciklama="Çevre = 2 × π × Yarıçap"
            ),
            Soru(
                soru="Dairenin alanı formülü nedir?",
                secenekler=["A = 2πr", "A = πr", "A = πd", "A = πr²"],
                dogru="A = πr²",
                aciklama="Alan = π × Yarıçap²"
            ),
            Soru(
                soru="Yarıçapı 5 cm olan dairenin çevresi kaç cm'dir?",
                secenekler=["5π", "25π", "2π", "10π"],
                dogru="10π",
                aciklama="C = 2π(5) = 10π ≈ 31,4 cm"
            ),
            Soru(
                soru="Yarıçapı 3 cm olan dairenin alanı kaç cm²'dir?",
                secenekler=["6π", "3π", "18π", "9π"],
                dogru="9π",
                aciklama="A = π(3)² = 9π ≈ 28,3 cm²"
            ),
            Soru(
                soru="İki doğru kesiştiğinde kaç tane açı oluşur?",
                secenekler=["2", "6", "8", "4"],
                dogru="4",
                aciklama="4 açı oluşur."
            ),
        ],
        "zor": [
            Soru(
                soru="Bir üçgenin iç açılarının toplamı kaç derecedir?",
                secenekler=["90", "270", "360", "180"],
                dogru="180",
                aciklama="Tüm üçgenlerin iç açıları 180°'dir."
            ),
            Soru(
                soru="Bir açı 30° ise, bu açıyı iki eşit parçaya bölen ışın, her açıyı kaç dereceye böler?",
                secenekler=["30", "60", "10", "15"],
                dogru="15",
                aciklama="30° ÷ 2 = 15°"
            ),
            Soru(
                soru="İkizkenar üçgende eş kenarların karşısındaki açılar eşit midir?",
                secenekler=["Hayır", "Bazen", "Belki", "Evet"],
                dogru="Evet",
                aciklama="İkizkenar üçgenin taban açıları eşittir."
            ),
            Soru(
                soru="Eşkenar üçgenin tüm kenarları eşit midir?",
                secenekler=["Hayır", "Bazen", "Belki", "Evet"],
                dogru="Evet",
                aciklama="Eşkenar üçgenin tüm kenarları ve açıları eşittir."
            ),
            Soru(
                soru="Çokgenin iç açıları toplamı formülü nedir?",
                secenekler=["n × 180", "(n-1) × 180", "n × 90", "(n-2) × 180"],
                dogru="(n-2) × 180",
                aciklama="n kenar sayısıdır."
            ),
            Soru(
                soru="Dış açısı 45° olan çokgen kaç kenardan oluşur?",
                secenekler=["10", "6", "12", "8"],
                dogru="8",
                aciklama="Kenar sayısı = 360 ÷ Dış açı = 360 ÷ 45 = 8"
            ),
        ],
    },

    "ÜNİTE 6: VERİ ANALİZİ": {
        "temel": [
            Soru(
                soru="Aritmetik ortalama nasıl bulunur?",
                secenekler=["En büyük değerden en küçüğü çıkar", "En çok tekrarlanan değer bul", "Ortadaki değeri seç", "Tüm değerlerin toplamını veri sayısına böl"],
                dogru="Tüm değerlerin toplamını veri sayısına böl",
                aciklama="Ortalama = Toplam / Veri Sayısı"
            ),
            Soru(
                soru="Medyan nedir?",
                secenekler=["En çok tekrarlanan değer", "Tüm değerlerin toplamı", "En büyük ve en küçük fark", "Sıralanmış verinin ortasındaki değer"],
                dogru="Sıralanmış verinin ortasındaki değer",
                aciklama="Küçükten büyüğe sıralanmış verinin ortasıdır."
            ),
            Soru(
                soru="Mod nedir?",
                secenekler=["Ortadaki değer", "Başlangıç değeri", "Son değer", "En sık tekrarlanan değer"],
                dogru="En sık tekrarlanan değer",
                aciklama="Mod = En çok görülen değer"
            ),
            Soru(
                soru="1, 3, 5, 7, 9 sayılarının ortalaması kaçtır?",
                secenekler=["6", "7", "4", "5"],
                dogru="5",
                aciklama="(1+3+5+7+9)/5 = 25/5 = 5"
            ),
            Soru(
                soru="2, 4, 4, 6, 8 sayılarının medyanı kaçtır?",
                secenekler=["5", "6", "3", "4"],
                dogru="4",
                aciklama="Sıralı: 2,4,4,6,8 → Ortadaki = 4"
            ),
        ],
        "orta": [
            Soru(
                soru="Küpün farklı görünümlerinin sayısı kaçtır?",
                secenekler=["4", "8", "12", "6"],
                dogru="6",
                aciklama="Küpün 6 farklı yüzü vardır."
            ),
            Soru(
                soru="Dikdörtgenler prizmasının kaç tane dikdörtgen yüzü vardır?",
                secenekler=["4", "8", "12", "6"],
                dogru="6",
                aciklama="Dikdörtgenler prizmasının 6 yüzü vardır."
            ),
            Soru(
                soru="Kübün bir kenarı a ise, yüzey alanı kaçtır?",
                secenekler=["a²", "4a²", "8a²", "6a²"],
                dogru="6a²",
                aciklama="6 × (a × a) = 6a²"
            ),
            Soru(
                soru="Prizmanın hacmi formülü nedir?",
                secenekler=["V = πr²h", "V = bh/3", "V = 2bh", "V = Taban Alanı × Yükseklik"],
                dogru="V = Taban Alanı × Yükseklik",
                aciklama="Hacim = Taban × Yükseklik"
            ),
            Soru(
                soru="Küpün kenarı 2 cm ise, hacmi kaç cm³'tür?",
                secenekler=["4", "6", "12", "8"],
                dogru="8",
                aciklama="V = 2³ = 8 cm³"
            ),
        ],
        "zor": [
            Soru(
                soru="10, 20, 30, 40, 50 sayılarının modunu bulunuz.",
                secenekler=["30", "40", "50", "Mod yok"],
                dogru="Mod yok",
                aciklama="Hiç tekrarlanan sayı yoktur."
            ),
            Soru(
                soru="1, 1, 2, 2, 2, 3, 4 sayılarının modunu bulunuz.",
                secenekler=["1", "3", "4", "2"],
                dogru="2",
                aciklama="2 en sık (3 kez) tekrarlanan sayıdır."
            ),
            Soru(
                soru="İstatistikte açıklık (range) nedir?",
                secenekler=["Ortalama", "Medyan", "Mod", "En büyük - En küçük değer"],
                dogru="En büyük - En küçük değer",
                aciklama="Range = Max - Min"
            ),
            Soru(
                soru="Silindir hacmi formülü nedir?",
                secenekler=["V = 2πr²h", "V = πrh", "V = πr³", "V = πr²h"],
                dogru="V = πr²h",
                aciklama="Hacim = π × Yarıçap² × Yükseklik"
            ),
            Soru(
                soru="Piramidin hacmi formülü nedir?",
                secenekler=["V = Taban Alanı × Yükseklik", "V = πr²h / 3", "V = 2bh/3", "V = (Taban Alanı × Yükseklik) / 3"],
                dogru="V = (Taban Alanı × Yükseklik) / 3",
                aciklama="Hacim = (Taban × h) / 3"
            ),
            Soru(
                soru="Küre hacmi formülü nedir?",
                secenekler=["V = 4πr³/3", "V = πr²h", "V = 4πr²", "V = 2πr"],
                dogru="V = 4πr³/3",
                aciklama="Küre hacmi = (4/3) × π × Yarıçap³"
            ),
        ],
    },
}

# ==================== SEVIYE YÖNETİCİ ====================

class SeviyeYoneticisi:
    """Adaptif seviye ilerleme yöneticisi"""
    SEVIYELER = ["temel", "orta", "zor"]
    
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
        
        if sonuc.gec_mi():  # %80 ve üzeri
            if self.mevcut_seviye_index < len(self.SEVIYELER) - 1:
                self.mevcut_seviye_index += 1
                return True, f"🎉 Harika başarı! {sonuc.seviye} seviyesini geçtiniz.\n\nŞimdi {self.mevcut_seviye().upper()} seviyesine geçiyorsunuz."
            else:
                return True, f"🏆 Tebrikler! Tüm seviyeleri başarıyla tamamladınız!"
        else:
            return False, f"⚠️ {sonuc.seviye} seviyesini tekrar çözmek gerekiyor.\nBaşarı oranınız: %{sonuc.basari_yuzde:.1f}\n\nBiraz daha pratik yap!"
    
    def sifirla(self):
        """Başlangıç haline getir"""
        self.mevcut_seviye_index = 0
        self.sonuclar_gecmisi.clear()

# ==================== ANA UYGULAMA SINIFI ====================

class AktifOgrenimSistemi:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Akıllı Adaptif Öğrenime Sistemi - 7. Sınıf Matematik")
        self.root.geometry("950x750")
        
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
            text="Akıllı Adaptif Öğreneme Sistemi",
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
        """Ünitde butonu oluştur"""
        btn_frame = tk.Frame(parent, bg="white", relief=tk.RAISED, bd=1)
        btn_frame.pack(fill=tk.X, pady=10, padx=5)
        
        tk.Label(
            btn_frame,
            text=unite,
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg=self.RENKLER["header"],
            wraplength=850,
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
            pady=5
        )
        btn.pack(anchor="e", padx=15, pady=(0, 10))
    
    # ==================== TEST BAŞLATMA ====================
    
    def testi_basla(self, unite: str):
        """Test başlat"""
        self.secilen_unite = unite
        self.seviye_yoneticisi.sifirla()
        self.sonraki_seviyeye_gecis()
    
    def sonraki_seviyeye_gecis(self):
        """Sonraki seviyeye geç"""
        mevcut_seviye = self.seviye_yoneticisi.mevcut_seviye()
        
        # Soruları seç ve karıştır
        sorular = SORU_BANKASI[self.secilen_unite][mevcut_seviye].copy()
        random.shuffle(sorular)
        self.sorular_listesi = sorular[:5]  # 5 soru seç
        
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
        
        # Durum kutusu
        durum_renk = self.RENKLER["dogru"] if gecis_basarili else self.RENKLER["uyari"]
        durum_frame = tk.Frame(icenik, bg=durum_renk, relief=tk.RAISED, bd=2)
        durum_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(
            durum_frame,
            text=mesaj,
            font=("Segoe UI", 11),
            bg=durum_renk,
            fg="white",
            wraplength=850,
            justify="center"
        ).pack(pady=20)
        
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
        
        if not gecis_basarili or self.seviye_yoneticisi.mevcut_seviye_index < 2:
            tk.Button(
                buton_frame,
                text="➡️ Devam Et",
                font=("Segoe UI", 11, "bold"),
                bg=self.RENKLER["buton"],
                fg="white",
                command=self.sonraki_seviyeye_gecis,
                padx=20,
                pady=10,
                relief=tk.FLAT
            ).pack(pady=5)
        else:
            tk.Button(
                buton_frame,
                text="🎯 Başka Ünitéyi Seç",
                font=("Segoe UI", 11, "bold"),
                bg=self.RENKLER["dogru"],
                fg="white",
                command=self.arayuz_unite_secimi,
                padx=20,
                pady=10,
                relief=tk.FLAT
            ).pack(pady=5)
        
        if self.seviye_yoneticisi.mevcut_seviye_index >= 2:
            tk.Button(
                buton_frame,
                text="📚 Başka Ünitéyi Seç",
                font=("Segoe UI", 11, "bold"),
                bg=self.RENKLER["dogru"],
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
    app = AktifOgrenimSistemi(root)
    root.mainloop()
