# Workflows Documentation

This document outlines the two primary workflows within the Communication Hub: **Quick Broadcast (Single Send)** and **Automation Journey (Canvas)** . Both flows are designed with a focus on usability, clarity, and efficiency for HR, communications, and marketing teams.

---

## 1. Quick Broadcast (Single Send)

Use this flow to send a one‑time message to a specific audience.

### 1.1 Entry Point

- **Sidebar Navigation:**  
  The user clicks the **Communication Hub** icon (Pillar 2) in the left sidebar.  
  *What does the user see on the main screen?*  
  The main screen provides an overview of recent sends, scheduled messages, and key metrics—not just a “New Send” button. This context helps users understand the current state before creating a new broadcast.

- **Action Button:**  
  In the top‑right corner, the user clicks the primary button **“+ New Send”**.

- **Workflow Selection (Dropdown/Overlay):**  
  A compact list appears with two options. The user selects **“1. Quick Broadcast (One‑time Alerts)”** .  
  *Design note:* With only two options, a dropdown is acceptable, but consider using a segmented button or two large cards to make the choice more visual and reduce friction.

### 1.2 Step 1: Audience Definition (Modal Overlay – Step 1/4)

- **Interface:**  
  The modal presents a **Smart Segment Picker** – a hybrid control that combines a searchable dropdown with a simple, no‑code query builder.

- **Actions:**  
  - The user can type a segment name (e.g., “All Employees”) and select it from pre‑saved segments.  
  - Alternatively, they can build a custom filter using the **No‑Code Query Builder** (e.g., `Department == 'Headquarters' AND Status == 'Active'`).  
    *UX consideration:* To minimize friction for non‑technical users, the query builder uses plain‑language labels and operators (e.g., “Department equals Headquarters”), and offers suggestions as the user types.

- **Live Preview & Feedback:**  
  At the bottom of the modal, a dynamic counter updates in real time:  
  *“Estimated reach: 2,450 people”*  
  Additionally, a “Preview Audience” link lets the user see a sample list of recipients (e.g., names and roles) to ensure the right people—including executives—are included.

- **Navigation:**  
  The user clicks **“Next: Content”** .

### 1.3 Step 2: Message Composition (Split‑View Interface – Step 2/4)

- **Left Panel – WYSIWYG Editor:**  
  Instead of a JSON‑based editor, the user works with a familiar rich‑text editor (similar to Word or email clients).  
  - They enter a **Title** (e.g., “New Meal Card”).  
  - They compose the **Body** using blocks: paragraph, image, button, etc. The available blocks adapt based on the channels selected later, but for simplicity, the editor includes common elements from the start.

- **Right Panel – Multi‑Channel Live Preview:**  
  Three tabs show how the message will appear on each channel: **[Email] [MS Teams] [WhatsApp]** .  
  *Why include previews now?*  
  Seeing the preview early helps users understand how their content translates across channels (graceful degradation). For example:  
  - **Email:** Rich HTML layout.  
  - **Teams:** Adaptive Card with interactive buttons.  
  - **WhatsApp:** Plain text with a formatted link (images may be omitted if not yet supported).

- **Navigation:**  
  The user clicks **“Next: Channels & Delivery”** .

### 1.4 Step 3: Delivery Configuration (Step 3/4)

- **Channel Selection:**  
  Checkboxes allow the user to select one or more channels (Email, MS Teams, WhatsApp) based on technical availability.

- **Scheduling (not Priority):**  
  Instead of a “priority” selector, the user sets a specific date and time for delivery. For immediate sends, a “Send Now” option is available.  
  *Rationale:* Scheduling aligns with how users naturally think about message timing; urgency can be implied by choosing “Send Now”.

- **Navigation:**  
  The user clicks **“Next: Review”** .

### 1.5 Step 4: Governance & Safety Checks (Step 4/4)

- **Impact Summary:**  
  A prominent card displays:  
  *“You are about to notify 2,450 people across 2 channels.”*

- **Deviation Safeguard:**  
  If the estimated audience size is significantly larger than the user’s typical sends, an extra confirmation appears:  
  *“This volume is above your usual pattern. Confirm mass send?”*

- **Final Action:**  
  The user clicks **“Send Now”** (or “Schedule” if a future time was chosen).

### 1.6 Completion Feedback

- The modal closes, and the user remains on the **Send Feed** (or **Calendar** view for scheduled messages).  
- A green toast notification appears in the top‑right corner:  
  *“Send scheduled.”* (or *“Send in progress…”* for immediate sends)  
- In the feed, a new card appears with real‑time status (e.g., “Sending…” with a progress bar).

---

## 2. Automation Journey (Canvas)

Use this flow to create multi‑step, event‑driven automated campaigns (e.g., onboarding, birthday messages).

