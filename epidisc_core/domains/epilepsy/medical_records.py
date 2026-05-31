"""
Medical Records Processing System

Transformative enhancement: Comprehensive medical records processing
for epilepsy consultation with support for multiple formats (text, PDF, images).

This system handles:
- Text medical records
- PDF medical reports
- Images (EEG, MRI, CT)
- Confidential patient record storage
- Integration with persistent memory
- Semantic extraction for epilepsy consultation
"""

import os
import json
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import hashlib
import base64

# Try to import document processing libraries
try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False

try:
    from PIL import Image
    import pytesseract
    IMAGE_PROCESSING_AVAILABLE = True
except ImportError:
    IMAGE_PROCESSING_AVAILABLE = False


@dataclass
class MedicalRecord:
    """Comprehensive medical record for epilepsy patients"""
    patient_id: str
    record_type: str  # "text", "pdf", "image", "ekg", "eeg", "mri", "ct"
    content: Any  # Text content, extracted text, or image data
    original_file: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    confidentiality_level: str = "high"  # "high", "medium", "low"

    def __hash__(self):
        return hash((self.patient_id, self.record_type, self.timestamp))


@dataclass
class PatientRecord:
    """Complete patient record for epilepsy consultation"""
    patient_id: str
    demographics: Dict[str, Any] = field(default_factory=dict)
    medical_records: List[MedicalRecord] = field(default_factory=list)
    seizure_history: List[Dict[str, Any]] = field(default_factory=list)
    medication_history: List[Dict[str, Any]] = field(default_factory=list)
    eeg_records: List[MedicalRecord] = field(default_factory=list)
    imaging_records: List[MedicalRecord] = field(default_factory=list)
    consultation_notes: List[str] = field(default_factory=list)
    created_date: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)

    def add_record(self, record: MedicalRecord) -> None:
        """Add a medical record to the patient's file"""
        self.medical_records.append(record)
        self.last_updated = datetime.now()

        # Categorize by type
        if record.record_type == "eeg":
            self.eeg_records.append(record)
        elif record.record_type in ["mri", "ct"]:
            self.imaging_records.append(record)

    def get_relevant_records(self, query_type: str) -> List[MedicalRecord]:
        """Get records relevant to a specific consultation query"""
        relevant_records = []

        if "seizure" in query_type.lower():
            relevant_records.extend([r for r in self.medical_records if "seizure" in str(r.content).lower()])

        if "eeg" in query_type.lower() or "electroencephalogram" in query_type.lower():
            relevant_records.extend(self.eeg_records)

        if "mri" in query_type.lower() or "imaging" in query_type.lower():
            relevant_records.extend(self.imaging_records)

        return relevant_records


