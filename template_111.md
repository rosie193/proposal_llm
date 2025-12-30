# Technical Proposal Template - Complete Structure

> **Purpose**: This template outlines the COMMON structure that appears in all technical proposals. Use this as an outline to fill in variable information from Deal Transfer documents and customer requirements.

> **Note**: This template focuses on variable sections only. Fixed sections (company introduction, standard disclaimers, etc.) are excluded.

> **Source Reference:**
> - **S1:** Commercial Sheet (File New Deal Transfer)
> - **S2:** Technical Sheet (File New Deal Transfer)
> - **Sx:** Other sheets (File New Deal Transfer)

---

## 1. COVER PAGE

| Content | Source/Guidance |
|---------|------------------|
| Company Logo | Standard viAct logo |
| Proposal Title | Format: "AI-Powered Video Analytics Solution Proposal for [Customer Name]" OR "Technical Proposal - [Project Name]"<br>**Source**: S1 - "Customer overview (short introduction about customer business)" + S1 - "What are the solutions that they are looking to implement?" |
| Client Name | Customer company name<br>**Source**: S1 - "Customer overview (short introduction about customer business)" (extract company name) |
| Date | Proposal submission date |
| Duration | Project duration<br>**Source**: S1 - "If real project, expected timeline (including tender if any)" |

---

## 2. PROJECT REQUIREMENT STATEMENT

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **Project** | Format: "POC AI-Powered Video Analytics for [Purpose]" OR "[Project Name]"<br>**Logic**: Derive from pain points → General project description<br>**Example**: "POC AI-Powered Video Analytics for Safety Monitoring"<br>**Source**: S1 - "Current Pain Points of end customer" → Convert to positive objective |
| **Project Owner** | Customer company name<br>**Source**: S1 - "Customer overview (short introduction about customer business)" |
| **Work Scope** | Format: "[Deployment method] AI system to [Primary objective]"<br>**Example**: "On-premise AI system to Monitor Vessel Safety in Real time"<br>**Components**:<br>1. Deployment method (Source: S2 - "Specific HW/SW requirements (deployment method)?")<br>2. AI system<br>3. General project description (from pain points)<br>**Logic**: Deployment method + AI system + Primary objective derived from pain points |
| **Project Duration** | X years/months<br>**Source**: S1 - "If real project, expected timeline (including tender if any)" |
| **Camera Number** | X cameras<br>**Source**: S1 - "If VA: camera status & scope" (extract number from answer) |
| **Number of AI Module per Camera** | Suggest based on customer pain points and use cases<br>**Logic**: If not mentioned, suggest average 3-4 AI modules/camera<br>**Source**: S2 - "List of VA use cases" → Count modules, divide by camera number |
| **AI Modules** | List of primary modules<br>**Source**: S2 - "List of VA use cases" → **Convert use cases to module names**<br>**Conversion Logic**:<br>- Use case description → Standard module name<br>- Example: "PPE detection" → "PPE Detection Module"<br>- Example: "People counting" → "People Counting Module"<br>- If no standard module exists → Mark as "Custom Module" |

### 2.1 Project Objectives / Work Scope Statement

**Primary Objective:**
- [Main objective - derived from pain points]

**Secondary Objectives:**
- [Objective 2]
- [Objective 3]

**Source from Deal Transfer:**
- **Derive from**: S1 - "Current Pain Points of end customer" (exact field name in Deal Transfer)
- **Logic**: Convert pain points into positive objectives
  - Example: Pain point "Manual counting is inaccurate" → Objective "Automate counting with AI"
  - Example: Pain point "Safety incidents not detected in time" → Objective "Real-time safety monitoring"
  - Example: Pain point "No visibility into operations" → Objective "Real-time operational visibility and monitoring"

**Note**: Do NOT include Stakeholders, Decision Makers, or detailed customer profile in proposal (these are internal Deal Transfer info only)

---

