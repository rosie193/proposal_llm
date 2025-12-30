# Technical Proposal Template - Common Structure

> **Purpose**: This template outlines the COMMON structure that appears in all technical proposals. Use this as an outline to fill in variable information from Deal Transfer documents and customer requirements.

> **Note**: This template focuses on variable sections only. Fixed sections (company introduction, standard disclaimers, etc.) are excluded.

---

## 1. PROJECT REQUIREMENT STATEMENT

### Common Items (Always Present):

#### 1.1 Project Information
```
Project: [Project Name]
Project Owner: [Customer Company Name]
Project Duration: [X years/months]
Camera Number: [X] cameras
AI Modules: [List of primary modules]
```

**Source from Deal Transfer:**
- Project Name: From Deal Transfer → Commercial → "Customer overview" + "Solutions they are looking to implement"
- Project Owner: From Deal Transfer → Commercial → "Customer overview"
- Duration: From Deal Transfer → Commercial → "Expected timeline" OR Technical → "Project duration"
- Camera Number: From Deal Transfer → Technical → "How many cameras"
- AI Modules: From Deal Transfer → Technical → "List of VA use cases" → **Convert use cases to module names**

#### 1.2 Project Objectives / Work Scope Statement
```
Primary Objective:
- [Main objective - derived from pain points]

Secondary Objectives:
- [Objective 2]
- [Objective 3]
```

**Source from Deal Transfer:**
- **Derive from**: Deal Transfer → Commercial → "Current Pain Points"
- **Logic**: Convert pain points into objectives
  - Example: Pain point "Manual counting is inaccurate" → Objective "Automate counting with AI"
  - Example: Pain point "Safety incidents not detected in time" → Objective "Real-time safety monitoring"

**Note**: Do NOT include Stakeholders, Decision Makers, or detailed customer profile in proposal (these are internal Deal Transfer info only)

---

## 2. WORK SCOPE

### Common Items (Always Present):

#### 2.1 Scope of Work - Responsibilities

**viAct Responsibilities:**
- Software: License, maintenance, support
- AI Modules: [List modules to be provided]
- Camera Integration: [Integration method]
- [Additional responsibilities based on project]

**Customer Responsibilities:**
- Hardware: [Procurement / Installation / Configuration / Maintenance]
- [Additional responsibilities based on project]

**Source from Deal Transfer:**
- **viAct scope**: From Deal Transfer → Technical → "Deployment method" + "AI use cases"
- **Customer scope**: From Deal Transfer → Technical → "Do they have cameras?" + "Do we handle HW?"
- **Logic**: 
  - If customer has cameras → Customer handles HW, viAct handles software
  - If new installation → May need to specify who handles what
  - If on-premise → Customer may need to provide server/workstation

#### 2.2 Solution Overview (Optional - if needed for clarity)
**What will be implemented:**
- [Solution component 1]
- [Solution component 2]

**Source from Deal Transfer:**
- From Deal Transfer → Commercial → "Solutions they are looking to implement"
- **Convert**: Technical requirements → Solution description

---

## 3. SYSTEM ARCHITECTURE

### Common Items (Always Present):

#### 3.1 Architecture Type
- [ ] On-Premise
- [ ] Cloud
- [ ] Hybrid
- [ ] Edge Processing

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Deployment method" OR "HW/SW requirements"
- **Logic**: 
  - "On-premise" → On-Premise architecture
  - "Cloud" → Cloud architecture
  - "Local processing at each station" → Edge Processing
  - "Unstable internet" → On-Premise or Edge

#### 3.2 System Components

**Cameras:**
- Existing: [Number, type if known]
- New: [Number, specifications]
- Total: [Total count]

**Processing:**
- AI Workstation: [Location - Central / Edge / Per site]
- Dashboard Server: [Location]

**Storage:**
- Video Retention: [Duration]
- Storage Location: [Customer / Partner / viAct]

**Source from Deal Transfer:**
- Cameras: From Deal Transfer → Technical → "How many cameras" + "Do they have cameras installed?"
- Processing: From Deal Transfer → Technical → "Deployment method" + "Internet connection stability"
- Storage: From Deal Transfer → Technical → "Data retention" OR Commercial → "Storage requirements"

#### 3.3 Integration Points (If Applicable)

**VMS Integration:**
- VMS System: [Brand/Type]
- Integration Method: [RTSP / API / SDK]

**Other Integrations:**
- [Integration type]: [Method]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "VMS integration" OR "Camera type" (RTSP capability)
- From Deal Transfer → Technical → "Any IoT integration" OR "Access control integration"

#### 3.4 Architecture Diagram Description
- [Brief description of how components connect]

**Source from Deal Transfer:**
- **Derive from**: All technical requirements combined
- **Logic**: Based on deployment method, number of sites, camera locations

---

## 4. SYSTEM REQUIREMENT

### Common Items (Always Present):

#### 4.1 Hardware Requirements

