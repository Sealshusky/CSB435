### Code Snippet #1 — Patient Search

Type of injection:  
SQL injection

Attack payload:  
%' OR '1'='1

What an attacker could do:  
They can make the query return every patient record. Basically full data exposure.

---

### Code Snippet #2 — Medical Report Generator

Type of injection:  
Command injection

Attack payload:  
123; rm -rf /

What an attacker could do:  
Run whatever system commands they want. Delete files, steal data, or take over the whole machine.

Why shell commands with user input are dangerous:  
The shell treats characters like ; and | as separators. If user input lands inside a shell command, they can break out and run anything.

---

### Code Snippet #3 — Patient Notes Display

Two separate injection issues here.

#### SQL Injection (note_id)

Payload:  
1 OR 1=1

Impact:  
Read any note, dump all notes, or possibly modify data depending on DB permissions.

#### XSS (note content)

Payload:  
<script>alert('owned')</script>

Impact:  
Steal cookies, impersonate users, or run arbitrary JavaScript in the victim’s browser.

---

### Code Snippet #4 — Prescription Lookup

Two SQL injection points: patient_id and medication.

#### patient_id

Why vulnerable without quotes:  
SQL doesn’t need quotes for numbers. Injecting something like 1 OR 1=1 still works.

Payload:  
1 OR 1=1

#### medication

UNION attack to dump patient data:  
x' UNION SELECT id, name, 'x' FROM patients --

How it works:  
You close the original string, add a UNION that selects from another table, and comment out the rest. The DB returns both sets of rows, including sensitive patient data.

---

### Code Snippet #5 — Appointment Email Notifications

Vulnerability:  
Command injection because of shell=True and user-controlled email.

Attack payload:  
test@example.com; cat /etc/passwd

How the attack works:  
The shell sees ; and treats everything after it as a new command. The attacker’s command runs with the app’s privileges.

When shell=True should be used:  
Pretty much never with user input. Only for fully static commands you control.

---

### Code Snippet #6 — Password Storage

Two major crypto mistakes:

#### Using MD5

What’s wrong:  
MD5 is fast and broken.

Attack enabled:  
Brute-force the hash easily.

Fix:  
Use bcrypt, scrypt, Argon2, or PBKDF2.

#### No salt

What’s wrong:  
Same password always produces the same hash.

Attack enabled:  
Rainbow tables and easy correlation between users.

Fix:  
Generate a random salt per user and use a real password hashing algorithm.

#### Timing attack?

String comparison isn’t constant-time, but honestly the MD5/no-salt issue is so bad that timing doesn’t matter here.

---

### Code Snippet #7 — Session Token Generation

Main crypto mistake:  
Using random seeded with the current timestamp. Predictable.

How an attacker predicts tokens:  
Guess the server time, seed their own RNG the same way, and generate the same numbers.

How long tokens should be:  
At least 128 bits of entropy so guessing is impossible.

random vs secrets:  
random is predictable and not for security.  
secrets is designed for secure tokens.

---

### Risk Assessment Table

| Rank | Snippet | Vulnerability | Severity |
|------|---------|---------------|----------|
| 0 | 2 | Command injection (pandoc) | Critical |
| 1 | 5 | Command injection (mail) | Critical |
| 2 | 6 | MD5 and no salt | High |
| 3 | 7 | Predictable session tokens | High |
| 4 | 1 | SQL injection | High |
| 5 | 3 | SQL injection and XSS | High |
| 6 | 4 | SQL injection (two params) | High |

---

### Which vulnerability would I fix first?

The pandoc command injection. It gives an attacker direct access to run system commands. Once they have that, they can take over the entire server. That’s the fastest path to a full breach.

---

### Which vulnerability would take the longest to fix?

The password hashing issue. Switching from MD5 to a real password hashing algorithm means dealing with existing users, migrating hashes, possibly forcing password resets, and updating the login flow. It’s not a quick fix.

---

### How much would I charge?

A few thousand dollars. There are multiple critical issues and it’s a medical app, so the stakes are high.

---

### Would I sign up for FroggyHealthPortal?

Not right now. Too many ways for attackers to get in or steal data. If they fix the command injection and the crypto problems, maybe, but in its current state, I don't think so.
