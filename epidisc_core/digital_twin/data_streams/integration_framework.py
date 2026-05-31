"""
EPIDISC Data Stream Integration Framework
Handles continuous data inputs from wearables, sensors, and patient reports
"""

from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum
import json
from abc import ABC, abstractmethod


class DataSource(Enum):
    """Types of data sources"""
    WEARABLE_DEVICE = "wearable_device"
    MOBILE_APP = "mobile_app"
    PATIENT_REPORT = "patient_report"
    CLINICIAN_REPORT = "clinician_report"
    SMART_MONITOR = "smart_monitor"
    ENVIRONMENTAL_SENSOR = "environmental_sensor"
    LAB_RESULTS = "lab_results"
    EPISODE_LOGGER = "episode_logger"


class DataFrequency(Enum):
    """Data collection frequencies"""
    CONTINUOUS = "continuous"  # Every second
    HIGH_FREQUENCY = "high_frequency"  # Every minute
    MEDIUM_FREQUENCY = "medium_frequency"  # Every hour
    LOW_FREQUENCY = "low_frequency"  # Daily
    EPISODIC = "episodic"  # As needed


@dataclass
class DataStreamConfig:
    """Configuration for a data stream"""
    stream_name: str
    source_type: DataSource
    frequency: DataFrequency
    enabled: bool = True
    retention_days: int = 365
    quality_threshold: float = 0.7
    metadata: Dict[str, Any] = None


class StreamProcessor(ABC):
    """Abstract base class for stream processors"""

    @abstractmethod
    def process(self, raw_data: Any) -> Any:
        """Process raw data into standardized format"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate data quality"""
        pass


class SleepDataProcessor(StreamProcessor):
    """Process sleep data from various sources"""

    def process(self, raw_data: Any) -> Dict:
        """Process raw sleep data"""
        if isinstance(raw_data, dict):
            return {
                'duration_hours': raw_data.get('duration', 0),
                'quality_score': raw_data.get('quality', 0.5),
                'deep_sleep_percentage': raw_data.get('deep_sleep', 0),
                'rem_sleep_percentage': raw_data.get('rem_sleep', 0),
                'sleep_efficiency': raw_data.get('efficiency', 0.8),
                'interruptions': raw_data.get('interruptions', 0),
                'bedtime': raw_data.get('bedtime'),
                'wake_time': raw_data.get('wake_time'),
                'timestamp': raw_data.get('timestamp', datetime.now().isoformat())
            }
        return raw_data

    def validate(self, data: Any) -> bool:
        """Validate sleep data"""
        if isinstance(data, dict):
            duration = data.get('duration', 0)
            return 0 <= duration <= 24  # Reasonable sleep duration
        return False


class MedicationDataProcessor(StreamProcessor):
    """Process medication adherence data"""

    def process(self, raw_data: Any) -> Dict:
        """Process raw medication data"""
        if isinstance(raw_data, dict):
            return {
                'medication_name': raw_data.get('medication'),
                'scheduled_time': raw_data.get('scheduled_time'),
                'actual_time': raw_data.get('actual_time'),
                'dose': raw_data.get('dose'),
                'status': self._determine_status(raw_data),
                'side_effects': raw_data.get('side_effects', []),
                'timestamp': raw_data.get('timestamp', datetime.now().isoformat())
            }
        return raw_data

    def _determine_status(self, data: Dict) -> str:
        """Determine adherence status"""
        scheduled = data.get('scheduled_time')
        actual = data.get('actual_time')

        if not actual:
            return 'missed'

        if scheduled:
            scheduled_dt = datetime.fromisoformat(scheduled) if isinstance(scheduled, str) else scheduled
            actual_dt = datetime.fromisoformat(actual) if isinstance(actual, str) else actual

            time_diff = (actual_dt - scheduled_dt).total_seconds() / 60  # minutes

            if time_diff < -15:  # Taken too early
                return 'early'
            elif time_diff > 60:  # Taken more than 1 hour late
                return 'late'
            else:
                return 'taken'

        return 'taken'

    def validate(self, data: Any) -> bool:
        """Validate medication data"""
        if isinstance(data, dict):
            return bool(data.get('medication'))
        return False


