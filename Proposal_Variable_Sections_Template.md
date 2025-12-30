# Technical Proposal Template - Variable Sections Only

> **Note**: This template covers only the variable components that change between projects. Fixed/common sections (company introductions, standard terms, etc.) are excluded.

---

## 1. PROJECT REQUIREMENT STATEMENT

### 1.1 Project Information
```
Project Name: [Customer/Project Name]
Project Owner: [Company Name]
Project Duration: [X years/months]
Total Camera Number: [Number] cameras
Primary AI Modules: [List of main modules]
```

### 1.2 Customer Overview
- **Company Name**: [Full company name]
- **Industry**: [Oil & Gas / Manufacturing / Construction / Telecommunications / etc.]
- **Business Type**: [End-customer / SI / Partner]
- **If SI**: End-customer overview:
  - End-customer name and business
  - Relationship between SI and end-customer
- **Company Profile**: [Brief 2-3 sentences about what the company does]

### 1.3 Stakeholders & Decision Makers
- **Primary Contact**: 
  - Name, Title, Email
  - Role in project (requirement owner / decision maker / etc.)
- **Key Stakeholders**:
  - [List names, titles, roles, LinkedIn if available]
- **Decision-Making Process**: [Who approves what, timeline for decisions]

### 1.4 Current Pain Points
- [Pain point 1]: [Detailed description]
- [Pain point 2]: [Detailed description]
- [Pain point 3]: [Detailed description]

