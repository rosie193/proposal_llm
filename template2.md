# 1. COVER PAGE

Company Logo

| Content | Source/Guidance |
|---------|------------------|
| Proposal Title | |
| Client Name | |
| Duration time | |

---

# 2. PROJECT REQUIREMENT STATEMENT

**Source Reference:**
- **S1:** Commercial Sheet (File New Deal Transfer)
- **S2:** Technical Sheet (File New Deal Transfer)
- **Sx:** Other sheets (File New Deal Transfer)

| Content | Source/Guidance |
|---------|------------------|
| Project | General paint point Example: POC AI-Powered Video Analytics for Safety Monitoring Source: S1-"Current Pain Points of end customer" |
| Project Owner | Customer overview - Customer name Source: S1 - "Customer overview (short introduction about customer business)" |
| Work Scope | Deployment method (Source: S2 - "Any specific HW/SW requirements such as deployment method?") + AI system + General project description Example: On premise AI system to Monitor Vessel Safety in Real time |
| Project Duration | Source: S1 - "If real project, please specific the expected timeline (including tender process if available)" |
| Camera Number | Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?" |
| Number of AI Module per Camera | Suggest base on customer pain point, if not mentioned then suggest the average number is 3 - 4 AI modules/ cameras |
| AI Modules | Source: S2 - "List of VA use cases" |

---

# 3. SCOPE OF WORK

Scope of Work: available slide, will add requirement if have specific requirement from client in

| Content | Source/Guidance |
|---------|------------------|
| viAct | Software: license, maintenance, support |
| | Camera integration |
| Client | Hardware: procurement, configuration, installation, and maintenance |
| | Other Requirement if needed |

---

# 4. SYSTEM ARCHITECTURE
First,  chooose  deployment method  -->  architecture

Architecture (On Premise, On Cloud, ...)

Source: (Deal Transfer + Knowledge base +..) => Draw architecture slides.

| Content | Source/Guidance |
|---------|------------------|
| Deployment method (Source: S2 - "Specific HW/SW requirements (deployment method)?"): On cloud | Deal Transfer: need update<br>+ Number of Camera: Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?"<br>+ List AI modules: Source: S2 - "List of VA use cases"<br>Reference KB:<br>- Architecture: KB "Architecture"<br>Slide System Architecture(On Cloud-Slide 4): System_architecture.pdf |
| Deployment method (Source: S2 - "Any specific HW/SW requirements such as deployment method?"): On Premise | Deal Transfer: need change<br>+ Number of Camera: Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?"<br>+ List AI modules: Source: S2 - "List of VA use cases"<br>Reference:<br>- Architecture: KB "Architecture"<br>Slide System Architecture (On Premise- slide 6,8): System_architecture.pdf |
| Deployment method (Source: S2 - "Any specific HW/SW requirements such as deployment method?"): Not mentioned -> Suggest Hybrid | Deal Transfer: need change<br>+ Number of Camera: Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?"<br>+ List AI modules:Specific HW/SW requirements (deployment method)? Source: S2 - "List of VA use cases"<br>Reference KB:<br>- Architecture: KB "Architecture"<br>Slide System Architecture (Hybrid- slide11): System_architecture.pdf |

| Other Component | Add other HW component like NVR/ VPN Bridge if needed |


Detailed Technical Description for the System Architecture section. This should serve as a blueprint for a designer to create the visual slide. Include:

Data Flow: Trace the path from Camera -> Network Switch -> AI Workstation -> Cloud/Dashboard.

Hardware Components: Placement of AI Workstation, NVR, VPN Bridge, and peripheral devices (speakers, kiosks, etc.).

Network Topology: Distinction between Local Area Network (LAN) for cameras and Wide Area Network (WAN) for dashboard access.

System Layers: Clear separation between Edge (at site), Cloud (storage/backend), and Application layers (Mobile/Web).
---

# 5. SYSTEM REQUIREMENTS