**AI Inference Workstation:**
- CPU: [Specification]
- GPU: [Specification]
- RAM: [Specification]
- Storage: [Specification]
- Operating System: [OS]
- Quantity: [Number]
- Location: [Where deployed]

**Additional Workstations** (if needed):
- [Training/Dashboard workstation specs]

**Source from Deal Transfer:**
- **Standard specs**: Use standard viAct workstation specs (may vary by number of cameras/modules)
- **Quantity**: Based on number of cameras and deployment architecture
- **Location**: Based on deployment method (on-premise → customer site, cloud → data center)

#### 4.2 Network Requirements
- Bandwidth: [If specified]
- Connection Type: [LAN / WAN / Wireless]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Internet connection" + "Connection speed"
- **Logic**: 
  - If unstable internet → May need local processing
  - If satellite/low bandwidth → Edge processing recommended

#### 4.3 Power Requirements
- Power Source: [Stable / UPS / etc.]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Stable power source"

---

## 5. TIMELINE

### Common Items (Always Present):

#### 5.1 Project Timeline
```
T0: [Starting point - e.g., Project awarded]
T1: T0 + [X weeks] - [Phase description]
T2: T1 + [X weeks] - [Phase description]
T3: T2 + [X weeks] - [Phase description]
T4: T3 + [X weeks] - [Phase description - UAT/Go-Live]
```

**Standard Phases:**
- T0: Project awarded / Contract signed
- T1: Proposal review, System integration and deployment planning
- T2: Hardware deployment finish
- T3: Software deployment finish
- T4: UAT (User Acceptance Testing)
- T5: Project hand-off

**Source from Deal Transfer:**
- From Deal Transfer → Commercial → "Expected timeline" OR "If real project, timeline"
- **Logic**: 
  - If pilot/PoC → Shorter timeline (4-6 weeks)
  - If full deployment → Longer timeline (2-4 months)
  - Custom modules → Add development time (4-8 weeks)

#### 5.2 Development Time (If Custom Modules)
- Standard Modules: [X weeks]
- Custom Modules: [X weeks]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Custom AI use cases"
- **Logic**: 
  - Standard modules → 4 weeks integration
  - Custom modules → 6-8 weeks development

---

## 6. AI MODULES

### Common Items (Always Present):

#### 6.1 List of AI Modules
```
1. [Module Name 1]
2. [Module Name 2]
3. [Module Name 3]
[...]
```

**Source from Deal Transfer:**
- **Primary source**: Deal Transfer → Technical → "List of VA use cases"
- **Conversion Logic**: 
  - Use case description → Module name
  - Example: "PPE detection" → "PPE Detection Module"
  - Example: "People counting" → "People Counting Module"
  - Example: "Restricted area monitoring" → "Restricted Area Monitoring Module"

#### 6.2 Module Descriptions (If Detailed Explanation Needed)

**For each module, if clarification needed:**
- **Module Name**: [Name]
- **Purpose**: [What it detects/monitors]
- **Detection Criteria**: [Specific rules/thresholds if custom]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Custom AI use cases" (if any custom requirements)
- From Deal Transfer → Technical → "List of VA use cases" (detailed descriptions)
- **Logic**: 
  - Standard modules → Use standard descriptions
  - Custom requirements → Add custom detection criteria

#### 6.3 Module-to-Pain-Point Mapping (Internal Logic)
**How to derive modules from pain points:**

| Pain Point (Deal Transfer) | → | AI Module (Proposal) |
|----------------------------|---|---------------------|
| Safety incidents not detected | → | PPE Detection, Unsafe Behavior Detection |
| Manual counting inaccurate | → | People/Vehicle/Object Counting |
| Unauthorized access | → | Facial Recognition, Intrusion Detection |
| Spills/debris not cleaned | → | Spill Detection, Debris Detection |
| Equipment collision risk | → | Anti-collision Detection |
| Workers in restricted areas | → | Restricted Area Monitoring |

**Source from Deal Transfer:**
- From Deal Transfer → Commercial → "Current Pain Points"
- **Logic**: Map each pain point to corresponding AI module(s)

---

## 7. ALERT, NOTIFICATION, DASHBOARD, REPORT

### Common Items (Always Present):

#### 7.1 Alert & Notification System

**Alert Methods:**
- [ ] Dashboard Pop-ups
- [ ] Email Notifications
- [ ] Mobile Alerts
- [ ] On-site Alarms
- [ ] VMS Integration

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "How do they want to alert operators on-site?"
- **Logic**: 
  - "Email/dashboard" → Email + Dashboard
  - "On-site alarm" → Sound/visual alarms
  - "VMS integration" → VMS pop-up alerts

#### 7.2 Dashboard Requirements

**Dashboard Features:**
- Real-time Monitoring: [What to monitor]
- KPI Widgets: [List KPIs if specified]
- [Additional features if custom]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Any customized Dashboard"
- **Logic**: 
  - If no custom requirement → Standard dashboard
  - If custom KPIs specified → List them
  - If multi-dashboard (per site + HQ) → Specify

