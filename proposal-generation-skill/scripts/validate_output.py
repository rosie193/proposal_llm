#!/usr/bin/env python3
"""
Validate generated proposal files.

Usage:
    python validate_output.py <template_file> [reasoning_file] [checklist_file]
"""

import re
import sys
from pathlib import Path

def validate_template(content):
    """Check template file format."""
    errors = []
    warnings = []
    
    # Check for source references (should not exist)
    if re.search(r'S[12]\s*-\s*["\']', content):
        errors.append("❌ Template contains source references (S1/S2)")
    
    # Check for reasoning text
    if re.search(r'(Based on|Logic:|Calculated as|Extracted from)', content, re.IGNORECASE):
        errors.append("❌ Template contains reasoning text")
    
    # Check placeholder format
    placeholder_pattern = r'\d+\s+\w+\s*\[[A-Z_]+\d+\]'
    placeholders = re.findall(placeholder_pattern, content)
    if not placeholders:
        warnings.append("⚠️  No placeholders found (may be intentional if all values confirmed)")
    else:
        # Validate placeholder format
        for placeholder in placeholders:
            if not re.match(r'.+\s+\[[A-Z_]+\d+\]', placeholder):
                errors.append(f"❌ Invalid placeholder format: {placeholder}")
    
    # Check for empty sections
    if re.search(r'##\s+\w+.*\n\n(?!\s)', content):
        warnings.append("⚠️  Some sections may be empty")
    
    return errors, warnings

def validate_reasoning(content):
    """Check reasoning file format."""
    errors = []
    warnings = []
    
    # Should contain source references
    if not re.search(r'S[12]\s*-\s*["\']', content):
        warnings.append("⚠️  Reasoning file should contain S1/S2 references")
    
    # Should contain "Content in Template" sections
    if not re.search(r'\*\*Content in Template\*\*:', content):
        warnings.append("⚠️  Reasoning file should reference template content")
    
    return errors, warnings

def validate_checklist(content):
    """Check checklist file format."""
    errors = []
    warnings = []
    
    # Should contain table with correct columns
    if '| ID |' not in content or '| Section |' not in content:
        errors.append("❌ Checklist missing required table columns")
    
    # Should have placeholder IDs
    placeholder_ids = re.findall(r'\[([A-Z_]+\d+)\]', content)
    if not placeholder_ids:
        warnings.append("⚠️  No placeholder IDs found in checklist")
    
    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_output.py <template_file> [reasoning_file] [checklist_file]")
        sys.exit(1)
    
    template_file = Path(sys.argv[1])
    reasoning_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    checklist_file = Path(sys.argv[3]) if len(sys.argv) > 3 else None
    
    all_errors = []
    all_warnings = []
    
    # Validate template
    if template_file.exists():
        template_content = template_file.read_text()
        errors, warnings = validate_template(template_content)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        print(f"\n📄 Validating {template_file.name}:")
        if errors:
            print("\n".join(errors))
        if warnings:
            print("\n".join(warnings))
        if not errors and not warnings:
            print("✅ Template file is valid")
    else:
        print(f"❌ Template file not found: {template_file}")
    
    # Validate reasoning
    if reasoning_file and reasoning_file.exists():
        reasoning_content = reasoning_file.read_text()
        errors, warnings = validate_reasoning(reasoning_content)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        print(f"\n📄 Validating {reasoning_file.name}:")
        if errors:
            print("\n".join(errors))
        if warnings:
            print("\n".join(warnings))
        if not errors and not warnings:
            print("✅ Reasoning file is valid")
    
    # Validate checklist
    if checklist_file and checklist_file.exists():
        checklist_content = checklist_file.read_text()
        errors, warnings = validate_checklist(checklist_content)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        print(f"\n📄 Validating {checklist_file.name}:")
        if errors:
            print("\n".join(errors))
        if warnings:
            print("\n".join(warnings))
        if not errors and not warnings:
            print("✅ Checklist file is valid")
    
    # Summary
    print(f"\n{'='*50}")
    if all_errors:
        print(f"❌ Found {len(all_errors)} error(s)")
        sys.exit(1)
    elif all_warnings:
        print(f"⚠️  Found {len(all_warnings)} warning(s)")
    else:
        print("✅ All files are valid!")

if __name__ == '__main__':
    main()

