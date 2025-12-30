# Technical Proposal Template - Complete Structure

> **Project**: Medical Lab Productivity Monitoring System
> **Generated from**: New_DT.xlsx Deal Transfer

---

## 1. COVER PAGE

| Content | Source/Guidance |
|---------|------------------|
| Company Logo | Standard viAct logo |
| Proposal Title | AI-Powered Video Analytics Solution for Medical Lab Workforce Monitoring |
| Client Name | Medical Laboratory (via Farha International Holding Group) |
| Date | [CURRENT_DATE] |
| Duration | 3-4 weeks implementation (post-award) + ongoing maintenance |

---

## 2. PROJECT REQUIREMENT STATEMENT

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **Project** | AI-Powered Video Analytics for Medical Lab Workforce Monitoring and Productivity Tracking<br>**Source**: S1 - "Current Pain Points" → Converted to positive objective |
| **Project Owner** | Medical Laboratory (KSA)<br>**Source**: S1 - "If SI, provide overview of end-customer" |
| **Work Scope** | On-premise AI system to monitor workforce presence, activity levels, and productivity in medical laboratory workstations<br>**Components**:<br>1. Deployment method: On-premise (Source: S2 - "Specific HW/SW requirements")<br>2. AI system<br>3. Primary objective: Workforce monitoring and productivity tracking (from pain points) |
| **Project Duration** | Implementation: 3-4 weeks post-award<br>**Source**: S1 - "If real project, expected timeline" |
| **Camera Number** | 10-20 cameras (to be confirmed by customer for key areas)<br>**Source**: S1 - "If VA: camera status & scope" - "likely 10–20 for key areas" |
| **Number of AI Module per Camera** | Estimated 2-3 AI modules/camera<br>**Logic**: Based on use cases (workforce presence, inactivity, activity level, sleep/man-down, PPE mask) |
| **AI Modules** | 1. Workforce Presence Detection<br>2. Workstation Inactivity Detection (Custom)<br>3. Activity Level Detection (Custom)<br>4. Sleep/Man-down Detection (Custom)<br>5. PPE Mask Compliance Detection<br>**Source**: S2 - "List of VA use cases" → Convert to module names |

### 2.1 Project Objectives / Work Scope Statement

**Primary Objective:**
- Implement AI-powered workforce monitoring system to track employee presence and productivity in medical laboratory workstations in real-time

**Secondary Objectives:**
- Monitor workstation activity levels and detect inactive/idle periods
- Alert management when workstations are unstaffed for extended periods (3-4 hours)
- Ensure PPE compliance (mask wearing) for laboratory safety
- Detect safety incidents (man-down/sleep detection)
- Provide productivity insights through custom dashboard analytics

**Source from Deal Transfer:**
- **Derive from**: S1 - "Current Pain Points of end customer"
- **Logic**: Convert pain points into positive objectives
  - Pain point: "No AI capability on existing CCTV system" → Objective: "Implement AI analytics on existing CCTV"
  - Pain point: "Need to monitor employee presence and activity level" → Objective: "Real-time workforce presence and activity monitoring"
  - Pain point: "Lack of visibility into inactive staff (idle, using phones)" → Objective: "Detect and alert on staff inactivity and mobile phone usage"
  - Pain point: "No system to alert when areas are unstaffed for hours" → Objective: "Automated alerts for unstaffed workstations (>3-4 hours)"
  - Pain point: "Requires on-premise solution" → Objective: "On-premise deployment for data security"

**Note**: Stakeholders, Decision Makers not included in proposal (internal Deal Transfer info only)

---

