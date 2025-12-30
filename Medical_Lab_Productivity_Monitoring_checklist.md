# Items Requiring Confirmation - Medical Lab Productivity Monitoring

> **Project**: Medical Lab Productivity Monitoring System
> **Generated from**: New_DT.xlsx Deal Transfer

## Items Requiring Confirmation

| ID | Section | Item | Question/What to Confirm | Source Reference | Priority |
|----|---------|------|--------------------------|------------------|----------|
| PLACEHOLDER_TIMELINE_001 | 6. IMPLEMENTATION PLAN | Phase T1 Duration | Hardware deployment duration: Client has existing cameras, only need to deploy AI workstation. Confirm if 1 week is sufficient or if additional time needed for server procurement/installation? | S1 - "64 existing CCTV cameras. No hardware supply needed" + S2 - On-premise deployment | Medium |
| PLACEHOLDER_TIMELINE_002 | 6. IMPLEMENTATION PLAN | Phase T2 Duration | Software deployment duration: With 3 custom modules (Workstation Inactivity, Activity Level Detection, Sleep/Man-down), estimated 8-10 weeks. Confirm if this timeline is acceptable or if client expects faster delivery? | S2 - "Any customized AI use cases" = 3 custom modules | High |
| PLACEHOLDER_TIMELINE_003 | 6. IMPLEMENTATION PLAN | Total Timeline vs Client Request | Client requested 3-4 weeks implementation, but realistic timeline with 3 custom modules is 10-14 weeks. This is a significant gap. Clarify with client: (1) Can timeline be extended? (2) Can some modules be delivered in phases? (3) What is the actual deadline/priority? | S1 - "implementation within 3–4 weeks once awarded" vs S2 - 3 custom modules requiring 6-8 weeks each | **CRITICAL** |
| PLACEHOLDER_CAMERA_001 | 2. PROJECT REQUIREMENT STATEMENT, 4. SYSTEM ARCHITECTURE | Number of Cameras for AI Processing | Client has 64 cameras total, but number of cameras for AI processing is "likely 10–20 for key areas" (not confirmed). Confirm: (1) Exact number of cameras for AI? (2) Which cameras/workstations will be monitored? (3) Camera selection criteria? | S1 - "Number of cameras to run AI model not yet defined; customer will confirm (likely 10–20 for key areas)" | **HIGH** |
| PLACEHOLDER_MODULE_001 | 7. PROPOSED MODULES | Workstation Inactivity Threshold | Custom module requires inactivity threshold, but S2 mentions "3–4 hours". Confirm exact threshold: (1) 3 hours or 4 hours? (2) Is this configurable per workstation? (3) What defines "inactive" - no presence or no activity? | S2 - "Workstation inactivity detection (3–4 hours idle alert)" + "alert if no staff for 3–4 hrs" | High |
| PLACEHOLDER_MODULE_002 | 7. PROPOSED MODULES | Activity Level Detection - Active/Inactive Definition | Custom Activity Level Detection module needs clear definition of "active" vs "inactive" states. S2 mentions "Need more data from client for final modeling logic (definition of 'active/inactive')". Request from client: (1) What defines "active work" - specific actions, equipment use, body posture? (2) What defines "inactive" - mobile phone use, sitting idle, away from workstation? (3) Sample videos/images showing both states? | S2 - "Custom 'activity recognition' (detect idle phone use vs. active machine/laptop use)" + "Need more data from client for final modeling logic (definition of 'active/inactive')" | **HIGH** |
| PLACEHOLDER_MODULE_003 | 7. PROPOSED MODULES | Sleep/Man-down Detection Details | Custom Sleep/Man-down Detection module needs clarification: (1) Should this detect lying down in all areas or only specific zones? (2) Should it distinguish between sleep (violation) and man-down (safety incident) or treat all as alerts? (3) Are there areas where lying down is acceptable (break areas, rest areas)? | S2 - "Custom 'sleep/man-down' detection (lying on ground)" | Medium |
| PLACEHOLDER_ARCH_001 | 4. SYSTEM ARCHITECTURE | Site Plan and Camera Positions | S2 states "Site plan & camera position: Not available yet. Customer will provide layout and number of cameras per AI use case later." Request from client: (1) Site layout/floor plan? (2) Camera positions for existing 64 cameras? (3) Which cameras/workstations for each AI use case? (4) Workstation zone definitions? | S2 - "Site plan & camera position: Not available yet. Customer will provide layout and number of cameras per AI use case later" | High |
| PLACEHOLDER_DASHBOARD_001 | 8. USER INTERFACE & REPORTING | Dashboard Detailed Requirements | Custom dashboard requirements need more details: (1) Presence duration - show per day, per week, per month? (2) Active/inactive time - breakdown by hour, shift, workstation? (3) Alerts summary - what information needed? (4) Export format - Excel, PDF, CSV? (5) Real-time updates or batch reports? | S2 - "Any customized Dashboard: Yes – require custom productivity dashboard showing presence duration, active/inactive time per workstation, and alerts summary" | Medium |
| PLACEHOLDER_NETWORK_001 | 5. SYSTEM REQUIREMENTS | Network Bandwidth Confirmation | Estimated external bandwidth 10-20 Mbps for updates/support, local LAN 120-240 Mbps for 10-20 cameras. Confirm: (1) Is current LAN capacity sufficient? (2) External bandwidth available for remote support? (3) Network architecture details? | S2 - "Stable internet connection: Yes – all cameras connected to one rack and control room with stable LAN network. Internet available for remote update and support" | Low |
| PLACEHOLDER_WORKSTATION_001 | 5. SYSTEM REQUIREMENTS | AI Workstation Specifications | Client to provide on-premise server/workstation. Confirm: (1) Client will procure or viAct to specify requirements? (2) Preferred specifications (CPU, GPU, RAM, Storage)? (3) Installation location (control room, server rack)? (4) Delivery timeline? | S2 - On-premise deployment (client provides server) | Medium |
| PLACEHOLDER_INTEGRATION_001 | 3. SCOPE OF WORK | Integration with Existing NVR | Client has existing NVR system. Confirm: (1) NVR brand/model for compatibility? (2) RTSP link configuration - client to provide or viAct to configure? (3) Any NVR integration requirements? (4) Video storage - use existing NVR storage or separate? | S1 - "64 cameras with NVR only" + S2 - "IP-based cameras with RTSP links (64 channels)" | Medium |
| PLACEHOLDER_ALERT_001 | 8. USER INTERFACE & REPORTING | Alert Configuration Details | Alerts via Email and Telegram confirmed. Clarify: (1) Email distribution list (who receives alerts)? (2) Telegram group/bot setup? (3) Alert frequency - immediate, batched, summary? (4) Alert severity levels needed? (5) Escalation rules? | S2 - "How do they want to alert operators on-site: Primarily email and Telegram. SMS not preferred" | Low |
| PLACEHOLDER_BUDGET_001 | General | Budget Confirmation | Budget not confirmed in Deal Transfer. S1 states "Not confirmed. Amro will check with the end client and revert." Follow up required. | S1 - "What are the customer's budget: Not confirmed. Amro will check with the end client and revert" | **HIGH** |
| PLACEHOLDER_COMPETITOR_001 | General | Competitor Pricing | Competitor: Visionify. Customer said demo "was good" and agreed to share competitor price after receiving viAct proposal. Follow up required after proposal submission. | S1 - "Competitors: Competitor: Visionify (another AI vendor from China/India). Customer said that vendor's demo 'was good' but they are waiting for pricing comparison. Agreed to share competitor price after receiving viAct proposal" | Medium |

