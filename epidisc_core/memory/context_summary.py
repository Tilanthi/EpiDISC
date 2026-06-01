"""
Context Summary Management System for EPIDISC

Automatically summarizes conversations when approaching context limits,
enabling seamless `/clear` operations while preserving critical context.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional


class ContextSummary:
    """Manages conversation context summaries for long-running sessions."""

    def __init__(self, summary_dir: Optional[Path] = None):
        """Initialize the context summary system.

        Args:
            summary_dir: Directory for storing summaries. Defaults to
                        epidisc_core/data/context/
        """
        if summary_dir is None:
            # Default to epidisc_core/data/context/
            base_dir = Path(__file__).parent.parent.parent / "data" / "context"
            summary_dir = base_dir

        self.summary_dir = Path(summary_dir)
        self.summary_dir.mkdir(parents=True, exist_ok=True)

        # Single summary file that gets constantly updated
        self.summary_file = self.summary_dir / "active_conversation_summary.json"

        # Context thresholds (adjust based on model)
        self.warning_threshold = 0.7  # 70% of context
        self.critical_threshold = 0.85  # 85% of context
        self.max_context_tokens = 200000  # For Opus 4.8

    def should_summarize(self, current_context_length: int) -> bool:
        """Check if conversation should be summarized.

        Args:
            current_context_length: Current token count of conversation

        Returns:
            True if summarization is recommended
        """
        context_ratio = current_context_length / self.max_context_tokens

        # Summarize at 70% of context to leave room for response
        return context_ratio >= self.warning_threshold

    def save_summary(self, summary: str, metadata: dict = None) -> Path:
        """Save a conversation summary to disk.

        Args:
            summary: The summary text
            metadata: Optional metadata (topics, patient_ids, etc.)

        Returns:
            Path to the saved summary file
        """
        summary_data = {
            "timestamp": datetime.now().isoformat(),
            "summary": summary,
            "metadata": metadata or {},
            "version": "1.0.0"
        }

        # Write to summary file (overwrites previous)
        with open(self.summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)

        return self.summary_file

    def load_summary(self) -> Optional[dict]:
        """Load the most recent conversation summary.

        Returns:
            Summary data dict or None if no summary exists
        """
        if not self.summary_file.exists():
            return None

        try:
            with open(self.summary_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

    def get_restoration_context(self) -> str:
        """Get formatted context for conversation restoration.

        Returns:
            Formatted string to restore conversation context
        """
        summary_data = self.load_summary()

        if not summary_data:
            return ""

        timestamp = summary_data.get("timestamp", "Unknown time")
        summary = summary_data.get("summary", "")
        metadata = summary_data.get("metadata", {})

        context_parts = [
            f"# Context Restored from {timestamp}",
            "",
            summary
        ]

        # Add metadata if present
        if metadata:
            context_parts.append("")
            context_parts.append("## Session Metadata")
            for key, value in metadata.items():
                context_parts.append(f"- {key}: {value}")

        return "\n".join(context_parts)

    def clear_summary(self) -> None:
        """Clear the stored summary (start fresh)."""
        if self.summary_file.exists():
            self.summary_file.unlink()


def create_context_summary(summary_dir: Optional[Path] = None) -> ContextSummary:
    """Factory function to create a ContextSummary instance.

    Args:
        summary_dir: Optional custom summary directory

    Returns:
        ContextSummary instance
    """
    return ContextSummary(summary_dir)


# Convenience function for quick restoration
def restore_conversation_context() -> str:
    """Quick restoration of conversation context after /clear.

    Returns:
        Formatted context string or empty string if no summary exists
    """
    ctx_summary = create_context_summary()
    return ctx_summary.get_restoration_context()


def get_context_status() -> dict:
    """Get status of context summary system.

    Returns:
        Dict with status information
    """
    ctx_summary = create_context_summary()
    summary_data = ctx_summary.load_summary()

    return {
        "has_summary": summary_data is not None,
        "summary_file": str(ctx_summary.summary_file),
        "last_summary_time": summary_data.get("timestamp") if summary_data else None,
        "summary_exists": ctx_summary.summary_file.exists()
    }