## 3. SCOPE OF WORK

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **viAct Responsibilities** | Software: License, maintenance, support<br>Camera integration: Integration with existing 64 IP cameras via RTSP links<br>AI Modules: Workforce Presence Detection, Workstation Inactivity Detection (Custom), Activity Level Detection (Custom), Sleep/Man-down Detection (Custom), PPE Mask Compliance Detection<br>Custom Dashboard Development: Productivity dashboard with presence duration, active/inactive time per workstation, alerts summary<br>**Source**: S2 - "Specific HW/SW requirements (deployment method)?" = On-premise + S2 - "List of VA use cases" + S2 - "Any customized Dashboard" |
| **Client Responsibilities** | Hardware: Existing cameras (64 IP cameras) and NVR are provided and maintained by client<br>Network Infrastructure: LAN network, control room infrastructure (client maintains)<br>On-premise Server/Workstation: Client to provide server/workstation for AI processing (on-premise deployment)<br>Camera Configuration: Client provides RTSP links for cameras<br>Power Supply: Centralized rack power (client maintains)<br>**Source**: S1 - "If VA: camera status & scope" = "64 existing CCTV cameras (NVR-based, IP cameras). No hardware supply needed" + S2 - "Specific HW/SW requirements" = On-premise |

**Note**: Use available slide template for Scope of Work, add specific requirements if customer has special needs.

---

## 4. SYSTEM ARCHITECTURE

> **First Step**: Deployment method = On-Premise → Select On-Premise architecture

| Content | Source/Guidance |
|---------|------------------|
| **Deployment Method: On Premise** | **Source**: S2 - "Specific HW/SW requirements (deployment method)?" = "On-premise deployment is mandatory"<br>**Inputs needed**:<br>+ Number of Camera: 10-20 cameras (to be confirmed) for AI processing<br>+ List AI modules: Workforce Presence, Inactivity Detection, Activity Level Detection, Sleep/Man-down Detection, PPE Mask Detection<br>**Reference KB**:<br>- Architecture: KB "DOCUMENT" → Search "Architecture" (On-Premise variants)<br>- Slide: System_architecture.pdf (On Premise - slide 6, 8) |
| **Other Components** | NVR (Network Video Recorder) - existing, provided by client<br>Centralized Control Room - existing infrastructure<br>AI Workstation - to be deployed on-premise (client to provide)<br>**Source**: S1 - "64 cameras with NVR only" + S2 - On-premise deployment requirement |

### 4.1 Architecture Diagram Description

**Detailed Technical Description for the System Architecture section** (Blueprint for designer to create visual slide):

**Data Flow:**
- Existing IP Cameras (64 cameras) → NVR (existing) → RTSP Links → AI Workstation (on-premise) → Local Dashboard (Control Room)
- Alert flow: AI Workstation → Email/Telegram notifications → Dashboard alerts
- External connection: Only for software updates and AI retraining (internet allowed for updates only)

**Hardware Components Placement:**
- AI Workstation: Located in control room or server rack (on-premise)
- NVR: Existing, maintained by client
- Existing Cameras: 64 IP cameras, connected to NVR
- AI Processing: 10-20 cameras selected for AI analytics

**Network Topology:**
- Local Area Network (LAN): All cameras connected to one rack and control room (stable LAN network)
- Internet connectivity: Available for remote updates and AI retraining support (external connection allowed for updates only)
- No cloud processing: 100% local server processing (on-premise mandatory)

**System Layers:**
- Edge Layer: At site (existing IP cameras)
- Processing Layer: On-premise AI Workstation (local server)
- Application Layer: Local Dashboard (Control Room) + Email/Telegram alerts

**Source from Deal Transfer:**
- **Derive from**: All technical requirements combined (S2)
- **Logic**: On-premise deployment, existing cameras, stable LAN, external internet for updates only

---

## 5. SYSTEM REQUIREMENTS

### Common Items (Always Present):

