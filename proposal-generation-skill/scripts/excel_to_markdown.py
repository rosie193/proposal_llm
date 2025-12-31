#!/usr/bin/env python3
"""
Convert Excel file to Markdown format with sheet names.

Usage:
    python excel_to_markdown.py <excel_file> [output_file]

Output:
    Markdown file with all sheets, each sheet name as a header
"""

import pandas as pd
import sys
from pathlib import Path

def excel_to_markdown(excel_path, output_path=None):
    """Convert Excel file to Markdown format with sheet names."""
    try:
        xls = pd.ExcelFile(excel_path)
        
        if output_path is None:
            output_path = Path(excel_path).stem + '.md'
        
        markdown_content = []
        
        # Add title
        markdown_content.append(f"# {Path(excel_path).stem}\n")
        markdown_content.append(f"*Converted from Excel file*\n\n")
        markdown_content.append("---\n\n")
        
        # Process each sheet
        for sheet_name in xls.sheet_names:
            # Add sheet name as header
            markdown_content.append(f"## Sheet: {sheet_name}\n\n")
            
            # Read sheet
            df = pd.read_excel(excel_path, sheet_name=sheet_name)
            
            if df.empty:
                markdown_content.append("*Sheet is empty*\n\n")
            else:
                # Convert DataFrame to Markdown table
                markdown_table = df.to_markdown(index=False, tablefmt='github')
                markdown_content.append(markdown_table)
                markdown_content.append("\n\n")
            
            # Add separator between sheets
            markdown_content.append("---\n\n")
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"✓ Converted {len(xls.sheet_names)} sheets to {output_path}")
        return output_path
        
    except FileNotFoundError:
        print(f"✗ Error: File not found: {excel_path}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: excel_to_markdown.py <excel_file> [output_file]")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    excel_to_markdown(excel_file, output_file)