### 2.1 Entry Point

From the “+ New Send” menu, the user selects **“2. Automation Journey”** .

### 2.2 Step 1: Blueprint Selection (Smooth Landing)

- **Gallery of Templates (Blueprints):**  
  Instead of an empty canvas, the user sees a gallery of pre‑built journey templates. Options include:
  - **“Blank Canvas”** – Start from scratch.
  - **“Standard Welcome”** – Trigger: Hire Date → Email → Wait 2 days → Teams message.
  - **“Birthday Greetings”** – Trigger: Birthday month → Email.  
    *Note:* Birthdays are handled as recurring triggers (e.g., daily check for birthdays). The same pattern applies to work anniversaries, recognitions, etc. Users can duplicate and customize these blueprints.

- **Action:**  
  The user selects **“Standard Welcome”** to avoid starting from zero.

- **Result:**  
  The canvas loads with the logical structure already in place.

### 2.3 Step 2: The Visual Canvas (Main Interaction)

- **Layout:**  
  - **Left Toolbox:** Draggable nodes categorised as *Triggers* (Clock, ERP Event), *Actions* (Email, Teams), and *Flow Control* (Delay, Condition).  
  - **Central Stage:** The visual flow. For example, the loaded blueprint shows:  
    `[Trigger: Hire Date]` → `[Action: Welcome Email]` → `[Delay: 2 days]` → `[Action: Teams Follow‑up]`.  
  - **Top Toolbar:** Zoom, Undo/Redo, Save Draft, Activate toggle.

- **Editing a Node:**  
  Clicking on a node (e.g., `[Action: Welcome Email]`) opens a **Property Drawer** from the right—no modal overlay, so the user always sees the full flow.

### 2.4 Step 3: Node Configuration (Property Drawer)

- The drawer content mirrors the **Message Composition** step from the Quick Broadcast flow, ensuring consistency:
  - Rich editor (channel‑aware).
  - Preview tabs (Email/Teams/WhatsApp).
  - Variable insertion (e.g., “Hello `{{employee_name}}`”).

- After editing, the user clicks **“Save Node”** and the drawer closes.

### 2.5 Step 4: Adding Logic (Drag & Drop)

- **Scenario:** The user wants to send a Teams reminder 2 days after the welcome email.  
  **Actions:**  
  1. Drag a **“Delay”** node from the toolbox onto the canvas.  
  2. Connect the email node’s output to the delay node’s input.  
  3. Click the delay node and set “Wait: `2` `Days`” in the drawer.  
  4. Drag an **“Action – Teams”** node and connect it after the delay.

- **Handling Multi‑Message Sequences:**  
  *What if a user needs to send multiple messages on specific days (e.g., day 1, day 4, day 8)?*  
  They can add several delay nodes in sequence, each with a different duration. Alternatively, a **“Timeline”** view could be offered as an optional representation—similar to a board with days as columns—but the canvas approach with delays is flexible and aligns with common visual programming patterns. For complex sequences, users can combine delays and multiple action nodes.

### 2.6 Step 5: Validation and Activation

- **Health Check:**  
  Before activation, the system silently validates the flow.  
  - **Error:** Any node that is disconnected or missing content gets a red border and an alert icon. The “Activate” toggle is disabled.  
  - **Success:** All nodes are green.

- **Activation:**  
  The user flips the toggle at the top‑right from **“Inactive”** to **“Active”** .  
  A confirmation modal appears:  
  *“The ‘Welcome’ journey is now active. New employees hired from this point forward will receive these messages.”*

### 2.7 Feedback and Return

- The user is redirected to the **Journeys List** (filtered to “Automations” in the Hub).  
- The newly activated journey appears with a **green (pulsing) status** indicator, meaning it is live and listening for events.

---

## 3. Additional UX Considerations

- **Smart Segment Picker:** Combines search, saved segments, and a no‑code query builder with natural language to reduce the learning curve.
- **Audience Preview:** Allows users to verify recipients, addressing the concern that a count alone doesn’t confirm inclusion of specific individuals (e.g., executives).
- **WYSIWYG Over JSON:** The primary user base (HR, Comms, Marketing) is familiar with rich‑text editors; JSON is hidden.
- **Multi‑Channel Previews:** Shown early to set expectations about how content will appear on each channel.
- **Scheduling Over Priority:** Users think in terms of “when” rather than abstract priority levels.
- **Canvas with Property Drawer:** Keeps the flow visible while editing details.
- **Delay vs. Days:** While “delay” is a flexible concept, the interface can present it in terms of calendar days (e.g., “Wait 7 days”) to match user mental models of day‑based sequences.
- **Blueprint Gallery:** Reduces the intimidation of a blank canvas and accelerates common use cases.