| Content | Source/Guidance |
|---------|------------------|
| **Network** | **If Deployment method is On-premise**:<br>+ External bandwidth: Internet bandwidth for remote access, software updates, and AI retraining support (estimate: 10-20 Mbps)<br>+ Per-camera bandwidth: 12 Mbps/Camera (for AI processing cameras)<br>+ Total system bandwidth: 12 Mbps × [10-20 cameras] = 120-240 Mbps (local LAN)<br>**Calculation**:<br>- External bandwidth: 10-20 Mbps (for updates and support)<br>- Per-camera bandwidth: 12 Mbps (local LAN)<br>- Total system bandwidth: 120-240 Mbps (for 10-20 cameras on LAN)<br>**Source**: S2 - "Stable internet connection?" = "Yes – all cameras connected to one rack and control room with stable LAN network. Internet available for remote update and support" |
| **Camera** | **Standard Specifications**:<br>+ Resolution: 1080p@25fps (minimum)<br>+ Connectivity Type: IP-based cameras with RTSP support<br>**Output Format**:<br>+ Resolution: Existing IP cameras (to be confirmed with client)<br>+ Frame rate: Standard (25-30fps typical for IP cameras)<br>+ Connectivity Type: IP, RTSP<br>**Source**: S2 - "Can client camera provide RTSP link?" = "Yes – IP-based cameras with RTSP links (64 channels)"<br>**Note**: Client has existing cameras - specifications to be confirmed |
| **AI Inference Workstation, AI Training Workstation, Dashboard** | **Input from Deal Transfer**:<br>+ Number of cameras: 10-20 cameras (for AI processing)<br>+ Number of AI modules/camera: 2-3 modules/camera (average)<br>**Output**:<br>+ Template: Slide 7 System Architecture Slide (System_architecture.pdf)<br>+ Calculate Workstation specs: Use file "AI_Workstation_Calculator" + Knowledge Base<br>**Reference KB**:<br>- Search KB "DOCUMENT" for workstation specifications<br>- Use AI_Workstation_Calculator.xlsx to calculate based on camera count and modules<br>**Standard Specs (Reference for 10-20 cameras, 2-3 modules/camera)**:<br>- CPU: Core i7/i9 (based on load)<br>- GPU: RTX series (based on AI module complexity)<br>- RAM: 32-64GB (based on camera count)<br>- Storage: 2TB+ (based on retention needs) |
| **Additional Equipment** | None required - using existing infrastructure<br>**Source**: S2 - "Any customized HW / IoT?" = "No custom hardware required. Using existing IP cameras and NVR" |

### 5.1 Power Requirements

| Content | Source/Guidance |
|---------|------------------|
| **Power Source** | Stable centralized rack power<br>**Source**: S2 - "Stable power source?" = "Yes – all cameras and NVR powered from centralized rack" |

---

## 6. IMPLEMENTATION PLAN (TIMELINE)

### Common Items (Always Present):

### 6.1 Key Milestones

- **Proposal submission date**: [CURRENT_DATE]
- **Project award date** (T0): [To be confirmed]
- **Hardware deployment** (T1): [PLACEHOLDER_TIMELINE_001]
- **Software deployment** (T2): [PLACEHOLDER_TIMELINE_002]
- **Integration period** (T3): 2-4 weeks
- **Handover / completion** (T4): End of T3

### 6.2 Phasing Structure

| Phase | Description | Duration | Source/Guidance |
|-------|-------------|----------|-----------------|
| **Phase T0** | Project Award / Contract Signed | — | **Source**: S1 - "If real project, expected timeline" = "No official tender deadline. End client requested implementation within 3–4 weeks once awarded" → Start date TBD |
| **Phase T1** | Hardware Deployment | 1 week | **Logic**:<br>- Customer has existing cameras: 1-2 weeks (mainly server/workstation deployment)<br>- Since cameras exist, only need to deploy AI workstation<br>**Source**: S1 - "If VA: camera status & scope" = "64 existing CCTV cameras" → Cameras exist, minimal hardware deployment |
| **Phase T2** | Software Deployment | 6-8 weeks | **Logic**: Depends on number of modules and classification<br>- Standard Modules (Workforce Presence, PPE Mask): 2 weeks integration<br>- Custom Modules (Workstation Inactivity, Activity Level Detection, Sleep/Man-down Detection): 6-8 weeks per module × 3 modules = 18-24 weeks (but can be parallelized to 8-10 weeks)<br>- Custom Dashboard: 2-3 weeks<br>- **Estimate**: 8-10 weeks total (with parallel development)<br>**Source**: S2 - "List of VA use cases" → Identify standard vs custom (check S2 - "Any customized AI use cases") = 3 custom modules |
| **Phase T3** | System Integration & Handover / UAT | 2-4 weeks | **Standard**: 2-4 weeks<br>**Includes**: Integration testing, UAT, training, dashboard customization |

