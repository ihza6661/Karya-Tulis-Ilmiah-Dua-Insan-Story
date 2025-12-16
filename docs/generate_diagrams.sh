#!/bin/bash

# Script untuk generate diagram images menggunakan OpenAI API
# Usage: ./generate_diagrams.sh [API_KEY]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/images"
API_KEY="${1:-$OPENAI_API_KEY}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}════════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════════${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ️  $1${NC}"
}

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    print_error "curl is not installed. Please install curl first."
    exit 1
fi

# Check if API key is provided
if [ -z "$API_KEY" ]; then
    print_header "OpenAI API Key Required"
    echo ""
    print_error "No API key provided"
    echo ""
    echo "Usage:"
    echo "  ./generate_diagrams.sh 'sk-your-api-key'"
    echo ""
    echo "Or set environment variable:"
    echo "  export OPENAI_API_KEY='sk-your-api-key'"
    echo "  ./generate_diagrams.sh"
    echo ""
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

print_header "AI Diagram Image Generator"
print_info "Output directory: $OUTPUT_DIR"
echo ""

# Prompt untuk Gambar 2.2
PROMPT_2_2="Create a professional flowchart diagram showing the Wedding Invitation Ordering Process with a horizontal layout. Show these steps left to right: Customer Sees Promotion on Social Media → Admin Receives Request → Customer Fills Event Data → Admin Calculates Price → Customer Transfers Payment → Admin Verifies Payment (diamond decision) → If Valid: Record Order in Book → If Invalid: Request Confirmation Again (loops back) → Designer Receives Data. Use light professional blue and white colors, clear arrows, icons for each role, clean modern design, 1920x800 landscape, white background, Indonesian text, professional typography."

# Prompt untuk Gambar 2.3
PROMPT_2_3="Create a professional flowchart diagram showing the Sales Reporting Process with a horizontal linear layout. Show steps left to right: End of Month Period → Admin Takes Notebook → Admin Sums All Revenue → Group Orders by Type → Record Recap in Monthly Report → Create Sales Report → Owner Reviews Report → Owner Evaluates Performance → Owner Makes Marketing Decisions → Approve and Archive Report. Use light professional blue and white colors, clear arrows, icons for each action, clean modern design, 1920x800 landscape, white background, Indonesian text, professional typography."

# Function to generate image
generate_image() {
    local prompt="$1"
    local output_file="$2"
    local name="$3"
    
    echo ""
    print_info "Generating: $name"
    
    # Create temporary file for response
    temp_response=$(mktemp)
    
    # Call OpenAI API
    http_code=$(curl -s -w "%{http_code}" -o "$temp_response" \
        -X POST https://api.openai.com/v1/images/generations \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $API_KEY" \
        -d "{
            \"prompt\": \"$prompt\",
            \"n\": 1,
            \"size\": \"1920x800\",
            \"quality\": \"hd\",
            \"model\": \"dall-e-3\"
        }")
    
    # Check HTTP status
    if [ "$http_code" != "200" ]; then
        print_error "API Error (HTTP $http_code)"
        cat "$temp_response"
        rm "$temp_response"
        return 1
    fi
    
    # Extract image URL
    image_url=$(grep -o '"url":"[^"]*' "$temp_response" | head -1 | cut -d'"' -f4)
    
    if [ -z "$image_url" ]; then
        print_error "Failed to extract image URL"
        cat "$temp_response"
        rm "$temp_response"
        return 1
    fi
    
    # Download image
    print_info "Downloading image..."
    if ! curl -s -o "$output_file" "$image_url"; then
        print_error "Failed to download image"
        rm "$temp_response"
        return 1
    fi
    
    # Check file size
    file_size=$(du -h "$output_file" | cut -f1)
    
    print_success "$name generated: $output_file ($file_size)"
    rm "$temp_response"
    return 0
}

# Generate images
GAMBAR_2_2="$OUTPUT_DIR/gambar_2_2_dall_e.png"
GAMBAR_2_3="$OUTPUT_DIR/gambar_2_3_dall_e.png"

generate_image "$PROMPT_2_2" "$GAMBAR_2_2" "Gambar 2.2"
RESULT_2_2=$?

generate_image "$PROMPT_2_3" "$GAMBAR_2_3" "Gambar 2.3"
RESULT_2_3=$?

# Summary
echo ""
print_header "Summary"

if [ $RESULT_2_2 -eq 0 ]; then
    print_success "Gambar 2.2 (Sistem Berjalan Pemesanan)"
else
    print_error "Gambar 2.2 (Sistem Berjalan Pemesanan)"
fi

if [ $RESULT_2_3 -eq 0 ]; then
    print_success "Gambar 2.3 (Sistem Berjalan Laporan)"
else
    print_error "Gambar 2.3 (Sistem Berjalan Laporan)"
fi

if [ $RESULT_2_2 -eq 0 ] && [ $RESULT_2_3 -eq 0 ]; then
    echo ""
    print_success "All images generated successfully!"
    exit 0
else
    echo ""
    print_error "Some images failed to generate"
    exit 1
fi
