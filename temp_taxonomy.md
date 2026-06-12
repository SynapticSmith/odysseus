To help you manage the 576 open issues for the Odysseus project, I have analyzed the provided list alongside the codebase architecture. By aligning the reported issues with the internal directory structure (e.g., `services/hwfit/` for Cookbook, `src/agent_tools` for agent capabilities, and `routes/` for UI endpoints), we can map these issues into a structured taxonomy.

Below is the comprehensive organization document. Potential duplicates have been consolidated, and all issue numbers are now directly linked to the repository for seamless navigation.

---

### 📊 Statistical Summary of Analyzed Issues

Based on the provided dataset of open issues, here is the distribution across the primary domains representing the project's current operational bottlenecks:

| Domain | Concentration | Primary Bottlenecks |
| --- | --- | --- |
| **UI/UX & Frontend** | ~29% | Mobile responsiveness and component scaling |
| **Agent Engine & Core Logic** | ~25% | Tool gating and context window amnesia |
| **Model Providers & Hardware** | ~21% | GPU detection and Windows/Ollama parity |
| **External Integrations** | ~15% | Calendar/Email timezone bugs and Search APIs |
| **Infrastructure & Security** | ~10% | CI/CD pipelines and macOS/Windows build scripts |

---

### 🗂️ Odysseus Issue Taxonomy

### 1. 🖥️ UI/UX & Frontend Platform (`static/js/`, `static/css/`)

**Accessibility & Responsiveness**