class MedicalRecordsProcessor:
    """
    Medical records processing system with support for multiple formats.

    Transformative capabilities:
    - Text extraction from PDF medical reports
    - OCR processing of medical images
    - Confidential storage of patient records
    - Semantic extraction for epilepsy consultation
    - Integration with persistent memory
    """

    def __init__(self, storage_dir: str = "epidisc_core/data/patients"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.patients: Dict[str, PatientRecord] = {}

    def process_record(self, patient_id: str, file_path: str, record_type: str) -> MedicalRecord:
        """
        Process a medical record file and extract content.

        Args:
            patient_id: Patient identifier
            file_path: Path to the medical record file
            record_type: Type of medical record

        Returns:
            MedicalRecord with extracted content
        """
        file_extension = Path(file_path).suffix.lower()

        if file_extension == ".pdf":
            content = self._extract_pdf_text(file_path)
        elif file_extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
            content = self._extract_image_text(file_path)
        elif file_extension in [".txt", ".md"]:
            content = self._read_text_file(file_path)
        else:
            content = f"Unsupported file format: {file_extension}"

        # Create medical record
        record = MedicalRecord(
            patient_id=patient_id,
            record_type=record_type,
            content=content,
            original_file=file_path,
            metadata={
                "file_size": os.path.getsize(file_path),
                "file_extension": file_extension,
                "processed_date": datetime.now().isoformat()
            }
        )

        return record

    def _extract_pdf_text(self, pdf_path: str) -> str:
        """Extract text from PDF medical reports"""
        if not PYPDF2_AVAILABLE:
            return "PDF processing not available - PyPDF2 not installed"

        try:
            import PyPDF2
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text_content = []

                for page in reader.pages:
                    text_content.append(page.extract_text())

                return "\n".join(text_content)
        except Exception as e:
            return f"Error processing PDF: {str(e)}"

    def _extract_image_text(self, image_path: str) -> str:
        """Extract text from medical images using OCR"""
        if not IMAGE_PROCESSING_AVAILABLE:
            return "Image processing not available - PIL and pytesseract not installed"

        try:
            from PIL import Image
            import pytesseract

            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            return f"Error processing image: {str(e)}"

    def _read_text_file(self, text_path: str) -> str:
        """Read text medical records"""
        try:
            with open(text_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error reading text file: {str(e)}"

    def create_patient_record(self, patient_id: str, demographics: Dict[str, Any] = None) -> PatientRecord:
        """Create a new patient record"""
        patient_record = PatientRecord(
            patient_id=patient_id,
            demographics=demographics or {}
        )

        self.patients[patient_id] = patient_record
        self._save_patient_record(patient_record)

        return patient_record

    def add_record_to_patient(self, patient_id: str, record: MedicalRecord) -> None:
        """Add a medical record to a patient's file"""
        if patient_id not in self.patients:
            self.create_patient_record(patient_id)

        self.patients[patient_id].add_record(record)
        self._save_patient_record(self.patients[patient_id])

    def get_patient_record(self, patient_id: str) -> Optional[PatientRecord]:
        """Retrieve a patient's complete record"""
        if patient_id not in self.patients:
            self._load_patient_record(patient_id)

        return self.patients.get(patient_id)

    def search_records(self, patient_id: str, search_term: str) -> List[MedicalRecord]:
        """Search within a patient's records for specific terms"""
        patient_record = self.get_patient_record(patient_id)
        if not patient_record:
            return []

        matching_records = []
        search_lower = search_term.lower()

        for record in patient_record.medical_records:
            content_str = str(record.content).lower()
            if search_term.lower() in content_str:
                matching_records.append(record)

        return matching_records

    def _save_patient_record(self, patient_record: PatientRecord) -> None:
        """Save patient record to disk (confidential storage)"""
        patient_dir = self.storage_dir / patient_record.patient_id
        patient_dir.mkdir(exist_ok=True)

        # Save patient record as JSON
        record_file = patient_dir / "patient_record.json"

        # Convert datetime objects to strings for JSON serialization
        record_data = {
            "patient_id": patient_record.patient_id,
            "demographics": patient_record.demographics,
            "medical_records": [
                {
                    "patient_id": r.patient_id,
                    "record_type": r.record_type,
                    "content": str(r.content)[:1000],  # Truncate for storage
                    "original_file": r.original_file,
                    "timestamp": r.timestamp.isoformat(),
                    "metadata": r.metadata,
                    "confidentiality_level": r.confidentiality_level
                }
                for r in patient_record.medical_records
            ],
            "seizure_history": patient_record.seizure_history,
            "medication_history": patient_record.medication_history,
            "consultation_notes": patient_record.consultation_notes,
            "created_date": patient_record.created_date.isoformat(),
            "last_updated": patient_record.last_updated.isoformat()
        }

        with open(record_file, 'w') as f:
            json.dump(record_data, f, indent=2)

    def _load_patient_record(self, patient_id: str) -> Optional[PatientRecord]:
        """Load patient record from disk"""
        patient_dir = self.storage_dir / patient_id
        record_file = patient_dir / "patient_record.json"

        if not record_file.exists():
            return None

        try:
            with open(record_file, 'r') as f:
                record_data = json.load(f)

            patient_record = PatientRecord(
                patient_id=record_data["patient_id"],
                demographics=record_data["demographics"],
                seizure_history=record_data.get("seizure_history", []),
                medication_history=record_data.get("medication_history", []),
                consultation_notes=record_data.get("consultation_notes", []),
                created_date=datetime.fromisoformat(record_data["created_date"]),
                last_updated=datetime.fromisoformat(record_data["last_updated"])
            )

            self.patients[patient_id] = patient_record
            return patient_record

        except Exception as e:
            print(f"Error loading patient record: {e}")
            return None

    def get_consultation_context(self, patient_id: str, query: str) -> Dict[str, Any]:
        """
        Get relevant patient context for epilepsy consultation.

        This is transformative - it retrieves all relevant medical records
        to provide comprehensive context for consultation.
        """
        patient_record = self.get_patient_record(patient_id)
        if not patient_record:
            return {"patient_id": patient_id, "available": False}

        # Analyze query to determine relevant records
        query_lower = query.lower()

        context = {
            "patient_id": patient_id,
            "demographics": patient_record.demographics,
            "available": True,
            "relevant_records": [],
            "seizure_count": len(patient_record.seizure_history),
            "medication_count": len(patient_record.medication_history)
        }

        # Add relevant records based on query
        if "seizure" in query_lower or "episode" in query_lower:
            context["relevant_records"].extend(patient_record.seizure_history)
            context["seizure_history_available"] = True

        if "medication" in query_lower or "aed" in query_lower or "drug" in query_lower:
            context["relevant_records"].extend(patient_record.medication_history)
            context["medication_history_available"] = True

        if "eeg" in query_lower or "electroencephalogram" in query_lower:
            context["eeg_records"] = len(patient_record.eeg_records)
            context["eeg_content"] = [str(r.content)[:500] for r in patient_record.eeg_records]

        if "mri" in query_lower or "imaging" in query_lower:
            context["imaging_records"] = len(patient_record.imaging_records)
            context["imaging_content"] = [str(r.content)[:500] for r in patient_record.imaging_records]

        return context


# Factory function
def create_medical_records_processor(storage_dir: str = "epidisc_core/data/patients") -> MedicalRecordsProcessor:
    """
    Create medical records processor.

    Args:
        storage_dir: Directory for confidential patient record storage

    Returns:
        MedicalRecordsProcessor configured for multi-format processing
    """
    return MedicalRecordsProcessor(storage_dir)