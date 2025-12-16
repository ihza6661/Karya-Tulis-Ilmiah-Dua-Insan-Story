#!/usr/bin/env python3
"""
Script untuk generate diagram images menggunakan OpenAI DALL-E API
Gunakan untuk membuat Gambar 2.2 dan 2.3 dari AI Image Generator
"""

import os
import sys
import requests
from pathlib import Path
from typing import Optional

def generate_image_dalle(prompt: str, output_path: str, api_key: Optional[str] = None) -> bool:
    """
    Generate image using OpenAI DALL-E API
    
    Args:
        prompt: Text prompt for image generation
        output_path: Path where to save the image
        api_key: OpenAI API key (uses env var if not provided)
    
    Returns:
        True if successful, False otherwise
    """
    api_key = api_key or os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        return False
    
    try:
        print(f"🎨 Generating image: {output_path}")
        print(f"📝 Prompt length: {len(prompt)} characters")
        
        response = requests.post(
            'https://api.openai.com/v1/images/generations',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'prompt': prompt,
                'n': 1,
                'size': '1920x800',
                'quality': 'hd',
                'model': 'dall-e-3'
            },
            timeout=120
        )
        
        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code}")
            print(f"   {response.text}")
            return False
        
        image_url = response.json()['data'][0]['url']
        
        # Download image
        print("⬇️  Downloading image...")
        img_response = requests.get(image_url, timeout=30)
        
        if img_response.status_code != 200:
            print(f"❌ Download failed: {img_response.status_code}")
            return False
        
        # Save image
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(img_response.content)
        
        file_size = Path(output_path).stat().st_size / 1024
        print(f"✅ Image saved: {output_path} ({file_size:.1f} KB)")
        return True
        
    except requests.exceptions.Timeout:
        print("❌ Request timeout - API took too long to respond")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main execution"""
    
    prompt_gambar_2_2 = """Create a professional flowchart diagram showing the "Wedding Invitation Ordering Process" with a horizontal layout. The diagram should show these steps from left to right: Customer Sees Promotion on Social Media → Admin Receives Request → Customer Fills Event Data → Admin Calculates Price → Customer Transfers Payment → Admin Verifies Payment (diamond decision node) → If Valid: Record Order in Book → If Invalid: Request Confirmation Again (loops back to payment) → Designer Receives Data. 

Design with: light professional blue and white color scheme, clear directional arrows, icons representing each role, clean modern minimalist design, 1920x800 landscape format, white background, all text in Indonesian language, professional typography, clear visual hierarchy."""

    prompt_gambar_2_3 = """Create a professional flowchart diagram showing the "Sales Reporting Process" with a horizontal linear layout. Steps from left to right: End of Month Period → Admin Takes Notebook → Admin Sums All Revenue → Group Orders by Type (Digital/Print) → Record Recap in Monthly Report → Create Sales Report → Owner Reviews Report → Owner Evaluates Performance → Owner Makes Marketing Decisions → Approve and Archive Report.

Design with: light professional blue and white color scheme, clear arrows connecting steps, icons representing each action, clean modern minimalist design, 1920x800 landscape format, white background, all text in Indonesian language, professional typography, clear visual hierarchy."""

    output_dir = Path('images')
    
    print("=" * 60)
    print("AI Diagram Image Generator")
    print("=" * 60)
    
    # Check API key
    if not os.getenv('OPENAI_API_KEY'):
        print("\n⚠️  Warning: OPENAI_API_KEY environment variable not set")
        print("To use this script, set your API key:\n")
        print("  Linux/Mac: export OPENAI_API_KEY='sk-...'")
        print("  Windows:   set OPENAI_API_KEY=sk-...")
        print("\nOr pass it as argument: python generate_diagrams.py 'your-api-key'\n")
        
        if len(sys.argv) > 1:
            api_key = sys.argv[1]
        else:
            print("❌ No API key provided. Exiting.")
            return 1
    else:
        api_key = None
    
    print(f"\n📁 Output directory: {output_dir}")
    output_dir.mkdir(exist_ok=True)
    
    # Generate images
    results = []
    
    print("\n" + "=" * 60)
    print("Generating Gambar 2.2 - Sistem Berjalan Pemesanan Undangan")
    print("=" * 60)
    result1 = generate_image_dalle(
        prompt_gambar_2_2,
        str(output_dir / 'gambar_2_2_dall_e.png'),
        api_key
    )
    results.append(('Gambar 2.2', result1))
    
    print("\n" + "=" * 60)
    print("Generating Gambar 2.3 - Sistem Berjalan Laporan Penjualan")
    print("=" * 60)
    result2 = generate_image_dalle(
        prompt_gambar_2_3,
        str(output_dir / 'gambar_2_3_dall_e.png'),
        api_key
    )
    results.append(('Gambar 2.3', result2))
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name, result in results:
        status = "✅ Success" if result else "❌ Failed"
        print(f"{name}: {status}")
    
    success_count = sum(1 for _, r in results if r)
    total_count = len(results)
    
    print(f"\nTotal: {success_count}/{total_count} images generated")
    
    return 0 if success_count == total_count else 1

if __name__ == '__main__':
    sys.exit(main())
