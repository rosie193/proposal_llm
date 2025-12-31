# Quick Start - Proposal Generation Skill

Hướng dẫn nhanh để bắt đầu sử dụng skill.

## ⚡ Setup Nhanh (1 phút)

```bash
# 1. Chạy script setup tự động
cd proposal-generation-skill
./setup.sh

# 2. Deploy cho Claude Code (project-specific)
mkdir -p ../.claude/skills
cp -r . ../.claude/skills/proposal-generation-skill
```

## 🚀 Sử Dụng

### Trong Claude Code:

1. Mở Claude Code
2. Attach file Deal Transfer Excel
3. Nói: **"Generate proposal from this Deal Transfer"**
4. Claude sẽ tự động generate 3 files:
   - `[Project_Name]_template.md`
   - `[Project_Name]_reasoning.md`
   - `[Project_Name]_checklist.md`

### Trong Claude.ai (Web):

1. Zip skill: `cd proposal-generation-skill && zip -r ../proposal-generation-skill.zip .`
2. Upload: Settings → Features → Skills → Upload
3. Attach Deal Transfer file và request: "Generate proposal"

## 📋 Requirements

- Python 3.6+ với pandas, openpyxl
- File Deal Transfer Excel với 2 sheets: `Commercial` và `Technical`

## ❓ Troubleshooting

**Skill không được detect?**
- Kiểm tra skill đã copy vào `.claude/skills/` chưa
- Restart Claude Code

**Thiếu resources?**
- Chạy `./setup.sh` để copy các file cần thiết

**Xem hướng dẫn đầy đủ**: [HUONG_DAN_CHAY_SKILL.md](./HUONG_DAN_CHAY_SKILL.md)

