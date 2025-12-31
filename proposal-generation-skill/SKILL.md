---
name: proposal-generation
description: Generate technical proposals from Deal Transfer Excel files and Knowledge base. Use when user provides Deal Transfer document or asks to generate proposal. Creates template, reasoning, and checklist files following viAct proposal structure.
---

# Proposal Generation Skill

## Overview

This skill generates technical proposals based on Deal Transfer documents (Excel files with Commercial Sheet S1 and Technical Sheet S2) and Knowledge Base references. It creates three output files: a clean proposal template, detailed reasoning documentation, and a checklist for presale confirmation.

## Resources Available

This skill includes the following resources (loaded as needed):

- **TEMPLATE.md**: Proposal structure and guidance - Contains the complete template with Source/Guidance for each section
- **STANDARD_MODULES.md**: List of standard AI modules - Reference for checking if a module is standard or custom
- **FIELD_NAMES_REFERENCE.md**: Deal Transfer field names reference - Exact field names from S1 and S2 sheets
- **scripts/extract_deal_transfer.py**: Utility script to extract and parse Deal Transfer Excel files
- **scripts/validate_output.py**: Script to validate generated proposal format

## When to Use This Skill

Use this skill when:
- User provides a Deal Transfer Excel file
- User asks to generate a technical proposal
- User mentions "proposal", "Deal Transfer", "S1", "S2"
- User needs proposal template, reasoning, or checklist files

## Process

### Step 1: Extract Information from Deal Transfer

Read the Deal Transfer Excel file and extract:
- **Commercial Sheet (S1)**: All fields using field names from FIELD_NAMES_REFERENCE.md
- **Technical Sheet (S2)**: All fields using field names from FIELD_NAMES_REFERENCE.md

**How to extract:**
1. Use Python pandas to read Excel: `pd.read_excel(file, sheet_name='Commercial')` and `sheet_name='Technical'`
2. Or use the utility script: `python scripts/extract_deal_transfer.py <excel_file>`
3. Reference FIELD_NAMES_REFERENCE.md for field names 

### Step 2: Generate Proposal Content (Template File)

Fill in each section following the structure in **TEMPLATE.md**. Read TEMPLATE.md to understand the structure and Source/Guidance for each section.

**IMPORTANT**: The `[Project_Name]_template.md` file should contain:
- ✅ **ONLY** the actual proposal content (text, numbers, descriptions)
- ✅ Clean, professional proposal language
- ✅ **Estimated values with placeholder IDs**: Format `[Estimated Value] [PLACEHOLDER_ID]`
  - Example: `30 Mbps [NETWORK_001]` (estimated value first, then placeholder ID)
  - This allows presale to see the estimate and confirm/update via checklist
- ❌ **NO** source references (e.g., "S2 - Field name")
- ❌ **NO** reasoning explanations (e.g., "Based on KB...", "Logic: ...")
- ❌ **NO** mapping details (e.g., "Extracted from...", "Calculated as...")

### Step 3: Generate Reasoning File

Create `[Project_Name]_reasoning.md` with detailed source references and logic for EACH section.

**IMPORTANT**: The reasoning file should contain:
- ✅ Source references (S1/S2 field names from FIELD_NAMES_REFERENCE.md)
- ✅ Mapping logic and calculations
- ✅ KB references used 
- ✅ Reasoning for estimates
- ✅ Alternative options considered

**Format for each section:**
```markdown
## [Section Name]

#### [Item Name]
**Content in Template**: [What appears in template file]
**Source**: S1/S2 - "[Field Name]" → [Extracted value]
**Logic**: [How value was derived]
**KB Reference**: [If applicable]
**Placeholder ID**: [If applicable]
**Reason for Placeholder**: [Why placeholder was needed]
```

### Step 4: Handle Missing/Unclear Information

If any information is missing from Deal Transfer:
1. **Make reasonable estimates** based on:
   - Standard viAct practices
   - Similar projects in KB
   - Industry standards
2. **Format in Template**: Use format `[Estimated Value] [PLACEHOLDER_ID]` where:
   - Estimated Value: The specific estimated number/text (e.g., `30 Mbps`, `T0 + 2 weeks`, `Intel Core i7-14700K`)
   - PLACEHOLDER_ID: Unique ID (e.g., `[NETWORK_001]`, `[TIMELINE_002]`)
   - Example: `30 Mbps [NETWORK_001]` (estimated value shown first, then placeholder ID)
3. **Add to both files**:
   - Template file: Show estimated value with placeholder ID (e.g., `30 Mbps [NETWORK_001]`)
   - Reasoning file: Document the estimated value, why it was estimated, and what needs confirmation
   - Checklist file: Add entry with the estimated value for presale to confirm/update

