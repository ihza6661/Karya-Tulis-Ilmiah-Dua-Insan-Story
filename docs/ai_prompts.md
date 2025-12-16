# AI Image Generator Prompts untuk Diagram

## Gambar 2.1 - Struktur Organisasi Toko Dua Insan Story

### Prompt untuk DALL-E / Midjourney / Stable Diffusion:

```
Create a professional organizational chart diagram for "Toko Dua Insan Story Organization Structure" showing hierarchical positions and responsibilities.

The diagram should show:

1. TOP LEVEL - Owner/Pemilik box:
   Title: "Pemilik (Owner) - Ihzah Mahendra"
   Responsibilities: Business policies, funding, overall monitoring, system management, customer satisfaction evaluation

2. MIDDLE LEVEL - Two branches below Owner:

   LEFT BRANCH - Admin box:
   Title: "Administrator / Customer Service"
   Responsibilities: Customer communication via website, order processing, payment confirmation, design proofs upload, customer inquiries, promo management, order status monitoring

   RIGHT BRANCH - Designer box:
   Title: "Desainer Grafis (Graphic Designer)"
   Responsibilities: Design production, converting customer event data to visual design, revisions per feedback, preparing final files, coordinating with admin

3. Connection lines showing hierarchy from Owner to both positions

Design requirements:
- Professional organizational hierarchy chart
- Light blue/white professional color scheme
- Clear rectangular boxes for each position
- Position titles in both Indonesian and English
- Responsibility descriptions visible or implied
- Hierarchical connection lines from top to bottom
- Clean, modern, minimalist design
- Suitable for academic document
- Image size: 1920x800 pixels
- White background
- Professional typography
- Clear visual hierarchy showing reporting structure
```

---

## Gambar 2.2 - Sistem Berjalan Pemesanan Undangan

### Prompt untuk DALL-E / Midjourney / Stable Diffusion:

```
Create a professional flowchart diagram showing the "Wedding Invitation Ordering Process" with a horizontal layout. 

The diagram should include these steps in sequence from left to right:
1. Customer icon with "Customer Sees Promotion on Social Media"
2. Admin icon with "Admin Receives Request"
3. Form icon with "Customer Fills Event Data"
4. Calculator icon with "Admin Calculates Price"
5. Payment icon with "Customer Transfers Payment"
6. Verification diamond with "Admin Verifies Payment"
7. If Valid: Notebook icon with "Record Order in Book"
8. If Invalid: Red X icon with "Request Confirmation Again"
9. Designer icon with "Designer Receives Data"

The diagram should use:
- Light professional blue/white color scheme
- Clear arrows connecting each step
- Icons/emoji to represent each role (customer, admin, designer, payment)
- Clean, modern design suitable for academic document
- Wide landscape format (16:9 aspect ratio)
- White background
- Text in Indonesian language
- Professional typography
```

---

## Gambar 2.3 - Sistem Berjalan Laporan Penjualan

### Prompt untuk DALL-E / Midjourney / Stable Diffusion:

```
Create a professional flowchart diagram showing the "Sales Reporting Process" with a horizontal linear layout.

The diagram should include these sequential steps from left to right:
1. Calendar icon with "End of Month Period"
2. Book icon with "Admin Takes Notebook"
3. Calculator icon with "Admin Sums All Revenue"
4. Bar chart icon with "Group Orders by Type (Digital/Print)"
5. Document icon with "Record Recap in Monthly Report"
6. Report icon with "Create Sales Report"
7. Owner/Manager icon with "Owner Reviews Report"
8. Analysis icon with "Owner Evaluates Performance"
9. Strategy icon with "Owner Makes Marketing Decisions"
10. Archive icon with "Approve and Archive Report"

The diagram should use:
- Light professional blue/white color scheme
- Clear arrows showing process flow
- Icons/emoji representing each action
- Clean, modern design for academic use
- Wide landscape format (16:9 aspect ratio)
- White background
- Text in Indonesian language
- Professional, clean typography
- Simple and clear visual hierarchy
```

---

