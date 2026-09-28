# Security, Privacy & Legal Compliance Audit

## 1. Regulatory Compliance (PA State Law)
In accordance with Pennsylvania Title 18, Section 7104 (Fortune Telling), we have implemented a high-authority disclosure strategy.

*   **Mandatory Footer**: "Services provided by Crystal Shadows are for entertainment and self-discovery purposes only. No medical, legal, or financial advice is implied."
*   **Interactive Consent**: A pre-requisite checkbox on the booking form ensuring users acknowledge the professional nature of the guidance.

## 2. Data Privacy & GDPR/CCPA
*   **PII (Personally Identifiable Information)**: Only the user's name, email, and DOB (required for charts) are collected.
*   **Encryption**: All transmission via TLS 1.3. No data is stored in the local site database; it is piped directly to Square's PCI-compliant vault.
*   **Right to Erasure**: A simple contact method for clients to request their chart data be deleted.

## 3. Security Infrastructure
*   **DDoS Protection**: Managed via Layer 7 WAF (Web Application Firewall).
*   **Integrity Checks**: Weekly automated scans of the `antigravitys_take` directory for file modification.

---
*Prepared by: Security Engineer Division*