## 3. SCOPE OF WORK

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **viAct Responsibilities** | Software: License, maintenance, support<br>Camera integration<br>AI Modules: [List modules to be provided]<br>[Additional responsibilities based on project]<br>**Source**: S2 - "Specific HW/SW requirements (deployment method)?" + S2 - "List of VA use cases" |
| **Client Responsibilities** | Hardware: Procurement, configuration, installation, and maintenance<br>Other Requirements if needed<br>**Source**: S1 - "If VA: camera status & scope" (check if cameras exist)<br>**Logic**:<br>- If customer has cameras → Customer handles HW, viAct handles software<br>- If new installation → Specify who handles what<br>- If on-premise → Customer may need to provide server/workstation |

**Note**: Use available slide template for Scope of Work, add specific requirements if customer has special needs.

---

## 4. SYSTEM ARCHITECTURE

> **First Step**: Choose deployment method → Select architecture type

| Content | Source/Guidance |
|---------|------------------|
| **Deployment Method: On Cloud** | **Source**: S2 - "Specific HW/SW requirements (deployment method)?" = "Cloud"<br>**Inputs needed**:<br>+ Number of Camera: S1 - "If VA: camera status & scope" (extract number)<br>+ List AI modules: S2 - "List of VA use cases"<br>**Reference KB**:<br>- Architecture: KB "DOCUMENT" → Search "Architecture-Cloud"<br>- Slide: System_architecture.pdf (On Cloud - Slide 4) |
| **Deployment Method: On Premise** | **Source**: S2 - "Specific HW/SW requirements (deployment method)?" = "On-premise" or answer mentions "on-premise"<br>**Inputs needed**:<br>+ Number of Camera: S1 - "If VA: camera status & scope" (extract number)<br>+ List AI modules: S2 - "List of VA use cases"<br>**Reference KB**:<br>- Architecture: KB "DOCUMENT" → Search "Architecture" (On-Premise variants)<br>- Slide: System_architecture.pdf (On Premise - slide 6, 8) |
| **Deployment Method: Not mentioned → Suggest Hybrid** | **Source**: S2 - "Specific HW/SW requirements (deployment method)?" = Not specified or blank<br>**Logic**: When deployment method not mentioned, suggest Hybrid<br>**Inputs needed**:<br>+ Number of Camera: S1 - "If VA: camera status & scope" (extract number)<br>+ List AI modules: S2 - "List of VA use cases"<br>**Reference KB**:<br>- Architecture: KB "DOCUMENT" → Search "Architecture-Hybrid"<br>- Slide: System_architecture.pdf (Hybrid - slide 11) |
| **Deployment Method: Edge Processing** | **Source**: S2 - "Specific HW/SW requirements (deployment method)?" mentions "local processing" OR S2 - "Stable internet connection?" = "No" or unstable<br>**Logic**: Edge processing for multiple sites or unstable internet<br>**Reference KB**: KB "DOCUMENT" → Search edge/on-premise architectures |
| **Other Components** | Add other HW components if needed:<br>- NVR (Network Video Recorder)<br>- VPN Bridge<br>- Additional network equipment<br>**Source**: S2 - Integration requirements, multiple sites, security requirements |

### 4.1 Architecture Diagram Description

**Detailed Technical Description for the System Architecture section** (Blueprint for designer to create visual slide):

**Data Flow:**
- Trace the path: Camera → Network Switch → AI Workstation → Cloud/Dashboard
- Include: Video stream direction, Alert data flow, Dashboard access

**Hardware Components Placement:**
- AI Workstation: [Location - Central / Edge / Per site]
- NVR: [If applicable]
- VPN Bridge: [If applicable]
- Peripheral devices: Speakers, kiosks, sensors, etc.

**Network Topology:**
- Local Area Network (LAN): For cameras and local processing
- Wide Area Network (WAN): For dashboard access and remote monitoring
- Internet connectivity: For cloud services (if applicable)

**System Layers:**
- Edge Layer: At site (cameras, edge processing)
- Cloud Layer: Storage/backend (if cloud deployment)
- Application Layer: Mobile/Web dashboard access

