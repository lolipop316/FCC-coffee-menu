# Study Artifacts — 2025-09-23

## Today Log
- Blocks completed:
  - FCC front-end practice — completed (2 blocks prior).
  - Linux / CLI basics — completed (pwd, whoami, mkdir, echo, chmod).
  - Process & Services reconnaissance — completed (netstat → lsof → ps).
  - Active recall flashcards session (Quizlet XSS test).
- Energy / notes: nap helped; basics feel easy → move to adversarial drills next.
- Proof artifacts created: `linux-cli-lab-2025-09-23.md`, `proc-svc-map-2025-09-23.md`, Quizlet screenshots.

---

## Security+ Flashcards (Anki-ready)
- **Lens:** Memory / Threat  
- **Domain Bridge:** Security+ concepts → cloud mitigation  
- **Artifact:** flashcards converted to Anki format (front/back)

1. **Q:** What is Cross-Site Scripting (XSS)?  
   **A:** A web vulnerability where attackers inject scripts into pages viewed by others — enables session theft, UI manipulation, or malicious actions. Prevent via input validation, output encoding, CSP, WAF.

2. **Q:** Why is input validation important for cloud apps?  
   **A:** Prevents injection (XSS/SQLi) and reduces attack surface; combine with least privilege, WAF, and secure design.

3. **Q:** What is MITM?  
   **A:** Attacker intercepts/relays messages between parties. Prevent with TLS, certificate pinning, secure DNS (DoH), mutual auth.

---

## FCC / Front-end Project Spin-off
**Filename:** `fcc-registration-v2-notes-2025-09-23.md`

- **Lens:** Architect  
- **Domain Bridge:** FCC template → custom project  
- **Objective:** take FCC Registration Form and create `registration-form-v2` with one extra field + theme changes  

### Changes made
- Added field: *Preferred Contact Method* (select).
- Changed primary color and font-size for `.form-header`.
- Created repo folder `registration-form-v2/` and initial commit.

### Actionables
- Commit message: `feat: add Preferred Contact Method + theme tweak`
- Next: add client-side validation, push to GitHub, add simple README.

### Lesson
Scaffolds accelerate iteration → small variations build confidence.

---

## Linux CLI Lab
**Filename:** `linux-cli-lab-2025-09-23.md`

- **Lens:** Threat Lens  
- **Domain Bridge:** Security+ auth & permissions → Linux basics  
- **Objective:** confirm basic file ops & permissions; create config, restrict access.  

### Commands run
```
pwd
whoami
mkdir projects
echo "password=1234" > projects/config.txt
ls -l projects/   # before
chmod 600 projects/config.txt
ls -l projects/   # after
```

### Findings
- `config.txt` created and restricted to user read/write (`-rw-------`) after `chmod 600`.

### Lesson
Basic permissions are quick win for containing secrets.

---

## Process & Service Mapping
**Filename:** `proc-svc-map-2025-09-23.md`

- **Lens:** Recon / Threat  
- **Objective:** map listening services → identify owner processes → recommend mitigations  

### Commands executed
```
netstat -an | grep LISTEN
lsof -n -P -iTCP -sTCP:LISTEN
lsof -n -P -iTCP:5000 -sTCP:LISTEN
ps aux > /tmp/ps-2025-09-23.txt
```

### Findings
- Ports listening: `55621`, `8088`, `5000`, `7000`.
- `ControlCe` (PID 561) → ports 5000, 7000 → Apple Control Center.  
- `rapportd` (PID 602) → port 55621 → Apple Continuity/Handoff daemon.  
- `com.docke` (PID 93076) → port 8088 → Docker backend.

### Defender Notes
- If a dev server is listening on `*:5000`, bind to localhost: `flask run --host 127.0.0.1`.  
- If Continuity/Handoff unused, disable in System Preferences.  
- Docker: review container published ports.

### Lesson
Baseline the dev laptop now — saves hours diagnosing unexpected open ports later.

---

## Anki Cards
1. **Q:** Command to list listening TCP sockets on macOS (with PID & process)?  
   **A:** `lsof -n -P -iTCP -sTCP:LISTEN`

2. **Q:** Why is binding a dev server to 0.0.0.0 risky?  
   **A:** Exposes service on all interfaces → attackers can access. Mitigate with `127.0.0.1` binding or firewall.

3. **Q:** chmod command to restrict a file to owner only?  
   **A:** `chmod 600 <file>`

---

## Checklist
- [x] Today Log · 2025-09-23  
- [x] FCC: registration-form-v2 — Git commit  
- [x] Linux CLI lab artifact + screenshots  
- [x] Process & service mapping artifact + screenshots  
- [x] Add 3 Anki cards (commands + red-flag)  
