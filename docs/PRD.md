# CODY Platform Documentation

## 1. Executive Summary

CODY is an internal communication orchestration platform (iPaaS) designed to replace the legacy "EVA" system. The platform centralizes governance for corporate communications (Email, MS Teams, WhatsApp), enabling HR and Communications teams to create automated journeys and one‑time broadcasts.

The strategic objective is to internalize message orchestration—reducing operational costs, increasing data governance, and preparing the architecture for future AI integrations. CODY's key differentiator is its hybrid capability: it serves both HR (through intuitive interfaces) and IT (through robust APIs), leveraging a high‑performance asynchronous architecture. Furthermore, CODY's architecture is designed for modularity and scalability, paving the way for a future evolution into a marketable SaaS product.

---

## 2. Problem Statement & Drivers

- **Cost & Rigidity:**  
  The current system (EVA) has high licensing costs and limits critical customizations needed for current business needs—such as creating new user fields on demand or integrating natively with generative AI tools.

- **Process Latency & Manual Insertion:**  
  Although Active Directory (AD) is the source of truth, there is a natural latency between document receipt, ERP registration, and the propagation of system routines. This gap frequently requires manual user insertion to ensure new hires do not miss critical events (e.g., welcome meetings) while the official sync cycle completes.

- **Operational Gap:**  
  The technical interval between a person's hiring date and their actual processing in the ERP can leave them temporarily "invisible" to system automations, requiring parallel management to ensure a smooth onboarding experience.

- **UX/UI Optimization:**  
  The current solution meets immediate functional needs but presents an opportunity to improve operational efficiency by unifying concepts that currently reside in separate modules ("Flows," "Campaigns," "Acknowledgments"). CODY proposes a consolidated interface to reduce cognitive load and speed up the creation of new communications.

---

## 3. Core Functional Requirements (The 4 Pillars)

### 3.1. Pillar 1: Home / Business Pulse

**Focus:** Operational visibility, impact governance, engagement metrics.

**Strategic KPIs:**
- **Total Send Volume (Month):** Month‑over‑month % change.
- **Unique Reach (Impacted People):** Distinct individuals reached.
- **Active Journeys:** Total workflows currently running.
- **Success Rate:** Confirmed deliveries vs. failures.

**Dashboard Visualizations:**
- **Impact Trend:** Monthly evolution chart (Users Impacted vs. Actions).
- **Channel Distribution (Share of Voice):** Donut chart (Email vs. Teams vs. WhatsApp).
- **Top Impacted Employees:** List of users who receive the most messages (fatigue prevention).
- **Journey Efficiency:** Channel matrix by flow type (e.g., "Agility Journey uses 90% Email, 10% Teams").

**Live Operations:**
- **Send Feed:** List of the last 5 sends with status indicators (green/yellow/red).
- **Business Alerts:** Proactive notifications (e.g., "Birthday flow has had no sends today").

---

### 3.2. Pillar 2: Communication Hub

**Focus:** Centralized send management and flow governance.

**Unified View Strategy (View Switcher):**  
A persistent toggle to switch between two views of the same data:
- **Calendar View:** Monthly/weekly view focused on planning and date collision detection.
- **List View:** Data grid focused on management, status, and bulk actions (Pause/Activate).

**Dual‑Track Creation (Intentional Approach):**
- **Track A – Quick Broadcast:** Simplified wizard (step‑by‑step) for one‑time alerts.
- **Track B – Automation Journey:** Visual canvas for logical flows (Triggers, Delays, Conditionals).

**Blueprints:** Pre‑configured templates that automatically load the canvas (e.g., "Birthdays," "Work Anniversaries").

---

### 3.3. Pillar 3: Audience Explorer

**Focus:** Advanced segmentation and data reconciliation.

**Smart Segments (No‑Code Query Builder):**
- Visual rule builder (AND/OR) using a React‑compatible library (e.g., `react-querybuilder`).
- **Live Preview:** Real‑time impact analysis (user count + visual sample) before saving a rule.
- **Safety Lock:** Standard‑deviation validation before mass sends.

**Manual Onboarding & Reconciliation:**
- **Provisional Registration:** Manually insert an employee (Name, Email, Start Date). The record receives a `manual_entry` tag.
- **Match Waterfall:** A nightly job attempts to merge the manual record with the official ERP record, following this order:
  1. Corporate Email
  2. CPF (Brazilian taxpayer ID)
  3. Personal Email
- **Tags:** Manual management and bulk import (CSV) for quick labeling (e.g., "Race Participants").

---

### 3.4. Pillar 4: Settings & Admin

**Focus:** Governance, security, and SaaS readiness.

**RBAC & Hierarchy:**
- **Global Admin:** Full access, manages custom fields and users.
- **Coordinator:** Visibility restricted to their hierarchical scope (Department/Cost Center).
- **Editor:** Can create and edit; requires approval to send.
- **Viewer:** Read‑only/audit access.

**Data Management:**
- **Custom Fields Manager:** Admin‑only. Create typed fields (stored as JSONB).
- **User Self‑View:** "My Profile" page for employees to audit their own data and tags.

**SaaS Readiness:** A `tenant_id` column is included in all critical tables to support future multi‑tenant segregation.

---

## 4. Technical Strategy & Architecture

### 4.1. Data Integration Strategy (Configurable)

- **ERP (TOTVS):** Reads from views (batch D‑1). Cron schedule and batch size are externalized via environment variables.
- **Identity (Azure AD):** Microsoft Graph API via Delta Query (near real‑time). Polling configuration is externalized.
- **Golden Record Logic:** An internal PostgreSQL (sqlite for dev) database resolves conflicts using configurable precedence rules.

### 4.2. Multi‑Channel Template Engine

- **Abstract Blocks (JSON):** Content is saved in neutral blocks (Header, Paragraph, Image, Action).
- **Graceful Degradation:**
  - **Email:** Full HTML / MJML.
  - **Teams:** Adaptive Cards (colors mapped to semantics).
  - **Other Channels:** Plain text with intelligent formatting (e.g., links).
- **Live Preview:** The editor displays preview tabs.

### 4.3. Technology Stack

- **Backend:** Python (FastAPI)
- **Frontend:** React
- **Database:** PostgreSQL 15+ / sqlite for dev  (heavy use of JSONB)
- **Task Queue:** TaskIQ + Redis

---

## 5. Non‑Functional Requirements (NFRs)

- **Internationalization (i18n):**  
  The MVP focuses only on UI translation via a PT/EN selector. Message content remains the author's responsibility.