**Example formats:**
- Safety concerns: [Specific safety issues]
- Operational inefficiencies: [What's not working]
- Manual processes: [What needs automation]
- Lack of visibility: [What they can't see/monitor]

---

## 2. WORK SCOPE

### 2.1 Project Objectives
```
Primary Objective:
- [Main goal of the project]

Secondary Objectives:
- [Objective 2]
- [Objective 3]
```

### 2.2 Solution Overview
**What the customer is looking to implement:**
- [Solution component 1]: [Description]
- [Solution component 2]: [Description]
- [Solution component 3]: [Description]

### 2.3 Scope of Work - Responsibilities

**viAct Responsibilities:**
- Software: [License type, maintenance, support details]
- AI Modules: [List of modules to be provided]
- Camera Integration: [Integration approach]
- [Custom responsibility if any]

**Customer Responsibilities:**
- Hardware: [Procurement, installation, configuration, maintenance]
  - Camera specifications: [If customer provides]
  - Networking: [Details]
  - Storage: [If customer provides]
- Integration: [Any hardware integrations needed]
- Configuration: [Any customer-side configuration]
- [Other custom responsibilities]

---

## 3. AI MODULES & USE CASES

### 3.1 List of AI Modules
```
Module Category: [Safety / Operations / Security / etc.]
1. [Module Name 1]
2. [Module Name 2]
3. [Module Name 3]
[...]
```

**Module Categories commonly used:**
- **Safety & Compliance**: PPE Detection, Restricted Area Monitoring, Unsafe Behavior Detection
- **Operations**: People Counting, Vehicle Counting, Package/Object Counting
- **Security**: Facial Recognition, Intrusion Detection, Loitering Detection
- **Environmental**: Spill/Leakage Detection, Debris Detection, Fire & Smoke Detection
- **Process-Specific**: [Industry-specific modules]

### 3.2 Detailed Module Descriptions
For each module, specify:

**Module Name: [e.g., PPE Detection]**
- **Purpose**: [What it detects/monitors]
- **Detection Criteria**: [Specific rules, thresholds]
  - Example: "Helmet detection (but only for crane operators)"
  - Example: "Loitering with seconds-level threshold: [X seconds]"
- **Alert Triggers**: [What conditions trigger alerts]
- **Target Areas**: [Where this module will be deployed]
- **Special Requirements**: [Any customizations needed]

### 3.3 Custom AI Use Cases
If any custom modules are required:
- **Use Case Name**: [Description]
- **Business Need**: [Why it's needed]
- **Detection Logic**: [How it should work]
- **Videos/Materials**: [Reference to provided videos]

---

## 4. SYSTEM ARCHITECTURE

### 4.1 Deployment Architecture Type
- [ ] On-Premise
- [ ] Cloud
- [ ] Hybrid
- [ ] Edge Processing (local at each site/station)

**Customer Preference**: [On-premise / Cloud / Hybrid / Edge]
**Reason**: [Why this deployment method - data security, internet stability, compliance, etc.]

### 4.2 Infrastructure Components

**Camera Setup:**
- Existing Cameras: [Number, type, brand, status]
- New Cameras Required: [Number, specifications]
- Total Cameras: [Total count]
- Camera Specifications: 
  - Type: [IP-based / Analog / etc.]
  - Resolution: [e.g., 8MP minimum]
  - Power: [POE / AC / etc.]
  - Special Requirements: [PTZ, wide FoV, etc.]

**Network Infrastructure:**
- Internet Connection: [Stable / Unstable / Satellite]
  - Speed: [Upload/Download speeds if known]
  - Impact on architecture: [If unstable, may require on-prem]
- Network Setup: [LAN / WAN / Wireless bridge, etc.]

**Storage:**
- Video Retention: [Duration, e.g., 3 months continuous, 1 year archive]
- Storage Provider: [Customer / Partner / viAct]
- Archive Requirements: [If any]

**Server/Workstation:**
- AI Inference Workstation: [Location, specs if known]
- Dashboard/Training Workstation: [Location, specs if known]
- Central NVR: [If required]

### 4.3 Integration Points

**VMS Integration:**
- Existing VMS: [Brand, model, version]
- Integration Method: [API / RTSP / SDK / etc.]
- Integration Requirements: [What needs to be integrated]

**Access Control Integration:**
- System Type: [Lenel / Honeywell / etc.]
- Integration Method: [API / Event-based / etc.]
- Purpose: [Face-based access, attendance, etc.]

**ERP/Other Systems:**
- ERP Integration: [Yes/No, which system]
- API Requirements: [JSON/REST API / etc.]
- Data Push Requirements: [What data needs to be sent where]

**IoT Integration:**
- IoT Devices: [List devices if any - heat sensors, etc.]
- Integration Method: [How to integrate]
- Data Flow: [What data from IoT, how it's used]

### 4.4 Architecture Diagram Description
- **Site Layout**: [Number of sites/locations]
- **Camera Placement Strategy**: [Overview of where cameras will be placed]
- **Processing Points**: [Where AI processing happens]
- **Data Flow**: [How data flows through the system]
- **Alert Distribution**: [How alerts are sent/distributed]

---

## 5. CAMERA PLACEMENT & CONFIGURATION

### 5.1 Site Information
- **Number of Sites**: [Single site / Multiple sites]
- **Site Locations**: [If multiple]
- **Site Characteristics**: [Indoor / Outdoor / Both, environment conditions]

### 5.2 Camera Placement Strategy
**Area 1: [Area Name, e.g., Entry Gate]**
- Number of Cameras: [X]
- Purpose: [Facial recognition / People counting / etc.]
- Camera Type: [PTZ / Fixed / etc.]
- View Angle: [If specified]
- Height/Position: [If known]

**Area 2: [Area Name]**
- [Same structure]

### 5.3 Camera Placement Diagram
- Reference to site plans/diagrams
- Specific placement requirements for each area

### 5.4 Special Camera Requirements
- PTZ Camera Presets: [If applicable, e.g., "Presets 1-6 for tripper area"]
- Multiple Camera Views: [If same area needs multiple angles]
- Camera Positioning Constraints: [Any limitations]

---

## 6. SYSTEM REQUIREMENTS

### 6.1 Hardware Requirements

**AI Inference Workstation:**
- CPU: [e.g., Core i7-14700K (20C/28T)]
- GPU: [e.g., RTX 4070 TI Super or RTX 4500 ADA]
- RAM: [e.g., 64GB]
- Storage: [e.g., 2TB]
- Network Card: [e.g., 1Gbps]
- Operating System: [e.g., Ubuntu 22.04]
- Quantity: [Number of workstations]
- Location: [Where it will be deployed]

**Training/Dashboard Workstation** (if separate):
- CPU: [Specifications]
- GPU: [Specifications]
- RAM: [Specifications]
- Storage: [Specifications]
- Operating System: [Specifications]

**Edge Processing Units** (if edge deployment):
- Unit Type: [Description]
- Quantity: [Per site/station]
- Specifications: [Details]

### 6.2 Network Requirements
- Bandwidth Requirements: [If specified]
- Network Latency: [If critical]
- Connection Type: [LAN / WAN / Wireless]

### 6.3 Power Requirements
- Power Source: [Stable / Unstable / UPS available]
- Power Specifications: [If needed]

---

## 7. ALERT & NOTIFICATION SYSTEM

### 7.1 Alert Methods
- [ ] Dashboard Pop-ups
- [ ] Email Notifications
  - Recipients: [Who receives emails]
- [ ] Mobile Alerts
  - App / SMS / Push notifications
- [ ] On-site Alarms
  - [ ] Sound Alarm / Siren
  - [ ] Visual Alerts
- [ ] VMS Integration
  - [ ] Pop-up on VMS interface
  - [ ] Video clip playback
- [ ] API/Webhook Integration
  - [ ] Push to external system
  - [ ] URL/Endpoint: [If specified]

### 7.2 Alert Recipients
- On-site Operators: [How they receive alerts]
- Safety Officers: [Notification method]
- Management: [Dashboard / Email / etc.]
- Control Room: [If applicable]

### 7.3 Alert Content
- Real-time Alerts: [What's included]
- Incident Reports: [Format, frequency]
- Video Clips: [Included in alerts? Duration?]
- Snapshot Images: [Included?]

---

## 8. DASHBOARD & REPORTING

### 8.1 Dashboard Requirements

**Dashboard Type:**
- [ ] Single Dashboard (centralized)
- [ ] Multi-Dashboard (per site/station + central HQ)
- [ ] Role-based Dashboards

**Dashboard Features:**
- Real-time Monitoring: [What needs to be monitored in real-time]
- KPI Widgets: [List of KPIs needed]
  - Example: Active pumps, Idle pumps, Queue length, Violations per hour, etc.
- Custom Views: [Any specific views needed]
- Filters: [Time range, area, event type, etc.]

### 8.2 Reporting Requirements

**Report Types:**
- **Daily Summary Report**: 
  - Time Range: [e.g., 7 AM - 9 PM]
  - Content: [What's included]
  - Format: [PDF / Excel / etc.]
  
- **Custom Reports**:
  - [Report Name]: [Description, frequency, format]
  
- **Export Capabilities**:
  - Excel Export: [Yes/No, what data]
  - Comparison Reports: [If customer wants to compare manual vs AI counts, etc.]
  - Filtering Options: [Timestamp range, area, type, etc.]

### 8.3 Data Access & Sharing
- API Access: [If customer needs API access to data]
- Data Export Formats: [CSV / JSON / Excel / etc.]
- Integration with Customer Systems: [If reports need to feed into other systems]

---

## 9. TIMELINE & PROJECT PHASES

### 9.1 Project Timeline
```
T0: [Starting point - e.g., Project awarded / Contract signed]
T1: T0 + [X weeks/months] - [Phase 1 description]
T2: T1 + [X weeks/months] - [Phase 2 description]
T3: T2 + [X weeks/months] - [Phase 3 description]
[Additional phases if needed]
```

**Example Structure:**
- T0: Project awarded / Contract signed
- T1: T0 + 2-4 weeks - Proposal review, System integration and deployment planning
- T2: T1 + X weeks - Hardware deployment finish
- T3: T2 + X weeks - Software deployment finish
- T4: T3 + X weeks - UAT (User Acceptance Testing)
- T5: T4 + X weeks - Project hand-off

### 9.2 Development Timeframes
If custom modules are needed:
- **Standard Modules**: [X weeks development time]
- **Custom Modules**: [X weeks development time]
- **Pre-built AI Modules**: [X weeks for integration]

### 9.3 Key Milestones
- Hardware Deployment Completion
- Software Deployment Completion
- UAT Completion
- Training Completion
- Go-Live Date
- Project Hand-off

### 9.4 Training & Support Timeline
- Training Duration: [X days/weeks]
- Training Location: [On-site / Remote / Hybrid]
- Post-Deployment Support: [X months of support included]

---

## 10. COMMERCIAL INFORMATION (For Internal Use / Proposal Pricing Section)

### 10.1 Project Budget
- Customer Budget: [If known / Not disclosed]
- Budget Range: [If approximate]
- Budget Context: [One-time / Annual / Per camera / etc.]

### 10.2 Pricing Structure Options
- **Option 1: Perpetual License**
  - Description: [One-time payment, on-premise deployment]
  
- **Option 2: Subscription/Cloud License**
  - Description: [Annual/monthly subscription]
  
- **Option 3: Hybrid**
  - Description: [Combination approach]

### 10.3 Pricing Components
- Software License: [Perpetual / Annual / etc.]
- AI Modules: [Pricing per module / per camera / package]
- Support & Maintenance: [Included / Separate / AMC]
- Hardware: [If viAct provides / Customer provides]
- Training: [Included / Additional cost]
- On-site Support: [If optional, separate pricing]
- Professional Services: [Custom development, integration, etc.]

### 10.4 Competitor Information (Internal)
- Competitors Mentioned: [If any]
- Competitor Pricing: [If known]
- Competitive Advantages: [viAct's strengths vs competitors]

---

## 11. COMPLIANCE & SECURITY REQUIREMENTS

### 11.1 Data Protection
- GDPR Requirements: [Yes / No / N/A]
- Local Data Protection Laws: [Specific regulations]
- Data Retention Policy: [Requirements]
- Data Processing Location: [Local / Cloud / Hybrid - may affect architecture]
- Access Control: [Who can access what data]

### 11.2 Security Requirements
- Encryption: [At rest / In transit]
- Access Control: [Authentication, authorization]
- Audit Logs: [If required]
- Confidentiality Requirements: [If any special requirements]

### 11.3 Industry-Specific Compliance
- Safety Standards: [If applicable]
- Industry Regulations: [Oil & Gas / Construction / etc.]
- Certification Requirements: [If any]

---

## 12. CUSTOM REQUIREMENTS & SPECIAL CONSIDERATIONS

### 12.1 Custom Hardware/IoT
- Custom Hardware Needed: [Description]
- IoT Devices: [List devices, integration requirements]
- Sensors: [Type, purpose, integration method]

### 12.2 Custom Integrations
- [Integration Name]: [Purpose, method, requirements]

### 12.3 Special Operational Requirements
- Multi-site Management: [If applicable]
- Mobile/Remote Access: [Requirements]
- Offline Operation: [If needed for periods]
- Backup/Redundancy: [Requirements]

### 12.4 Language & Localization
- Dashboard Language: [Required languages]
- Report Language: [Required languages]
- Alert Language: [If custom language needed]

---

## 13. SUCCESS CRITERIA & METRICS (Optional but Recommended)

### 13.1 Key Performance Indicators (KPIs)
- [KPI 1]: [Measurement method, target]
- [KPI 2]: [Measurement method, target]

### 13.2 Project Success Metrics
- [Metric 1]: [How it will be measured]
- [Metric 2]: [How it will be measured]

### 13.3 Evaluation Criteria
- Technical Performance: [What defines success]
- Business Impact: [Expected improvements]
- User Adoption: [Success criteria]

---

## NOTES ON USAGE:

1. **Source of Information**: Most variable information comes from "Deal Transfer" documents which contain:
   - Commercial section (customer info, budget, timeline)
   - Technical section (requirements, infrastructure)
   - Meeting notes (discussions, agreements)

2. **Completeness**: Not all sections will be needed for every project. Include only relevant sections.

3. **Priority**: Some projects are pilot/PoC (smaller scope) vs full deployment (comprehensive).

4. **Customization Level**: Standard modules vs custom development will affect scope and timeline significantly.

5. **Industry Variations**: 
   - Oil & Gas: Heavy on safety, remote locations, harsh environments
   - Manufacturing: Process monitoring, productivity metrics
   - Construction: Safety compliance, temporary sites, mobile deployment
   - Warehousing: Counting, inventory management, process automation