**Source from Deal Transfer:**
- **Primary source**: S1 - "If real project, expected timeline" = "implementation within 3–4 weeks once awarded"
- **Note**: Client requested 3-4 weeks implementation, but with 3 custom modules, realistic timeline is 10-14 weeks. This needs clarification [PLACEHOLDER_TIMELINE_003]
- **Logic**:
  - Custom modules → Add development time (6-8 weeks per custom module, but can parallelize)
  - Custom dashboard → Add 2-3 weeks

---

## 7. PROPOSED MODULES & FUNCTIONAL DESCRIPTION

### Common Items (Always Present):

### 7.1 Module Classification

**Divide modules into:**
- **Standard AI Modules**: Workforce Presence Detection, PPE Mask Compliance Detection (available in KB, can reuse existing descriptions)
- **Custom Modules**: Workstation Inactivity Detection, Activity Level Detection, Sleep/Man-down Detection (need to create new descriptions based on customer requirements)

**Source**: S2 - "List of VA use cases" → Check against `standard_AI_modules.md` to determine if standard or custom

### 7.2 Module Description Template

**For EACH module (both Standard and Custom), fill in the following template:**

#### Module 1: Workforce Presence Detection
| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | Workforce Presence Detection | **Source**: S2 - "List of VA use cases" → "Workforce presence detection" |
| **Module Type** | Standard | **Logic**: General presence detection is standard functionality |
| **Purpose Description** | Detects and monitors employee presence at workstation locations in real-time. Provides visibility into which workstations are staffed and tracks presence duration for productivity analysis. | **Source**: Standard presence detection module - derived from S2 use case |
| **Alert Trigger Logic** | Continuously monitors workstation areas. Alerts can be configured for presence/non-presence events as needed for dashboard analytics. | **Source**: Standard logic for presence detection |
| **Detection Criteria** | Detects human presence within defined workstation zones. Tracks presence duration for reporting. | **Source**: Standard detection criteria |
| **Preconditions** | Camera must maintain a suitable distance for clear observation of workstations, typically between 5 to 10 meters. Camera angle should provide clear view of workstation areas. | **Standard Template**: 5-10 meters for general detection |

#### Module 2: Workstation Inactivity Detection (Custom)
| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | Workstation Inactivity Detection | **Source**: S2 - "List of VA use cases" → "Workstation inactivity detection (3–4 hours idle alert)" |
| **Module Type** | Custom | **Logic**: Custom requirement for 3-4 hour inactivity threshold |
| **Purpose Description** | Detects when workstations are inactive (unstaffed) for extended periods (3-4 hours) and alerts management. Provides visibility into unstaffed workstation areas to optimize workforce allocation. | **Source**: S2 - "Any customized AI use cases" → "Custom 'workstation presence' detection (alert if no staff for 3–4 hrs)" |
| **Alert Trigger Logic** | Alert triggers when a workstation area is detected as unstaffed (no worker presence) for more than 3-4 hours continuously. Alert sent via email/Telegram to notify management. | **Source**: S2 - "Any customized AI use cases" = "alert if no staff for 3–4 hrs" |
| **Detection Criteria** | Monitors workstation zones for worker presence. If no presence detected for threshold duration (3-4 hours), triggers alert. | **Source**: S2 custom use case description |
| **Preconditions** | Camera must maintain a suitable distance for clear observation of workstation areas, typically between 5 to 10 meters. Camera should be positioned to cover workstation zones clearly. | **Standard Template**: 5-10 meters unless specified |
| **Client Data Requirements** | Request: Provide workstation layout and camera positioning information. Define workstation zones for monitoring. Clarify exact inactivity threshold (3 hours vs 4 hours). | **Source**: S2 - "Site plan & camera position" = "Not available yet. Customer will provide layout and number of cameras per AI use case later" |

