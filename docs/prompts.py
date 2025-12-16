#!/usr/bin/env python3
"""
Comprehensive Prompt Collection untuk Generate Diagram AI
Semua prompt dalam satu file untuk berbagai platform
"""

# ============================================================================
# GAMBAR 2.1 - STRUKTUR ORGANISASI TOKO DUA INSAN STORY
# ============================================================================

PROMPTS_GAMBAR_2_1 = {
    "name": "Struktur Organisasi Toko Dua Insan Story",
    "description": "Organizational chart menampilkan hierarki dan tanggung jawab setiap posisi",
    
    # Prompt untuk DALL-E 3 (OpenAI)
    "dall_e_3": """Create a professional organizational chart diagram for "Toko Dua Insan Story Organization Structure" showing hierarchical positions and responsibilities.

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
- Clear visual hierarchy showing reporting structure""",

    # Prompt untuk DALL-E 2
    "dall_e_2": """Professional organizational chart hierarchy diagram Toko Dua Insan Story. Top: Owner Ihzah Mahendra (business policies, funding, monitoring). Below: Administrator Customer Service (left) - order processing, customer communication, payments. Graphic Designer (right) - design production, revisions, file preparation. Connected with hierarchy lines. Professional blue white colors, 1024x1024 landscape, academic document, Indonesian text.""",

    # Prompt untuk Midjourney
    "midjourney": """professional organizational chart hierarchy diagram toko dua insan story owner ihzah mahendra top administrator customer service left graphic designer right hierarchy structure light blue white color scheme clean modern design landscape 1920x800 white background Indonesian English text academic document professional --ar 12:5 --q 2 --s 750""",

    # Prompt untuk Stable Diffusion
    "stable_diffusion": """professional organizational chart, hierarchy diagram, toko dua insan story, owner ihzah mahendra at top, administrator customer service on left, graphic designer on right, hierarchy lines, light blue white professional colors, clean modern design, academic document, 1920x800 landscape, white background, Indonesian English text, high quality, 8k""",

    # Prompt singkat
    "short": """Professional organizational hierarchy chart: Owner (Ihzah Mahendra) at top, Administrator/Customer Service and Graphic Designer below. Responsibilities listed. Professional blue/white design, Indonesian text, landscape format.""",

    # Konfigurasi teknis
    "config": {
        "width": 1920,
        "height": 800,
        "aspect_ratio": "12:5",
        "format": "png",
        "quality": "hd",
        "background": "white",
        "model": "dall-e-3"
    }
}

# ============================================================================
# GAMBAR 2.2 - SISTEM BERJALAN PEMESANAN UNDANGAN
# ============================================================================

