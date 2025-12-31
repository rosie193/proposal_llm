# Proposal Generation Skill

Agent Skill để generate technical proposals từ Deal Transfer documents.

> 📖 **Xem hướng dẫn chi tiết**: [HUONG_DAN_CHAY_SKILL.md](./HUONG_DAN_CHAY_SKILL.md) - Hướng dẫn đầy đủ cách setup và chạy skill

## Quick Start

```bash
# Chạy script setup tự động
./setup.sh

# Hoặc setup thủ công (xem HUONG_DAN_CHAY_SKILL.md)
```

## Cấu Trúc

```
proposal-generation-skill/
├── SKILL.md                    # Main instructions (Level 2)
├── TEMPLATE.md                 # Template reference (Level 3)
├── STANDARD_MODULES.md         # Standard modules list (Level 3)
├── FIELD_NAMES_REFERENCE.md    # Deal Transfer field names (Level 3)
├── scripts/
│   ├── extract_deal_transfer.py    # Extract from Excel
│   └── validate_output.py          # Validate output format
└── README.md                   # This file
```

## Setup

### 1. Copy Resources

```bash
# Từ project root
cp template_111.md proposal-generation-skill/TEMPLATE.md
cp standard_AI_modules.md proposal-generation-skill/STANDARD_MODULES.md
cp Deal_Transfer_Field_Names_Reference.md proposal-generation-skill/FIELD_NAMES_REFERENCE.md
```

### 2. Tạo Scripts (Optional)

Scripts đã được tạo sẵn trong `scripts/` directory.

### 3. Deploy Skill

#### Claude Code:
```bash
# Copy skill vào Claude Code skills directory
cp -r proposal-generation-skill ~/.claude/skills/proposal-generation-skill
# Hoặc cho project-specific:
cp -r proposal-generation-skill .claude/skills/proposal-generation-skill
```

#### Claude API:
```bash
# Zip skill directory
cd proposal-generation-skill
zip -r ../proposal-generation-skill.zip .
cd ..

# Upload via API (see API documentation)
```

#### Claude.ai:
1. Zip skill directory
2. Vào Settings → Features → Skills
3. Upload zip file

## Sử Dụng

### Trong Claude Code:
Claude tự động discover skill. Khi user nói:
- "Generate proposal from Deal Transfer"
- "I have a Deal Transfer file"
- "Create proposal template"

Claude sẽ tự động sử dụng skill này.

### Trong Claude API:
```python
container = {
    "type": "code_execution",
    "skill_ids": ["proposal-generation"]
}
```

### Trong Claude.ai:
Skill tự động available sau khi upload.

## Progressive Disclosure

Skill sử dụng progressive disclosure:

1. **Level 1 (Startup)**: Metadata từ SKILL.md frontmatter
2. **Level 2 (Triggered)**: SKILL.md được load khi skill được trigger
3. **Level 3 (As Needed)**: Resources chỉ được load khi cần:
   - TEMPLATE.md khi cần template structure
   - STANDARD_MODULES.md khi check modules
   - FIELD_NAMES_REFERENCE.md khi extract fields
   - Scripts khi cần parse/validate

## Testing

Test skill với sample Deal Transfer:
```bash
# Trong Claude Code hoặc API
# Provide sample Deal Transfer Excel file
# Ask: "Generate proposal from this Deal Transfer"
# Verify output: template.md, reasoning.md, checklist.md
```

## Maintenance

- Update SKILL.md khi có thay đổi process
- Update TEMPLATE.md khi template structure thay đổi
- Update STANDARD_MODULES.md khi có modules mới
- Update FIELD_NAMES_REFERENCE.md khi Deal Transfer format thay đổi

## References

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)

