# 📊 AI Prompts untuk Diagram Gambar 2.2 & 2.3

**Kode dan Dokumentasi untuk Generate Diagram Menggunakan AI Image Generator**

---

## 📁 File-File yang Tersedia

| File | Fungsi | Untuk Siapa |
|------|--------|-----------|
| **PROMPTS_SIMPLE.txt** | Prompt langsung siap copy-paste | Pemula, manual generation |
| **ai_prompts.md** | Dokumentasi lengkap (Python, Node.js, Curl) | Developer, automation |
| **generate_diagrams.py** | Script Python otomatis | Python users |
| **generate_diagrams.sh** | Script Bash otomatis | Linux/Mac users |
| **AI_PROMPTS_README.md** | Dokumentasi & troubleshooting | Referensi lengkap |

---

## 🎯 Pilihan Penggunaan

### ✨ CARA 1: Paling Mudah (Copy-Paste Manual)

**Langkah:**
1. Buka file `PROMPTS_SIMPLE.txt`
2. Pilih prompt untuk Gambar 2.2 atau 2.3
3. Copy prompt
4. Paste ke AI Image Generator:
   - DALL-E: https://openai.com/dall-e-3
   - Midjourney: Discord `/imagine` command
   - Stable Diffusion: ComfyUI atau WebUI

**Pros:** Mudah, tidak perlu setup API, cepat  
**Cons:** Manual, tidak bisa batch processing

---

### ⚙️ CARA 2: Otomatis Python (Recommended)

**Requirements:**
```bash
pip install requests
export OPENAI_API_KEY='sk-your-api-key-here'
```

**Run:**
```bash
python generate_diagrams.py
```

**Output:**
- `images/gambar_2_2_dall_e.png`
- `images/gambar_2_3_dall_e.png`

**Pros:** Otomatis, batch processing, resume-able  
**Cons:** Perlu OpenAI API key ($), setup awal

---

### 🔨 CARA 3: Otomatis Bash (Linux/Mac)

**Requirements:**
```bash
curl  # usually pre-installed
export OPENAI_API_KEY='sk-your-api-key-here'
```

**Run:**
```bash
./generate_diagrams.sh
# atau dengan API key
./generate_diagrams.sh 'sk-your-api-key-here'
```

**Pros:** Simple, minimal dependencies  
**Cons:** Hanya Linux/Mac, perlu curl

---

### 🌐 CARA 4: Online Tools (Zero Setup)

**Tools:**
- [DALL-E](https://openai.com/dall-e-3) - Dari OpenAI sendiri
- [Bing Image Creator](https://www.bing.com/images/create) - Free, berbasis DALL-E
- [Midjourney](https://midjourney.com) - Tinggi kualitas, subscription
- [Stable Diffusion Online](https://huggingface.co/spaces/stabilityai/stable-diffusion-3)

**Pros:** Tidak perlu setup, bisa trial gratis  
**Cons:** Limited free tier, perlu account baru

---

## 📝 Prompt Summary

### Gambar 2.2: Pemesanan Undangan
- **Tipe:** Flowchart dengan decision logic
- **Layout:** Horizontal, landscape
- **Steps:** 8-10 langkah dengan feedback loop
- **Colors:** Blue/White professional

### Gambar 2.3: Laporan Penjualan
- **Tipe:** Flowchart sequential
- **Layout:** Horizontal, linear left-to-right
- **Steps:** 10 langkah sequential
- **Colors:** Blue/White professional

---

## 💡 Quick Reference

### DALL-E (Paling Recommended)

**Biaya:** $0.08 per image (HD quality)  
**Kualitas:** Tinggi (9/10)  
**Setup:** Butuh API key OpenAI  
**Kecepatan:** 60-120 detik

```bash
# Python
python generate_diagrams.py

# Bash
./generate_diagrams.sh 'sk-xxx'
```

### Midjourney

**Biaya:** $10/bulan (subscription)  
**Kualitas:** Sangat tinggi (10/10)  
**Setup:** Discord + credit  
**Kecepatan:** 30-60 detik

```
/imagine prompt: [dari ai_prompts.md] --ar 12:5 --q 2
```

### Stable Diffusion (Free Local)

**Biaya:** Gratis  
**Kualitas:** Sedang (7/10)  
**Setup:** Download + GPU required  
**Kecepatan:** Tergantung GPU

```bash
# ComfyUI atau WebUI
# Copy prompt dari PROMPTS_SIMPLE.txt
```

---

## 🔐 API Key Safety

**JANGAN:**
- ❌ Share API key dengan orang lain
- ❌ Commit ke Git dengan API key
- ❌ Post di forum/Discord/social media

**DO:**
- ✅ Use environment variables
- ✅ Keep in `.env` file (gitignored)
- ✅ Regenerate jika accidentally exposed

---

## 📊 Size Specifications

| Property | Value |
|----------|-------|
| Width | 1920 px |
| Height | 800 px |
| Aspect Ratio | 12:5 (landscape) |
| Format | PNG |
| Quality | HD |
| DPI | 72 (web) |

---

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| "API Key not found" | `export OPENAI_API_KEY='sk-...'` |
| "Rate limit exceeded" | Tunggu 1 menit, coba lagi |
| "Generated image wrong" | Adjust prompt, add more details |
| "File too large" | Compression tools: TinyPNG, ImageMagick |
| "Bash script not running" | `chmod +x generate_diagrams.sh` |

---

## 📚 Next Steps

1. **Pilih metode** yang paling sesuai (Cara 1-4)
2. **Baca dokumentasi** sesuai pilihan:
   - Cara 1 → `PROMPTS_SIMPLE.txt`
   - Cara 2 → `generate_diagrams.py`
   - Cara 3 → `generate_diagrams.sh`
3. **Generate images**
4. **Replace** gambar Mermaid di `karya_tulis.md` jika puas dengan hasil
5. **Publish** atau cetak dokumen

---

## 📞 Support

- **Python errors:** `python generate_diagrams.py` (see error message)
- **API errors:** Check `ai_prompts.md` troubleshooting section
- **Prompt issues:** Edit `PROMPTS_SIMPLE.txt` with custom requirements
- **Scripts not running:** Check file permissions & dependencies

---

**Dibuat untuk:** Karya Tulis Ilmiah Dua Insan Story  
**Tanggal:** December 15, 2025  
**Versi:** 1.0