**Source from Deal Transfer:**
- **Derive from**: All technical requirements combined (S2)
- **Logic**: Based on deployment method, number of sites, camera locations, internet stability

---

## 5. SYSTEM REQUIREMENTS

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **Network** | **If Deployment method is On-premise or Hybrid**:<br>+ External bandwidth: Internet bandwidth for remote access and updates<br>+ Per-camera bandwidth: 12 Mbps/Camera<br>+ Total system bandwidth: 12 Mbps × Number of Cameras<br>**Calculation**:<br>- External bandwidth: [Value] (for remote access)<br>- Per-camera bandwidth: 12 Mbps<br>- Total system bandwidth: 12 Mbps × [Camera Number from S1]<br>**Source**: S2 - "Stable internet connection?" (check answer: Yes/No/Stable/Unstable)<br>**Logic**: If unstable internet → May need local processing, reduce cloud dependency |
| **Camera** | **Standard Specifications**:<br>+ Resolution: 1080p@25fps (minimum)<br>+ Connectivity Type: IP-based cameras with RTSP support<br>**Output Format**:<br>+ Resolution: [e.g., 1080p, 4K] - based on customer requirement<br>+ Frame rate: [e.g., 25fps, 30fps]<br>+ Connectivity Type: [IP, RTSP]<br>**Source**: S2 - "Can client camera provide RTSP link?" (check answer: yes/no)<br>**Note**: If customer has cameras, check S1 - "If VA: camera status & scope" for camera details |
| **AI Inference Workstation, AI Training Workstation, Dashboard** | **Input from Deal Transfer**:<br>+ Number of cameras: S1 - "If VA: camera status & scope" (extract number)<br>+ Number of AI modules/camera: Suggest 3-4 modules/camera (average) if not specified<br>**Output**:<br>+ Template: Slide 7 System Architecture Slide (System_architecture.pdf)<br>+ Calculate Workstation specs: Use file "AI_Workstation_Calculator" + Knowledge Base<br>**Reference KB**:<br>- Search KB "DOCUMENT" for workstation specifications<br>- Use AI_Workstation_Calculator.xlsx to calculate based on camera count and modules<br>**Standard Specs (Reference)**:<br>- CPU: Core i7/i9 (based on load)<br>- GPU: RTX series (based on AI module complexity)<br>- RAM: 32-64GB (based on camera count)<br>- Storage: 2TB+ (based on retention needs) |
| **Additional Equipment** | Access control devices, kiosks, sensors, IoT devices, etc.<br>**Source**: S2 - "Any IoT integration?" + S2 - "Any customized HW / IoT?" |

### 5.1 Power Requirements

| Content | Source/Guidance |
|---------|------------------|
| **Power Source** | Stable / UPS / Generator / etc.<br>**Source**: S2 - "Stable power source?" (check answer: yes/no) |

---

## 6. IMPLEMENTATION PLAN (TIMELINE)

### Common Items (Always Present):

### 6.1 Key Milestones

- **Proposal submission date**
- **Project award date** (T0)
- **Hardware deployment** (T1)
- **Software deployment** (T2)
- **Integration period** (T3)
- **Handover / completion** (T4)

### 6.2 Phasing Structure

| Phase | Description | Duration | Source/Guidance |
|-------|-------------|----------|-----------------|
| **Phase T0** | Project Award / Contract Signed | — | **Source**: S1 - "If real project, expected timeline (including tender if any)" → Start date |
| **Phase T1** | Hardware Deployment | X weeks | **Logic**:<br>- If customer has cameras: 1-2 weeks<br>- If new installation: 2-4 weeks<br>**Source**: S1 - "If VA: camera status & scope" (check if cameras exist) |
| **Phase T2** | Software Deployment | X weeks | **Logic**: Depends on number of modules and classification<br>- Standard Modules: 4-6 weeks<br>- Customize Modules: 6-8 weeks per module<br>- If mixed: Calculate based on module count<br>**Source**: S2 - "List of VA use cases" → Identify standard vs custom (check S2 - "Any customized AI use cases") |
| **Phase T3** | System Integration & Handover / UAT | X weeks | **Standard**: 2-4 weeks<br>**Includes**: Integration testing, UAT, training |

