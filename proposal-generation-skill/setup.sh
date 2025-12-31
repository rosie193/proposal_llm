#!/bin/bash
# Setup script for Proposal Generation Skill
# This script copies required resources and sets up the skill directory

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILL_DIR="$SCRIPT_DIR"

echo -e "${GREEN}=== Setup Proposal Generation Skill ===${NC}\n"

# Check if required source files exist
echo -e "${YELLOW}Checking source files...${NC}"

MISSING_FILES=0

if [ ! -f "$PROJECT_ROOT/template_111.md" ]; then
    echo -e "${RED}❌ Missing: template_111.md${NC}"
    MISSING_FILES=1
else
    echo -e "${GREEN}✅ Found: template_111.md${NC}"
fi

if [ ! -f "$PROJECT_ROOT/standard_AI_modules.md" ]; then
    echo -e "${RED}❌ Missing: standard_AI_modules.md${NC}"
    MISSING_FILES=1
else
    echo -e "${GREEN}✅ Found: standard_AI_modules.md${NC}"
fi

if [ ! -f "$PROJECT_ROOT/Deal_Transfer_Field_Names_Reference.md" ]; then
    echo -e "${RED}❌ Missing: Deal_Transfer_Field_Names_Reference.md${NC}"
    MISSING_FILES=1
else
    echo -e "${GREEN}✅ Found: Deal_Transfer_Field_Names_Reference.md${NC}"
fi

if [ $MISSING_FILES -eq 1 ]; then
    echo -e "\n${RED}Error: Some required source files are missing.${NC}"
    echo -e "Please ensure these files exist in the project root:"
    echo -e "  - template_111.md"
    echo -e "  - standard_AI_modules.md"
    echo -e "  - Deal_Transfer_Field_Names_Reference.md"
    exit 1
fi

echo ""

# Copy resources
echo -e "${YELLOW}Copying resources...${NC}"

cp "$PROJECT_ROOT/template_111.md" "$SKILL_DIR/TEMPLATE.md"
echo -e "${GREEN}✅ Copied: TEMPLATE.md${NC}"

cp "$PROJECT_ROOT/standard_AI_modules.md" "$SKILL_DIR/STANDARD_MODULES.md"
echo -e "${GREEN}✅ Copied: STANDARD_MODULES.md${NC}"

cp "$PROJECT_ROOT/Deal_Transfer_Field_Names_Reference.md" "$SKILL_DIR/FIELD_NAMES_REFERENCE.md"
echo -e "${GREEN}✅ Copied: FIELD_NAMES_REFERENCE.md${NC}"

# Check Python dependencies
echo -e "\n${YELLOW}Checking Python dependencies...${NC}"

if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo -e "${RED}❌ Python not found. Please install Python 3.6+${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Found: $PYTHON_CMD${NC}"

# Check if pandas and openpyxl are installed
if $PYTHON_CMD -c "import pandas" 2>/dev/null; then
    echo -e "${GREEN}✅ pandas is installed${NC}"
else
    echo -e "${YELLOW}⚠️  pandas not found. Installing...${NC}"
    pip install pandas openpyxl
    echo -e "${GREEN}✅ Installed pandas and openpyxl${NC}"
fi

# Make scripts executable
echo -e "\n${YELLOW}Setting script permissions...${NC}"
chmod +x "$SKILL_DIR/scripts/extract_deal_transfer.py"
chmod +x "$SKILL_DIR/scripts/validate_output.py"
echo -e "${GREEN}✅ Scripts are executable${NC}"

# Summary
echo -e "\n${GREEN}=== Setup Complete! ===${NC}\n"

echo -e "Skill directory structure:"
echo -e "  ${SKILL_DIR}/"
echo -e "  ├── SKILL.md ✅"
echo -e "  ├── TEMPLATE.md ✅"
echo -e "  ├── STANDARD_MODULES.md ✅"
echo -e "  ├── FIELD_NAMES_REFERENCE.md ✅"
echo -e "  ├── scripts/"
echo -e "  │   ├── extract_deal_transfer.py ✅"
echo -e "  │   └── validate_output.py ✅"
echo -e "  └── README.md ✅"

echo -e "\n${YELLOW}Next steps:${NC}"
echo -e "1. For Claude Code (project-specific):"
echo -e "   ${GREEN}mkdir -p .claude/skills${NC}"
echo -e "   ${GREEN}cp -r proposal-generation-skill .claude/skills/proposal-generation-skill${NC}"
echo -e ""
echo -e "2. For Claude Code (user-level):"
echo -e "   ${GREEN}cp -r proposal-generation-skill ~/.claude/skills/proposal-generation-skill${NC}"
echo -e ""
echo -e "3. For Claude.ai (web):"
echo -e "   ${GREEN}cd proposal-generation-skill && zip -r ../proposal-generation-skill.zip . && cd ..${NC}"
echo -e "   Then upload via Settings → Features → Skills"
echo -e ""
echo -e "See HUONG_DAN_CHAY_SKILL.md for detailed instructions."