* [#3467](https://github.com/pewdiepie-archdaemon/odysseus/issues/3467) UI SCALE OPTIMIZATION
* [#3969](https://github.com/pewdiepie-archdaemon/odysseus/issues/3969) Cannot insert newlines in chat on mobile devices
* [#3962](https://github.com/pewdiepie-archdaemon/odysseus/issues/3962) The edit textbox for user chats is too narrow
* [#3203](https://github.com/pewdiepie-archdaemon/odysseus/issues/3203) iOS PWA layout does not fully respect safe areas
* [#977](https://github.com/pewdiepie-archdaemon/odysseus/issues/977) Font size is too large / illegible on low-resolution screens
* [#1074](https://github.com/pewdiepie-archdaemon/odysseus/issues/1074) Panel docking only supports left and bottom snap zones
* [#3497](https://github.com/pewdiepie-archdaemon/odysseus/issues/3497) mobile: can't access top controls on pwa mode on iPhone

**Navigation & Layout**

* [#4071](https://github.com/pewdiepie-archdaemon/odysseus/issues/4071) codebase readability improvements for contributor onboarding
* [#3860](https://github.com/pewdiepie-archdaemon/odysseus/issues/3860) feat(ui): reorder sidebar tools and icon rail via drag-and-drop
* [#3871](https://github.com/pewdiepie-archdaemon/odysseus/issues/3871) fix(ui): icon rail and full sidebar both visible after expanding
* [#3123](https://github.com/pewdiepie-archdaemon/odysseus/issues/3123) Sidebar collapses when opening Calendar but not other tools
* [#3789](https://github.com/pewdiepie-archdaemon/odysseus/issues/3789) Add tabs for multiple windows snapped to the same side
* [#2245](https://github.com/pewdiepie-archdaemon/odysseus/issues/2245) Add a hamburger menu for the landing page

**Components & State Management**

* [#3878](https://github.com/pewdiepie-archdaemon/odysseus/issues/3878) Chat User Message Scroll Marker
* [#4045](https://github.com/pewdiepie-archdaemon/odysseus/issues/4045) Toast notifications disappear too quickly to read (1200ms default)
* [#3893](https://github.com/pewdiepie-archdaemon/odysseus/issues/3893) Drop downs hang over card edge on Scan/Download cookbook card
* [#4001](https://github.com/pewdiepie-archdaemon/odysseus/issues/4001), [#4002](https://github.com/pewdiepie-archdaemon/odysseus/issues/4002), [#3547](https://github.com/pewdiepie-archdaemon/odysseus/issues/3547), [#3546](https://github.com/pewdiepie-archdaemon/odysseus/issues/3546) Brain/skills editing box bugs and editor mode
* [#3993](https://github.com/pewdiepie-archdaemon/odysseus/issues/3993) Live chat leaves executed email tool fences visible until reload
* [#4035](https://github.com/pewdiepie-archdaemon/odysseus/issues/4035) window rendering error when email view is maximized

**Theming & Customization**

* [#3692](https://github.com/pewdiepie-archdaemon/odysseus/issues/3692) Add default themes based on the catppuccin palettes
* [#3679](https://github.com/pewdiepie-archdaemon/odysseus/issues/3679) Optional animated login theme (admin toggle)
* [#3197](https://github.com/pewdiepie-archdaemon/odysseus/issues/3197) Custom background images for odysseus

---

### 2. 🧠 Agent Engine & Core Logic (`src/agent_tools/`, `src/chat_processor.py`)

**Reasoning & Tool Execution**

* [#3041](https://github.com/pewdiepie-archdaemon/odysseus/issues/3041) Agent Mode Is Broken and It barely perform as an agent
* [#3998](https://github.com/pewdiepie-archdaemon/odysseus/issues/3998) Agent mode: next round's reasoning streams into the reply bubble
* [#3992](https://github.com/pewdiepie-archdaemon/odysseus/issues/3992) Agent persists pre-tool prose before the real tool result
* [#3604](https://github.com/pewdiepie-archdaemon/odysseus/issues/3604) Agent mode executes ordinary Markdown code fences as tool calls
* [#3668](https://github.com/pewdiepie-archdaemon/odysseus/issues/3668) Agent intent-without-action supervisor (`_INTENT_RE`) is English-only
* [#3792](https://github.com/pewdiepie-archdaemon/odysseus/issues/3792) Task Scheduler: filter thinking deltas from agent loop results
* [#3436](https://github.com/pewdiepie-archdaemon/odysseus/issues/3436) Need HITL (Human-in-the-loop) in `stream_agent_loop` to prevent infinite error loops

**Context & Memory Management**

* [#4050](https://github.com/pewdiepie-archdaemon/odysseus/issues/4050) add memory pruning, and corresponding "deep memory" search for long persistence
* [#3890](https://github.com/pewdiepie-archdaemon/odysseus/issues/3890), [#3889](https://github.com/pewdiepie-archdaemon/odysseus/issues/3889), [#3888](https://github.com/pewdiepie-archdaemon/odysseus/issues/3888) Memory tidy lifecycle, OAuth credentials, and 100-entry limit
* [#3729](https://github.com/pewdiepie-archdaemon/odysseus/issues/3729) Native TRACE-inspired and MemMachine Hierarchical Memory Engine
* [#3745](https://github.com/pewdiepie-archdaemon/odysseus/issues/3745) Memory Amnesia Bug Fix & Subsystem Hardening (Context Compactor + CRUD Tools)
* [#2750](https://github.com/pewdiepie-archdaemon/odysseus/issues/2750) Agent prompt token bloat: measure, slim, and modularize
* [#1893](https://github.com/pewdiepie-archdaemon/odysseus/issues/1893) Hierarchical B+Tree memory for Agent mode to fix context bloat

**Tool Access & Routing Filters**

* [#4048](https://github.com/pewdiepie-archdaemon/odysseus/issues/4048) Agent without ChromaDB has NO file tools
* [#3766](https://github.com/pewdiepie-archdaemon/odysseus/issues/3766) `_classify_agent_request()` strips all tools for non-English queries
* [#3934](https://github.com/pewdiepie-archdaemon/odysseus/issues/3934) Tool-RAG low-signal gate hides most available tools
* [#3709](https://github.com/pewdiepie-archdaemon/odysseus/issues/3709) Opt-in hard gate: block high-impact tools when the agent's context is untrusted
* [#3605](https://github.com/pewdiepie-archdaemon/odysseus/issues/3605) Agent never offered `generate_image`/`edit_image`

---

### 3. ⚙️ Model Providers & Hardware / Cookbook (`services/hwfit/`)

**Local Providers & Hardware Detection**

* [#4059](https://github.com/pewdiepie-archdaemon/odysseus/issues/4059), [#4017](https://github.com/pewdiepie-archdaemon/odysseus/issues/4017), [#3995](https://github.com/pewdiepie-archdaemon/odysseus/issues/3995), [#3897](https://github.com/pewdiepie-archdaemon/odysseus/issues/3897) Cookbook downloader crashes, silent stalls, and orphaned hf/python processes
* [#4049](https://github.com/pewdiepie-archdaemon/odysseus/issues/4049) Model files disappear after update/rebuild (cache unawareness)
* [#3882](https://github.com/pewdiepie-archdaemon/odysseus/issues/3882) `detect_system()` no-GPU result missing gpus/gpu_groups/homogeneous keys
* [#3939](https://github.com/pewdiepie-archdaemon/odysseus/issues/3939) Scanning for models appears to spike CPU usage
* [#1504](https://github.com/pewdiepie-archdaemon/odysseus/issues/1504), [#488](https://github.com/pewdiepie-archdaemon/odysseus/issues/488), [#528](https://github.com/pewdiepie-archdaemon/odysseus/issues/528) Llama.cpp ROCm support and AMD GPU misclassification
* [#4056](https://github.com/pewdiepie-archdaemon/odysseus/issues/4056) Cookbook Serve: per-model compute backend selector
* [#3624](https://github.com/pewdiepie-archdaemon/odysseus/issues/3624) Add "wsl" as a cookbook server platform

**External APIs & Remote Integrations**

* [#4037](https://github.com/pewdiepie-archdaemon/odysseus/issues/4037) feat: Add native Google Gemini API provider support
* [#3145](https://github.com/pewdiepie-archdaemon/odysseus/issues/3145) Gemini-native models fall back to OpenAI-compatible chat/completions
* [#3021](https://github.com/pewdiepie-archdaemon/odysseus/issues/3021) Add Perplexity as an OpenAI-compatible provider
* [#2462](https://github.com/pewdiepie-archdaemon/odysseus/issues/2462) Add NEAR AI as a first-class provider (confidential/TEE inference)
* [#13](https://github.com/pewdiepie-archdaemon/odysseus/issues/13) feat: AWS Bedrock integration

---

### 4. 🔌 External Integrations (`services/search/`, `routes/`)

**Email & Calendar (CalDAV/IMAP)**

* [#3999](https://github.com/pewdiepie-archdaemon/odysseus/issues/3999) feat(email): Microsoft Graph (Exchange/Outlook) mail accounts and agent access
* [#3915](https://github.com/pewdiepie-archdaemon/odysseus/issues/3915), [#3832](https://github.com/pewdiepie-archdaemon/odysseus/issues/3832), [#3631](https://github.com/pewdiepie-archdaemon/odysseus/issues/3631) Timezone bugs (daily_brief, Reminders, and Calendar week view defaulting to UTC)
* [#4058](https://github.com/pewdiepie-archdaemon/odysseus/issues/4058) `manage_calendar` `list_events` returns no events when start == end
* [#3869](https://github.com/pewdiepie-archdaemon/odysseus/issues/3869) Email Calendar Events CalDAV Calendar Selection and Migration
* [#3345](https://github.com/pewdiepie-archdaemon/odysseus/issues/3345) Support Proton Mail accounts via Proton Mail Bridge

**Web Search & Research**

* [#3344](https://github.com/pewdiepie-archdaemon/odysseus/issues/3344) feat(search): add Perplexity Search as a selectable web-search provider
* [#4055](https://github.com/pewdiepie-archdaemon/odysseus/issues/4055) Bug: Polish-language web search requests classified as "low-signal"
* [#3696](https://github.com/pewdiepie-archdaemon/odysseus/issues/3696) Migrate to the maintained ddgs package (duckduckgo-search is frozen)
* [#2866](https://github.com/pewdiepie-archdaemon/odysseus/issues/2866) Add SerpApi as a search provider
* [#2703](https://github.com/pewdiepie-archdaemon/odysseus/issues/2703) Kagi - add as a search provider
* [#531](https://github.com/pewdiepie-archdaemon/odysseus/issues/531) Add Exa as an additional search provider

**MCP (Model Context Protocol) & Webhooks**

* [#4026](https://github.com/pewdiepie-archdaemon/odysseus/issues/4026) Built-in Browser MCP (@playwright/mcp) reports "not installed in npx cache"
* [#3877](https://github.com/pewdiepie-archdaemon/odysseus/issues/3877) MCP Streamable HTTP client crashes with "Attempted to exit cancel scope in a different task"
* [#2976](https://github.com/pewdiepie-archdaemon/odysseus/issues/2976), [#2975](https://github.com/pewdiepie-archdaemon/odysseus/issues/2975), [#2974](https://github.com/pewdiepie-archdaemon/odysseus/issues/2974) Add MS Teams, Slack, and Mattermost Webhook presets

---

### 5. 🏗️ Infrastructure, DevOps & Security (`.github/workflows/`, `core/`)

**Testing & CI/CD Pipelines**

* [#3983](https://github.com/pewdiepie-archdaemon/odysseus/issues/3983) tests: plan oversized test-file splits
* [#3973](https://github.com/pewdiepie-archdaemon/odysseus/issues/3973) tests: add non-blocking order-sensitivity reporting
* [#3968](https://github.com/pewdiepie-archdaemon/odysseus/issues/3968) install: Fresh install and smoke-test coverage tracker
* [#3694](https://github.com/pewdiepie-archdaemon/odysseus/issues/3694) Stabilization: slow down risky merges with clear PR review rules

**Security & Data Hardening**

* [#3803](https://github.com/pewdiepie-archdaemon/odysseus/issues/3803) Hardening audit: unversioned migrations, non-atomic writes, PII in logs, missing owner scoping
* [#3866](https://github.com/pewdiepie-archdaemon/odysseus/issues/3866) docs/security: add a minimal accountability checklist for privileged agent actions
* [#3966](https://github.com/pewdiepie-archdaemon/odysseus/issues/3966) API token PATCH should reject non-object JSON bodies instead of 500ing
* [#3200](https://github.com/pewdiepie-archdaemon/odysseus/issues/3200) DNS Rebinding SSRF in webpage content fetcher allows access to private networks

**Platforms & Packaging (Docker, Windows, macOS)**

* [#3896](https://github.com/pewdiepie-archdaemon/odysseus/issues/3896) Parameterize Docker volume paths for external orchestrators
* [#3846](https://github.com/pewdiepie-archdaemon/odysseus/issues/3846) Docker on Windows: entrypoint re-chowns multi-GB caches every boot
* [#3815](https://github.com/pewdiepie-archdaemon/odysseus/issues/3815) `build-macos-app.sh` produces unsigned bundle that Gatekeeper silently kills
* [#3747](https://github.com/pewdiepie-archdaemon/odysseus/issues/3747) Refactor `launch-windows.ps1` for uv installation and Python management

---

### 6. 📚 Documents, Notes & Canvas (`src/document_processor.py`)

**PDF & Formatting Engine**

* [#3861](https://github.com/pewdiepie-archdaemon/odysseus/issues/3861) Typst Support
* [#3447](https://github.com/pewdiepie-archdaemon/odysseus/issues/3447) PDF form: unchecked AcroForm checkboxes render and export as checked
* [#3327](https://github.com/pewdiepie-archdaemon/odysseus/issues/3327) PDF OCR fails silently for image-only/scanned PDFs
* [#2135](https://github.com/pewdiepie-archdaemon/odysseus/issues/2135) PDF form export drops fields with non-ASCII names

**Editor & Notes Panel**

* [#4066](https://github.com/pewdiepie-archdaemon/odysseus/issues/4066) Notes: per-item and whole-note agent integration
* [#4065](https://github.com/pewdiepie-archdaemon/odysseus/issues/4065) Notes: per-note sharing (view/edit collaborators) with its security hardening
* [#4064](https://github.com/pewdiepie-archdaemon/odysseus/issues/4064) Notes: preview panel as the single editor
* [#3788](https://github.com/pewdiepie-archdaemon/odysseus/issues/3788) Notes pane renders behind other views and chat controls
* [#2909](https://github.com/pewdiepie-archdaemon/odysseus/issues/2909) Proper DOCX editing in Documents

**Library & Attachments**

* [#3938](https://github.com/pewdiepie-archdaemon/odysseus/issues/3938) Proper document library
* [#3750](https://github.com/pewdiepie-archdaemon/odysseus/issues/3750) Make individual documents from the library drag&drop elements
* [#3646](https://github.com/pewdiepie-archdaemon/odysseus/issues/3646) Add ability to attach files directly from the library

---

### 7. 🗄️ Workspace, Research & Memory (`services/research/`)

**Deep Research Pipeline**

* [#2787](https://github.com/pewdiepie-archdaemon/odysseus/issues/2787) [feat] Deep Research: allow manual search provider override
* [#2339](https://github.com/pewdiepie-archdaemon/odysseus/issues/2339) Add an expand/fullscreen control to the Deep Research synapse graph
* [#2741](https://github.com/pewdiepie-archdaemon/odysseus/issues/2741) Add backup support for Deep Research runs
* [#2718](https://github.com/pewdiepie-archdaemon/odysseus/issues/2718) The Agent can trigger the deep reasearch but cant draw context from the result

**Knowledge & Extraction**

* [#3965](https://github.com/pewdiepie-archdaemon/odysseus/issues/3965) Skill extraction can save the later JSON object from multi-object output
* [#3854](https://github.com/pewdiepie-archdaemon/odysseus/issues/3854) Visual report title extraction deletes a mid-document section heading

**Session & History Management**

* [#4005](https://github.com/pewdiepie-archdaemon/odysseus/issues/4005) Research "Discuss" (spin-off) chats lose the report under compaction
* [#3531](https://github.com/pewdiepie-archdaemon/odysseus/issues/3531) Backspace while renaming a chat opens the delete-session prompt
* [#3402](https://github.com/pewdiepie-archdaemon/odysseus/issues/3402) feat(library): show cumulative session token count in chat cards

---

### 8. 🔐 Authentication & Permissions (`core/auth.py`)

**Access Control & Isolation**

* [#4061](https://github.com/pewdiepie-archdaemon/odysseus/issues/4061) Notes routes treat an identity-less request as the single-user mode (fail-open)
* [#4052](https://github.com/pewdiepie-archdaemon/odysseus/issues/4052) Bearer/API-token clients are siloed as the "api" pseudo-user on chat, model, and upload routes
* [#3149](https://github.com/pewdiepie-archdaemon/odysseus/issues/3149) Add default-deny API token capability checks for bearer routes

**Login & Auth Providers**

* [#3561](https://github.com/pewdiepie-archdaemon/odysseus/issues/3561) Login returns 500 when password is longer than 72 bytes (bcrypt ValueError)
* [#2960](https://github.com/pewdiepie-archdaemon/odysseus/issues/2960) Design a reusable OAuth/device-flow provider component
* [#806](https://github.com/pewdiepie-archdaemon/odysseus/issues/806) SSO via OIDC support

---

### 9. 🛠️ Tooling, Scripts & Subprocesses (`scripts/`)

**CLI & Execution Environment**

* [#3446](https://github.com/pewdiepie-archdaemon/odysseus/issues/3446) shell exec: timeout=0 times out immediately instead of running unbounded
* [#3430](https://github.com/pewdiepie-archdaemon/odysseus/issues/3430) Agent bash/python tool output only appears after command finishes
* [#2957](https://github.com/pewdiepie-archdaemon/odysseus/issues/2957) Windows agent shell tool: stray quote breaks commands + defaults to Unix commands
* [#2759](https://github.com/pewdiepie-archdaemon/odysseus/issues/2759) feat: add native PowerShell agent tool alongside bash

**Diagnostics & Dev Tools**

* [#3060](https://github.com/pewdiepie-archdaemon/odysseus/issues/3060) feat: Trace collector dev-tool for flagging successful/failed agent interactions
* [#2122](https://github.com/pewdiepie-archdaemon/odysseus/issues/2122) `odysseus-*` CLI list/search commands return wrong or missing results

---

### 🛡️ Architectural Resolution Strategy

Based on the `THREAT_MODEL.md` and `README.md` documents provided in the codebase, many of these issues intersect directly with core security and architectural rules. When tackling this backlog, apply these strict codebase invariants:

1. **Enforce Owner-Scoping:** A major pattern of bugs (e.g., [#4052](https://github.com/pewdiepie-archdaemon/odysseus/issues/4052), [#2352](https://github.com/pewdiepie-archdaemon/odysseus/issues/2352), [#2286](https://github.com/pewdiepie-archdaemon/odysseus/issues/2286)) stems from bypassing or mishandling the `owner_filter` logic. As stated in the threat model, "A caller must NEVER see another owner's row". All CRUD operations affecting memory, tokens, tasks, and documents must pass through `get_current_user` or the bearer-token owner-attribution sentinel before hitting the database.
2. **Un-Gate the Agent Safely:** Issues requesting more open tool execution ([#3604](https://github.com/pewdiepie-archdaemon/odysseus/issues/3604), [#3605](https://github.com/pewdiepie-archdaemon/odysseus/issues/3605)) must be balanced against `src/tool_security.py`. High-risk capabilities (shell, Python execution, file writes) must remain admin-only by default (`NON_ADMIN_BLOCKED_TOOLS`).
3. **Sanitize Untrusted Data:** Issues dealing with Deep Research ingestion or webpage parsing ([#2135](https://github.com/pewdiepie-archdaemon/odysseus/issues/2135), [#3854](https://github.com/pewdiepie-archdaemon/odysseus/issues/3854)) must be routed through `untrusted_context_message()` to prevent prompt-injection attacks from poisoning the RAG pipeline.

---

### 🗺️ Odysseus Issue Taxonomy Graph (Visual Map)

This text-based tree structure maps out the categories defined above. You can directly copy it into the repository's `ROADMAP.md` or `CONTRIBUTING.md` to guide new contributors.

```text
Odysseus Project (576 Open Issues)
│
├── 1. 🖥️ UI/UX & Frontend Platform
│   ├── Accessibility & Responsiveness (Mobile PWA, UI Scaling)
│   ├── Navigation & Layout (Sidebar, Multi-window tabs)
│   ├── Components & State (Chat scroll, Modals, Toasts)
│   └── Theming & Customization (Catppuccin, Dark Mode)
│
├── 2. 🧠 Agent Engine & Core Logic
│   ├── Reasoning & Tool Execution (Markdown parsing, infinite loops)
│   ├── Context & Memory Management (Amnesia, Context Compaction)
│   └── Tool Access & Routing Filters (Language gating, Untrusted Context)
│
├── 3. ⚙️ Model Providers & Hardware (Cookbook)
│   ├── Local Providers & Hardware (AMD ROCm, Windows/WSL, llama.cpp)
│   └── External APIs (Gemini, Perplexity, Bedrock)
│
├── 4. 🔌 External Integrations
│   ├── Email & Calendar (Outlook, IMAP, CalDAV, Timezones)
│   ├── Web Search (DuckDuckGo, SerpAPI, Perplexity)
│   └── MCP & Webhooks (Playwright MCP, Slack/Teams)
│
├── 5. 🏗️ Infrastructure, DevOps & Security
│   ├── Testing & CI/CD Pipelines (Test splits, PR rules)
│   ├── Security & Data Hardening (SSRF, Auth boundaries)
│   └── Platforms & Packaging (Docker multi-stage, macOS/Windows native)
│
├── 6. 📚 Documents, Notes & Canvas
│   ├── PDF & Formatting Engine (OCR, Typst, AcroForm)
│   ├── Editor & Notes Panel (Markdown unified model, Collab)
│   └── Library & Attachments (Drag & Drop, Zip export)
│
├── 7. 🗄️ Workspace, Research & Memory
│   ├── Deep Research Pipeline (Fallback providers, Synapse Graph)
│   └── Session & History Management (Discuss spin-offs, DB migrations)
│
├── 8. 🔐 Authentication & Permissions
│   ├── Access Control (Bearer tokens, API pseudo-user)
│   └── Login & Auth Providers (OIDC, OAuth2, Rate Limits)
│
└── 9. 🛠️ Tooling, Scripts & Subprocesses
    ├── CLI & Execution Environment (PowerShell tool, Bash timeouts)
    └── Diagnostics & Dev Tools (Trace collector)

```

---

### 🏷️ Recommended GitHub Label Taxonomy

To map this taxonomy directly into GitHub, I recommend creating a standardized labeling system to bulk-apply and instantly organize the repository.

**Domain Labels (Color: `#1d76db` - Blue):**

* `domain: ui/ux`
* `domain: agent-engine`
* `domain: hardware/cookbook`
* `domain: integrations`
* `domain: memory/context`
* `domain: infrastructure/ci`

**Type Labels (Color: `#e99695` - Red/Pink):**

* `type: bug` (Core logic failures, crashes)
* `type: enhancement` (New features)
* `type: papercut` (Minor UI annoyances, typos)
* `type: security` (Hardening, SSRF, prompt injection)
* `type: developer-experience` (Build scripts, docs, testing)

**Platform Labels (Color: `#0e8a16` - Green):**

* `platform: windows`
* `platform: macos`
* `platform: linux/docker`
* `platform: mobile/pwa`

**Status/Triage Labels (Color: `#fbca04` - Yellow):**

* `status: needs-validation`
* `status: blocked`
* `status: good-first-issue`

---

### 🚀 Recommendations & Phased Execution Plan

**Consolidate Redundancies:** You have highly related clusters in "Timezone/UTC Calendar bugs" ([#3915](https://github.com/pewdiepie-archdaemon/odysseus/issues/3915), [#3832](https://github.com/pewdiepie-archdaemon/odysseus/issues/3832), [#3631](https://github.com/pewdiepie-archdaemon/odysseus/issues/3631)) and "Cookbook Download Stalls" ([#4059](https://github.com/pewdiepie-archdaemon/odysseus/issues/4059), [#4017](https://github.com/pewdiepie-archdaemon/odysseus/issues/4017), [#3995](https://github.com/pewdiepie-archdaemon/odysseus/issues/3995)). Creating GitHub Epic tracker issues for these will collapse them and simplify the backlog.

With 576 issues, a maintainer cannot tackle everything at once. Use this 4-phase approach to burn down the backlog systematically:

**Phase 1: Stop the Bleeding (P0/P1 Security & Blockers)**

* **Focus:** Security vulnerabilities and critical crashes.
* **Target Issues:** [#3200](https://github.com/pewdiepie-archdaemon/odysseus/issues/3200) (DNS Rebinding SSRF), [#2891](https://github.com/pewdiepie-archdaemon/odysseus/issues/2891) (RCE via `manage_mcp`), [#1940](https://github.com/pewdiepie-archdaemon/odysseus/issues/1940) (Memory lost-update race condition), and Cookbook download crashes ([#4059](https://github.com/pewdiepie-archdaemon/odysseus/issues/4059), [#2722](https://github.com/pewdiepie-archdaemon/odysseus/issues/2722)).
* **Action:** Lock down the untrusted context boundaries, secure the bearer tokens ([#3149](https://github.com/pewdiepie-archdaemon/odysseus/issues/3149)), and fix the concurrent write locks on the SQLite/JSON memory files.

**Phase 2: Agent Stability & Core User Experience**

* **Focus:** Making sure the AI actually behaves like an agent.
* **Target Issues:** Un-gating the RAG tools ([#4048](https://github.com/pewdiepie-archdaemon/odysseus/issues/4048), [#3766](https://github.com/pewdiepie-archdaemon/odysseus/issues/3766), [#3934](https://github.com/pewdiepie-archdaemon/odysseus/issues/3934)), fixing context amnesia ([#3745](https://github.com/pewdiepie-archdaemon/odysseus/issues/3745)), and preventing markdown code-fence execution loops ([#3604](https://github.com/pewdiepie-archdaemon/odysseus/issues/3604)).
* **Action:** Rewrite the `_classify_agent_request` to be less aggressive and language-agnostic. Implement strict HITL (Human-in-the-loop) circuit breakers for infinite loops.

**Phase 3: Hardware Parity & Provider Integrations**

* **Focus:** Ensuring users can actually run the local models.
* **Target Issues:** AMD ROCm detection ([#1504](https://github.com/pewdiepie-archdaemon/odysseus/issues/1504), [#488](https://github.com/pewdiepie-archdaemon/odysseus/issues/488)), Windows path quoting ([#2957](https://github.com/pewdiepie-archdaemon/odysseus/issues/2957), [#2642](https://github.com/pewdiepie-archdaemon/odysseus/issues/2642)), and resolving API integration timezone bugs ([#3915](https://github.com/pewdiepie-archdaemon/odysseus/issues/3915), [#3832](https://github.com/pewdiepie-archdaemon/odysseus/issues/3832)).
* **Action:** Consolidate the platform-specific hardware checks into a unified `hwfit` module. Standardize all `datetime` parsing to strictly capture and respect the user's local timezone offset over UTC.

**Phase 4: UX Papercuts & "Good First Issues"**

* **Focus:** Quality of life and onboarding new contributors.
* **Target Issues:** UI scaling ([#3467](https://github.com/pewdiepie-archdaemon/odysseus/issues/3467)), edit textbox sizes ([#3962](https://github.com/pewdiepie-archdaemon/odysseus/issues/3962)), missing hamburger menus ([#2245](https://github.com/pewdiepie-archdaemon/odysseus/issues/2245)), and drag-and-drop support ([#3750](https://github.com/pewdiepie-archdaemon/odysseus/issues/3750)).
* **Action:** Create a GitHub Project Board specifically for "Frontend Papercuts" and tag them all as `good-first-issue` to attract open-source contributors to help clear out the remaining ~30% of the backlog.

---

### 🤖 Automation: Auto-Labeling Script

Since manually organizing and labeling 576 issues is a massive undertaking, the most practical next step is automation.

If you have maintainer access, you can use the GitHub API to bootstrap this organization. Save the following Python script using the `PyGithub` library as `scripts/triage_bot.py`. It will automatically create the taxonomy labels defined above and begin categorizing open issues based on title and body heuristics.

*(Note: You will need a GitHub Personal Access Token assigned to `GITHUB_TOKEN` with repository write access).*

```python
import os
from github import Github

# Configuration
REPO_NAME = "pewdiepie-archdaemon/odysseus"
TOKEN = os.getenv("GITHUB_TOKEN")

# Define our new Taxonomy Labels (Name, Color, Description)
LABELS = {
    # Domains
    "domain: ui/ux": ("1d76db", "Frontend, styling, mobile, and accessibility"),
    "domain: agent-engine": ("1d76db", "Core LLM routing, RAG gates, and reasoning loops"),
    "domain: hardware/cookbook": ("1d76db", "Local model serving, GPUs, Ollama, vLLM"),
    "domain: integrations": ("1d76db", "Email, Calendar, Web Search, MCP"),
    "domain: memory/context": ("1d76db", "Context window, ChromaDB, vector storage"),
    "domain: infrastructure/ci": ("1d76db", "Docker, build scripts, GitHub Actions"),

    # Types
    "type: bug": ("e99695", "Something isn't working correctly"),
    "type: enhancement": ("a2eeef", "New feature or request"),
    "type: security": ("d73a4a", "Vulnerabilities, SSRF, auth bypass"),

    # Platforms
    "platform: windows": ("0e8a16", "Windows native or WSL specific"),
    "platform: macos": ("0e8a16", "macOS or Apple Silicon specific"),
    "platform: docker": ("0e8a16", "Containerized deployment specific")
}

# Simple keyword heuristics for auto-tagging
KEYWORD_MAP = {
    "domain: ui/ux": ["ui", "frontend", "mobile", "pwa", "css", "scroll", "button", "sidebar"],
    "domain: hardware/cookbook": ["cookbook", "rocm", "amd", "gpu", "cuda", "vllm", "llama.cpp", "gguf"],
    "domain: integrations": ["email", "calendar", "outlook", "imap", "mcp", "searxng", "duckduckgo"],
    "domain: memory/context": ["memory", "chromadb", "rag", "context", "amnesia"],
    "platform: windows": ["windows", "ps1", "powershell", ".bat"],
    "platform: macos": ["macos", "apple silicon", "m1", "m2", "m3", "gatekeeper"]
}

def setup_labels(repo):
    print("Setting up taxonomy labels...")
    existing_labels = {l.name: l for l in repo.get_labels()}

    for name, (color, desc) in LABELS.items():
        if name in existing_labels:
            print(f"Updating label: {name}")
            existing_labels[name].edit(name=name, color=color, description=desc)
        else:
            print(f"Creating label: {name}")
            repo.create_label(name=name, color=color, description=desc)

def auto_triage_issues(repo):
    print("Scanning open issues for auto-triage...")
    issues = repo.get_issues(state='open')

    for issue in issues:
        if issue.pull_request: # Skip PRs
            continue

        text_to_search = (str(issue.title) + " " + str(issue.body)).lower()
        tags_to_apply = []

        for label, keywords in KEYWORD_MAP.items():
            if any(kw in text_to_search for kw in keywords):
                tags_to_apply.append(label)

        if tags_to_apply:
            print(f"Tagging #{issue.number} ({issue.title[:30]}...) with {tags_to_apply}")
            # issue.add_to_labels(*tags_to_apply) # UNCOMMENT TO ACTUALLY APPLY

if __name__ == "__main__":
    if not TOKEN:
        print("Please set GITHUB_TOKEN environment variable.")
        exit(1)

    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)

    setup_labels(repo)
    # auto_triage_issues(repo) # Run cautiously!
    print("Done.")

```