## Python Script untuk Generate dengan OpenAI API

```python
import openai
import requests
from pathlib import Path

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

def generate_diagram_image(prompt, output_filename):
    """
    Generate image from prompt using OpenAI DALL-E
    """
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1920x800",
            quality="hd"
        )
        
        image_url = response['data'][0]['url']
        
        # Download and save image
        img_data = requests.get(image_url).content
        with open(output_filename, 'wb') as f:
            f.write(img_data)
        
        print(f"✓ Image saved: {output_filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error generating image: {e}")
        return False

# Prompt untuk Gambar 2.2
prompt_gambar_2_2 = """
Create a professional flowchart diagram showing the "Wedding Invitation Ordering Process" with a horizontal layout. 

The diagram should include these steps in sequence from left to right:
1. Customer icon with "Customer Sees Promotion on Social Media"
2. Admin icon with "Admin Receives Request"
3. Form icon with "Customer Fills Event Data"
4. Calculator icon with "Admin Calculates Price"
5. Payment icon with "Customer Transfers Payment"
6. Verification diamond with "Admin Verifies Payment"
7. If Valid: Notebook icon with "Record Order in Book"
8. If Invalid: Red X icon with "Request Confirmation Again"
9. Designer icon with "Designer Receives Data"

Design specifications:
- Light professional blue/white color scheme
- Clear arrows connecting each step
- Icons/emoji to represent each role
- Clean, modern design suitable for academic document
- Wide landscape format (1920x800 px)
- White background
- Text in Indonesian language
- Professional typography
"""

# Prompt untuk Gambar 2.3
prompt_gambar_2_3 = """
Create a professional flowchart diagram showing the "Sales Reporting Process" with a horizontal linear layout.

The diagram should include these sequential steps from left to right:
1. Calendar icon with "End of Month Period"
2. Book icon with "Admin Takes Notebook"
3. Calculator icon with "Admin Sums All Revenue"
4. Bar chart icon with "Group Orders by Type (Digital/Print)"
5. Document icon with "Record Recap in Monthly Report"
6. Report icon with "Create Sales Report"
7. Owner/Manager icon with "Owner Reviews Report"
8. Analysis icon with "Owner Evaluates Performance"
9. Strategy icon with "Owner Makes Marketing Decisions"
10. Archive icon with "Approve and Archive Report"

Design specifications:
- Light professional blue/white color scheme
- Clear arrows showing process flow
- Icons/emoji representing each action
- Clean, modern design for academic use
- Wide landscape format (1920x800 px)
- White background
- Text in Indonesian language
- Professional, clean typography
"""

# Generate images
if __name__ == "__main__":
    print("Generating diagram images...")
    
    generate_diagram_image(
        prompt_gambar_2_2,
        "gambar_2_2_ai_generated.png"
    )
    
    generate_diagram_image(
        prompt_gambar_2_3,
        "gambar_2_3_ai_generated.png"
    )
    
    print("\nDone!")
```

---

## Node.js Script untuk Generate dengan OpenAI API

```javascript
const axios = require('axios');
const fs = require('fs');
const path = require('path');

const OPENAI_API_KEY = process.env.OPENAI_API_KEY || 'your-api-key-here';

async function generateDiagramImage(prompt, outputFilename) {
  try {
    console.log(`Generating ${outputFilename}...`);
    
    const response = await axios.post(
      'https://api.openai.com/v1/images/generations',
      {
        prompt: prompt,
        n: 1,
        size: '1920x800',
        quality: 'hd'
      },
      {
        headers: {
          'Authorization': `Bearer ${OPENAI_API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    const imageUrl = response.data.data[0].url;
    const imageResponse = await axios.get(imageUrl, {
      responseType: 'arraybuffer'
    });
    
    fs.writeFileSync(outputFilename, imageResponse.data);
    console.log(`✓ Image saved: ${outputFilename}`);
    
  } catch (error) {
    console.error(`✗ Error generating image: ${error.message}`);
  }
}