**Source from Deal Transfer:**
- **Primary source**: S1 - "If real project, expected timeline (including tender if any)"
- **Logic**:
  - If pilot/PoC → Shorter timeline (4-6 weeks total)
  - If full deployment → Longer timeline (2-4 months total)
  - Custom modules → Add development time (6-8 weeks per custom module)

---

## 7. PROPOSED MODULES & FUNCTIONAL DESCRIPTION

### Common Items (Always Present):

### 7.1 Module Classification

**Divide modules into:**
- **Standard AI Modules**: Available in KB (reference `standard_AI_modules.md`), can reuse existing descriptions from KB
- **Custom Modules**: Not found in standard list, need to create descriptions based on customer requirements

**Source**: S2 - "List of VA use cases" → Check against `standard_AI_modules.md` to determine if standard or custom

### 7.2 Module Description Template

**For EACH module (both Standard and Custom), fill in the following template:**

| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | [Module Name] | **Source**: S2 - "List of VA use cases" → Convert use case to module name<br>**Logic**: Use standard module name from `standard_AI_modules.md` if available, otherwise create descriptive name |
| **Module Type** | Standard / Custom | **Logic**: Check if module name exists in `standard_AI_modules.md`<br>- If found → Standard<br>- If not found → Custom |
| **Purpose Description** | Describe what this module detects and why it matters | **Source**:<br>- Standard: Search KB "DOCUMENT" or "viAct_Proposal" for module description<br>- Custom: S2 - "Any customized AI use cases (description & videos)?" → Extract purpose<br>**Format**: 1-2 sentences explaining what it detects and business value |
| **Alert Trigger Logic** | When does it alert? | **Source**:<br>- Standard: From KB module descriptions<br>- Custom: S2 - "Any customized AI use cases" → Extract alert conditions<br>**Examples**:<br>- "Alert triggers when worker not wearing safety helmet detected"<br>- "Alert triggers when person enters restricted area"<br>- "Alert triggers when loitering detected for more than [X] seconds" |
| **Detection Criteria** (if custom or specific) | Specific rules, thresholds, conditions | **Source**: S2 - "Any customized AI use cases" → Extract specific requirements<br>**Examples**:<br>- "Loitering threshold: [X] seconds"<br>- "Proximity alert: within 30cm (1 foot) of moving forklift"<br>- "Only for crane operators" (if role-specific) |
| **Preconditions** | Camera angle, height, lighting requirements | **Standard Template**:<br>"Camera must maintain a suitable distance for clear observation, typically between [X] to [Y] meters"<br>**Source**:<br>- Standard: From KB (typically 5-10 meters for general detection, 3-5 meters for detailed PPE)<br>- Custom: S2 - "Any customized AI use cases" → Extract if mentioned<br>**Common Preconditions**:<br>- Distance: 5-10 meters (general), 3-5 meters (detailed detection)<br>- Camera angle: Must face work area directly<br>- Lighting: Avoid glare or strong reflections |
| **Client Data Requirements** (if custom module) | Images, video samples, or labels required for training | **Source**: S2 - "Any customized AI use cases" → Check if training data mentioned<br>**Format**:<br>"Request: Provide [object type] images (color, type) for model training"<br>**Only needed for**: Custom modules requiring model training |

**Module Template Format (Fill for each module):**

```
Module: [Module Name]
Module Type: [Standard / Custom]

• Purpose Description: [1-2 sentences describing what it detects and why it matters]

• Alert Trigger Logic: [When does it alert? Specific conditions]

• Detection Criteria: [If custom, specific rules/thresholds - e.g., "loitering > 30 seconds", "proximity < 30cm"]

• Preconditions: [Camera distance: typically X to Y meters. Camera angle, lighting requirements if specific]

• Client Data Requirements: [Only for custom modules: "Request: Provide [object type] images for model training"]
```

### 7.3 Process for Filling Module Descriptions