PROMPTS_GAMBAR_2_2 = {
    "name": "Sistem Berjalan Pemesanan Undangan",
    "description": "Flowchart horizontal menampilkan proses pemesanan undangan secara manual",
    
    # Prompt untuk DALL-E 3 (OpenAI)
    "dall_e_3": """Create a professional flowchart diagram showing the "Wedding Invitation Ordering Process" with a horizontal layout. The diagram should show these steps from left to right: 

1. Customer icon with label "Customer Sees Promotion on Social Media"
2. Arrow to Admin icon with label "Admin Receives Request"  
3. Arrow to Form/Document icon with label "Customer Fills Event Data"
4. Arrow to Calculator icon with label "Admin Calculates Price"
5. Arrow to Payment/Money icon with label "Customer Transfers Payment"
6. Arrow to Diamond decision node with label "Admin Verifies Payment"
7. From diamond, if "Valid" arrow: Notebook icon with "Record Order in Book"
8. From diamond, if "Invalid" arrow: X/Cross icon with "Request Confirmation Again"
9. Invalid path loops back to Payment step
10. From Record Order: arrow to Designer icon with "Designer Receives Data"

Design requirements:
- Horizontal flowchart layout (landscape orientation)
- Light professional color scheme (blues, whites, light grays)
- Clear directional arrows between all steps
- Icons or emoji representing each role/action
- Clean, modern, minimalist design
- Suitable for academic/professional document
- Image size: 1920x800 pixels
- White background
- All text in Indonesian language
- Professional typography
- Clear visual hierarchy
- All text labels clearly visible""",

    # Prompt untuk DALL-E 2
    "dall_e_2": """Professional flowchart horizontal layout wedding invitation ordering system. Customer sees promotion → Admin receives request → Customer fills event data → Admin calculates price → Customer transfers payment → Admin verifies payment (diamond) → Valid path: Record order in book → Designer receives data. Invalid path: Request confirmation again (loop back). Professional blue and white colors, clear arrows, icons, clean modern design, 1024x1024 landscape aspect, white background, Indonesian text.""",

    # Prompt untuk Midjourney
    "midjourney": """professional flowchart diagram horizontal layout wedding invitation ordering process customer sees promotion admin receives request customer fills event data admin calculates price customer transfers payment admin verifies payment record order book designer receives data light blue white color scheme clean modern design landscape 1920x800 white background Indonesian text --ar 12:5 --q 2 --s 750""",

    # Prompt untuk Stable Diffusion
    "stable_diffusion": """professional flowchart, horizontal layout, wedding invitation ordering system, customer sees social media → admin receives → customer fills data → admin calculates price → customer transfers payment → admin verifies → valid: record order → designer receives, invalid: request again, light blue white professional colors, clean modern design, clear arrows, icons, Indonesian text, high quality, 8k""",

    # Prompt singkat untuk quick testing
    "short": """Horizontal flowchart: Wedding invitation ordering process with steps from customer seeing promotion through designer receiving data. Includes payment verification decision point. Professional blue/white design, Indonesian text.""",

    # Konfigurasi teknis
    "config": {
        "width": 1920,
        "height": 800,
        "aspect_ratio": "12:5",
        "format": "png",
        "quality": "hd",
        "background": "white",
        "model": "dall-e-3"
    }
}

# ============================================================================
# GAMBAR 2.3 - SISTEM BERJALAN LAPORAN PENJUALAN
# ============================================================================