class StressDataProcessor(StreamProcessor):
    """Process stress level data"""

    def process(self, raw_data: Any) -> Dict:
        """Process raw stress data"""
        if isinstance(raw_data, dict):
            return {
                'stress_level': raw_data.get('level', 5),  # 1-10 scale
                'hrv': raw_data.get('hrv'),  # Heart rate variability
                'cortisol_indicator': raw_data.get('cortisol'),
                'self_reported': raw_data.get('self_reported', True),
                'factors': raw_data.get('factors', []),
                'timestamp': raw_data.get('timestamp', datetime.now().isoformat())
            }
        elif isinstance(raw_data, (int, float)):
            return {
                'stress_level': max(1, min(10, raw_data)),  # Clamp to 1-10
                'self_reported': True,
                'timestamp': datetime.now().isoformat()
            }
        return raw_data

    def validate(self, data: Any) -> bool:
        """Validate stress data"""
        if isinstance(data, dict):
            level = data.get('level', 0)
            return 1 <= level <= 10
        return False


class EnvironmentalDataProcessor(StreamProcessor):
    """Process environmental trigger data"""

    def process(self, raw_data: Any) -> Dict:
        """Process raw environmental data"""
        if isinstance(raw_data, dict):
            return {
                'weather_condition': raw_data.get('weather'),
                'temperature': raw_data.get('temperature'),
                'humidity': raw_data.get('humidity'),
                'barometric_pressure': raw_data.get('pressure'),
                'air_quality_index': raw_data.get('aqi'),
                'uv_index': raw_data.get('uv'),
                'light_exposure': raw_data.get('light'),
                'noise_level': raw_data.get('noise'),
                'location': raw_data.get('location'),
                'timestamp': raw_data.get('timestamp', datetime.now().isoformat())
            }
        return raw_data

    def validate(self, data: Any) -> bool:
        """Validate environmental data"""
        return isinstance(data, dict)


class SeizureEventDataProcessor(StreamProcessor):
    """Process detailed seizure event reports"""

    def process(self, raw_data: Any) -> Dict:
        """Process raw seizure event data"""
        if isinstance(raw_data, dict):
            return {
                'seizure_type': raw_data.get('type'),
                'duration_seconds': raw_data.get('duration', 0),
                'severity': raw_data.get('severity', 'moderate'),
                'aura_present': raw_data.get('aura', False),
                'aura_description': raw_data.get('aura_description'),
                'triggers': raw_data.get('triggers', []),
                'postictal_state': raw_data.get('postictal'),
                'context': {
                    'activity': raw_data.get('activity'),
                    'location': raw_data.get('location'),
                    'witnesses': raw_data.get('witnesses', False)
                },
                'timestamp': raw_data.get('timestamp', datetime.now().isoformat())
            }
        return raw_data

    def validate(self, data: Any) -> bool:
        """Validate seizure event data"""
        if isinstance(data, dict):
            return bool(data.get('type'))
        return False


