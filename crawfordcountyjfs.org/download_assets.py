#!/usr/bin/env python3
"""
Script to download images and assets from Crawford County JFS website
"""

import os
import requests
from urllib.parse import urlparse
from pathlib import Path

# Base directory
base_dir = Path(__file__).parent / "assets"
base_dir.mkdir(exist_ok=True)

# Assets to download
assets = [
    {
        "url": "https://crawfordcountyjfs.org/wp-content/uploads/2020/05/cropped-rlogo-e1593194881614.png",
        "filename": "logo.png"
    }
]

# PDFs referenced on the site (if available)
pdfs = [
    {
        "url": "https://crawfordcountyjfs.org/wp-content/uploads/2021/03/2021-Preservice.pdf",
        "filename": "foster-care-preservice-training-2021.pdf"
    },
    {
        "url": "https://crawfordcountyjfs.org/wp-content/uploads/2024/05/Title-XX-hearing-Notice-2024.pdf",
        "filename": "title-xx-hearing-notice-2024.pdf"
    },
    {
        "url": "https://crawfordcountyjfs.org/wp-content/uploads/2023/09/RFP-for-NET-2023-2024.xls",
        "filename": "rfp-net-2023-2024.xls"
    }
]

def download_file(url, filepath):
    """Download a file from URL to filepath"""
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"  ✓ Saved to {filepath}")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        return False

def main():
    print("Crawford County JFS Asset Downloader")
    print("=" * 50)

    # Create subdirectories
    (base_dir / "images").mkdir(exist_ok=True)
    (base_dir / "documents").mkdir(exist_ok=True)

    # Download images
    print("\nDownloading images...")
    for asset in assets:
        filepath = base_dir / "images" / asset["filename"]
        download_file(asset["url"], filepath)

    # Download PDFs and documents
    print("\nDownloading documents...")
    for pdf in pdfs:
        filepath = base_dir / "documents" / pdf["filename"]
        download_file(pdf["url"], filepath)

    print("\n" + "=" * 50)
    print("Download complete!")
    print(f"Assets saved to: {base_dir.absolute()}")

if __name__ == "__main__":
    main()