| Step | Action | Source/Guidance |
|------|--------|------------------|
| **Step 1: Identify Modules** | Extract list from S2 - "List of VA use cases" | Convert use case descriptions to module names |
| **Step 2: Classify** | Check each module in `standard_AI_modules.md` | Standard → Search KB for description<br>Custom → Use Deal Transfer description |
| **Step 3: Fill Template** | For each module, fill all fields in template above | Use KB search for standard modules<br>Use S2 - "Any customized AI use cases" for custom |
| **Step 4: Standard Modules** | Search KB "DOCUMENT" or "viAct_Proposal" | Find existing module descriptions to reuse text (Purpose, Alert Logic, Preconditions) |
| **Step 5: Custom Modules** | Extract from S2 - "Any customized AI use cases" | Create description based on customer requirements |

### 7.4 Module-to-Pain-Point Mapping (Internal Logic)

**How to derive modules from pain points:**

| Pain Point (Deal Transfer S1) | → | AI Module (Proposal) |
|----------------------------|---|---------------------|
| Safety incidents not detected | → | PPE Detection, Unsafe Behavior Detection, Human Down Detection |
| Manual counting inaccurate | → | People Counting, Vehicle Counting, Object/Package Counting |
| Unauthorized access | → | Facial Recognition, Intrusion Detection, Restricted Area Monitoring |
| Spills/debris not cleaned | → | Spill Detection, Debris Detection |
| Equipment collision risk | → | Anti-collision Detection, Worker-Machine Anti-Collision |
| Workers in restricted areas | → | Restricted Area Monitoring, Red Zone Management |
| Fire/smoke incidents | → | Fire & Smoke Detection |
| Loitering concerns | → | Loitering Detection |
| Vehicle/parking violations | → | Vehicle Detection, Parking Violation Detection |
| Process inefficiencies | → | Process Monitoring, Queue Management |

**Source from Deal Transfer:**
- **Primary source**: S1 - "Current Pain Points of end customer"
- **Logic**: Map each pain point to corresponding AI module(s)
- **Secondary source**: S2 - "List of VA use cases" (if customer already specified)

---

## 8. USER INTERFACE & REPORTING

### Common Items (Always Present):

### 8.1 Alerts & Notifications

| Content | Source/Guidance |
|---------|------------------|
| **Channels** | Email, Mobile App, SMS, Dashboard Pop-ups, On-site Alarms, VMS Integration<br>**Source**: S2 - "How do they want to alert operators on-site?" (exact field name)<br>**Logic**:<br>- Answer mentions "Email/dashboard" → Email + Dashboard<br>- Answer mentions "On-site alarm" → Sound/visual alarms<br>- Answer mentions "VMS integration" → VMS pop-up alerts<br>- If answer is blank/not specified → Standard (Email + Dashboard) |

### 8.2 Dashboard Visualizations

| Content | Source/Guidance |
|---------|------------------|
| **Event Analysis** | Charts and graphs of detection frequencies<br>**Source**: Standard feature, mention if customer needs specific KPIs |
| **Alert Timelines** | Chronological view of incidents<br>**Source**: Standard feature |
| **Evidence Snapshots** | Image/Video clips of the detected event<br>**Source**: Standard feature |
| **Custom KPIs** | If customer specified custom KPIs<br>**Source**: S2 - "Any customized dashboard?" → Extract KPI requirements from answer<br>**Example**: Active pumps, Idle pumps, Queue length, Violations per hour, etc. |
| **Multi-Dashboard** | If customer needs per-site + central HQ dashboard<br>**Source**: S2 - "Any customized dashboard?" → Check if answer mentions multi-dashboard |

### 8.3 Daily / Weekly Summary Reports

| Content | Source/Guidance |
|---------|------------------|
| **Automated Reporting Features** | Sent to stakeholders<br>**Source**: S2 - "Any customized dashboard?" → Check answer for reporting requirements<br>**Logic**:<br>- If answer mentions "daily report" → Include daily summary<br>- If answer mentions "excel export" → Include Excel export<br>- If answer mentions "timestamp filter" → Include filtering options<br>**Format**:<br>- Time range: [e.g., 7 AM - 9 PM] (extract from answer if mentioned)<br>- Export: Excel / PDF / CSV<br>- Filtering: Timestamp, area, event type |