PROMPTS_GAMBAR_2_3 = {
    "name": "Sistem Berjalan Laporan Penjualan",
    "description": "Flowchart horizontal menampilkan proses pembuatan laporan bulanan",
    
    # Prompt untuk DALL-E 3 (OpenAI)
    "dall_e_3": """Create a professional flowchart diagram showing the "Sales Reporting Process" with a horizontal linear layout. The diagram should show these sequential steps from left to right:

1. Calendar icon with label "End of Month Period"
2. Arrow to Book/Notebook icon with "Admin Takes Notebook"
3. Arrow to Calculator icon with "Admin Sums All Revenue"
4. Arrow to Bar Chart icon with "Group Orders by Type (Digital/Print)"
5. Arrow to Document icon with "Record Recap in Monthly Report"
6. Arrow to Report icon with "Create Sales Report"
7. Arrow to Manager/Owner icon with "Owner Reviews Report"
8. Arrow to Magnifying Glass icon with "Owner Evaluates Performance"
9. Arrow to Light Bulb/Strategy icon with "Owner Makes Marketing Decisions"
10. Arrow to Archive/Check icon with "Approve and Archive Report"

Design requirements:
- Horizontal linear flowchart (flowing left to right)
- Light professional color scheme (blues, whites, light grays)
- Clear directional arrows connecting all steps
- Icons or emoji representing each action/role
- Clean, modern, minimalist design
- Suitable for academic/professional document
- Image size: 1920x800 pixels
- White background
- All text in Indonesian language
- Professional typography
- Clear visual hierarchy
- All text labels clearly readable""",

    # Prompt untuk DALL-E 2
    "dall_e_2": """Professional flowchart horizontal linear layout sales reporting process monthly. End of month → Admin takes notebook → Sums revenue → Groups orders by type digital print → Records recap → Creates report → Owner reviews → Evaluates performance → Makes marketing decisions → Approves archives. Professional blue white colors, clear arrows, icons, clean modern design, 1024x1024 landscape, white background, Indonesian text.""",

    # Prompt untuk Midjourney
    "midjourney": """professional flowchart diagram horizontal linear sales reporting process end of month admin takes notebook sums revenue group orders by type record recap create report owner reviews evaluates performance makes marketing decisions archive light blue white color scheme clean modern design landscape 1920x800 white background Indonesian text --ar 12:5 --q 2 --s 750""",

    # Prompt untuk Stable Diffusion
    "stable_diffusion": """professional flowchart, horizontal linear layout, sales reporting process, end of month → admin takes notebook → sums revenue → groups orders → records recap → creates report → owner reviews → evaluates performance → makes decisions → archives, light blue white professional colors, clean modern design, clear arrows, icons, Indonesian text, high quality, 8k""",

    # Prompt singkat
    "short": """Horizontal linear flowchart: Monthly sales reporting process from end of month through admin notebook review, revenue calculation, report creation, owner review and evaluation, decision making, and archival. Professional blue/white design, Indonesian text.""",

    # Konfigurasi teknis
    "config": {
        "width": 1920,
        "height": 800,
        "aspect_ratio": "12:5",
        "format": "png",
        "quality": "hd",
        "background": "white",
        "model": "dall-e-3"
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def print_prompt(diagram_num: int, platform: str = "dall_e_3"):
    """
    Print prompt untuk diagram tertentu dan platform
    
    Args:
        diagram_num: 1, 2, atau 3
        platform: 'dall_e_3', 'dall_e_2', 'midjourney', 'stable_diffusion', 'short'
    """
    if diagram_num == 1:
        prompts = PROMPTS_GAMBAR_2_1
    elif diagram_num == 2:
        prompts = PROMPTS_GAMBAR_2_2
    else:
        prompts = PROMPTS_GAMBAR_2_3
    
    print(f"\n{'='*70}")
    print(f"PROMPT: {prompts['name']} - {platform.upper()}")
    print(f"{'='*70}\n")
    print(prompts[platform])
    print(f"\n{'='*70}\n")

def get_prompt(diagram_num: int, platform: str = "dall_e_3") -> str:
    """Get prompt string"""
    if diagram_num == 1:
        prompts = PROMPTS_GAMBAR_2_1
    elif diagram_num == 2:
        prompts = PROMPTS_GAMBAR_2_2
    else:
        prompts = PROMPTS_GAMBAR_2_3
    return prompts[platform]

def get_config(diagram_num: int) -> dict:
    """Get configuration for diagram"""
    if diagram_num == 1:
        config = PROMPTS_GAMBAR_2_1
    elif diagram_num == 2:
        config = PROMPTS_GAMBAR_2_2
    else:
        config = PROMPTS_GAMBAR_2_3
    return config["config"]

def list_all_prompts():
    """Print semua prompts tersedia"""
    print("\n" + "="*70)
    print("AVAILABLE PROMPTS")
    print("="*70 + "\n")
    
    for diagram_num, diagrams in [(1, PROMPTS_GAMBAR_2_1), (2, PROMPTS_GAMBAR_2_2), (3, PROMPTS_GAMBAR_2_3)]:
        print(f"\nGAMBAR 2.{diagram_num}: {diagrams['name']}")
        print(f"Deskripsi: {diagrams['description']}")
        print("Platforms:")
        for key in diagrams.keys():
            if key not in ['name', 'description', 'config']:
                print(f"  - {key}")

# ============================================================================
# MAIN - Interactive CLI
# ============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python prompts.py 1 [platform]  - Print Gambar 2.1 prompt (Struktur Organisasi)")
        print("  python prompts.py 2 [platform]  - Print Gambar 2.2 prompt (Pemesanan Undangan)")
        print("  python prompts.py 3 [platform]  - Print Gambar 2.3 prompt (Laporan Penjualan)")
        print("  python prompts.py list          - List all available prompts")
        print("\nPlatforms: dall_e_3, dall_e_2, midjourney, stable_diffusion, short")
        print("\nExample:")
        print("  python prompts.py 1 dall_e_3")
        print("  python prompts.py 2 midjourney")
        print("  python prompts.py 3 stable_diffusion")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_all_prompts()
    else:
        diagram_num = int(command)
        platform = sys.argv[2] if len(sys.argv) > 2 else "dall_e_3"
        
        if platform not in ["dall_e_3", "dall_e_2", "midjourney", "stable_diffusion", "short"]:
            print(f"Unknown platform: {platform}")
            sys.exit(1)
        
        print_prompt(diagram_num, platform)