| Content | Source/Guidance |
|---------|------------------|
| Network | + If Deployment method (Source: S2 - "Specific HW/SW requirements (deployment method)?") is On-premise or Hybrid: External bandwidth: Internet bandwidth for remote access and updates<br>+ Per-camera bandwidth: 12 Mbps/ Camera. Total: 12Mbps x Number of Camera (Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?")<br>Output:<br>+ External bandwidth: [Value]<br>+ Per-camera bandwidth: [Value]<br>+ Total system bandwidth: [Value] |
| Camera | + Resolution: 1080p@25fps<br>+ Connectivity Type: IP-based cameras with RTSP support<br>Output:<br>+ Resolution: [e.g., 1080p, 4K]<br>+ Frame rate: [e.g., 25fps, 30fps]<br>+ Connectivity Type: [e.g., IP, RTSP] |
| AI Inference Work Station, AI Training Work Station, Dashboard | Deal transfer input:<br>+ Number of camera (Source: S1 - "If VA, do they already have camera installed? Do we need to handle HW implementation? How many camera they would like to run AI model?")<br>+ Number of AI modules/ camera (Suggest base on customer pain point, if not mentioned then suggest the average number is 3 - 4 AI modules/ cameras)<br>Output:<br>+ Template: Slide 7 System Architecture Slide (System_architecture.pdf)<br>+ Calculate WS spec: file  AI_Workstation_Calculator + Knowledge Base: Search and get suggest for WS spec |
| Additional Equipment | Access control devices, kiosks, sensors, etc. |

---

# 6. IMPLEMENTATION PLAN

## Key Milestones

- **Proposal submission date**
- **Project award date**
- **Hardware deployment**
- **Software deployment**
- **Integration period**
- **Handover / completion**

## Phasing Structure

| Phase | Description | Duration |
|-------|-------------|----------|
| **Phase T0** | Project Award | — |
| **Phase T1** | Hardware Deployment | X weeks|
| **Phase T2** | Software Deployment | X weeks (Depend on number of Modules and classification of Standard/ Customize<br>Standard Modules: 4-6 weeks<br>Customize Modules: 6-8 weeks)|
| **Phase T3** | System Integration & Handover | X weeks (2-4 weeks) |

---

---

# 7. PROPOSED MODULES & FUNCTIONAL DESCRIPTION

Divde to standard / custom  module (give  a file  contain standard module  base on   KB:  Search for same use case in KB)

(but all module follow this block below)
Module: [Insert Module Name]
• Purpose Description: Describe what this module detects and why it matters.  
• Alert Trigger Logic: When does it alert? (e.g., "Alert triggers when a person crosses line A").  
• Client Data Requirements: Images, video samples, or labels required for training.  
• Preconditions: Camera angle, height, lighting requirements.  


| Content | Source/Guidance |
|---------|------------------|
| Standard AI modules (KB) | Input:<br>+ Standard AI Modules name<br>Reference:<br>1. Search for same use case in KB<br>2. Copy the same Slide AI modules Use case from KB<br>3. If Client have footage -> insert image to slice<br>Output:<br>+ insert available slides |
| Customize Modules | Input:<br>+ Description of Customize Modules<br>Reference:<br>1. Search or create use case image with description form outline<br>2. Use Gemini/Veo3 to create image/video if needed<br>3. Insert image/video in slide and draw red bounding box around violation area.<br>4. Insert the Slide content, include:<br>+ Purpose<br>+ Alert<br>+ Request (provide object types image for model training)<br>+ Pre-condition: Camera must maintain a suitable distance for clear observation of object, typically between ... to ... meters (5 to 10 meters)<br>Output:<br>+ a slide with description and image |

---

# 8. USER INTERFACE & REPORTING

## 8.1. Alerts & Notifications

| Content | Source/Guidance |
|---------|------------------|
| Channels | Email, Mobile App, SMS, ... |

## 8.2. Dashboard Visualizations

| Content | Source/Guidance |
|---------|------------------|
| Event Analysis | Charts and graphs of detection frequencies. |
| Alert Timelines | Chronological view of incidents. |
| Evidence Snapshots | Image/Video clips of the detected event. |

## 8.3. Daily / Weekly Summary Reports

| Content | Source/Guidance |
|---------|------------------|
| Automated reporting features | sent to stakeholders. |

---