#### 7.3 Reporting Requirements

**Report Types:**
- Daily Summary Report: [Time range, content]
- [Custom reports if specified]

**Export Capabilities:**
- Excel Export: [Yes/No]
- [Other formats if specified]

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Any customized Dashboard" (reporting section)
- **Logic**: 
  - If customer mentions "excel export" → Include Excel export
  - If customer mentions "daily report" → Include daily summary
  - If customer mentions "timestamp filter" → Include filtering options

---

## SUPPORTING SECTIONS (Use to inform main sections above)

### A. Compliance & Security Requirements

**Use this information to inform:**
- System Architecture (deployment method)
- System Requirements (data storage location)
- Integration Points (data handling)

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "GDPR requirements" OR "Data protection"
- **Logic**: 
  - GDPR required → On-premise or EU cloud
  - Data retention policy → Storage requirements
  - Access control → Integration requirements

### B. Custom Requirements

**Use this information to inform:**
- AI Modules (custom modules needed)
- System Architecture (custom integrations)
- System Requirements (custom hardware)
- Dashboard/Reporting (custom features)

**Source from Deal Transfer:**
- From Deal Transfer → Technical → "Custom AI use cases" + "Custom Dashboard" + "Custom HW/IoT"
- **Logic**: 
  - Custom use case → Custom module development → Timeline adjustment
  - Custom dashboard → Dashboard requirements section
  - Custom IoT → Integration points section

---

## MAPPING GUIDE: Deal Transfer → Proposal

### Step-by-Step Conversion Process:

#### Step 1: Extract Project Basics
**From Deal Transfer → Commercial:**
- Customer name → Project Owner
- Solutions they want → Project Objectives
- Timeline → Project Timeline

**From Deal Transfer → Technical:**
- Number of cameras → Camera Number
- VA use cases → AI Modules List
- Deployment method → System Architecture Type

#### Step 2: Convert Pain Points to Objectives
**Logic:**
- Read pain points → Identify root causes → Formulate objectives
- Example: "Manual counting inaccurate" → "Automate counting process"
- Example: "Safety incidents not detected" → "Real-time safety monitoring"

#### Step 3: Map Use Cases to Modules
**Logic:**
- Use case description → Standard module name
- If no standard module → Custom module (note in timeline)
- Example: "PPE detection" → "PPE Detection Module"
- Example: "Count packages at gate" → "Object Counting Module" (customize for packages)

#### Step 4: Determine Architecture
**Logic:**
- Internet stable + no data security concern → Cloud possible
- Internet unstable → On-premise or Edge
- Data security concern → On-premise
- Multiple sites → Edge or Hybrid
- Single site → Centralized or Edge

#### Step 5: Define Responsibilities
**Logic:**
- Customer has cameras → Customer handles HW
- New installation → Specify who handles what
- On-premise → Customer may provide server
- Cloud → viAct handles infrastructure

#### Step 6: Calculate Timeline
**Logic:**
- Standard modules only → 4-6 weeks (pilot) or 2-3 months (full)
- Custom modules → Add 6-8 weeks development
- Hardware deployment → Add 2-4 weeks
- UAT → Add 1-2 weeks

#### Step 7: Configure Alerts & Dashboard
**Logic:**
- Customer specifies alert method → Use that
- No specification → Standard (Email + Dashboard)
- Custom KPIs mentioned → Include in dashboard
- Excel export mentioned → Include export feature

---

## COMMON PATTERNS & LOGIC

### Pattern 1: Safety-Focused Projects
**Typical Modules:**
- PPE Detection
- Restricted Area Monitoring
- Unsafe Behavior Detection
- Anti-collision

**Typical Architecture:**
- On-premise (data security)
- Real-time alerts critical

### Pattern 2: Operations-Focused Projects
**Typical Modules:**
- People/Vehicle/Object Counting
- Queue Management
- Process Monitoring

**Typical Architecture:**
- Cloud or Hybrid (scalability)
- Dashboard with KPIs important

### Pattern 3: Security-Focused Projects
**Typical Modules:**
- Facial Recognition
- Intrusion Detection
- Loitering Detection

**Typical Architecture:**
- On-premise (privacy)
- Access control integration

---

## NOTES FOR PRESALE TEAM

1. **Always start with Deal Transfer**: Extract all Commercial and Technical information first

2. **Pain Points → Objectives**: Don't just copy pain points, convert them into positive objectives

3. **Use Cases → Modules**: Map each use case to a specific module name (standard or custom)

4. **Architecture Decision**: Base on internet stability, data security, and number of sites

5. **Timeline Realism**: 
   - Pilot: 4-6 weeks
   - Full deployment: 2-4 months
   - Custom modules: +6-8 weeks

6. **Responsibilities Clarity**: Clearly separate viAct vs Customer responsibilities

7. **Custom Requirements**: Always check for custom use cases, dashboard, or hardware - these affect timeline and scope

8. **Missing Information**: If Deal Transfer lacks info, mark as "[To be confirmed]" in proposal