## Priority Summary

- **CRITICAL (1)**: Timeline discrepancy (3-4 weeks vs 10-14 weeks)
- **HIGH (5)**: Number of cameras, Activity definition, Inactivity threshold, Budget, Module details
- **MEDIUM (7)**: Dashboard details, Workstation specs, Integration, Site plan, Network, Alerts
- **LOW (2)**: Network confirmation, Alert configuration details

## Next Steps

1. **Immediate Actions**:
   - Clarify timeline discrepancy with client (PLACEHOLDER_TIMELINE_003)
   - Confirm exact number of cameras for AI processing (PLACEHOLDER_CAMERA_001)
   - Request activity definition details from client (PLACEHOLDER_MODULE_002)
   - Follow up on budget confirmation (PLACEHOLDER_BUDGET_001)

2. **Before Proposal Submission**:
   - Request site plan and camera positions (PLACEHOLDER_ARCH_001)
   - Clarify inactivity threshold (PLACEHOLDER_MODULE_001)
   - Get detailed dashboard requirements (PLACEHOLDER_DASHBOARD_001)

3. **After Proposal Submission**:
   - Follow up on competitor pricing (PLACEHOLDER_COMPETITOR_001)
   - Confirm workstation specifications (PLACEHOLDER_WORKSTATION_001)
   - Finalize integration details (PLACEHOLDER_INTEGRATION_001)

