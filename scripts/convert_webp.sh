#!/bin/bash
# Bolt: Convert background images in bg/ to WebP with fallbacks for performance

# Check if cwebp is installed
if ! command -v cwebp &> /dev/null; then
    echo "cwebp could not be found. Please install webp (e.g., sudo apt-get install webp)"
    # return instead of exit to not break session if sourced, though it shouldn't be sourced
    return 1 2>/dev/null || true
fi

echo "Converting images in bg/ to WebP..."

# Find all png, jpg, jpeg images in bg/ and convert them
find bg/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read img; do
    # Skip favicon as it's specifically needed as png for some older browsers/platforms
    if [[ "$img" == *"favicon"* ]]; then
        continue
    fi

    webp_path="${img%.*}.webp"

    # Check if we already have the webp file and it's newer than the source
    if [ ! -f "$webp_path" ] || [ "$img" -nt "$webp_path" ]; then
        echo "Converting $img to $webp_path"
        # Convert to WebP with good quality (80%)
        cwebp -q 80 "$img" -o "$webp_path" -quiet
    else
        echo "Skipping $img (WebP already exists and is up to date)"
    fi
done

echo "Done! Remember to use <picture> tags for fallbacks in HTML, for example:"
echo "<picture>"
echo "  <source srcset=\"image.webp\" type=\"image/webp\">"
echo "  <img src=\"image.png\" alt=\"Description\" loading=\"lazy\">"
echo "</picture>"