---

## SUPPORTING SECTIONS (Use to inform main sections above)

### A. Compliance & Security Requirements

**Use this information to inform:**
- System Architecture (deployment method selection)
- System Requirements (data storage location)
- Integration Points (data handling)

**Source from Deal Transfer:**
- S2 - "Any GDPR / data privacy requirements?" (exact field name)
- **Logic**:
  - If answer mentions GDPR or data privacy concerns → On-premise or EU cloud deployment
  - Data retention policy → Storage requirements section (if mentioned in answer)
  - Access control requirements → Integration points section (if mentioned)

### B. Custom Requirements

**Use this information to inform:**
- AI Modules (custom modules needed → Section 7)
- System Architecture (custom integrations → Section 4)
- System Requirements (custom hardware → Section 5)
- Dashboard/Reporting (custom features → Section 8)

**Source from Deal Transfer:**
- S2 - "Any customized AI use cases (description & videos)?" → Custom Modules (Section 7)
- S2 - "Any customized dashboard?" → Dashboard Requirements (Section 8)
- S2 - "Any customized HW / IoT?" → Additional Equipment (Section 5)
- **Logic**:
  - If answer to "Any customized AI use cases" has content → Custom module development → Timeline adjustment (Section 6)
  - If answer to "Any customized dashboard" has content → Dashboard requirements section (Section 8)
  - If answer to "Any customized HW / IoT" has content → Integration points section (Section 4)

---

## MAPPING GUIDE: Deal Transfer → Proposal

### Step-by-Step Conversion Process:

#### Step 1: Extract Project Basics
**From Deal Transfer → Commercial (S1):**
- Customer name → **Cover Page**: Client Name + **Section 2**: Project Owner
- Solutions they want → **Section 2**: Project Objectives
- Timeline → **Section 2**: Project Duration + **Section 6**: Timeline

**From Deal Transfer → Technical (S2):**
- Camera number: S1 - "If VA: camera status & scope" → **Section 2**: Camera Number + **Section 4**: Architecture inputs
- VA use cases: S2 - "List of VA use cases" → **Section 2**: AI Modules List + **Section 7**: Module descriptions
- Deployment method: S2 - "Specific HW/SW requirements (deployment method)?" → **Section 4**: Architecture Type

#### Step 2: Convert Pain Points to Objectives
**Logic:**
- Read pain points (S1) → Identify root causes → Formulate positive objectives
- Example: "Manual counting inaccurate" → "Automate counting process with AI"
- Example: "Safety incidents not detected" → "Real-time safety monitoring and alerting"
- **Output**: **Section 2** - Project Objectives / Work Scope Statement

#### Step 3: Map Use Cases to Modules
**Logic:**
- Use case description (S2) → Standard module name (search KB first)
- If found in KB → Standard module (reuse KB slides)
- If not found → Custom module (create new slide)
- Example: "PPE detection" → "PPE Detection Module" (standard)
- Example: "Count packages at gate" → "Object Counting Module" (may be custom)
- **Output**: **Section 7** - List of AI Modules + Module descriptions

#### Step 4: Determine Architecture
**Logic:**
- Internet stable + no data security concern → Cloud possible
- Internet unstable → On-premise or Edge
- Data security concern → On-premise
- Multiple sites → Edge or Hybrid
- Single site → Centralized or Edge
- **Source**: S2 - "Specific HW/SW requirements (deployment method)?" + S2 - "Stable internet connection?" + S2 - "Any GDPR / data privacy requirements?"
- **Output**: **Section 4** - Architecture Type + Components

#### Step 5: Define Responsibilities
**Logic:**
- Check S1 - "If VA: camera status & scope" → If cameras exist, customer handles HW, viAct handles software
- New installation → Specify who handles what
- Check S2 - "Specific HW/SW requirements (deployment method)?" → If on-premise, customer may provide server/workstation
- If cloud → viAct handles infrastructure
- **Output**: **Section 3** - Scope of Work

