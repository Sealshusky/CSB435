# 1. Roles

## 1.1 Applicant
External user applying for jobs. Only interacts with their own application.

## 1.2 Recruiter
Handles most of the hiring pipeline: sourcing, communication, scheduling, and moving candidates through stages.

## 1.3 Hiring Manager
Owns the hiring decision for their team. Works closely with the recruiter but doesn’t need full system‑wide access.

## 1.4 Interviewer
Only interacts with candidates they’re assigned to interview. Can leave feedback but nothing more.

## 1.5 HR Admin
HR power user. Handles approvals, has broader visibility, and can run sensitive reports.

## 1.6 System Admin
Technical owner of the ATS. Manages users, roles, and system configuration.

## 1.7 Reporting & Compliance
Runs reports, handles audits, and manages privacy‑related data deletion.

---

# 2. Permissions

## 2.1 Job Requisition Permissions
- Create job requisition  
- Edit job requisition  
- Submit requisition for approval  
- Approve requisition  
- View team requisitions  
- View all requisitions  
- Archive requisitions  
- Post job to external job boards  

## 2.2 Candidate & Application Permissions
- Apply to a job  
- Withdraw own application  
- View own application status  
- View candidate basic info (name, job, stage)  
- View full candidate profile (resume, notes, etc.)  
- View candidate contact info  
- View salary/offer details  
- Update candidate status  
- Add interview notes  
- Edit own notes  
- Schedule interviews  
- Send rejection email  
- Extend job offer  
- Delete candidate data for privacy requests  

## 2.3 Communication Permissions
- Send one‑off messages  
- Send bulk messages  
- Edit email templates  

## 2.4 Admin & Reporting Permissions
- Manage users and roles  
- Run basic reports  
- Run sensitive reports  
- View audit logs  
- System configuration 

---

# 3. Role–Permission Mapping

## 3.1 Applicant
- Apply to a job  
- Withdraw own application  
- View own application status  

## 3.2 Recruiter
- Create job requisition  
- Edit job requisition  
- Submit requisition for approval  
- View team requisitions  
- Archive requisitions  
- Post job externally  
- View candidate basic info  
- View full candidate profile  
- View candidate contact info  
- View salary/offer details  
- Update candidate status  
- Add notes  
- Edit own notes  
- Schedule interviews  
- Send rejection email  
- Extend job offer  
- Send one‑off messages  
- Send bulk messages  
- Edit email templates  
- Run basic reports (for their requisitions)  

## 3.3 Hiring Manager
- Create job requisition  
- Edit requisitions they own  
- Submit requisition for approval  
- View team requisitions  
- View candidate basic info  
- View full candidate profile  
- View candidate contact info  
- View salary/offer details  
- Update candidate status  
- Add notes  
- Edit own notes  
- Schedule interviews  
- Extend job offer (depending on org policy)  
- Send one‑off messages  
- Run basic reports  

## 3.4 Interviewer
- View candidate basic info (assigned candidates only)  
- View full candidate profile (assigned candidates only)  
- Add notes  
- Edit own notes  

## 3.5 HR Admin
- View all requisitions  
- Approve requisitions  
- Archive requisitions  
- View all candidate info  
- View salary/offer details  
- Update candidate status  
- Send rejection email  
- Run basic reports  
- Run sensitive reports  

## 3.6 System Admin
- Manage users and roles  
- System configuration  
- View audit logs  

## 3.7 Reporting & Compliance
- Run basic reports  
- Run sensitive reports  
- View audit logs  
- Delete candidate data for privacy requests  

---

# 4. Rationale

- Each role only gets what they need to do their job.  
- Interviewers stay limited to feedback only.  
- Applicants only see their own data.  
- Recruiters and Hiring Managers share a lot, but approvals and sensitive reporting stay with HR Admin.  
- System Admin handles the system, not the hiring process.  
- Compliance gets deletion + audit access but nothing that affects hiring outcomes.  

---

# 5. Things I Decided Not to Include


- Stage‑specific permissions (e.g., only HR can move someone to “Hired”)    
- Field‑level permissions (e.g., who can see SSN)    
- Outside recruiting agencies  
- Region‑specific privacy rules  

---

# 6. What I Would Add With More Time


- A coordinator role with slightly reduced permissions  
- A diagram showing the hiring workflow  
- More granular reporting permissions  
- Region‑specific compliance rules  
- A more detailed breakdown of candidate stages and who can move candidates between them  

---

# 7. Areas I’m Less Confident About

- The exact boundary between HR Admin vs Reporting/Compliance 
- Whether Hiring Managers should always see salary details  
- How much visibility System Admins should have into candidate data  
