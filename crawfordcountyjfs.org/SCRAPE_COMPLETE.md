# Crawford County JFS Website - Scrape Complete

## Summary

Complete scrape of https://crawfordcountyjfs.org/ performed on **2025-11-06**

## What Was Scraped

### Pages (14 total)
- ✓ Homepage
- ✓ OhioMeansJobs
- ✓ Child/Adult Protective Services (main)
  - ✓ Adult Protective Services (sub-page)
  - ✓ Kinship Care (sub-page)
- ✓ Foster Care & Adoption
- ✓ Public Assistance
- ✓ Child Support
- ✓ Additional Resources
- ✓ Join Our Team
- ✓ Current RFPs
- ✓ Report Child Abuse
- ✓ Fraud Assistance
- ✓ Privacy Policy

### Assets Downloaded
- ✓ Crawford County JFS Logo (PNG)
- ✓ Foster Care Preservice Training 2021 (PDF)
- ✓ Title XX Hearing Notice 2024 (PDF)
- ✓ RFP for NET 2023-2024 (Excel)

## Directory Structure

```
crawfordcountyjfs.org/
├── README.md                          # Project overview and guide
├── SITEMAP.md                         # Complete site structure map
├── SCRAPE_COMPLETE.md                 # This file
├── download_assets.py                 # Asset download script
│
├── home/
│   └── index.md
├── ohio-means-jobs/
│   └── index.md
├── child-protective-services/
│   ├── index.md
│   ├── adult-protective-services/
│   │   └── index.md
│   └── kinship/
│       └── index.md
├── foster-care-adopt/
│   └── index.md
├── public-assistance/
│   └── index.md
├── child-support/
│   └── index.md
├── additional-resources/
│   └── index.md
├── join-our-team/
│   └── index.md
├── current-rfps/
│   └── index.md
├── report-child-abuse/
│   └── index.md
├── fraud-assistance/
│   └── index.md
├── privacy-policy/
│   └── index.md
│
└── assets/
    ├── ASSETS_INVENTORY.md
    ├── images/
    │   └── logo.png
    └── documents/
        ├── foster-care-preservice-training-2021.pdf
        ├── title-xx-hearing-notice-2024.pdf
        └── rfp-net-2023-2024.xls
```

## Statistics

- **Total Directories:** 18
- **Total Markdown Files:** 17
- **Total Images:** 1
- **Total Documents:** 3
- **Total Assets:** 4

## Content Format

All page content has been saved as Markdown (.md) files, preserving:
- Headings and structure
- Text content
- Contact information
- Lists and formatting
- External links and references

## Notes

1. Two navigation links returned 404 errors:
   - Crawford County Family & Children First Council page
   - Ongoing Case Services sub-page

2. The website uses WordPress with lazy-loading for images, so only directly accessible images were downloaded

3. All external links to partner organizations (benefits.ohio.gov, fosterandadopt.jfs.ohio.gov, etc.) have been preserved in the text

## Key Contact Information

**Crawford County Job and Family Services**
- Address: 224 Norton Way, Bucyrus, OH 44820
- Main: (419) 562-0015
- Hours: M-F 7:30 AM - 4:00 PM

### Department Contacts
- Public Assistance: (419) 562-0015
- Ohio Means Jobs: (419) 562-8066
- Child Support: (419) 562-0773
- Child Protective Services: (419) 563-1570
- Adult Protective Services: 567-393-4729
- Foster Care (Beth Sergent): 567-393-4733

## Files to Review

- `README.md` - Start here for an overview
- `SITEMAP.md` - Complete site navigation map
- `assets/ASSETS_INVENTORY.md` - Details on downloaded files

---

**Scrape Status:** ✓ COMPLETE
**Date:** 2025-11-06
**Source:** https://crawfordcountyjfs.org/
