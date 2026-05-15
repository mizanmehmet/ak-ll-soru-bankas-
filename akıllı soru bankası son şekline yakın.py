# ==================== AKILLI SORU BANKASI: 7. SINIF MATEMATİK ====================
# 7. Sınıf Matematik Müfredat (Güncellenmiş Üniteler)
# Python + Tkinter
# Kitap tarzında, ünite seçimli, 4 şıklı test

import tkinter as tk
from tkinter import messagebox, ttk
import time
from datetime import datetime
import random

# ==================== KAPSAMLI SORU HAVUZU - 7. SINIF MATEMATİK ====================

SORU_BANKASI = {
    "ÜNİTE 1: TAM SAYILARLA İŞLEMLER": {
        "1": [
            {
                "soru": "(-8) + 15 = ?",
                "secenekler": ["7", "-7", "23", "-23"],
                "dogru": "7",
                "aciklama": "Negatif ve pozitif sayıları toplarken mutlak değeri büyük olanın işareti sonuca yazılır."
            },
            {
                "soru": "6 - 11 = ?",
                "secenekler": ["-5", "5", "17", "-17"],
                "dogru": "-5",
                "aciklama": "6'dan 11 çıkarsa 5 eksik kalır. Yani -5 olur."
            },
            {
                "soru": "(-3) + (-7) = ?",
                "secenekler": ["-10", "10", "-4", "4"],
                "dogru": "-10",
                "aciklama": "Aynı işaretli sayılar toplanırken mutlak değerleri toplanır ve ortak işaret yazılır."
            },
            {
                "soru": "15 - (-5) = ?",
                "secenekler": ["20", "10", "-20", "-10"],
                "dogru": "20",
                "aciklama": "Çıkarma işleminde, çıkan sayının işareti değiştirilip toplama yapılır: 15 + 5 = 20"
            },
            {
                "soru": "(-5) × 6 = ?",
                "secenekler": ["-30", "30", "-1", "11"],
                "dogru": "-30",
                "aciklama": "Farklı işaretli sayılar çarpılırsa sonuç negatif olur."
            },
            {
                "soru": "(-4) × (-3) = ?",
                "secenekler": ["12", "-12", "7", "-7"],
                "dogru": "12",
                "aciklama": "Aynı işaretli sayılar çarpılırsa sonuç pozitif olur."
            },
            {
                "soru": "(-48) ÷ (-8) = ?",
                "secenekler": ["6", "-6", "8", "-8"],
                "dogru": "6",
                "aciklama": "Aynı işaretler bölünürse sonuç pozitif olur."
            },
            {
                "soru": "(-25) + 30 - 8 = ?",
                "secenekler": ["-3", "3", "-13", "13"],
                "dogru": "-3",
                "aciklama": "Soldan sağa işlem: (-25) + 30 = 5, sonra 5 - 8 = -3"
            },
            {
                "soru": "18 - 24 + (-6) = ?",
                "secenekler": ["-12", "12", "-6", "6"],
                "dogru": "-12",
                "aciklama": "18 - 24 = -6, sonra -6 + (-6) = -12"
            },
            {
                "soru": "(-12) × 3 + 6 = ?",
                "secenekler": ["-30", "30", "-42", "42"],
                "dogru": "-30",
                "aciklama": "Önce çarpma: (-12) × 3 = -36, sonra toplama: -36 + 6 = -30"
            },
        ],
        "2": [
            {
                "soru": "(-20) + (-10) + 15 = ?",
                "secenekler": ["-15", "15", "-5", "5"],
                "dogru": "-15",
                "aciklama": "(-20) + (-10) = -30, sonra -30 + 15 = -15"
            },
            {
                "soru": "(-15) + 10 - (-5) = ?",
                "secenekler": ["0", "10", "-10", "20"],
                "dogru": "0",
                "aciklama": "(-15) + 10 = -5, sonra -5 - (-5) = -5 + 5 = 0"
            },
            {
                "soru": "7 + (-14) + 9 = ?",
                "secenekler": ["2", "-2", "30", "-30"],
                "dogru": "2",
                "aciklama": "7 - 14 = -7, sonra -7 + 9 = 2"
            },
            {
                "soru": "(-2) × 5 × (-3) = ?",
                "secenekler": ["30", "-30", "10", "-10"],
                "dogru": "30",
                "aciklama": "(-2) × 5 = -10, sonra (-10) × (-3) = 30"
            },
            {
                "soru": "20 ÷ (-4) × 2 = ?",
                "secenekler": ["-10", "10", "-5", "5"],
                "dogru": "-10",
                "aciklama": "Soldan sağa: 20 ÷ (-4) = -5, sonra -5 × 2 = -10"
            },
            {
                "soru": "(-3) × (-4) × (-2) = ?",
                "secenekler": ["-24", "24", "-12", "12"],
                "dogru": "-24",
                "aciklama": "(-3) × (-4) = 12, sonra 12 × (-2) = -24"
            },
            {
                "soru": "(-18) ÷ 3 = ?",
                "secenekler": ["-6", "6", "-3", "3"],
                "dogru": "-6",
                "aciklama": "Farklı işaretler bölünürse sonuç negatif olur."
            },
            {
                "soru": "(-100) + 50 - (-30) = ?",
                "secenekler": ["-20", "20", "-80", "80"],
                "dogru": "-20",
                "aciklama": "(-100) + 50 = -50, sonra -50 - (-30) = -50 + 30 = -20"
            },
            {
                "soru": "(-7) × (-8) + (-5) = ?",
                "secenekler": ["51", "-51", "45", "-45"],
                "dogru": "51",
                "aciklama": "(-7) × (-8) = 56, sonra 56 + (-5) = 51"
            },
            {
                "soru": "Bir asansör -3. kattan 5 kat yukarı çıkıyor. Hangi kat?",
                "secenekler": ["2", "-2", "8", "-8"],
                "dogru": "2",
                "aciklama": "-3 + 5 = 2"
            },
        ],
    },

    "ÜNİTE 2: RASYONEL SAYILAR VE RASYONEL SAYILARLA İŞLEMLER": {
        "1": [
            {
                "soru": "1/2 + 1/4 = ?",
                "secenekler": ["3/4", "2/6", "1/6", "5/4"],
                "dogru": "3/4",
                "aciklama": "Paydaları eşitle: 2/4 + 1/4 = 3/4"
            },
            {
                "soru": "3/5 - 1/5 = ?",
                "secenekler": ["2/5", "4/5", "2/0", "1/0"],
                "dogru": "2/5",
                "aciklama": "Paydası aynı olan kesirler çıkarılır: (3-1)/5 = 2/5"
            },
            {
                "soru": "2/3 × 3/4 = ?",
                "secenekler": ["1/2", "5/7", "6/12", "3/4"],
                "dogru": "1/2",
                "aciklama": "Paylar çarpılır, paydalar çarpılır: 6/12 = 1/2"
            },
            {
                "soru": "4/5 ÷ 2/5 = ?",
                "secenekler": ["2", "1", "8/25", "4/2"],
                "dogru": "2",
                "aciklama": "Bölünen kesir aynen yazılır, bölen kesir ters çevrilip çarpılır: 4/5 × 5/2 = 2"
            },
            {
                "soru": "0,5 = ?",
                "secenekler": ["1/2", "1/4", "2/3", "3/4"],
                "dogru": "1/2",
                "aciklama": "Ondalık kesir rasyonel sayıya çevrilir."
            },
            {
                "soru": "1/2 + 1/3 + 1/6 = ?",
                "secenekler": ["1", "2/3", "1/2", "4/6"],
                "dogru": "1",
                "aciklama": "Paydaları eşitle: 3/6 + 2/6 + 1/6 = 6/6 = 1"
            },
            {
                "soru": "7/8 - 1/4 = ?",
                "secenekler": ["5/8", "6/8", "1/2", "3/4"],
                "dogru": "5/8",
                "aciklama": "Paydaları eşitle: 7/8 - 2/8 = 5/8"
            },
            {
                "soru": "(-3/4) + 1/2 = ?",
                "secenekler": ["-1/4", "1/4", "-1/2", "1/2"],
                "dogru": "-1/4",
                "aciklama": "-3/4 + 2/4 = -1/4"
            },
            {
                "soru": "0,75 - 1/4 = ?",
                "secenekler": ["1/2", "1/4", "1/3", "2/3"],
                "dogru": "1/2",
                "aciklama": "0,75 = 3/4, sonra 3/4 - 1/4 = 2/4 = 1/2"
            },
            {
                "soru": "2/5 × 10/3 = ?",
                "secenekler": ["4/3", "3/4", "20/15", "1/2"],
                "dogru": "4/3",
                "aciklama": "20/15 = 4/3"
            },
        ],
        "2": [
            {
                "soru": "1/3 + 2/5 = ?",
                "secenekler": ["11/15", "3/8", "2/8", "3/15"],
                "dogru": "11/15",
                "aciklama": "Paydaları eşitle: 5/15 + 6/15 = 11/15"
            },
            {
                "soru": "5/6 - 1/3 = ?",
                "secenekler": ["1/2", "4/6", "2/3", "1/3"],
                "dogru": "1/2",
                "aciklama": "5/6 - 2/6 = 3/6 = 1/2"
            },
            {
                "soru": "3/4 × 2/5 = ?",
                "secenekler": ["3/10", "6/20", "5/9", "1/2"],
                "dogru": "3/10",
                "aciklama": "6/20 = 3/10"
            },
            {
                "soru": "5/9 ÷ 1/3 = ?",
                "secenekler": ["5/3", "3/5", "5/27", "1/3"],
                "dogru": "5/3",
                "aciklama": "5/9 × 3/1 = 15/9 = 5/3"
            },
            {
                "soru": "(-1/2) + (-1/3) = ?",
                "secenekler": ["-5/6", "-1/6", "-3/5", "-2/5"],
                "dogru": "-5/6",
                "aciklama": "-3/6 - 2/6 = -5/6"
            },
            {
                "soru": "2/5 ÷ 4/5 = ?",
                "secenekler": ["1/2", "2/4", "8/25", "1/1"],
                "dogru": "1/2",
                "aciklama": "2/5 × 5/4 = 10/20 = 1/2"
            },
            {
                "soru": "0,25 + 1/4 = ?",
                "secenekler": ["1/2", "1/4", "3/4", "1/8"],
                "dogru": "1/2",
                "aciklama": "0,25 = 1/4, sonra 1/4 + 1/4 = 1/2"
            },
            {
                "soru": "3/2 - 1/4 = ?",
                "secenekler": ["5/4", "2/4", "1/2", "3/4"],
                "dogru": "5/4",
                "aciklama": "6/4 - 1/4 = 5/4"
            },
            {
                "soru": "(-2/3) × 3/4 = ?",
                "secenekler": ["-1/2", "1/2", "-6/12", "6/12"],
                "dogru": "-1/2",
                "aciklama": "-6/12 = -1/2"
            },
            {
                "soru": "1/2 ÷ 2 = ?",
                "secenekler": ["1/4", "1/2", "2/1", "1/1"],
                "dogru": "1/4",
                "aciklama": "1/2 × 1/2 = 1/4"
            },
        ],
    },

    "ÜNİTE 3: CEBİRSEL İFADELER, EŞİTLİK VE DENKLEM": {
        "1": [
            {
                "soru": "3x + 5 + 2x = ?",
                "secenekler": ["5x + 5", "5x", "6x + 5", "x + 5"],
                "dogru": "5x + 5",
                "aciklama": "Benzer terimler toplanır: 3x + 2x = 5x"
            },
            {
                "soru": "2a + 3b - a + b = ?",
                "secenekler": ["a + 4b", "a + 3b", "3a + 4b", "a + 2b"],
                "dogru": "a + 4b",
                "aciklama": "2a - a = a, 3b + b = 4b"
            },
            {
                "soru": "x + 7 = 12 ise x kaçtır?",
                "secenekler": ["5", "19", "-5", "12"],
                "dogru": "5",
                "aciklama": "x = 12 - 7 = 5"
            },
            {
                "soru": "2x + 3 = 11 ise x kaçtır?",
                "secenekler": ["4", "5", "6", "8"],
                "dogru": "4",
                "aciklama": "2x = 8, x = 4"
            },
            {
                "soru": "3(x + 2) = 15 ise x kaçtır?",
                "secenekler": ["3", "5", "2", "4"],
                "dogru": "3",
                "aciklama": "3x + 6 = 15, 3x = 9, x = 3"
            },
            {
                "soru": "4x - 2 + x + 8 = ?",
                "secenekler": ["5x + 6", "5x", "5x - 6", "4x + 6"],
                "dogru": "5x + 6",
                "aciklama": "4x + x = 5x, -2 + 8 = 6"
            },
            {
                "soru": "x - 5 = 12 ise x kaçtır?",
                "secenekler": ["17", "7", "-7", "12"],
                "dogru": "17",
                "aciklama": "x = 12 + 5 = 17"
            },
            {
                "soru": "3x = 24 ise x kaçtır?",
                "secenekler": ["8", "24", "6", "12"],
                "dogru": "8",
                "aciklama": "x = 24 ÷ 3 = 8"
            },
            {
                "soru": "x/2 = 10 ise x kaçtır?",
                "secenekler": ["20", "5", "10", "2"],
                "dogru": "20",
                "aciklama": "x = 10 × 2 = 20"
            },
            {
                "soru": "2x + 1 = 9 ise x kaçtır?",
                "secenekler": ["4", "5", "8", "3"],
                "dogru": "4",
                "aciklama": "2x = 8, x = 4"
            },
        ],
        "2": [
            {
                "soru": "(x + 2)(x - 3) = ?",
                "secenekler": ["x² - x - 6", "x² + x - 6", "x² - 6", "x² - 5x - 6"],
                "dogru": "x² - x - 6",
                "aciklama": "Dağıtma özelliği: x² - 3x + 2x - 6 = x² - x - 6"
            },
            {
                "soru": "2x + 5 = 3x - 2 ise x kaçtır?",
                "secenekler": ["7", "5", "3", "2"],
                "dogru": "7",
                "aciklama": "5 + 2 = 3x - 2x, x = 7"
            },
            {
                "soru": "5(2x - 1) = 35 ise x kaçtır?",
                "secenekler": ["4", "5", "3", "6"],
                "dogru": "4",
                "aciklama": "10x - 5 = 35, 10x = 40, x = 4"
            },
            {
                "soru": "3x + 2y = 12 ve x = 2 ise y kaçtır?",
                "secenekler": ["3", "4", "5", "6"],
                "dogru": "3",
                "aciklama": "3(2) + 2y = 12, 6 + 2y = 12, y = 3"
            },
            {
                "soru": "3x - 5 = 16 ise x kaçtır?",
                "secenekler": ["7", "5", "6", "8"],
                "dogru": "7",
                "aciklama": "3x = 21, x = 7"
            },
            {
                "soru": "(x - 3)/2 = 5 ise x kaçtır?",
                "secenekler": ["13", "10", "8", "15"],
                "dogru": "13",
                "aciklama": "x - 3 = 10, x = 13"
            },
            {
                "soru": "4(x - 2) = 12 ise x kaçtır?",
                "secenekler": ["5", "4", "6", "3"],
                "dogru": "5",
                "aciklama": "x - 2 = 3, x = 5"
            },
            {
                "soru": "3x/2 = 9 ise x kaçtır?",
                "secenekler": ["6", "4", "8", "3"],
                "dogru": "6",
                "aciklama": "3x = 18, x = 6"
            },
            {
                "soru": "-2x + 8 = 2 ise x kaçtır?",
                "secenekler": ["3", "2", "4", "5"],
                "dogru": "3",
                "aciklama": "-2x = -6, x = 3"
            },
            {
                "soru": "5x - 3 = 2x + 9 ise x kaçtır?",
                "secenekler": ["4", "3", "5", "6"],
                "dogru": "4",
                "aciklama": "5x - 2x = 9 + 3, 3x = 12, x = 4"
            },
        ],
    },

    "ÜNİTE 4: ORAN - ORANTИ VE YÜZDELER": {
        "1": [
            {
                "soru": "Bir gömlek 80 TL'dir. %25 indirim yapılırsa, yeni fiyatı kaç TL'dir?",
                "secenekler": ["60", "70", "55", "65"],
                "dogru": "60",
                "aciklama": "80 × 25/100 = 20 indirim, 80 - 20 = 60 TL"
            },
            {
                "soru": "300'ün %10'u kaçtır?",
                "secenekler": ["30", "50", "20", "40"],
                "dogru": "30",
                "aciklama": "300 × 10/100 = 30"
            },
            {
                "soru": "Bir sınıfta 40 öğrenci vardır. %50'si erkek ise, kaç erkek vardır?",
                "secenekler": ["20", "25", "30", "15"],
                "dogru": "20",
                "aciklama": "40 × 50/100 = 20"
            },
            {
                "soru": "120 TL'nin %20 fazlası kaç TL'dir?",
                "secenekler": ["144", "140", "150", "160"],
                "dogru": "144",
                "aciklama": "120 × 20/100 = 24 artış, 120 + 24 = 144 TL"
            },
            {
                "soru": "2:4 oranını sadeleştirin.",
                "secenekler": ["1:2", "2:3", "1:3", "2:5"],
                "dogru": "1:2",
                "aciklama": "Her iki taraf 2'ye bölünür."
            },
            {
                "soru": "Bir kitap 50 TL'dir. %30 indirimliyse kaç TL'ye satılır?",
                "secenekler": ["35", "40", "30", "45"],
                "dogru": "35",
                "aciklama": "50 × 30/100 = 15 indirim, 50 - 15 = 35 TL"
            },
            {
                "soru": "50 sayısı 200 sayısının yüzde kaçıdır?",
                "secenekler": ["25", "20", "30", "15"],
                "dogru": "25",
                "aciklama": "50/200 × 100 = 25%"
            },
            {
                "soru": "Bir ürünün fiyatı 100 TL'den 150 TL'ye çıktı. Yüzde kaç artış oldu?",
                "secenekler": ["50", "40", "60", "30"],
                "dogru": "50",
                "aciklama": "(150-100)/100 × 100 = 50%"
            },
            {
                "soru": "3:5 oranında A:B vardır. Toplam 80 ise B kaçtır?",
                "secenekler": ["50", "40", "30", "60"],
                "dogru": "50",
                "aciklama": "3x + 5x = 80, 8x = 80, x = 10, B = 50"
            },
            {
                "soru": "200'ün %150'si kaçtır?",
                "secenekler": ["300", "250", "350", "400"],
                "dogru": "300",
                "aciklama": "200 × 150/100 = 300"
            },
        ],
        "2": [
            {
                "soru": "600'ün %35'i kaçtır?",
                "secenekler": ["210", "200", "220", "230"],
                "dogru": "210",
                "aciklama": "600 × 35/100 = 210"
            },
            {
                "soru": "Bir öğrenci 400 TL'den 480 TL'ye birikinti yaptı. Yüzde kaç artış?",
                "secenekler": ["20", "25", "15", "30"],
                "dogru": "20",
                "aciklama": "(480-400)/400 × 100 = 20%"
            },
            {
                "soru": "Bir mal %40 kâr ile 140 TL'ye satılıyor. Maliyet kaç TL?",
                "secenekler": ["100", "120", "110", "130"],
                "dogru": "100",
                "aciklama": "100 + 100×40/100 = 100 + 40 = 140"
            },
            {
                "soru": "2:3:5 oranında A:B:C vardır. Toplam 100 ise B kaçtır?",
                "secenekler": ["30", "25", "20", "40"],
                "dogru": "30",
                "aciklama": "2x + 3x + 5x = 100, 10x = 100, x = 10, B = 30"
            },
            {
                "soru": "Bir harita 1:1000 ölçekte yapılmıştır. 5 cm'lik harita uzunluğu gerçekte kaç metredir?",
                "secenekler": ["50", "40", "60", "30"],
                "dogru": "50",
                "aciklama": "5 cm × 1000 = 5000 cm = 50 m"
            },
            {
                "soru": "750'nin %24'ü kaçtır?",
                "secenekler": ["180", "200", "160", "220"],
                "dogru": "180",
                "aciklama": "750 × 24/100 = 180"
            },
            {
                "soru": "Bir ürün 120 TL'den %40 indirime sunuluyor. Yeni fiyat kaç TL?",
                "secenekler": ["72", "80", "70", "75"],
                "dogru": "72",
                "aciklama": "120 - 120×40/100 = 120 - 48 = 72"
            },
            {
                "soru": "Orantı: 3/x = 6/8 ise x kaçtır?",
                "secenekler": ["4", "3", "5", "6"],
                "dogru": "4",
                "aciklama": "6x = 24, x = 4"
            },
            {
                "soru": "Bir sınıfta erkek/kız oranı 3/4'tür. Sınıf 35 kişiyse erkek kaç?",
                "secenekler": ["15", "20", "10", "25"],
                "dogru": "15",
                "aciklama": "3x + 4x = 35, 7x = 35, x = 5, erkek = 15"
            },
            {
                "soru": "500'ün yüzde kaçı 125'tir?",
                "secenekler": ["25", "20", "30", "15"],
                "dogru": "25",
                "aciklama": "125/500 × 100 = 25%"
            },
        ],
    },

    "ÜNİTE 5: DOĞRULAR, AÇILAR, ÇOKGENLER, ÇEMBER VE DAİRE": {
        "1": [
            {
                "soru": "Bir açı 45° ise, tümleyeni (complementary) kaç derecedir?",
                "secenekler": ["45", "90", "135", "180"],
                "dogru": "45",
                "aciklama": "Tümleyen açı: 90° - 45° = 45°"
            },
            {
                "soru": "Bir açı 60° ise, bütünleyeni (supplementary) kaç derecedir?",
                "secenekler": ["120", "90", "60", "180"],
                "dogru": "120",
                "aciklama": "Bütünleyen açı: 180° - 60° = 120°"
            },
            {
                "soru": "Ters açılar eşit midir?",
                "secenekler": ["Evet", "Hayır", "Bazen", "Belki"],
                "dogru": "Evet",
                "aciklama": "Ters açılar her zaman eşittir."
            },
            {
                "soru": "İki doğru kesiştiğinde kaç tane açı oluşur?",
                "secenekler": ["4", "2", "6", "8"],
                "dogru": "4",
                "aciklama": "4 açı oluşur."
            },
            {
                "soru": "Dik açı kaç derecedir?",
                "secenekler": ["90", "180", "45", "60"],
                "dogru": "90",
                "aciklama": "Dik açı 90°'dir."
            },
            {
                "soru": "Dairenin çevresi formülü nedir?",
                "secenekler": ["C = 2πr", "C = πr²", "C = πr", "C = π²r"],
                "dogru": "C = 2πr",
                "aciklama": "Çevre = 2 × π × Yarıçap"
            },
            {
                "soru": "Dairenin alanı formülü nedir?",
                "secenekler": ["A = πr²", "A = 2πr", "A = πr", "A = πd"],
                "dogru": "A = πr²",
                "aciklama": "Alan = π × Yarıçap²"
            },
            {
                "soru": "Yarıçapı 5 cm olan dairenin çevresi kaç cm'dir?",
                "secenekler": ["10π", "5π", "25π", "2π"],
                "dogru": "10π",
                "aciklama": "C = 2π(5) = 10π ≈ 31,4 cm"
            },
            {
                "soru": "Yarıçapı 3 cm olan dairenin alanı kaç cm²'dir?",
                "secenekler": ["9π", "6π", "3π", "18π"],
                "dogru": "9π",
                "aciklama": "A = π(3)² = 9π ≈ 28,3 cm²"
            },
            {
                "soru": "Bir kare kaç kenarı vardır?",
                "secenekler": ["4", "3", "5", "6"],
                "dogru": "4",
                "aciklama": "Karenin 4 eşit kenarı vardır."
            },
        ],
        "2": [
            {
                "soru": "Bir üçgenin iç açılarının toplamı kaç derecedir?",
                "secenekler": ["180", "90", "270", "360"],
                "dogru": "180",
                "aciklama": "Tüm üçgenlerin iç açıları 180°'dir."
            },
            {
                "soru": "Bir açı 30° ise, bu açıyı iki eşit parçaya bölen ışın, her açıyı kaç dereceye böler?",
                "secenekler": ["15", "30", "60", "10"],
                "dogru": "15",
                "aciklama": "30° ÷ 2 = 15°"
            },
            {
                "soru": "İkizkenar üçgende eş kenarların karşısındaki açılar eşit midir?",
                "secenekler": ["Evet", "Hayır", "Bazen", "Belki"],
                "dogru": "Evet",
                "aciklama": "İkizkenar üçgenin taban açıları eşittir."
            },
            {
                "soru": "Eşkenar üçgenin tüm kenarları eşit midir?",
                "secenekler": ["Evet", "Hayır", "Bazen", "Belki"],
                "dogru": "Evet",
                "aciklama": "Eşkenar üçgenin tüm kenarları ve açıları eşittir."
            },
            {
                "soru": "Bir dikdörtgenin alan formülü nedir?",
                "secenekler": ["A = l × w", "A = s²", "A = b × h / 2", "A = πr²"],
                "dogru": "A = l × w",
                "aciklama": "Alan = Uzun kenar × Kısa kenar"
            },
            {
                "soru": "Karenin alanı s² ise, çevresi kaçtır?",
                "secenekler": ["4s", "2s", "s", "3s"],
                "dogru": "4s",
                "aciklama": "Çevre = 4 × kenar"
            },
            {
                "soru": "Parallelkenarın alanı kaç formülle bulunur?",
                "secenekler": ["A = b × h", "A = b² ", "A = 2b × h", "A = b × h / 2"],
                "dogru": "A = b × h",
                "aciklama": "Alan = Taban × Yükseklik"
            },
            {
                "soru": "Bir yamuk alanı nasıl bulunur?",
                "secenekler": ["A = (b₁ + b₂) × h / 2", "A = b × h", "A = b × h / 2", "A = πr²"],
                "dogru": "A = (b₁ + b₂) × h / 2",
                "aciklama": "Alan = (Tabanlar toplamı × Yükseklik) / 2"
            },
            {
                "soru": "Çokgenin iç açıları toplamı formülü nedir?",
                "secenekler": ["(n-2) × 180", "n × 180", "(n-1) × 180", "n × 90"],
                "dogru": "(n-2) × 180",
                "aciklama": "n kenar sayısıdır."
            },
            {
                "soru": "Düzgün beşgenin bir iç açısı kaç derecedir?",
                "secenekler": ["108", "120", "90", "100"],
                "dogru": "108",
                "aciklama": "(5-2) × 180 / 5 = 108"
            },
        ],
    },

    "ÜNİTE 6: VERİ ANALİZİ VE CİSİMLERİN FARKLI YÖNLERDEN GÖRÜNÜMLERI": {
        "1": [
            {
                "soru": "Aritmetik ortalama nasıl bulunur?",
                "secenekler": ["Tüm değerlerin toplamını veri sayısına böl", "En büyük değerden en küçüğü çıkar", "En çok tekrarlanan değer bul", "Ortadaki değeri seç"],
                "dogru": "Tüm değerlerin toplamını veri sayısına böl",
                "aciklama": "Ortalama = Toplam / Veri Sayısı"
            },
            {
                "soru": "Medyan nedir?",
                "secenekler": ["Sıralanmış verinin ortasındaki değer", "En çok tekrarlanan değer", "Tüm değerlerin toplamı", "En büyük ve en küçük fark"],
                "dogru": "Sıralanmış verinin ortasındaki değer",
                "aciklama": "Küçükten büyüğe sıralanmış verinin ortasıdır."
            },
            {
                "soru": "Mod nedir?",
                "secenekler": ["En sık tekrarlanan değer", "Ortadaki değer", "Başlangıç değeri", "Son değer"],
                "dogru": "En sık tekrarlanan değer",
                "aciklama": "Mod = En çok görülen değer"
            },
            {
                "soru": "1, 3, 5, 7, 9 sayılarının ortalaması kaçtır?",
                "secenekler": ["5", "6", "7", "4"],
                "dogru": "5",
                "aciklama": "(1+3+5+7+9)/5 = 25/5 = 5"
            },
            {
                "soru": "2, 4, 4, 6, 8 sayılarının medyanı kaçtır?",
                "secenekler": ["4", "5", "6", "3"],
                "dogru": "4",
                "aciklama": "Sıralı: 2,4,4,6,8 → Ortadaki = 4"
            },
            {
                "soru": "Küpün farklı görünümlerinin sayısı kaçtır?",
                "secenekler": ["6", "4", "8", "12"],
                "dogru": "6",
                "aciklama": "Küpün 6 farklı yüzü vardır."
            },
            {
                "soru": "Dikdörtgenler prizmasının kaç tane dikdörtgen yüzü vardır?",
                "secenekler": ["6", "4", "8", "12"],
                "dogru": "6",
                "aciklama": "Dikdörtgenler prizmasının 6 yüzü vardır."
            },
            {
                "soru": "Kübün bir kenarı a ise, yüzey alanı kaçtır?",
                "secenekler": ["6a²", "a²", "4a²", "8a²"],
                "dogru": "6a²",
                "aciklama": "6 × (a × a) = 6a²"
            },
            {
                "soru": "Prizmanın hacmi formülü nedir?",
                "secenekler": ["V = Taban Alanı × Yükseklik", "V = πr²h", "V = bh/3", "V = 2bh"],
                "dogru": "V = Taban Alanı × Yükseklik",
                "aciklama": "Hacim = Taban × Yükseklik"
            },
            {
                "soru": "Küpün kenarı 2 cm ise, hacmi kaç cm³'tür?",
                "secenekler": ["8", "4", "6", "12"],
                "dogru": "8",
                "aciklama": "V = 2³ = 8 cm³"
            },
        ],
        "2": [
            {
                "soru": "10, 20, 30, 40, 50 sayılarının modunu bulunuz.",
                "secenekler": ["Mod yok", "30", "40", "50"],
                "dogru": "Mod yok",
                "aciklama": "Hiç tekrarlanan sayı yoktur."
            },
            {
                "soru": "1, 1, 2, 2, 2, 3, 4 sayılarının modunu bulunuz.",
                "secenekler": ["2", "1", "3", "4"],
                "dogru": "2",
                "aciklama": "2 en sık (3 kez) tekrarlanan sayıdır."
            },
            {
                "soru": "Çeyrek sapma (Quartile Deviation) nedir?",
                "secenekler": ["(Q₃ - Q₁) / 2", "(Q₃ - Q₁)", "Q₃ - Q₁", "Q₁ + Q₃"],
                "dogru": "(Q₃ - Q₁) / 2",
                "aciklama": "Üst çeyrek - Alt çeyrek / 2"
            },
            {
                "soru": "İstatistikte açıklık (range) nedir?",
                "secenekler": ["En büyük - En küçük değer", "Ortalama", "Medyan", "Mod"],
                "dogru": "En büyük - En küçük değer",
                "aciklama": "Range = Max - Min"
            },
            {
                "soru": "Standart sapma neyi gösterir?",
                "secenekler": ["Verilerin ortalamadan sapması", "En büyük değer", "Toplam sayı", "Medyan"],
                "dogru": "Verilerin ortalamadan sapması",
                "aciklama": "Değerlerin ne kadar dağıldığını gösterir."
            },
            {
                "soru": "Silindir yüzey alanı formülü nedir?",
                "secenekler": ["A = 2πr² + 2πrh", "A = πr²h", "A = 2πrh", "A = πr² + πrh"],
                "dogru": "A = 2πr² + 2πrh",
                "aciklama": "Taban + Üst + Yanal Alan"
            },
            {
                "soru": "Silindir hacmi formülü nedir?",
                "secenekler": ["V = πr²h", "V = 2πr²h", "V = πrh", "V = πr³"],
                "dogru": "V = πr²h",
                "aciklama": "Hacim = π × Yarıçap² × Yükseklik"
            },
            {
                "soru": "Kare prizmanın taban kenarı 3 cm, yüksekliği 5 cm ise hacmi kaç cm³?",
                "secenekler": ["45", "50", "40", "55"],
                "dogru": "45",
                "aciklama": "V = 3² × 5 = 45 cm³"
            },
            {
                "soru": "Piramidin hacmi formülü nedir?",
                "secenekler": ["V = (Taban Alanı × Yükseklik) / 3", "V = Taban Alanı × Yükseklik", "V = πr²h / 3", "V = 2bh/3"],
                "dogru": "V = (Taban Alanı × Yükseklik) / 3",
                "aciklama": "Hacim = (Taban × h) / 3"
            },
            {
                "soru": "Koninin hacmi formülü nedir?",
                "secenekler": ["V = (πr²h) / 3", "V = πr²h", "V = (πrh) / 3", "V = πr³"],
                "dogru": "V = (πr²h) / 3",
                "aciklama": "Hacim = (π × r² × h) / 3"
            },
        ],
    },
}

