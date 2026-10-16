# 🛡️ CYBER LABS

CYBER LABS
 
adalah platform pembelajaran cyber security berbasis terminal yang dirancang untuk siapa saja yang ingin 
belajar keamanan siber secara terstruktur,
interaktif, dan menyenangkan — langsung dari command line, tanpa browser, 
tanpa internet.

> **Terminal-Based Cyber Security Learning Platform**
> Belajar cyber security dari nol — langsung di terminal, bilingual (ID/EN), interaktif.

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Offline](https://img.shields.io/badge/offline-100%25-orange)

---

## 📖 TENTANG

**CYBER LABS** adalah platform pembelajaran cyber security berbasis terminal yang dirancang untuk:

- 🎓 **Pemula** yang ingin memulai karier di cyber security
- 🔧 **Praktisi** yang ingin refresh konsep dasar
- 🏫 **Pengajar** yang butuh materi terstruktur
- 🌍 **Siapa saja** yang peduli keamanan digital

Semua materi disajikan **bilingual** (Indonesia + English), dengan kuis interaktif, progress tracking, dan bookmark sesi belajar.

**100% offline** — cukup Python 3, tanpa browser, tanpa internet, tanpa dependencies berat.

---

## 📸 PREVIEW

<img src='https://h.uguu.se/merPwUKS.jpg'/>

---

## ✨ FITUR UTAMA

| Fitur | Deskripsi |
|-------|-----------|
| 🌐 **Bilingual** | Bahasa Indonesia, English, atau Bilingual (campur) |
| 📚 **Struktur Modul** | 12 modul cyber security, 89 sub-topik |
| 🧠 **Kuis Interaktif** | 267 soal dengan penjelasan tiap jawaban |
| ⏱️ **Timer Kuis** | Progress bar 30 detik per soal, auto-skip |
| 📊 **Progress Tracking** | Skor & sub-topik yang selesai otomatis tersimpan |
| 🔖 **Save Session** | Simpan posisi belajar, lanjut kapan saja |
| 🔍 **Search Materi** | Cari topik lintas modul |
| 🎨 **UI Terminal Cantik** | Warna, border, ASCII banner, & emoji |
| 💾 **Auto-Save** | Skor & progress otomatis disimpan ke JSON |
| 🚀 **Ringan** | Jalan di Termux, Linux, macOS — tanpa dependencies berat |
| 🔒 **100% Offline** | Tidak butuh internet setelah instalasi |
| 📱 **Cross-Platform** | Termux, Linux, macOS, WSL |

---

## 📚 DAFTAR MODUL

| # | Modul | Sub | Soal |
|---|-------|-----|------|
| 01 | 🛡️ Mengenali Dunia Cyber Security | 12 | 36 |
| 02 | 🌐 Basic Networking | 7 | 21 |
| 03 | 💻 Operating System Security | 7 | 21 |
| 04 | 🔐 Kriptografi | 7 | 21 |
| 05 | 🦠 Malware & Threats | 7 | 21 |
| 06 | 🎭 Social Engineering | 7 | 21 |
| 07 | 🕸️ Web Security (OWASP) | 7 | 21 |
| 08 | 🔑 Password & Authentication | 7 | 21 |
| 09 | ⚔️ Ethical Hacking & Pentest | 7 | 21 |
| 10 | 🛡️ Blue Team & Defensive | 7 | 21 |
| 11 | 🔬 Digital Forensics | 7 | 21 |
| 12 | 🎯 Karier & Sertifikasi | 7 | 21 |

**Total: 12 modul · 89 sub-topik · 267 soal**

## Struktur Folder 📁

```
CYBER-LABS/
├── app.py                  
├── curriculum.py           
├── README.md               
├── LICENSE                
├── .gitignore             
├── content/
│   ├── __init__.py
│   ├── mod01.py        
│   ├── mod02.py            
│   ├── mod03.py            
│   ├── mod04.py           
│   ├── mod05.py            
│   ├── mod06.py         
│   ├── mod07.py         
│   ├── mod08.py            
│   ├── mod09.py      
│   ├── mod10.py            
│   ├── mod11.py            
│   └── mod12.py     
│
├── progress.json         
└── session.json         
```

---

## 📦 INSTALASI

### 1. Requirement

- **Python 3.8+** (cek: `python3 --version`)
- **Terminal** (Termux, bash, zsh, atau terminal Linux/macOS)
- **Git** (opsional, untuk clone)
- Tidak butuh library eksternal (murni standard library Python)

### 2. Clone / Setup

```bash
# Opsi 1: Clone dari repo (kalau ada)
git clone <repo-url> ~/CYBER-LABS

# Opsi 2: Setup manual
mkdir -p ~/CYBER-LABS/content
cd ~/CYBER-LABS
touch content/__init__.py