// Prompts
const promptGambar22 = `Create a professional flowchart diagram showing the "Wedding Invitation Ordering Process" with a horizontal layout. The diagram should include these steps in sequence from left to right: Customer Sees Promotion → Admin Receives Request → Customer Fills Event Data → Admin Calculates Price → Customer Transfers Payment → Admin Verifies Payment (diamond decision) → If Valid: Record Order in Book → Designer Receives Data. If Invalid: Request Confirmation Again (loops back). Use light professional blue/white color scheme, clear arrows, icons for each role, clean modern design, wide landscape format 1920x800 px, white background, Indonesian text, professional typography.`;

const promptGambar23 = `Create a professional flowchart diagram showing the "Sales Reporting Process" with a horizontal linear layout. Steps from left to right: End of Month Period → Admin Takes Notebook → Admin Sums All Revenue → Group Orders by Type (Digital/Print) → Record Recap in Monthly Report → Create Sales Report → Owner Reviews Report → Owner Evaluates Performance → Owner Makes Marketing Decisions → Approve and Archive Report. Use light professional blue/white color scheme, clear connecting arrows, icons representing each action, clean modern design, landscape format 1920x800 px, white background, Indonesian text, professional typography.`;

// Main execution
(async () => {
  console.log('Starting diagram generation...\n');
  
  await generateDiagramImage(promptGambar22, 'gambar_2_2_ai_generated.png');
  await generateDiagramImage(promptGambar23, 'gambar_2_3_ai_generated.png');
  
  console.log('\nDone!');
})();
```

---

## Curl Command untuk API Testing

### Gambar 2.2:
```bash
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "Create a professional flowchart diagram showing the Wedding Invitation Ordering Process with a horizontal layout. Include Customer Sees Promotion on Social Media → Admin Receives Request → Customer Fills Event Data → Admin Calculates Price → Customer Transfers Payment → Admin Verifies Payment (diamond decision) → If Valid: Record Order in Book → Designer Receives Data. If Invalid: Request Confirmation Again. Use light professional blue/white color scheme, clear arrows, icons for each role, clean modern design, wide landscape format, white background, Indonesian text, professional typography.",
    "n": 1,
    "size": "1920x800",
    "quality": "hd"
  }' > gambar_2_2_response.json
```

### Gambar 2.3:
```bash
curl https://api.openai.com/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "Create a professional flowchart diagram showing the Sales Reporting Process with a horizontal linear layout. Steps: End of Month Period → Admin Takes Notebook → Admin Sums All Revenue → Group Orders by Type → Record Recap in Monthly Report → Create Sales Report → Owner Reviews Report → Owner Evaluates Performance → Owner Makes Marketing Decisions → Approve and Archive Report. Use light professional blue/white color scheme, clear arrows, icons, clean modern design, landscape format 1920x800 px, white background, Indonesian text, professional typography.",
    "n": 1,
    "size": "1920x800",
    "quality": "hd"
  }' > gambar_2_3_response.json
```

---

## Custom Configuration untuk Midjourney

### Gambar 2.2:
```
/imagine prompt: professional flowchart diagram horizontal layout wedding invitation ordering process customer sees promotion admin receives request customer fills event data admin calculates price customer transfers payment admin verifies payment record order book designer receives data light blue white color scheme clean modern design landscape 1920x800 white background Indonesian text --ar 12:5 --q 2 --s 750
```

### Gambar 2.3:
```
/imagine prompt: professional flowchart diagram horizontal linear sales reporting process end of month admin takes notebook sums revenue group orders by type record recap create report owner reviews evaluates performance makes marketing decisions archive light blue white color scheme clean modern design landscape 1920x800 white background Indonesian text --ar 12:5 --q 2 --s 750
```

---

## Notes:
- Ganti `your-api-key-here` dengan API key OpenAI Anda
- Untuk Python, install: `pip install openai requests`
- Untuk Node.js, install: `npm install axios`
- Adjust prompts sesuai kebutuhan spesifik Anda
- Hasil dari AI mungkin tidak 100% sama dengan Mermaid version, perlu fine-tuning
