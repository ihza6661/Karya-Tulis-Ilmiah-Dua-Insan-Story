# 🎨 START HERE - AI Prompts untuk Diagram

Anda ingin generate Gambar 2.2 dan 2.3 menggunakan AI Image Generator? Ikuti panduan ini!

---

## ⚡ 3 Langkah Tercepat (< 5 Menit)

### Metode 1️⃣: Gratis di Bing (Paling Cepat!)

```
1. Buka: https://www.bing.com/images/create
2. Login dengan akun Microsoft
3. Buka file: PROMPTS_SIMPLE.txt
4. Copy prompt untuk Gambar 2.2
5. Paste di Bing Image Creator
6. Klik "Create"
7. Tunggu ~1 menit
8. Download gambar
9. Ulangi untuk Gambar 2.3
```

✅ **Keuntungan:** Free, cepat, tidak perlu API key  
⚠️ **Kekurangan:** Daily limit (50 kredit), tidak bisa batch

---

### Metode 2️⃣: DALL-E 3 dengan Python

```bash
# 1. Get API key dari https://platform.openai.com/api-keys
# 2. Set environment variable
export OPENAI_API_KEY='sk-proj-xxx'

# 3. Run script
python generate_diagrams.py

# Output: images/gambar_2_2_dall_e.png & gambar_2_3_dall_e.png
```

✅ **Keuntungan:** Otomatis, batch processing, konsisten  
⚠️ **Kekurangan:** Perlu biaya ($0.08 per image)

---

### Metode 3️⃣: Copy-Paste Manual

```
1. Buka file: PROMPTS_SIMPLE.txt
2. Copy prompt untuk Gambar 2.2
3. Pilih AI tool (DALL-E, Midjourney, Stable Diffusion)
4. Paste prompt
5. Adjust settings jika perlu
6. Generate
7. Download
8. Ulangi untuk Gambar 2.3
```

✅ **Keuntungan:** Full control, pilih platform  
⚠️ **Kekurangan:** Manual, memakan waktu

---

## 📚 Dokumentasi Tersedia

Pilih file sesuai kebutuhan:

| Kebutuhan | Buka File | Waktu Baca |
|-----------|-----------|-----------|
| **Mau cepat-cepat** | [PROMPTS_SIMPLE.txt](PROMPTS_SIMPLE.txt) | 2 menit |
| **Tidak tahu pilih apa** | [README_PROMPTS.md](README_PROMPTS.md) | 5 menit |
| **Setup Python automation** | [generate_diagrams.py](generate_diagrams.py) | 10 menit |
| **Developer mode** | [ai_prompts.md](ai_prompts.md) | 15 menit |
| **Cheat sheet** | [QUICK_REFERENCE.txt](QUICK_REFERENCE.txt) | 5 menit |
| **Navigation** | [INDEX_PROMPTS.md](INDEX_PROMPTS.md) | 3 menit |

---

## 🚀 Recommended Path by Profile

### 👨‍🎓 Mahasiswa (No coding)
1. Buka: PROMPTS_SIMPLE.txt
2. Copy-paste ke: bing.com/images/create
3. Download gambar
4. Done! ✅

### 👨‍💻 Developer (Python)
1. Get API key dari OpenAI
2. `export OPENAI_API_KEY='sk-xxx'`
3. `python generate_diagrams.py`
4. Done! ✅

### 🎨 Designer (Custom)
1. Buka: PROMPTS_SIMPLE.txt
2. Edit prompt untuk custom style
3. Generate di platform pilihan
4. Iterate until satisfied
5. Done! ✅

---

## 📊 Quick File Guide

```
Karya Tulis Ilmiah Dua Insan Story/
│
├─ 00_START_HERE.md ⭐️ ← You are here!
│
├─ PROMPTS_SIMPLE.txt ⭐️ ← Prompts to copy-paste
│
├─ generate_diagrams.py 🐍 ← Auto-generate (Python)
├─ generate_diagrams.sh 🔧 ← Auto-generate (Bash)
│
├─ README_PROMPTS.md 📖 ← Overview & comparison
├─ QUICK_REFERENCE.txt 📋 ← Cheat sheet
├─ INDEX_PROMPTS.md 🗺️ ← Navigation guide
│
├─ ai_prompts.md 👨‍💻 ← Code examples (for developers)
├─ AI_PROMPTS_README.md 📚 ← Detailed documentation
├─ prompts.py 🐍 ← Python module with all prompts
│
└─ images/ 📁
   ├─ gambar_2_2.png (current Mermaid version)
   └─ gambar_2_3.png (current Mermaid version)
```

---

## ⚠️ Common Questions

**Q: Mana yang paling cepat?**  
A: Bing Image Creator (bing.com/images/create) - gratis & instant

**Q: Mana yang terbaik kualitas?**  
A: Midjourney atau DALL-E 3 HD

**Q: Berapa biaya?**  
A: Gratis (Bing/Stable Diffusion) - $0.08 (DALL-E 3) - $10/month (Midjourney)

**Q: Bisa batch generate?**  
A: Ya, pakai `python generate_diagrams.py`

**Q: Prompts sudah tested?**  
A: Ya, semua prompts sudah di-validate

---

## 🆘 Help

| Masalah | Solusi |
|--------|--------|
| "Tidak tahu mau pakai apa" | Baca: README_PROMPTS.md |
| "Ingin copy-paste langsung" | Buka: PROMPTS_SIMPLE.txt |
| "Pakai Python automation" | Baca: generate_diagrams.py |
| "Pakai Bash" | Jalankan: ./generate_diagrams.sh |
| "Perlu cheat sheet" | Buka: QUICK_REFERENCE.txt |
| "Ada error" | Lihat: AI_PROMPTS_README.md → Troubleshooting |

---

## ✨ Next Steps

1. **Pilih metode** (Bing / Python / Manual)
2. **Buka file** yang sesuai (PROMPTS_SIMPLE.txt atau generate_diagrams.py)
3. **Generate gambar** (ikuti instruksi di file)
4. **Download hasil** dan simpan di folder `images/`
5. **Update karya_tulis.md** dengan gambar baru (optional)
6. **Done!** 🎉

---

## 📝 Files Summary

| File | Ukuran | Tipe | Untuk Apa |
|------|--------|------|----------|
| PROMPTS_SIMPLE.txt | 2.9 KB | Text | Copy-paste prompts |
| prompts.py | 9.2 KB | Python | Module with prompts |
| generate_diagrams.py | 6.0 KB | Python | Auto-generate |
| generate_diagrams.sh | 5.3 KB | Bash | Auto-generate |
| README_PROMPTS.md | 5.0 KB | Markdown | Overview |
| AI_PROMPTS_README.md | 5.7 KB | Markdown | Detailed docs |
| ai_prompts.md | 7.5 KB | Markdown | Code examples |
| QUICK_REFERENCE.txt | 8.2 KB | Text | Cheat sheet |
| INDEX_PROMPTS.md | 5.1 KB | Markdown | Navigation |

**Total: ~55 KB documentation & code**

---

## 🎯 TL;DR (Too Long; Didn't Read)

**Fastest:** Bing → PROMPTS_SIMPLE.txt → Copy-Paste → Download  
**Best:** DALL-E 3 → generate_diagrams.py → python → Download  
**Free:** Stable Diffusion → PROMPTS_SIMPLE.txt → Local generation

---

**Created:** December 15, 2025  
**Version:** 1.0  
**Status:** Ready to use ✅

👉 **Next:** Pilih metode dan buka file yang sesuai!