class DataStreamIntegration:
    """
    Main integration framework for all data streams.

    Handles collection, validation, processing, and routing of
    continuous health data from multiple sources.
    """

    def __init__(self):
        self.stream_configs: Dict[str, DataStreamConfig] = {}
        self.processors: Dict[str, StreamProcessor] = {}
        self.data_buffer: List[Dict] = []
        self.quality_metrics: Dict[str, float] = {}
        self._initialize_default_processors()

    def _initialize_default_processors(self):
        """Initialize default data processors"""
        self.processors['sleep'] = SleepDataProcessor()
        self.processors['medication'] = MedicationDataProcessor()
        self.processors['stress'] = StressDataProcessor()
        self.processors['environmental'] = EnvironmentalDataProcessor()
        self.processors['seizure_event'] = SeizureEventDataProcessor()

    def register_stream(self, config: DataStreamConfig) -> None:
        """Register a new data stream"""
        self.stream_configs[config.stream_name] = config

    def register_processor(self, stream_name: str, processor: StreamProcessor) -> None:
        """Register a custom processor for a stream"""
        self.processors[stream_name] = processor

    def ingest_data(self, stream_name: str, raw_data: Any, source: str = None) -> Optional[Dict]:
        """Ingest data from a stream"""
        if stream_name not in self.stream_configs:
            # Auto-register stream with default config
            self.register_stream(DataStreamConfig(
                stream_name=stream_name,
                source_type=DataSource.PATIENT_REPORT,
                frequency=DataFrequency.EPISODIC
            ))

        config = self.stream_configs[stream_name]

        if not config.enabled:
            return None

        # Get appropriate processor
        processor = self._get_processor_for_stream(stream_name)

        if processor:
            # Process and validate data
            processed_data = processor.process(raw_data)

            if processor.validate(processed_data):
                # Add metadata
                enriched_data = {
                    'stream_name': stream_name,
                    'source': source or config.source_type.value,
                    'processed_data': processed_data,
                    'timestamp': datetime.now().isoformat(),
                    'quality_score': self._calculate_quality_score(processed_data),
                    'config': {
                        'frequency': config.frequency.value,
                        'retention_days': config.retention_days
                    }
                }

                self.data_buffer.append(enriched_data)
                return enriched_data
            else:
                self._log_quality_issue(stream_name, processed_data)
                return None

        return None

    def _get_processor_for_stream(self, stream_name: str) -> Optional[StreamProcessor]:
        """Get appropriate processor for stream"""
        # Try exact match first
        if stream_name in self.processors:
            return self.processors[stream_name]

        # Try category match
        for key, processor in self.processors.items():
            if key in stream_name.lower():
                return processor

        return None

    def _calculate_quality_score(self, data: Any) -> float:
        """Calculate quality score for data"""
        score = 1.0

        # Check for completeness
        if isinstance(data, dict):
            total_fields = len(data)
            non_null_fields = sum(1 for v in data.values() if v is not None)
            completeness = non_null_fields / total_fields if total_fields > 0 else 0
            score *= completeness

        return score

    def _log_quality_issue(self, stream_name: str, data: Any) -> None:
        """Log data quality issues"""
        if stream_name not in self.quality_metrics:
            self.quality_metrics[stream_name] = 0.0

        # Simple quality tracking
        current_quality = self.quality_metrics[stream_name]
        self.quality_metrics[stream_name] = (current_quality * 0.9) + (0.0 * 0.1)

    def get_processed_data(self, stream_name: str = None, limit: int = 100) -> List[Dict]:
        """Get processed data from buffer"""
        if stream_name:
            return [d for d in self.data_buffer if d['stream_name'] == stream_name][-limit:]
        return self.data_buffer[-limit:]

    def get_quality_metrics(self) -> Dict[str, float]:
        """Get quality metrics for all streams"""
        return self.quality_metrics.copy()

    def flush_buffer(self) -> List[Dict]:
        """Flush all data from buffer"""
        data = self.data_buffer.copy()
        self.data_buffer.clear()
        return data

    def export_config(self) -> str:
        """Export stream configurations"""
        configs = {}
        for name, config in self.stream_configs.items():
            configs[name] = {
                'source_type': config.source_type.value,
                'frequency': config.frequency.value,
                'enabled': config.enabled,
                'retention_days': config.retention_days,
                'quality_threshold': config.quality_threshold,
                'metadata': config.metadata
            }
        return json.dumps(configs, indent=2)


class WearableDeviceIntegration:
    """Integration with specific wearable devices"""

    def __init__(self, integration_framework: DataStreamIntegration):
        self.framework = integration_framework
        self.device_connections = {}

    def connect_oura_ring(self, api_key: str) -> bool:
        """Connect to Oura Ring API"""
        try:
            # Placeholder for actual API connection
            self.device_connections['oura_ring'] = {
                'type': 'oura_ring',
                'api_key': api_key,
                'connected': True,
                'last_sync': None
            }
            return True
        except Exception as e:
            print(f"Failed to connect Oura Ring: {e}")
            return False

    def connect_apple_watch(self, api_key: str) -> bool:
        """Connect to Apple Watch HealthKit"""
        try:
            # Placeholder for actual API connection
            self.device_connections['apple_watch'] = {
                'type': 'apple_watch',
                'api_key': api_key,
                'connected': True,
                'last_sync': None
            }
            return True
        except Exception as e:
            print(f"Failed to connect Apple Watch: {e}")
            return False

    def sync_oura_data(self) -> int:
        """Sync data from Oura Ring"""
        if 'oura_ring' not in self.device_connections:
            return 0

        # Placeholder for actual data sync
        # In real implementation, this would:
        # 1. Fetch sleep data from Oura API
        # 2. Fetch readiness score
        # 3. Fetch activity data
        # 4. Process and ingest into framework

        records_count = 0  # Placeholder

        return records_count

    def sync_apple_watch_data(self) -> int:
        """Sync data from Apple Watch"""
        if 'apple_watch' not in self.device_connections:
            return 0

        # Placeholder for actual data sync
        # In real implementation, this would:
        # 1. Fetch HealthKit data
        # 2. Fetch heart rate variability
        # 3. Fetch sleep analysis
        # 4. Fetch activity rings
        # 5. Process and ingest into framework

        records_count = 0  # Placeholder

        return records_count

    def get_connected_devices(self) -> List[str]:
        """Get list of connected devices"""
        return list(self.device_connections.keys())


# Convenience function for creating integration framework
def create_integration_framework() -> DataStreamIntegration:
    """Create a new data stream integration framework"""
    return DataStreamIntegration()


def create_wearable_integration(framework: DataStreamIntegration) -> WearableDeviceIntegration:
    """Create wearable device integration"""
    return WearableDeviceIntegration(framework)