#### Module 3: Activity Level Detection (Custom)
| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | Activity Level Detection / Employee Productivity Detection | **Source**: S2 - "List of VA use cases" → "Employee productivity/activity level detection (mobile detection, sleep detection)" |
| **Module Type** | Custom | **Logic**: Custom requirement for activity recognition (idle phone vs active work) |
| **Purpose Description** | Detects and differentiates between active work (machine/laptop use) and inactive/idle behavior (mobile phone use, inactivity). Provides productivity insights by tracking activity levels at workstations. | **Source**: S2 - "Any customized AI use cases" → "Custom 'activity recognition' (detect idle phone use vs. active machine/laptop use)" |
| **Alert Trigger Logic** | Detects and classifies activity types: active work (using machines/laptops) vs. inactive/idle (mobile phone use, no active work). Alerts can be configured for extended idle periods or specific inactivity thresholds. | **Source**: S2 custom use case - "detect idle phone use vs. active machine/laptop use" |
| **Detection Criteria** | Distinguishes between: (1) Active work: worker interacting with machines, laptops, equipment; (2) Inactive/idle: worker using mobile phone, not engaged in work tasks. Requires definition of "active" vs "inactive" states. | **Source**: S2 - "Need more data from client for final modeling logic (definition of 'active/inactive')" |
| **Preconditions** | Camera must maintain a suitable distance for clear observation of workstation activities, typically between 3 to 5 meters for detailed activity detection. Camera angle must provide clear view of worker's hands and workspace. | **Standard Template**: 3-5 meters for detailed detection |
| **Client Data Requirements** | Request: Provide sample images/videos showing active work (machine/laptop use) vs inactive/idle states (mobile phone use). Define specific criteria for "active" vs "inactive" states. Provide workstation layouts for camera positioning. | **Source**: S2 - "Need more data from client for final modeling logic (definition of 'active/inactive')" |

#### Module 4: Sleep/Man-down Detection (Custom)
| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | Sleep/Man-down Detection | **Source**: S2 - "List of VA use cases" → "Man-down (laying down) / sleep detection" |
| **Module Type** | Custom | **Logic**: Custom requirement combining sleep and man-down detection |
| **Purpose Description** | Detects when workers are lying down (either sleeping or man-down incidents) in workstation areas. Provides safety monitoring and ensures alert response for potential incidents or violations. | **Source**: S2 - "Any customized AI use cases" → "Custom 'sleep/man-down' detection (lying on ground)" |
| **Alert Trigger Logic** | Alert triggers when a person is detected lying on the ground/floor in monitored areas. Alert sent immediately via email/Telegram for safety response. | **Source**: S2 custom use case - "lying on ground" detection |
| **Detection Criteria** | Detects horizontal body position (lying down) in workstation areas. Can distinguish between sleep (violation) and man-down (safety incident) based on context if needed. | **Source**: S2 custom use case description |
| **Preconditions** | Camera must maintain a suitable distance for clear observation of floor areas, typically between 5 to 10 meters. Camera angle should provide clear view of floor/ground level in workstation zones. | **Standard Template**: 5-10 meters for general detection |
| **Client Data Requirements** | Request: Provide sample images/videos showing workers lying down scenarios. Define areas where lying down should trigger alerts. | **Source**: S2 custom use case |

