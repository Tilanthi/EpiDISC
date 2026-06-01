"""
Context Summary Guidelines for EPIDISC

This module defines the structure and content requirements for
automatic conversation summaries that preserve critical medical context.
"""

# EPIDISC Context Summary Template

## When to Summarize
- When conversation approaches 70% of context window (~140k tokens for Opus 4.8)
- Before major topic shifts
- After completing significant medical consultations
- When user indicates they want to "clear" context

## Summary Structure

### 1. Session Overview (2-3 sentences)
- Date and time of session
- Primary consultation focus
- Key ongoing topics

### 2. Active Medical Topics (Bullet points)
- **Patient cases**: Brief identifier (not full PHI), key question, status
- **Consultations**: Specialty consulted, primary concern, recommendations
- **Technical work**: Code changes, architectural decisions, testing status
- **Documentation**: User manual updates, CLAUDE.md changes

### 3. Key Decisions Made (Bullet points)
- Medical recommendations with confidence levels
- Technical decisions and rationale
- Files modified and why
- Next steps or pending items

### 4. Important Context to Preserve
- Patient context (anonymized): ongoing conditions, medications, recent tests
- System state: what's been implemented, what's pending
- User preferences: specific approaches they prefer or dislike
- Open issues: bugs, problems, questions remaining

### 5. Next Steps (Optional)
- What work is pending
- What to prioritize next session
- Any dependencies

## Example Summary

```
EPIDISC Session Summary - 2026-06-01
=====================================

Session Overview:
Working on EPIDISC v2.0.0 medical consultation system. Focused on
epilepsy domain enhancements and fixing medical domain auto-loading.

Active Medical Topics:
- Implemented epilepsy-specific MORK ontology with 50+ concepts
- Fixed medical domain auto-loading in unified_enhanced.py
- Created medical records processing system (multi-format support)
- Enhanced epilepsy domain to v3.0.0 with semantic seizure classification

Key Decisions Made:
- Fixed keyword matching: replaced substring with word boundary regex
- All 6 medical domains now load successfully on initialization
- Patient records stored locally in epidisc_core/data/patients/ (privacy-first)

Important Context:
- System size: 26MB (cleaned of STAN/BIODISC leftovers)
- User is medical consultant seeking second opinions (not system demos)
- Privacy rule: NO GitHub pushes without explicit instruction
- Dashboard port: 8790

Next Steps:
- Consider adding context auto-summarization to prevent context limit errors
- Update user manual with new epilepsy capabilities
```

## Metadata to Include

When saving summaries, include relevant metadata:
- `session_date`: ISO date of session
- `primary_focus`: Main topic (e.g., "epilepsy domain enhancement")
- `patient_cases_active`: Count of active patient consultations (if any)
- `files_modified`: List of files changed
- `version`: EPIDISC version
- `user_role`: "medical consultant" or "developer"

## Auto-Summarization Triggers

The system should automatically summarize when:
1. Conversation length > 70% of context window
2. User mentions "clear", "restart", or "new session"
3. Major feature completion
4. Before long code generation tasks

## Restoration Format

When loading after `/clear`, format as:
```
# Context Restored from [timestamp]

[Summary content]

## Session Metadata
- session_date: [date]
- primary_focus: [topic]
- version: [version]
```

This ensures seamless continuation without losing critical context.