# ==================== UYGULAMA SINIFI ====================

class AkilliKitapSoruBankasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Akıllı Soru Bankası - 7. Sınıf Matematik")
        self.root.geometry("900x700")
        
        # Renkler
        self.BG_COLOR = "#f0f0f0"
        self.HEADER_COLOR = "#1e3a8a"
        self.BUTTON_COLOR = "#3b82f6"
        self.CORRECT_COLOR = "#10b981"
        self.WRONG_COLOR = "#ef4444"
        
        self.root.config(bg=self.BG_COLOR)
        
        self.durum = "UNITÉ_SECIMI"
        self.secilen_unité = None
        self.secilen_zorluk = None
        self.soru_index = 0
        
        self.dogru = 0
        self.yanlis = 0
        self.baslangic_zamani = None
        self.sorular_listesi = []
        
        self.arayuz_basla()
    
    # ==================== ÜNİTE SEÇİM ARAYÜZÜ ====================
    
    def arayuz_basla(self):
        self.temizle()
        
        # Header
        header = tk.Frame(self.root, bg=self.HEADER_COLOR, height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            header,
            text="📚 7. SINIF MATEMATİK",
            font=("Arial", 22, "bold"),
            bg=self.HEADER_COLOR,
            fg="white"
        ).pack(pady=15)
        
        tk.Label(
            header,
            text="Akıllı Soru Bankası",
            font=("Arial", 11),
            bg=self.HEADER_COLOR,
            fg="#e0e0e0"
        ).pack()
        
        # İçerik Frame
        icenik = tk.Frame(self.root, bg=self.BG_COLOR)
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            icenik,
            text="Çalışmak İstediğiniz Ünitéyi Seçin:",
            font=("Arial", 14, "bold"),
            bg=self.BG_COLOR
        ).pack(pady=20)
        
        # Ünite butonları scroll bar ile
        canvas = tk.Canvas(icenik, bg=self.BG_COLOR, highlightthickness=0)
        scrollbar = ttk.Scrollbar(icenik, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.BG_COLOR)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Üniteler
        for i, unité in enumerate(SORU_BANKASI.keys(), 1):
            btn = tk.Button(
                scrollable_frame,
                text=unité,
                font=("Arial", 11, "bold"),
                bg=self.BUTTON_COLOR,
                fg="white",
                height=2,
                command=lambda u=unité: self.unité_sec(u)
            )
            btn.pack(fill=tk.X, pady=8)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def unité_sec(self, unité):
        self.secilen_unité = unité
        self.zorluk_sec_arayuz()
    
    # ==================== ZORLUK SEÇİM ARAYÜZÜ ====================
    
    def zorluk_sec_arayuz(self):
        self.temizle()
        
        # Header
        header = tk.Frame(self.root, bg=self.HEADER_COLOR, height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            header,
            text=f"📖 {self.secilen_unité}",
            font=("Arial", 16, "bold"),
            bg=self.HEADER_COLOR,
            fg="white",
            wraplength=850
        ).pack(pady=15)
        
        # İçerik Frame
        icenik = tk.Frame(self.root, bg=self.BG_COLOR)
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            icenik,
            text="Zorluk Düzeyini Seçin:",
            font=("Arial", 14, "bold"),
            bg=self.BG_COLOR
        ).pack(pady=20)
        
        # Zorluk seçenekleri
        zorluk_frame = tk.Frame(icenik, bg=self.BG_COLOR)
        zorluk_frame.pack(fill=tk.BOTH, expand=True)
        
        zorluk_seviyeleri = {
            "1": ("⭐ Kolay (Başlangıç Seviyesi)", "Temel kavramlar ve basit sorular (10 soru)"),
            "2": ("⭐⭐⭐ Orta (İleri Seviye)", "Karışık işlemler ve problem çözme (10 soru)"),
        }
        
        for zorluk, (baslik, aciklama) in zorluk_seviyeleri.items():
            if zorluk in SORU_BANKASI[self.secilen_unité]:
                btn_frame = tk.Frame(zorluk_frame, bg="white", relief=tk.RAISED, bd=2)
                btn_frame.pack(fill=tk.X, pady=10)
                
                tk.Label(
                    btn_frame,
                    text=baslik,
                    font=("Arial", 12, "bold"),
                    bg="white",
                    fg="#1e3a8a"
                ).pack(anchor="w", padx=15, pady=8)
                
                tk.Label(
                    btn_frame,
                    text=aciklama,
                    font=("Arial", 10),
                    bg="white",
                    fg="#666"
                ).pack(anchor="w", padx=15, pady=(0, 8))
                
                btn = tk.Button(
                    btn_frame,
                    text="Başla ▶",
                    font=("Arial", 11, "bold"),
                    bg=self.BUTTON_COLOR,
                    fg="white",
                    command=lambda z=zorluk: self.test_basla(z),
                    width=20
                )
                btn.pack(pady=10)
        
        # Geri Butonu
        tk.Button(
            icenik,
            text="◀ Geri",
            font=("Arial", 10),
            bg="#6b7280",
            fg="white",
            command=self.arayuz_basla,
            width=15
        ).pack(pady=20)
    
    # ==================== TEST BAŞLAT ====================
    
    def test_basla(self, zorluk):
        self.secilen_zorluk = zorluk
        self.sorular_listesi = SORU_BANKASI[self.secilen_unité][zorluk]
        self.soru_index = 0
        self.dogru = 0
        self.yanlis = 0
        self.baslangic_zamani = time.time()
        self.durum = "SORU_CEVAPLAMA"
        self.soru_goster()
    
    # ==================== SORU GÖSTER ====================
    
    def soru_goster(self):
        if self.soru_index >= len(self.sorular_listesi):
            self.test_bitir()
            return
        
        self.temizle()
        
        soru_data = self.sorular_listesi[self.soru_index]
        soru_metni = soru_data["soru"]
        secenekler = soru_data["secenekler"]
        dogru_cevap = soru_data["dogru"]
        aciklama = soru_data["aciklama"]
        
        # Header
        header = tk.Frame(self.root, bg=self.HEADER_COLOR, height=120)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        unité_kisa = self.secilen_unité.split(":")[1].strip() if ":" in self.secilen_unité else self.secilen_unité
        tk.Label(
            header,
            text=f"📖 {unité_kisa}",
            font=("Arial", 14, "bold"),
            bg=self.HEADER_COLOR,
            fg="white",
            wraplength=850
        ).pack(pady=10)
        
        ilerleme = self.soru_index + 1
        toplam = len(self.sorular_listesi)
        tk.Label(
            header,
            text=f"Soru {ilerleme}/{toplam} | ✓ Doğru: {self.dogru} | ✗ Yanlış: {self.yanlis}",
            font=("Arial", 11),
            bg=self.HEADER_COLOR,
            fg="#e0e0e0"
        ).pack()
        
        # Progress Bar
        progress_frame = tk.Frame(header, bg="#1a2a5e", height=6)
        progress_frame.pack(fill=tk.X, padx=0, pady=(10, 0))
        
        progress_width = (ilerleme / toplam) * 900
        progress_bar = tk.Frame(progress_frame, bg=self.BUTTON_COLOR, height=6)
        progress_bar.place(width=progress_width, height=6)
        
        # İçerik
        icenik = tk.Frame(self.root, bg=self.BG_COLOR)
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Soru
        soru_frame = tk.Frame(icenik, bg="white", relief=tk.RAISED, bd=2)
        soru_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(
            soru_frame,
            text=soru_metni,
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#1e3a8a",
            wraplength=850,
            justify="left"
        ).pack(padx=20, pady=20)
        
        # Şıklar
        tk.Label(
            icenik,
            text="Doğru cevabı seçin:",
            font=("Arial", 11, "bold"),
            bg=self.BG_COLOR
        ).pack(anchor="w", pady=(10, 10))
        
        self.secim_var = tk.StringVar()
        
        for secenek in secenekler:
            btn = tk.Radiobutton(
                icenik,
                text=secenek,
                variable=self.secim_var,
                value=secenek,
                font=("Arial", 11),
                bg=self.BG_COLOR,
                activebackground=self.BG_COLOR,
                selectcolor="#e0e0e0"
            )
            btn.pack(anchor="w", padx=40, pady=5)
        
        # Butonlar
        buton_frame = tk.Frame(icenik, bg=self.BG_COLOR)
        buton_frame.pack(pady=20)
        
        tk.Button(
            buton_frame,
            text="✓ Cevabı Kontrol Et",
            font=("Arial", 11, "bold"),
            bg=self.CORRECT_COLOR,
            fg="white",
            command=lambda: self.kontrol_et(dogru_cevap, aciklama),
            width=20,
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            buton_frame,
            text="⊗ Atla",
            font=("Arial", 11, "bold"),
            bg="#f97316",
            fg="white",
            command=self.soruyu_atla,
            width=15,
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=5)
    
    # ==================== CEVAP KONTROL ====================
    
    def kontrol_et(self, dogru_cevap, aciklama):
        cevap = self.secim_var.get()
        
        if not cevap:
            messagebox.showwarning("Uyarı", "Lütfen bir seçenek seçin!")
            return
        
        if cevap == dogru_cevap:
            self.dogru += 1
            messagebox.showinfo(
                "✓ Doğru!",
                f"Harika! Doğru cevap: {dogru_cevap}\n\n"
                f"Açıklama:\n{aciklama}"
            )
        else:
            self.yanlis += 1
            messagebox.showerror(
                "✗ Yanlış!",
                f"Maalesef yanlış.\n\n"
                f"Sizin cevabınız: {cevap}\n"
                f"Doğru cevap: {dogru_cevap}\n\n"
                f"Açıklama:\n{aciklama}"
            )
        
        self.soru_index += 1
        self.soru_goster()
    
    def soruyu_atla(self):
        self.yanlis += 1
        self.soru_index += 1
        self.soru_goster()
    
    # ==================== TEST SONUCU ====================
    
    def test_bitir(self):
        sure = round(time.time() - self.baslangic_zamani, 1)
        toplam = self.dogru + self.yanlis
        basari_yuzde = (self.dogru / toplam * 100) if toplam > 0 else 0
        
        self.temizle()
        
        # Header
        header = tk.Frame(self.root, bg=self.HEADER_COLOR, height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        
        tk.Label(
            header,
            text="🎉 TEST TAMAMLANDI!",
            font=("Arial", 22, "bold"),
            bg=self.HEADER_COLOR,
            fg="white"
        ).pack(pady=20)
        
        # Sonuçlar
        icenik = tk.Frame(self.root, bg=self.BG_COLOR)
        icenik.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Başarı Durumu
        if basari_yuzde >= 80:
            durum_text = "🌟 Mükemmel! Harika başarı!"
            durum_renk = self.CORRECT_COLOR
        elif basari_yuzde >= 60:
            durum_text = "😊 İyi! Biraz daha pratik yap"
            durum_renk = "#f59e0b"
        else:
            durum_text = "📚 Daha fazla çalışma gerekiyor"
            durum_renk = self.WRONG_COLOR
        
        durum_frame = tk.Frame(icenik, bg=durum_renk, relief=tk.RAISED, bd=2)
        durum_frame.pack(fill=tk.X, pady=15)
        
        tk.Label(
            durum_frame,
            text=durum_text,
            font=("Arial", 14, "bold"),
            bg=durum_renk,
            fg="white"
        ).pack(pady=15)
        
        # İstatistikler
        istatistik_frame = tk.Frame(icenik, bg="white", relief=tk.RAISED, bd=2)
        istatistik_frame.pack(fill=tk.X, pady=15)
        
        istatistikler = [
            (f"✓ Doğru Cevaplar", str(self.dogru), self.CORRECT_COLOR),
            (f"✗ Yanlış Cevaplar", str(self.yanlis), self.WRONG_COLOR),
            (f"📊 Başarı Oranı", f"%{basari_yuzde:.1f}", "#3b82f6"),
            (f"⏱️ Geçen Süre", f"{sure} saniye", "#8b5cf6"),
        ]
        
        for label, value, renk in istatistikler:
            stat_subframe = tk.Frame(istatistik_frame, bg="white")
            stat_subframe.pack(fill=tk.X, padx=20, pady=10)
            
            tk.Label(
                stat_subframe,
                text=label,
                font=("Arial", 12, "bold"),
                bg="white",
                fg="#1e3a8a"
            ).pack(anchor="w")
            
            tk.Label(
                stat_subframe,
                text=value,
                font=("Arial", 16, "bold"),
                bg="white",
                fg=renk
            ).pack(anchor="w", padx=20)
        
        # Butonlar
        buton_frame = tk.Frame(icenik, bg=self.BG_COLOR)
        buton_frame.pack(pady=30)
        
        tk.Button(
            buton_frame,
            text="🔄 Aynı Testi Tekrar Et",
            font=("Arial", 11, "bold"),
            bg=self.BUTTON_COLOR,
            fg="white",
            command=lambda: self.test_basla(self.secilen_zorluk),
            width=25,
            padx=20,
            pady=10
        ).pack(pady=5)
        
        tk.Button(
            buton_frame,
            text="📚 Başka Ünitéyi Seç",
            font=("Arial", 11, "bold"),
            bg="#10b981",
            fg="white",
            command=self.arayuz_basla,
            width=25,
            padx=20,
            pady=10
        ).pack(pady=5)
        
        tk.Button(
            buton_frame,
            text="❌ Programdan Çık",
            font=("Arial", 11, "bold"),
            bg="#6b7280",
            fg="white",
            command=self.root.destroy,
            width=25,
            padx=20,
            pady=10
        ).pack(pady=5)
    
    # ==================== YARDIMCI FONKSİYONLAR ====================
    
    def temizle(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ==================== ÇALIŞTIR ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = AkilliKitapSoruBankasi(root)
    root.mainloop()