#### Module 5: PPE Mask Compliance Detection
| Field | Content | Source/Guidance |
|-------|---------|------------------|
| **Module Name** | PPE Mask Compliance Detection / Mask Violation Detection | **Source**: S2 - "List of VA use cases" → "PPE compliance (mask violation)" |
| **Module Type** | Standard | **Logic**: Mask detection is standard PPE compliance module |
| **Purpose Description** | Detects workers not wearing masks in laboratory workstations. Ensures PPE compliance for laboratory safety standards and provides real-time alerts for mask violations. | **Source**: Standard PPE mask detection - from S2 use case |
| **Alert Trigger Logic** | Alert triggers when a worker is detected without a mask in monitored workstation areas. Alert sent via email/Telegram immediately upon detection. | **Source**: Standard PPE compliance logic |
| **Detection Criteria** | Detects presence/absence of mask on worker's face. Can be configured for specific workstation zones where mask is mandatory. | **Source**: Standard detection criteria |
| **Preconditions** | Camera must maintain a suitable distance for clear observation of worker's face, typically between 3 to 5 meters. Camera angle must provide clear view of worker's face area. Avoid glare or obstructions. | **Standard Template**: 3-5 meters for detailed face detection |

### 7.3 Process for Filling Module Descriptions

Completed for all 5 modules above.

---

## 8. USER INTERFACE & REPORTING

### Common Items (Always Present):

### 8.1 Alerts & Notifications

| Content | Source/Guidance |
|---------|------------------|
| **Channels** | Email and Telegram notifications<br>**Source**: S2 - "How do they want to alert operators on-site?" = "Primarily email and Telegram. SMS not preferred (too many notifications)"<br>**Logic**: Client specifically requested Email + Telegram (not SMS) |

### 8.2 Dashboard Visualizations

| Content | Source/Guidance |
|---------|------------------|
| **Event Analysis** | Charts and graphs of detection frequencies<br>**Source**: Standard feature, mention if customer needs specific KPIs |
| **Alert Timelines** | Chronological view of incidents<br>**Source**: Standard feature |
| **Evidence Snapshots** | Image/Video clips of the detected event<br>**Source**: Standard feature |
| **Custom KPIs** | **Custom Productivity Dashboard** required:<br>- Presence duration per workstation<br>- Active/inactive time per workstation<br>- Alerts summary<br>**Source**: S2 - "Any customized Dashboard" = "Yes – require custom productivity dashboard showing presence duration, active/inactive time per workstation, and alerts summary" |
| **Multi-Dashboard** | Local dashboard in control room (on-premise)<br>**Source**: On-premise deployment - dashboard runs locally |

### 8.3 Daily / Weekly Summary Reports

| Content | Source/Guidance |
|---------|------------------|
| **Automated Reporting Features** | Custom productivity dashboard with:<br>- Presence duration tracking<br>- Active/inactive time per workstation<br>- Alerts summary<br>**Source**: S2 - "Any customized Dashboard" → Dashboard requirements include summary of activities<br>**Format**:<br>- Time range: Configurable<br>- Export: Dashboard visualization (Excel/PDF export if needed)<br>- Filtering: By workstation, time period, event type |

---

## SUPPORTING SECTIONS (Use to inform main sections above)

### A. Compliance & Security Requirements

**Use this information to inform:**
- System Architecture (deployment method selection) → On-premise (mandatory)
- System Requirements (data storage location) → Local storage on-premise
- Integration Points (data handling) → No external data sharing

**Source from Deal Transfer:**
- S2 - "Any GDPR / data privacy requirements?" = "Not mentioned. (Saudi Arabia jurisdiction – likely not GDPR-bound.)"
- S2 - "Specific HW/SW requirements" = "On-premise deployment is mandatory. 100% local server. External internet connection allowed for updates and AI retraining only"
- **Logic**:
  - On-premise deployment ensures data stays local (sensitive medical lab environment)
  - External internet only for software updates and support (no data transmission)