#### Step 6: Calculate Timeline
**Logic:**
- Standard modules only → 4-6 weeks (pilot) or 2-3 months (full deployment)
- Custom modules → Add 6-8 weeks development per custom module
- Hardware deployment → Add 2-4 weeks (if new installation)
- UAT → Add 2-4 weeks
- **Source**: S1 - "If real project, expected timeline (including tender if any)" + S2 - "Any customized AI use cases (description & videos)?"
- **Output**: **Section 6** - Implementation Plan

#### Step 7: Configure Alerts & Dashboard
**Logic:**
- Check S2 - "How do they want to alert operators on-site?" → If answer has content, use that
- If answer blank/not specified → Standard (Email + Dashboard)
- Check S2 - "Any customized dashboard?" → If answer mentions custom KPIs, include in dashboard
- If answer mentions excel export → Include export feature
- **Output**: **Section 8** - Alerts, Dashboard, Reporting

#### Step 8: Calculate System Requirements
**Logic:**
- Camera number: S1 - "If VA: camera status & scope" → Network bandwidth (12 Mbps × camera count)
- Number of cameras + modules (from S2 - "List of VA use cases") → Workstation specs (use AI_Workstation_Calculator)
- Deployment method: S2 - "Specific HW/SW requirements (deployment method)?" → Workstation location
- **Output**: **Section 5** - System Requirements

---

## COMMON PATTERNS & LOGIC

### Pattern 1: Safety-Focused Projects
**Typical Modules:**
- PPE Detection
- Restricted Area Monitoring
- Unsafe Behavior Detection
- Anti-collision Detection
- Human Down Detection

**Typical Architecture:**
- On-premise (data security)
- Real-time alerts critical

**Typical Timeline:**
- 2-3 months (full deployment)

### Pattern 2: Operations-Focused Projects
**Typical Modules:**
- People/Vehicle/Object Counting
- Queue Management
- Process Monitoring

**Typical Architecture:**
- Cloud or Hybrid (scalability)
- Dashboard with KPIs important

**Typical Timeline:**
- 4-6 weeks (pilot) or 2-3 months (full)

### Pattern 3: Security-Focused Projects
**Typical Modules:**
- Facial Recognition
- Intrusion Detection
- Loitering Detection

**Typical Architecture:**
- On-premise (privacy)
- Access control integration

**Typical Timeline:**
- 2-4 months (full deployment)

---

## NOTES FOR PRESALE TEAM

1. **Always start with Deal Transfer**: Extract all Commercial (S1) and Technical (S2) information first

2. **Pain Points → Objectives**: Don't just copy pain points, convert them into positive objectives (Section 2)

3. **Use Cases → Modules**: Map each use case to a specific module name (standard or custom). Always search KB first to see if it's a standard module (Section 7)

4. **Architecture Decision**: Base on S2 - "Stable internet connection?", S2 - "Any GDPR / data privacy requirements?", number of sites (Section 4)

5. **Timeline Realism**: 
   - Pilot: 4-6 weeks
   - Full deployment: 2-4 months
   - Custom modules: +6-8 weeks per module

6. **Responsibilities Clarity**: Clearly separate viAct vs Customer responsibilities (Section 3)

7. **Custom Requirements**: Always check S2 - "Any customized AI use cases (description & videos)?", S2 - "Any customized dashboard?", S2 - "Any customized HW / IoT?" - these affect timeline and scope (Supporting Sections)

8. **Missing Information**: If Deal Transfer lacks info, mark as "[To be confirmed]" in proposal

9. **KB Reference**: Always search KB "DOCUMENT" and "viAct_Proposal" for:
   - Standard modules → Reuse existing slides
   - Architecture diagrams → Reference existing slides
   - Workstation specs → Use AI_Workstation_Calculator

10. **Module Description Template**: All modules (standard and custom) should follow the same template structure: Purpose, Alert Logic, Data Requirements, Preconditions

