# AI Prompts untuk Generate Diagram - Gambar 2.2 & 2.3

Dokumentasi lengkap untuk membuat diagram menggunakan AI Image Generator

## 📋 Daftar File

1. **PROMPTS_SIMPLE.txt** - Prompt langsung yang bisa di-copy ke DALL-E, Midjourney, atau Stable Diffusion
2. **ai_prompts.md** - Dokumentasi lengkap dengan berbagai format (Python, Node.js, Curl, Midjourney)
3. **generate_diagrams.py** - Script Python untuk generate otomatis menggunakan OpenAI API

---

## 🚀 Quick Start

### Option 1: Manual (Copy-Paste Prompt)

**Untuk DALL-E Web Interface:**
1. Buka https://openai.com/dall-e-3 (login required)
2. Buka file `PROMPTS_SIMPLE.txt`
3. Copy prompt untuk Gambar 2.2
4. Paste ke DALL-E
5. Klik Generate
6. Ulangi untuk Gambar 2.3

**Untuk Midjourney:**
1. Buka Discord server Midjourney
2. Ke channel #general
3. Ketik `/imagine`
4. Copy prompt dari file `ai_prompts.md` (bagian Midjourney)
5. Adjust parameter `--ar` dan `--q` sesuai kebutuhan

**Untuk Stable Diffusion (Local):**
```bash
# Install ComfyUI atau WebUI
# Copy prompt dari PROMPTS_SIMPLE.txt ke text input
# Adjust settings (sampler, steps, etc.)
# Generate
```

---

### Option 2: Otomatis dengan Python Script

**Prerequisites:**
- Python 3.7+
- pip
- OpenAI API key (dari https://platform.openai.com/api-keys)

**Install dependencies:**
```bash
pip install requests
```

**Set API Key:**

Linux/Mac:
```bash
export OPENAI_API_KEY='sk-your-api-key-here'
```

Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY='sk-your-api-key-here'
```

Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=sk-your-api-key-here
```

**Run script:**
```bash
python generate_diagrams.py
```

**Output:**
- `images/gambar_2_2_dall_e.png`
- `images/gambar_2_3_dall_e.png`

---

## 📝 Prompt Details

### Gambar 2.2 - Sistem Berjalan Pemesanan Undangan

**Deskripsi:** Flowchart horizontal menampilkan proses pemesanan undangan secara manual melalui chat

**Steps:**
1. Customer sees promotion → 2. Admin receives request → 3. Customer fills data → 4. Admin calculates price → 5. Customer transfers payment → 6. Admin verifies (decision) → 7a. If valid: record order → 7b. If invalid: request again → 8. Designer receives data

**Key Design Elements:**
- Horizontal layout (landscape)
- Icons for each role
- Decision diamond for verification
- Feedback loop for invalid payment
- Professional blue/white color scheme

---

### Gambar 2.3 - Sistem Berjalan Laporan Penjualan

**Deskripsi:** Flowchart horizontal menampilkan proses pembuatan laporan bulanan

**Steps:**
1. End of month → 2. Admin takes notebook → 3. Sum revenue → 4. Group by type → 5. Record recap → 6. Create report → 7. Owner reviews → 8. Evaluate performance → 9. Make decisions → 10. Archive

**Key Design Elements:**
- Linear horizontal flow (left to right)
- Sequential steps
- Administrative and management roles
- Final archival step
- Professional design

---

## 🎯 Customization

### Mengubah Ukuran
```bash
# Di script Python, ubah:
'size': '1920x800'  # ke pilihan lain: '1024x1024', '1792x1024', '1024x1792'
```

### Mengubah Kualitas
```bash
# Untuk OpenAI:
'quality': 'hd'  # atau 'standard' (lebih murah)

# Untuk Midjourney:
--q 2  # kualitas tinggi
--q 1  # kualitas normal
```

### Mengubah Model
```bash
# Script mendukung DALL-E 3, untuk menggunakan 2:
'model': 'dall-e-2'
```

---

## 💰 Estimated Costs

**OpenAI DALL-E 3:**
- 1920x800 (HD): $0.08 per image
- Estimated: 2 images = $0.16

**OpenAI DALL-E 2:**
- 1024x1024: $0.020 per image
- Lebih murah tapi kualitas lebih rendah

**Midjourney:**
- Subscription dari $10-120/bulan
- Unlimited dengan plan tertentu

**Stable Diffusion:**
- Gratis (local generation)
- GPU required untuk kecepatan baik

---

## 🔧 Troubleshooting

### Error: "OPENAI_API_KEY not found"
- Pastikan API key sudah di-set
- Cek: `echo $OPENAI_API_KEY` (Linux/Mac) atau `echo %OPENAI_API_KEY%` (Windows)

### Error: "Invalid API key"
- Regenerate API key di https://platform.openai.com/api-keys
- Jangan share key dengan orang lain

### Error: "Rate limit exceeded"
- Tunggu beberapa menit sebelum request baru
- Upgrade plan OpenAI jika diperlukan

### Generated image tidak sesuai
- Adjust prompt descriptions
- Add more specific keywords
- Gunakan reference prompts dari `ai_prompts.md`

---

## 📚 Resources

- [OpenAI DALL-E API Docs](https://platform.openai.com/docs/guides/images)
- [Midjourney Docs](https://docs.midjourney.com)
- [Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [Prompt Engineering Tips](https://platform.openai.com/docs/guides/gpt-best-practices)

---

## 📄 File Structure

```
Karya Tulis Ilmiah Dua Insan Story/
├── karya_tulis.md              # Main document
├── images/
│   ├── gambar_2_2.png          # Current Mermaid version
│   ├── gambar_2_3.png          # Current Mermaid version
│   ├── gambar_2_2.mmd          # Mermaid source
│   ├── gambar_2_3.mmd          # Mermaid source
│   ├── gambar_2_2_dall_e.png   # AI Generated (if using script)
│   └── gambar_2_3_dall_e.png   # AI Generated (if using script)
├── PROMPTS_SIMPLE.txt          # Simple copy-paste prompts
├── ai_prompts.md               # Detailed prompts & code
├── generate_diagrams.py        # Python script for automation
└── AI_PROMPTS_README.md        # This file
```

---

## ✅ Checklist

- [ ] Read PROMPTS_SIMPLE.txt
- [ ] Choose generation method (manual or script)
- [ ] Set up API key (if using script)
- [ ] Generate images
- [ ] Review generated images
- [ ] Replace Mermaid images if needed
- [ ] Update karya_tulis.md with new images

---

**Last Updated:** December 15, 2025  
**Created for:** Karya Tulis Ilmiah Dua Insan Story
