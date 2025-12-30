# Prompt: Generate Technical Proposal from Deal Transfer

## Instruction

You are a presale engineer tasked with generating a technical proposal based on a Deal Transfer document. Use the following resources:

1. **Deal Transfer document** (Excel file with Commercial Sheet S1 and Technical Sheet S2)
2. **Template**: `template_hihi.md` - Contains the structure and guidance for filling proposal sections
3. **Standard AI Modules**: `standard_AI_modules.md` - Reference list of standard modules available
4. **Knowledge Base (KB)**: Access to viAct_Proposal and DOCUMENT KBs for reference

## Task

Generate a complete technical proposal file named `[Project_Name]_template.md` following the structure in `template_hihi.md`. Fill in ALL sections with information extracted and derived from the Deal Transfer document.

## Process

### Step 1: Extract Information from Deal Transfer

Read the Deal Transfer Excel file and extract:
- **Commercial Sheet (S1)**: All fields using exact field names from `Deal_Transfer_Field_Names_Reference.md`
- **Technical Sheet (S2)**: All fields using exact field names from `Deal_Transfer_Field_Names_Reference.md`

### Step 2: Generate Proposal Following Template Structure

Fill in each section of `template_hihi.md` using the following logic:

#### 1. COVER PAGE
- **Proposal Title**: Format: "AI-Powered Video Analytics Solution Proposal for [Customer Name]" OR derive from S1
- **Client Name**: Extract from S1 - "Customer overview (short introduction about customer business)"
- **Duration**: From S1 - "If real project, expected timeline (including tender if any)"

#### 2. PROJECT REQUIREMENT STATEMENT
- **Project**: Derive from S1 - "Current Pain Points of end customer" → Convert to positive objective format
- **Project Owner**: From S1 - "Customer overview"
- **Work Scope**: Format: "[Deployment method] AI system to [Primary objective]" (combine S2 deployment method + S1 pain points)
- **Project Duration**: From S1 - "If real project, expected timeline"
- **Camera Number**: Extract from S1 - "If VA: camera status & scope"
- **AI Modules**: From S2 - "List of VA use cases" → Convert to module names using `standard_AI_modules.md`
- **Project Objectives**: Convert S1 pain points to positive objectives

#### 3. SCOPE OF WORK
- **viAct Responsibilities**: Standard (Software, Camera integration) + modules from S2
- **Client Responsibilities**: Based on S1 - "If VA: camera status & scope" (check if cameras exist) and S2 deployment method

#### 4. SYSTEM ARCHITECTURE
- **Deployment Method**: From S2 - "Specific HW/SW requirements (deployment method)?" → Determine: On-Premise / Cloud / Hybrid / Edge
- **Components**: Extract from S1 camera info, S2 deployment method, S2 integrations
- **Architecture Description**: Describe data flow based on deployment method

#### 5. SYSTEM REQUIREMENTS
- **Network**: Calculate bandwidth (12 Mbps × camera count if on-premise/hybrid)
- **Camera**: Standard specs + check S2 - "Can client camera provide RTSP link?"
- **Workstation**: Estimate based on camera count + modules (use standard specs)
- **Additional Equipment**: From S2 - "Any IoT integration?" + "Any customized HW / IoT?"

#### 6. IMPLEMENTATION PLAN (TIMELINE)
- **T0**: Project award date
- **T1**: Hardware deployment (1-2 weeks if cameras exist, 2-4 weeks if new)
- **T2**: Software deployment (4-6 weeks standard, 6-8 weeks per custom module)
- **T3**: Integration & UAT (2-4 weeks)
- Calculate total based on S1 timeline + S2 custom modules

#### 7. PROPOSED MODULES & FUNCTIONAL DESCRIPTION
For EACH module in S2 - "List of VA use cases":
1. **Check if Standard**: Look up in `standard_AI_modules.md`
2. **If Standard**: 
   - Module Name: Use standard name
   - Purpose: Search KB or use standard description
   - Alert Logic: From KB or standard template
   - Preconditions: Standard (5-10 meters, or 3-5 meters for detailed detection)
3. **If Custom**: 
   - Module Name: Create descriptive name from use case
   - Purpose: Extract from S2 - "Any customized AI use cases"
   - Alert Logic: Extract from custom use case description
   - Preconditions: Standard template (5-10 meters) unless specified
   - Client Data Requirements: "Request: Provide [object type] images for model training"

#### 8. USER INTERFACE & REPORTING
- **Alerts**: From S2 - "How do they want to alert operators on-site?"
- **Dashboard**: From S2 - "Any customized dashboard?"
- **Reports**: Extract reporting requirements from S2 - "Any customized dashboard?"

### Step 3: Handle Missing Information

If any information is missing from Deal Transfer:
1. **Make reasonable estimates** based on:
   - Standard viAct practices
   - Similar projects in KB
   - Industry standards
2. **Mark with placeholder**: Use format `[PLACEHOLDER_ID]` where ID is unique (e.g., `[NETWORK_001]`, `[TIMELINE_002]`)
3. **Create Checklist**: List all placeholders in a separate file `[Project_Name]_checklist.md`

### Step 4: Create Checklist File

For each placeholder created, add entry to checklist:

```markdown
## Items Requiring Confirmation

| ID | Section | Item | Question/What to Confirm | Source Reference |
|----|---------|------|--------------------------|------------------|
| NETWORK_001 | 5. SYSTEM REQUIREMENTS | External Bandwidth | What is the required external bandwidth for remote access? | S2 - "Stable internet connection?" not specified |
| TIMELINE_002 | 6. IMPLEMENTATION PLAN | T1 Duration | How many weeks for hardware deployment? Customer has cameras but need to confirm integration time | S1 - Camera status unclear |
```

### Step 5: Quality Check

Before finalizing, verify:
- ✅ All sections from template_hihi.md are filled
- ✅ No sections left completely empty
- ✅ All references to S1/S2 use exact field names
- ✅ Module names match `standard_AI_modules.md` when standard
- ✅ Timeline calculations are logical (consider standard vs custom modules)
- ✅ Architecture matches deployment method
- ✅ Responsibilities are clearly divided

## Output Files

1. **`[Project_Name]_template.md`**: Complete proposal following template structure
2. **`[Project_Name]_checklist.md`**: List of items requiring confirmation with unique IDs

## Example Placeholder IDs

Use descriptive prefixes:
- `NETWORK_001`, `NETWORK_002` - Network requirements
- `TIMELINE_001`, `TIMELINE_002` - Timeline questions
- `ARCH_001` - Architecture clarifications
- `MODULE_001` - Module-specific questions
- `DASHBOARD_001` - Dashboard requirements
- `INTEGRATION_001` - Integration questions

## Important Rules

1. **Always extract from Deal Transfer first** - Use exact field names
2. **Never leave sections completely empty** - Make best estimate or use placeholder
3. **Use standard module names** when available in `standard_AI_modules.md`
4. **Convert pain points to objectives** - Don't copy directly
5. **Calculate timeline realistically** - Consider standard vs custom modules
6. **Be specific** - Avoid vague statements, use concrete numbers and details
7. **Maintain consistency** - Camera numbers, module counts should be consistent across sections