### Step 5: Create Checklist File

For each placeholder created, add entry to checklist:

```markdown
## Items Requiring Confirmation

| ID | Section | Item | Content estimated in template outline | Presale's Answer |
|----|---------|------|-----------------------------------------------------|-------------------------|
| NETWORK_001 | 5. SYSTEM REQUIREMENTS | External Bandwidth | 30 Mbps (estimated for remote access) | |
| TIMELINE_002 | 6. IMPLEMENTATION PLAN | T1 Duration | T0 + 2 weeks (estimated, customer has cameras) | |
```

### Step 6: Quality Check

Before finalizing, verify:

**For Template File:**
- ✅ All sections from TEMPLATE.md are filled
- ✅ No sections left completely empty
- ✅ Clean proposal language (no source references visible)
- ✅ Placeholder IDs are present for uncertain items
- ✅ Module names match STANDARD_MODULES.md when standard
- ✅ Timeline calculations are logical (consider standard vs custom modules)
- ✅ Architecture matches deployment method
- ✅ Responsibilities are clearly divided
- ✅ Consistent numbers across sections (camera count, module count, etc.)

**For Reasoning File:**
- ✅ Every section has corresponding reasoning entry
- ✅ All S1/S2 references use field names from FIELD_NAMES_REFERENCE.md
- ✅ All KB references are documented
- ✅ All calculations are shown
- ✅ All placeholders are explained

**For Checklist File:**
- ✅ All placeholders from template are listed
- ✅ Estimated values are clearly shown
- ✅ Format matches required structure

**Validation:**
Run `python scripts/validate_output.py` to check output format if needed.

## Output Files

Generate three files:

1. **`[Project_Name]_template.md`**: Clean proposal content ready for use
   - Contains: Proposal text, numbers, descriptions, placeholder IDs
   - Purpose: Direct use in proposal creation
   - Format: NO source references, NO reasoning

2. **`[Project_Name]_reasoning.md`**: Detailed source references and logic
   - Contains: S1/S2 field references, KB references, calculations, mapping logic
   - Purpose: Documentation of how content was derived, for review and updates

3. **`[Project_Name]_checklist.md`**: Items requiring presale confirmation
   - Contains: Placeholder IDs, estimated values, blank column for presale answers
   - Purpose: Track items needing confirmation from presale team

## Using Resources

- **When you need template structure**: Read `TEMPLATE.md` to understand section structure and Source/Guidance
- **When checking if module is standard**: Read `STANDARD_MODULES.md` and search for module name
- **When extracting Deal Transfer fields**: Reference `FIELD_NAMES_REFERENCE.md` for exact field names
- **When parsing Excel**: Use `python scripts/extract_deal_transfer.py <file>` if needed
- **When validating output**: Run `python scripts/validate_output.py` to check format

## Important Rules

### Content Separation Rules

1. **Template File**:
   - ✅ Contains ONLY proposal content (clean, professional)
   - ✅ Show estimated values with placeholder IDs: Format `[Estimated Value] [PLACEHOLDER_ID]`
   - ❌ NO source references
   - ❌ NO reasoning text
   - ❌ NO KB references

2. **Reasoning File**:
   - ✅ Contains ALL source references (S1/S2 field names)
   - ✅ Contains ALL mapping logic and calculations
   - ✅ Contains ALL KB references used
   - ✅ Explains why placeholders were created

3. **Checklist File**:
   - ✅ Lists all placeholders with estimated values
   - ✅ Format: ID | Section | Item | Content estimated | presale's Answer

### Content Generation Rules

1. **Always extract from Deal Transfer first** - Use exact field names from FIELD_NAMES_REFERENCE.md
2. **Never leave sections completely empty** - Make best estimate and use placeholder
3. **Use standard module names** when available in STANDARD_MODULES.md
4. **Convert pain points/VA use cases to AI modules** - Map each use case to specific module
5. **Calculate timeline realistically** - Consider standard vs custom modules
6. **Be specific** - Avoid vague statements, use concrete numbers and details
7. **Maintain consistency** - Camera numbers, module counts should be consistent across sections
8. **Document everything in reasoning file** - Even obvious mappings should be documented for traceability

## Example Placeholder IDs

Use descriptive prefixes:
- `NETWORK_001`, `NETWORK_002` - Network requirements
- `TIMELINE_001`, `TIMELINE_002` - Timeline questions
- `ARCH_001` - Architecture clarifications
- `MODULE_001` - Module-specific questions
- `DASHBOARD_001` - Dashboard requirements
- `INTEGRATION_001` - Integration questions

