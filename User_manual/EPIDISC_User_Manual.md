# EPIDISC User Manual
## Medical Discovery and Intelligence System for Consultation

**Version**: 1.0.0  
**Publication Date**: May 2026  
**Author**: Tilanthi

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [System Overview](#2-system-overview)
3. [Getting Started](#3-getting-started)
4. [Using EPIDISC](#4-using-epidisc)
5. [Medical Specialties](#5-medical-specialties)
6. [Epilepsy Consultation](#6-epilepsy-consultation)
7. [Privacy and Security](#7-privacy-and-security)
8. [Dashboard Guide](#8-dashboard-guide)
9. [Troubleshooting](#9-troubleshooting)
10. [Medical Disclaimer](#10-medical-disclaimer)
11. [Support and Resources](#11-support-and-resources)

---

## 1. Introduction

### 1.1 What is EPIDISC?

EPIDISC (Medical Discovery and Intelligence System for Consultation) is a private, medical-focused consultation system that integrates biological knowledge with medical specialties for patient consultation and second opinions. The system transforms advanced biological research capabilities into a comprehensive medical consultation platform designed for healthcare professionals and medical researchers.

### 1.2 Key Features

- **Multi-Specialty Consultation**: Access to medical specialties with automatic domain selection
- **Privacy-First Architecture**: All patient records stored locally with no external transmission
- **Second Opinion Mode**: Multi-specialty consultation with uncertainty quantification
- **Natural Language Interface**: Ask questions in plain language, no technical commands needed
- **Epilepsy Specialization**: Comprehensive seizure disorder consultation and EEG interpretation
- **Anti-Hallucination Protection**: Verification system for medical claims

### 1.3 Target Users

- Healthcare professionals seeking second opinions
- Medical researchers requiring biological knowledge integration
- General practitioners needing specialist consultation
- Medical educators and students
- Healthcare institutions requiring private consultation systems

### 1.4 System Philosophy

EPIDISC is built on the principle that medical consultation should be:
- **Private**: Patient data never leaves your local machine
- **Natural**: Ask questions in plain language, no programming required
- **Reliable**: With built-in verification and confidence scoring
- **Accessible**: Through both web interface and natural language queries

---

## 2. System Overview

### 2.1 System Architecture

EPIDISC consists of multiple integrated layers:

**Entry Layer**
- Natural language questions and consultation requests
- Automatic specialty selection based on your question

**Medical Specialty Layer**
- Cardiology: Heart and cardiovascular disorders
- Epilepsy: Seizure disorders and neurological consultation
- General Practice: Primary care and triage
- Orthopedics: Musculoskeletal conditions and trauma
- Pharmacology: Medication and drug interactions

**Biological Knowledge Layer**
- Molecular Biology, Biochemistry, Genetics
- Cell Biology, Biophysics, Bioinformatics
- Genomics, Proteomics, Systems Biology

**Advanced Capabilities Layer**
- Causal reasoning and meta-learning
- Cross-specialty coordination
- Memory systems with local storage

**Privacy Layer**
- All patient data stored locally
- No external transmission of consultation records
- Persistent memory with privacy protection

### 2.2 Medical Specialties Available

**Epilepsy**
- Seizure classification and diagnosis
- EEG interpretation and seizure semiology
- Antiepileptic medication management
- Seizure first aid and safety protocols
- Epilepsy syndrome recognition
- Treatment-resistant epilepsy evaluation

**Cardiology**
- ECG/EKG interpretation
- Chest pain evaluation and cardiac risk assessment
- Blood pressure and hypertension management
- Heart failure management
- Arrhythmia evaluation

**General Practice**
- Triage and urgent care assessment
- Symptom evaluation and differential diagnosis
- Preventive care and health screening
- Chronic disease management
- Medication reconciliation

**Orthopedics**
- Fracture assessment and management
- Joint pain evaluation
- Sports injuries and soft tissue injuries
- Arthritis management

**Pharmacology**
- Drug interaction checking
- Side effect evaluation and management
- Medication dosing and adjustment
- Polypharmacy review

---

## 3. Getting Started

### 3.1 Installation Requirements

**System Requirements**
- Compatible with macOS, Linux, or Windows operating systems
- Modern web browser for dashboard access
- Minimum 4GB RAM memory (8GB recommended)
- At least 2GB of available disk space
- Local network access for dashboard (no internet required)

### 3.2 Installation Process

**Step 1: Obtain EPIDISC**
Download the EPIDISC system files to your computer. The system is provided as a complete package ready for installation.

**Step 2: Installation**
Run the installation program and follow the on-screen instructions. The installer will place all necessary files in the appropriate locations on your system.

**Step 3: Initial Configuration**
When prompted, choose your preferred settings:
- Dashboard port (default: 8790)
- Data storage location (default: system default)
- Memory settings (default: recommended)

**Step 4: System Verification**
After installation, EPIDISC will automatically verify that all components are properly installed and ready for use.

### 3.3 First Launch

**Starting EPIDISC**
Launch the EPIDISC application from your computer. The system will initialize all medical domains and prepare the consultation interface.

**Dashboard Access**
Once started, open your web browser and access the dashboard at the displayed address (typically http://localhost:8790).

**System Ready**
When you see the main consultation interface, EPIDISC is ready to assist with medical consultations.

---

## 4. Using EPIDISC

### 4.1 Basic Consultation

EPIDISC is designed to understand natural language questions. Simply type your medical question or consultation request in plain language, just as you would ask a colleague.

**Example Questions You Can Ask:**
- "My patient experienced an episode of staring and unresponsiveness lasting two minutes. What type of seizure might this be?"
- "How should I interpret this EEG showing spike-and-wave discharges in the temporal lobe?"
- "What are the first-line medications for focal seizures?"
- "When should I consider epilepsy surgery for a patient with treatment-resistant seizures?"

### 4.2 How to Ask Questions

**Be Specific About Symptoms**
Instead of: "The patient had a seizure"
Try: "The patient experienced a sudden episode of right arm jerking followed by confusion lasting about three minutes"

**Include Relevant History**
Instead of: "What medication should I use?"
Try: "For a 25-year-old woman with focal seizures who plans to become pregnant, what AED would you recommend?"

**Describe Test Results**
Instead of: "What does this EEG show?"
Try: "This EEG shows rhythmic sharp wave discharges at 3 Hz over the left temporal region during sleep"

### 4.3 Understanding Responses

Each consultation response includes:

**Answer**: Detailed medical consultation addressing your specific question

**Confidence Level**: How certain the system is about the consultation (shown as a percentage)
- High confidence (90%+): Suitable for clinical decision support
- Medium confidence (70-89%): Requires additional verification
- Low confidence (<70%): Recommend specialist consultation

**Specialty Used**: Which medical domain provided the consultation

**Sources**: Medical guidelines and references used for the consultation

### 4.4 Follow-Up Questions

EPIDISC maintains context during your consultation session, allowing you to ask follow-up questions:

**Initial Question**: "What are the side effects of levetiracetam?"

**Follow-up Question**: "How does that compare to lamotrigine?" (EPIDISC knows you're still discussing AEDs)

**Another Follow-up**: "What about during pregnancy?" (Context maintained throughout the discussion)

---

## 5. Medical Specialties

### 5.1 Automatic Specialty Selection

EPIDISC automatically determines which medical specialty is best suited to answer your question based on the content and keywords in your question.

**How It Works:**
When you ask a question, EPIDISC analyzes:
- The medical terms and concepts you use
- The symptoms and conditions you describe
- The type of consultation you're requesting

**Example:**
Question: "Patient with seizure, what AED should I start?"
- Keywords detected: "seizure", "AED" (antiepileptic drug)
- Automatic selection: Epilepsy specialty
- Result: Seizure treatment consultation

### 5.2 Specialty Capabilities

**Epilepsy Domain**
- Seizure classification (focal, generalized, unknown onset)
- EEG pattern recognition
- Antiepileptic drug selection and monitoring
- Seizure emergency management
- Epilepsy syndrome identification
- Treatment resistance evaluation
- Pre-surgical assessment considerations

**Cardiology Domain**
- ECG interpretation and cardiac rhythm analysis
- Chest pain differential diagnosis
- Hypertension management guidelines
- Heart failure treatment strategies
- Arrhythmia evaluation and management

**General Practice Domain**
- Symptom evaluation and differential diagnosis
- Preventive care and screening recommendations
- Chronic disease management (diabetes, hypertension, etc.)
- Medicication review and reconciliation
- Specialist referral guidance

**Orthopedics Domain**
- Fracture assessment and management
- Joint pain evaluation
- Sports injury management
- Arthritis treatment options

**Pharmacology Domain**
- Drug interaction checking
- Side effect evaluation
- Medication dosing guidance
- Polypharmacy review

---

## 6. Epilepsy Consultation

### 6.1 Seizure Classification

EPIDISC helps classify seizures according to the International League Against Epilepsy (ILAE) classification system.

**Focal Onset Seizures**
- **Focal Aware Seizures**: Patient remains aware during the episode
- **Focal Impaired Awareness Seizures**: Patient's awareness is impaired
- **Focal Motor Seizures**: Movement-based symptoms (jerking, stiffness)
- **Focal Non-Motor Seizures**: Sensory, autonomic, or cognitive symptoms

**Generalized Onset Seizures**
- **Tonic-Clonic Seizures**: Convulsions with loss of consciousness
- **Absence Seizures**: Brief staring spells, common in children
- **Myoclonic Seizures**: Sudden brief muscle jerks
- **Atonic Seizures**: Sudden loss of muscle tone
- **Tonic Seizures**: Sudden muscle stiffness

**Unknown Onset Seizures**
- When the onset cannot be determined (often unwitnessed events)

### 6.2 EEG Interpretation Assistance

EPIDISC provides guidance on EEG findings and their clinical significance.

**Common EEG Patterns in Epilepsy**

**Interictal Epileptiform Discharges**
- **Spikes**: Sharp, transient waves (20-70 ms duration)
- **Sharp Waves**: Similar to spikes but longer duration (70-200 ms)
- **Spike-and-Wave Discharges**: Complexes with slow wave following spike

**Ictal Patterns** (during seizures)
- **Rhythmic Theta Activity**: Suggests focal seizure onset
- **Generalized Spike-and-Wave**: 3 Hz pattern typical of absence seizures
- **Electrodecremental Patterns**: Flattening suggesting seizure onset

**Localization Significance**
- **Temporal Lobe Spikes**: Common in mesial temporal lobe epilepsy
- **Frontal Lobe Discharges**: Often associated with sleep-related seizures
- **Generalized Patterns**: Suggest generalized epilepsy syndromes

### 6.3 Antiepileptic Medication Consultation

**First-Line AED Selection**

**For Focal Seizures**
- Levetiracetam: Broad-spectrum, well-tolerated, minimal drug interactions
- Lamotrigine: Well-tolerated, mood-stabilizing properties, requires slow titration
- Carbamazepine: Effective, but significant drug interactions and side effects

**For Generalized Seizures**
- Valproate: Broad-spectrum, effective for multiple seizure types
- Levetiracetam: Effective for both focal and generalized seizures
- Lamotrigine: Effective for generalized seizures, mood benefits

**Special Considerations**

**Women of Childbearing Age**
- Avoid valproate due to teratogenic risk
- Lamotrigine preferred (lower teratogenic risk)
- Levetiracetam acceptable (limited pregnancy data)

**Elderly Patients**
- Consider renal function when dosing
- Lower starting doses to avoid side effects
- Prefer AEDs with fewer drug interactions

**Patients with Comorbidities**
- Liver disease: Avoid hepatically metabolized AEDs
- Renal impairment: Adjust doses of renally excreted AEDs
- Psychiatric history: Some AEDs may affect mood

### 6.4 Seizure Emergency Management

**Status Epilepticus**

**Definition**: Seizure lasting longer than 5 minutes or recurrent seizures without recovery between episodes.

**Emergency Management Steps**:
1. Ensure airway protection and oxygenation
2. Establish intravenous access
3. Administer benzodiazepine (lorazepam first-line)
4. If seizure continues, administer emergency AED
5. Identify and treat underlying cause

**Seizure First Aid for Non-Medical Personnel**

**During a Seizure**:
- Protect from injury (cushion head, remove hazards)
- Do not restrain the person
- Do not put anything in the mouth
- Time the seizure
- Place in recovery position if possible

**After a Seizure**:
- Check for breathing and provide rescue breathing if needed
- Stay with person until fully recovered
- Note seizure characteristics for medical report

### 6.5 Epilepsy Syndromes

**Common Epilepsy Syndromes**

**Mesial Temporal Lobe Epilepsy (MTLE)**
- Most common epilepsy syndrome in adults
- Typical aura: epigastric rising sensation, déjà vu, fear
- Often associated with hippocampal sclerosis
- Good surgical outcomes if drug-resistant

**Idiopathic Generalized Epilepsy**
- **Juvenile Myoclonic Epilepsy**: Myoclonic jerks, generalized tonic-clonic seizures, often provoked by sleep deprivation and alcohol
- **Childhood Absence Epilepsy**: Frequent absence seizures in children, often outgrown
- **Generalized tonic-clonic seizures alone**: Later onset generalized epilepsy

**Lennox-Gastaut Syndrome**
- Severe childhood-onset epilepsy
- Multiple seizure types (tonic, atonic, atypical absence)
- Treatment-resistant, poor prognosis
- Requires multiple AEDs

### 6.6 Treatment-Resistant Epilepsy

**Definition**: Failure of two appropriately chosen and tolerated AEDs to achieve sustained seizure freedom.

**Evaluation Approach**:
1. Confirm diagnosis (are events really epileptic seizures?)
2. Review AED trials (were they adequate doses and durations?)
3. Identify precipitating factors (sleep deprivation, alcohol, medications)
4. Consider alternative diagnoses (psychogenic nonepileptic seizures, syncope)

**Management Options**:
- Add another AED (rational polytherapy)
- Evaluate for epilepsy surgery
- Consider neurostimulation (VNS, DBS, responsive neurostimulation)
- Dietary therapies (ketogenic diet, modified Atkins diet)

---

## 7. Privacy and Security

### 7.1 Privacy Commitment

EPIDISC is designed with privacy as the foundational principle:

✅ **Local Storage Only**: All patient data stored on your local machine  
✅ **No External Transmission**: No patient information sent to external servers  
✅ **Natural Language Privacy**: Consultations remain in your local environment  
✅ **Persistent Privacy**: Privacy settings maintained across sessions  

### 7.2 Data Storage Locations

All patient consultation data is stored in secure local directories on your computer. No information is transmitted to external services or cloud storage.

### 7.3 Privacy Features

**Local Memory System**
- Patient records stored only on your computer
- Consultation history kept locally
- No data transmitted to external services

**Session Privacy**
- Each consultation session remains isolated
- No cross-contamination between patient records
- Memory cleared between sessions if desired

**No External LLM Calls**
- All medical knowledge processing happens locally
- No patient queries sent to external AI services
- Complete privacy of consultation content

### 7.4 Security Considerations

- **Local Access Control**: Protect your computer access with passwords
- **Backup Security**: Secure backup procedures for consultation data
- **Dashboard Privacy**: Dashboard accessible only on your local computer
- **No Network Dependency**: System designed to work without internet connection

---

## 8. Dashboard Guide

### 8.1 Dashboard Interface

The EPIDISC dashboard provides a user-friendly web interface for medical consultation through your web browser.

**Accessing the Dashboard**
- Open your web browser
- Navigate to the displayed address (typically http://localhost:8790)
- The dashboard will load automatically

### 8.2 Dashboard Features

**Consultation Interface**
- Natural language input field for your questions
- Clear display of consultation responses
- Confidence level indicators
- Source references for medical information

**Patient Management**
- Local patient record storage
- Consultation history tracking
- Test result storage
- Progress notes

**Multi-Specialty Coordination**
- Second opinion request options
- Cross-specialty consultation
- Reference tracking

**Settings and Preferences**
- Customize consultation display
- Adjust privacy settings
- Configure memory options

### 8.3 Dashboard Navigation

**Main Consultation Tab**
- Ask your medical questions
- Receive consultation responses
- View confidence scores and sources

**Patient Records Tab**
- Access stored patient information
- Review consultation history
- Update patient details

**Settings Tab**
- Adjust system preferences
- Configure privacy options
- Manage storage locations

---

## 9. Troubleshooting

### 9.1 Common Issues

**System Not Responding**

**Symptoms**: Long wait times, no response to questions

**Solutions**:
- Check your computer has sufficient memory available
- Restart the EPIDISC application
- Clear memory cache through settings

**Import Errors**

**Symptoms**: System messages about missing components

**Solutions**:
- Verify EPIDISC installation is complete
- Restart your computer
- Reinstall EPIDISC if needed

**Dashboard Not Accessible**

**Symptoms**: Cannot access dashboard in web browser

**Solutions**:
- Ensure EPIDISC application is running
- Check that the dashboard address is correct
- Try refreshing your web browser

**Memory Not Persisting**

**Symptoms**: Consultation history not saved between sessions

**Solutions**:
- Ensure memory system is initialized
- Check storage location permissions
- Verify sufficient disk space available

### 9.2 Performance Optimization

**For Large Patient Records**
- Use specific questions rather than broad requests
- Access individual patient consultations directly

**For Repeated Consultations**
- Use the persistent session feature
- Access consultation history for follow-up questions

### 9.3 Getting Help

If issues persist:

1. Review this user manual for relevant information
2. Check system status in the dashboard
3. Review error messages carefully
4. Verify system installation integrity

---

## 10. Medical Disclaimer

### 10.1 Important Notice

**EPIDISC provides second opinion consultation and is NOT a replacement for professional medical care.**

### 10.2 System Limitations

EPIDISC is designed to:
- ✅ Provide second opinions on epilepsy and neurological conditions
- ✅ Assist with EEG interpretation guidance
- ✅ Offer consultation on seizure management
- ✅ Provide cross-specialty consultation
- ✅ Deliver health information and education

EPIDISC is NOT designed to:
- ❌ Replace professional medical diagnosis
- ❌ Make treatment decisions without physician oversight
- ❌ Handle medical emergencies
- ❌ Replace clinical judgment

### 10.3 Emergency Care

**For medical emergencies, contact emergency services immediately.**

Do not rely on EPIDISC for:
- Status epilepticus (prolonged seizures)
- Seizure clusters
- First-time seizures
- Seizures with injury
- Postictal complications

### 10.4 Clinical Decision Making

All medical decisions should be made in consultation with qualified healthcare professionals. EPIDISC consultation should be:
- Considered as a second opinion
- Verified with clinical judgment
- Supplemented with current medical guidelines
- Used in conjunction with patient assessment

### 10.5 Professional Responsibility

Users of EPIDISC are responsible for:
- Ensuring appropriate use of consultation results
- Maintaining professional standards of care
- Protecting patient privacy and confidentiality
- Following local regulations and guidelines
- Obtaining appropriate medical training and credentials

---

## 11. Support and Resources

### 11.1 Documentation

- **User Manual**: This document
- **Quick Reference Guide**: Summary of common consultations
- **Clinical Guidelines**: Integration with current epilepsy guidelines

### 11.2 Testing and Verification

**System Health Check**
- The EPIDISC dashboard includes system status verification
- Regular testing ensures all components are functioning

**Domain Verification**
- All medical domains are tested for proper consultation responses
- Accuracy verification for epilepsy consultations

### 11.3 Citation

If you use EPIDISC in your research, please cite:

```text
EPIDISC: Medical Discovery and Intelligence System for Consultation
Version 1.0.0, May 2026
Author: Tilanthi
Available: https://github.com/Tilanthi/EPIDISC
```

### 11.4 License

This project is licensed under the MIT License - see the LICENSE file for details.

### 11.5 Contact and Contributions

For questions, issues, or contributions:
- GitHub: https://github.com/Tilanthi/EPIDISC
- Issues: https://github.com/Tilanthi/EPIDISC/issues

---

## Appendix A: Quick Reference

### Epilepsy Consultation Examples

**Seizure Classification Questions**
- "My patient had a seizure starting with right hand jerking, then became confused. What type of seizure is this?"
- "What's the difference between focal and generalized seizures?"
- "How do I classify a seizure when the onset wasn't witnessed?"

**EEG Interpretation Questions**
- "This EEG shows sharp waves in the left temporal region. What does this indicate?"
- "What are the characteristic EEG findings in absence epilepsy?"
- "How do I distinguish between epileptiform and normal variants on EEG?"

**Medication Questions**
- "What first-line AED should I choose for a 30-year-old with new-onset focal seizures?"
- "How should I manage levetiracetam side effects like irritability?"
- "Which AEDs are safe in pregnancy?"
- "What are the common drug interactions with carbamazepine?"

**Emergency Questions**
- "What should I do for a patient who has been seizing for 10 minutes?"
- "What's the emergency management of status epilepticus?"
- "What seizure first aid should I teach to family members?"

### Confidence Level Interpretation

| Confidence | Range | Action |
|------------|-------|--------|
| High | ≥90% | Suitable for clinical decision support |
| Medium | 70-89% | Verify with additional information |
| Low | <70% | Recommend specialist consultation |

### Emergency Keywords

The system automatically detects emergency conditions:
- Status epilepticus
- Prolonged seizures
- Seizure clusters
- First seizure
- Seizure with injury

---

## Appendix B: Example Consultations

### Example 1: Seizure Classification

**Question**: "My patient experienced an episode where she suddenly stopped speaking, stared blankly, and didn't respond to her name for about 30 seconds. Then she returned to normal without confusion. What type of seizure might this be?"

**EPIDISC Response**: "This description suggests a **focal aware seizure** or possibly an **absence seizure**. The key features are:

- **Brief duration** (30 seconds) - typical of absence seizures
- **Sudden onset and offset** - characteristic of both absence and focal seizures
- **No postictal confusion** - suggests absence or focal aware seizure
- **Staring and unresponsiveness** - common to both types

**Distinguishing Features**:
- **Absence seizures**: Typically very brief (5-10 seconds), more common in children, often provoked by hyperventilation
- **Focal aware seizures**: May have aura, longer duration, may have automatisms

**Recommendation**: EEG evaluation would help distinguish between these possibilities. Hyperventilation and photic stimulation during EEG may provoke absence seizures."

**Confidence**: 85%

### Example 2: AED Selection

**Question**: "What antiepileptic drug would you recommend for a 28-year-old woman with focal seizures who is planning to become pregnant in the next year?"

**EPIDISC Response**: "For this patient, I recommend **lamotrigine** as the first-line choice, with **levetiracetam** as an alternative.

**Lamotrigine Advantages**:
- Lower teratogenic risk compared to other AEDs
- Good efficacy for focal seizures
- Mood-stabilizing properties may be beneficial
- Well-tolerated overall

**Lamotrigine Considerations**:
- Requires slow titration (to avoid rash)
- Needs dose adjustment during pregnancy
- May have less efficacy than some alternatives

**Levetiracetam Alternative**:
- Also considered safe in pregnancy
- Can be started at effective dose quickly
- Different side effect profile (behavioral effects possible)

**To Avoid**:
- **Valproate**: High teratogenic risk (neural tube defects, cognitive effects)
- **Phenytoin**: Significant teratogenic risk
- **Phenobarbital**: Teratogenic risk and cognitive effects

**Confidence**: 90%

### Example 3: EEG Consultation

**Question**: "This EEG report describes 'sharp wave discharges over the left anterior temporal region during sleep'. What does this finding indicate?"

**EPIDISC Response**: "This EEG finding suggests **focal epilepsy**, likely **temporal lobe epilepsy (TLE)**.

**Interpretation of the Finding**:

**'Sharp wave discharges'**: These are interictal epileptiform discharges (IEDs) indicating cortical hyperexcitability. Sharp waves are similar to spikes but slightly longer in duration (70-200 ms vs 20-70 ms).

**'Left anterior temporal region'**: This localization strongly suggests:
- **Mesial temporal lobe epilepsy** (most common)
- Possible hippocampal sclerosis
- Often associated with focal impaired awareness seizures

**'During sleep'**: Epileptiform discharges often activate during sleep, particularly in temporal lobe epilepsy. This increases the yield of EEG monitoring.

**Clinical Correlation**:
- Does the patient have focal seizures with impaired awareness?
- Are there any auras (rising epigastric sensation, déjà vu, fear)?
- Any history of febrile seizures or meningitis?

**Next Steps**:
- Consider MRI brain to evaluate for hippocampal sclerosis
- Sleep-deprived EEG or prolonged monitoring if seizures are frequent
- If drug-resistant, consider presurgical evaluation

**Confidence**: 88%

---

## Appendix C: Consultation Guidelines

### How to Get the Best Consultations

**1. Be Specific About Your Question**

Instead of: "What medication for epilepsy?"
Try: "What AED would you recommend for a 45-year-old man with focal seizures who also has hypertension?"

**2. Include Relevant Clinical Context**

- Patient age and gender
- Seizure type and frequency
- Previous AED trials and responses
- Comorbid medical conditions
- Current medications
- Any relevant test results

**3. Describe Test Results Accurately**

For EEG consultations:
- "The EEG shows rhythmic sharp wave discharges at 4 Hz over the left temporal region"
- Include activation methods (hyperventilation, photic stimulation, sleep)

For imaging:
- "MRI shows left hippocampal atrophy on T1-weighted sequences"

**4. Ask Clear, Focused Questions**

- "What are the indications for epilepsy surgery in this case?"
- "How should I manage this patient's seizure clusters?"
- "What's the differential diagnosis for these episodes?"

---

**End of User Manual**

*This manual provides comprehensive guidance for using the EPIDISC medical consultation system. For the most current information, check for updates at the project repository.*

*Version 1.0.0 - May 2026*