### B. Custom Requirements

**Use this information to inform:**
- AI Modules (custom modules needed → Section 7): 3 custom modules identified
- System Architecture (custom integrations → Section 4): No custom integrations, standard on-premise
- System Requirements (custom hardware → Section 5): No custom hardware
- Dashboard/Reporting (custom features → Section 8): Custom productivity dashboard required

**Source from Deal Transfer:**
- S2 - "Any customized AI use cases (description & videos)?" → 3 Custom Modules (Section 7)
- S2 - "Any customized dashboard?" → Custom Productivity Dashboard (Section 8)
- S2 - "Any customized HW / IoT?" = "No custom hardware required"
- **Logic**:
  - 3 custom modules → Timeline adjustment (Section 6): Add 6-8 weeks per module (can parallelize)
  - Custom dashboard → Dashboard requirements section (Section 8): 2-3 weeks development

---

## MAPPING GUIDE: Deal Transfer → Proposal

### Step-by-Step Conversion Process Applied:

#### Step 1: Extract Project Basics ✓
- Customer name → Medical Laboratory (via Farha International Holding Group)
- Solutions they want → AI Video Analytics for workforce monitoring
- Timeline → 3-4 weeks (client request, but needs adjustment for custom modules)

#### Step 2: Convert Pain Points to Objectives ✓
- Converted all 5 pain points to positive objectives (Section 2.1)

#### Step 3: Map Use Cases to Modules ✓
- Mapped 5 use cases to 5 modules (3 custom, 2 standard)

#### Step 4: Determine Architecture ✓
- On-premise (mandatory) → On-premise architecture selected

#### Step 5: Define Responsibilities ✓
- Client has cameras → Client handles HW, viAct handles software
- On-premise → Client provides server/workstation

#### Step 6: Calculate Timeline ✓
- Custom modules → Added development time
- Estimated 10-14 weeks (needs confirmation - placeholder created)

#### Step 7: Configure Alerts & Dashboard ✓
- Email + Telegram (client specified)
- Custom productivity dashboard requirements extracted

#### Step 8: Calculate System Requirements ✓
- Network, camera, workstation requirements calculated

---

## COMMON PATTERNS & LOGIC

This project follows **Pattern: Operations-Focused Projects** with custom productivity monitoring:
- **Typical Modules**: Workforce Presence, Activity Detection, Productivity Tracking
- **Typical Architecture**: On-premise (data security for medical lab)
- **Typical Timeline**: Extended due to custom modules (10-14 weeks vs. standard 4-6 weeks)

---

## NOTES FOR PRESALE TEAM

1. **Deal Transfer Reviewed**: New_DT.xlsx processed ✓

2. **Pain Points → Objectives**: Converted 5 pain points to objectives ✓

3. **Use Cases → Modules**: Mapped 5 use cases, identified 3 as custom ✓

4. **Architecture Decision**: On-premise (mandatory requirement) ✓

5. **Timeline Realism**: 
   - Client requested: 3-4 weeks
   - Realistic with custom modules: 10-14 weeks
   - **Action Required**: Clarify timeline with client [PLACEHOLDER_TIMELINE_003]

6. **Responsibilities Clarity**: Clearly defined (client has cameras, on-premise server) ✓

7. **Custom Requirements**: 3 custom modules + custom dashboard identified ✓

8. **Missing Information**: 
   - Number of cameras for AI: 10-20 (to be confirmed) [PLACEHOLDER_CAMERA_001]
   - Exact inactivity threshold: 3 vs 4 hours [PLACEHOLDER_MODULE_001]
   - Active/inactive definition: Need client input [PLACEHOLDER_MODULE_002]
   - Site plan and camera positions: To be provided [PLACEHOLDER_ARCH_001]

9. **KB Reference**: Standard modules (Workforce Presence, PPE Mask) can reference KB ✓

10. **Module Description Template**: All 5 modules filled with template structure ✓

