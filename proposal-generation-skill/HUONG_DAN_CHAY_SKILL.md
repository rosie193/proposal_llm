# Hướng Dẫn Chạy Proposal Generation Skill

Hướng dẫn chi tiết cách setup và sử dụng Agent Skill để generate technical proposals từ Deal Transfer documents.

## Mục Lục

1. [Chuẩn Bị](#chuẩn-bị)
2. [Setup Skill](#setup-skill)
3. [Sử Dụng trong Claude Code](#sử-dụng-trong-claude-code)
4. [Sử Dụng trong Claude API](#sử-dụng-trong-claude-api)
5. [Sử Dụng trong Claude.ai (Web)](#sử-dụng-trong-claudeai-web)
6. [Test Skill](#test-skill)
7. [Troubleshooting](#troubleshooting)

---

## Chuẩn Bị

### Yêu Cầu

- Python 3.6+ (để chạy utility scripts)
- Thư viện Python: `pandas`, `openpyxl` (để đọc Excel)
- Claude account (Claude Code, Claude API, hoặc Claude.ai)

### Cài Đặt Dependencies

```bash
# Cài đặt pandas và openpyxl để đọc Excel files
pip install pandas openpyxl
```

---

## Setup Skill

### Bước 1: Copy Resources Cần Thiết

Skill cần các file reference sau đây. Nếu chưa có, copy từ project root:

```bash
# Từ thư mục project root
cd /home/tth193/Documents/01_LLM_193/Proposal_generation

# Copy các file reference vào skill directory
cp template_111.md proposal-generation-skill/TEMPLATE.md
cp standard_AI_modules.md proposal-generation-skill/STANDARD_MODULES.md
cp Deal_Transfer_Field_Names_Reference.md proposal-generation-skill/FIELD_NAMES_REFERENCE.md
```

**Lưu ý**: Các file này là **bắt buộc** vì skill sẽ reference chúng khi generate proposal:
- `TEMPLATE.md`: Cấu trúc proposal và hướng dẫn
- `STANDARD_MODULES.md`: Danh sách modules chuẩn để check
- `FIELD_NAMES_REFERENCE.md`: Tên các fields trong Deal Transfer để extract

### Bước 2: Kiểm Tra Cấu Trúc

Đảm bảo skill directory có cấu trúc đầy đủ:

```
proposal-generation-skill/
├── SKILL.md                    # ✅ Đã có - Main instructions
├── TEMPLATE.md                 # ⚠️  Cần copy
├── STANDARD_MODULES.md         # ⚠️  Cần copy
├── FIELD_NAMES_REFERENCE.md    # ⚠️  Cần copy
├── scripts/
│   ├── extract_deal_transfer.py    # ✅ Đã có
│   └── validate_output.py          # ✅ Đã có
└── README.md                   # ✅ Đã có
```

### Bước 3: Deploy Skill

Tùy theo môi trường bạn sử dụng Claude:

---

## Sử Dụng trong Claude Code

### Cách 1: Project-Specific Skill (Khuyên Dùng)

Đặt skill trong project để chia sẻ với team:

```bash
# Từ project root
mkdir -p .claude/skills
cp -r proposal-generation-skill .claude/skills/proposal-generation-skill
```

### Cách 2: User-Level Skill (Cá Nhân)

Đặt skill ở user level để dùng cho mọi project:

```bash
# Copy skill vào Claude skills directory
cp -r proposal-generation-skill ~/.claude/skills/proposal-generation-skill
```

### Sử Dụng Skill

Sau khi deploy, Claude sẽ tự động discover skill. Khi bạn chat với Claude và nói:

- ✅ "Generate proposal from Deal Transfer"
- ✅ "I have a Deal Transfer file"
- ✅ "Create proposal template"
- ✅ "Tôi có file Deal Transfer, hãy generate proposal"

Claude sẽ tự động:
1. **Load SKILL.md** (Level 2) để hiểu process
2. **Load TEMPLATE.md** khi cần cấu trúc (Level 3)
3. **Load STANDARD_MODULES.md** khi check modules (Level 3)
4. **Load FIELD_NAMES_REFERENCE.md** khi extract fields (Level 3)
5. **Chạy scripts** khi cần parse/validate

### Ví Dụ Sử Dụng

```
Bạn: Tôi có file Deal Transfer New_DT.xlsx, hãy generate proposal theo skill proposal-generation

[Attach file: New_DT.xlsx]

Claude: [Tự động detect skill và generate proposal]
```

---

## Sử Dụng trong Claude API

### Bước 1: Zip Skill Directory

```bash
cd proposal-generation-skill
zip -r ../proposal-generation-skill.zip .
cd ..
```

### Bước 2: Upload Skill qua API

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Upload skill
with open("proposal-generation-skill.zip", "rb") as f:
    skill = client.skills.create(
        name="proposal-generation",
        files=[f]
    )

print(f"Skill uploaded with ID: {skill.id}")
```

### Bước 3: Sử Dụng Skill trong Conversation

```python
# Sử dụng skill trong message
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=16000,
    tools=[{"type": "code_execution"}],
    container={
        "type": "code_execution",
        "skill_ids": ["proposal-generation"]  # Reference skill ID
    },
    messages=[{
        "role": "user",
        "content": "Generate proposal from this Deal Transfer file",
        # Attach Deal Transfer file here
    }]
)
```

**Lưu ý**: Tham khảo [Claude API Documentation](https://docs.anthropic.com/claude/reference/skills-create) để biết cách attach files.

---

## Sử Dụng trong Claude.ai (Web)

### Bước 1: Zip Skill Directory

```bash
cd proposal-generation-skill
zip -r ../proposal-generation-skill.zip .
cd ..
```

### Bước 2: Upload Skill

1. Vào [claude.ai](https://claude.ai)
2. Click vào avatar/profile → **Settings**
3. Vào tab **Features** → **Skills**
4. Click **Upload Skill**
5. Chọn file `proposal-generation-skill.zip`
6. Skill sẽ được upload và activate

### Bước 3: Sử Dụng

1. Mở conversation mới
2. Upload Deal Transfer Excel file
3. Nói: "Generate proposal from this Deal Transfer file"
4. Claude sẽ tự động detect và sử dụng skill

---

## Test Skill

### Test với Sample Deal Transfer

1. **Chuẩn bị file Deal Transfer**:
   - Excel file có 2 sheets: `Commercial` (S1) và `Technical` (S2)
   - Đảm bảo có đủ thông tin cần thiết

2. **Chạy Test**:
   ```
   Bạn: Generate proposal from Deal Transfer file [attach file]
   ```

3. **Kiểm Tra Output**:
   Skill sẽ generate 3 files:
   - `[Project_Name]_template.md`: Proposal content sạch
   - `[Project_Name]_reasoning.md`: Source references và logic
   - `[Project_Name]_checklist.md`: Items cần confirm từ presale

4. **Validate Output** (Optional):
   ```bash
   cd proposal-generation-skill
   python scripts/validate_output.py \
     [Project_Name]_template.md \
     [Project_Name]_reasoning.md \
     [Project_Name]_checklist.md
   ```

### Test Script Extract

Test script extract Deal Transfer:

```bash
cd proposal-generation-skill
python scripts/extract_deal_transfer.py /path/to/Deal_Transfer.xlsx
```

Script sẽ output JSON với:
- `sheets`: Danh sách sheets
- `S1`: Data từ Commercial sheet
- `S2`: Data từ Technical sheet

---

## Troubleshooting

### Skill Không Được Detect

**Vấn đề**: Claude không tự động detect skill

**Giải pháp**:
1. Kiểm tra skill đã được copy đúng chưa:
   ```bash
   ls -la .claude/skills/proposal-generation-skill/
   # hoặc
   ls -la ~/.claude/skills/proposal-generation-skill/
   ```

2. Đảm bảo `SKILL.md` có YAML frontmatter đúng:
   ```yaml
   ---
   name: proposal-generation
   description: Generate technical proposals...
   ---
   ```

3. Restart Claude Code nếu cần

### Missing Resources

**Vấn đề**: Skill báo lỗi thiếu TEMPLATE.md, STANDARD_MODULES.md, etc.

**Giải pháp**:
```bash
# Copy các file reference cần thiết
cp template_111.md proposal-generation-skill/TEMPLATE.md
cp standard_AI_modules.md proposal-generation-skill/STANDARD_MODULES.md
cp Deal_Transfer_Field_Names_Reference.md proposal-generation-skill/FIELD_NAMES_REFERENCE.md
```

### Script Extract Không Chạy

**Vấn đề**: Script extract_deal_transfer.py báo lỗi

**Giải pháp**:
1. Kiểm tra Python và dependencies:
   ```bash
   python3 --version  # Phải >= 3.6
   pip install pandas openpyxl
   ```

2. Kiểm tra file Excel có đúng format:
   - Sheet names: `Commercial` và `Technical` (hoặc `S1` và `S2`)
   - File không bị corrupt

3. Kiểm tra quyền execute:
   ```bash
   chmod +x scripts/extract_deal_transfer.py
   ```

### Output Không Đúng Format

**Vấn đề**: Generated proposal không đúng format

**Giải pháp**:
1. Validate output:
   ```bash
   python scripts/validate_output.py template.md reasoning.md checklist.md
   ```

2. Kiểm tra các file reference đã đầy đủ chưa
3. Xem lại SKILL.md để đảm bảo process đúng

### Claude Không Hiểu Request

**Vấn đề**: Claude không trigger skill khi bạn nói về proposal

**Giải pháp**:
1. Sử dụng keywords rõ ràng:
   - ✅ "Generate proposal from Deal Transfer"
   - ✅ "Create proposal template"
   - ❌ "Make a document" (quá mơ hồ)

2. Attach Deal Transfer file khi request

3. Explicit reference skill name nếu cần:
   ```
   "Sử dụng skill proposal-generation để generate proposal từ file này"
   ```

---

## Workflow Đầy Đủ

### 1. Setup Lần Đầu

```bash
# 1. Cài dependencies
pip install pandas openpyxl

# 2. Copy resources
cd /home/tth193/Documents/01_LLM_193/Proposal_generation
cp template_111.md proposal-generation-skill/TEMPLATE.md
cp standard_AI_modules.md proposal-generation-skill/STANDARD_MODULES.md
cp Deal_Transfer_Field_Names_Reference.md proposal-generation-skill/FIELD_NAMES_REFERENCE.md

# 3. Deploy skill (Claude Code)
mkdir -p .claude/skills
cp -r proposal-generation-skill .claude/skills/proposal-generation-skill
```

### 2. Sử Dụng Hàng Ngày

```
1. Mở Claude Code
2. Attach Deal Transfer Excel file
3. Nói: "Generate proposal from this Deal Transfer"
4. Claude generate 3 files output
5. Review và validate nếu cần
```

### 3. Update Skill

Khi có thay đổi:
- Update `SKILL.md` nếu process thay đổi
- Update `TEMPLATE.md` nếu template structure thay đổi
- Update `STANDARD_MODULES.md` nếu có modules mới
- Update `FIELD_NAMES_REFERENCE.md` nếu Deal Transfer format thay đổi
- Restart Claude Code để load changes

---

## Tài Liệu Tham Khảo

- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)
- [Claude API Skills Documentation](https://docs.anthropic.com/claude/reference/skills-create)

---

## FAQ

**Q: Skill có tự động load tất cả resources không?**  
A: Không. Skill sử dụng **progressive disclosure** - chỉ load khi cần, giúp tiết kiệm tokens.

**Q: Có thể customize skill không?**  
A: Có. Chỉnh sửa `SKILL.md` để thay đổi process, hoặc các file reference để update template/modules.

**Q: Skill có thể dùng với Knowledge Base không?**  
A: Có. Skill được thiết kế để integrate với KB references. Xem SKILL.md section "Using Resources".

**Q: Làm sao để share skill với team?**  
A: Đặt skill trong `.claude/skills/` ở project root và commit vào Git. Team members sẽ có skill khi clone project.

**Q: Có thể dùng nhiều skills cùng lúc không?**  
A: Có. Claude có thể sử dụng multiple skills trong cùng một conversation.




