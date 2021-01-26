from enum import Enum

class ExpThresholds(Enum):
    Minimum = 100
    Low = 500
    Medium = 1000
    High = 1500

class ExpMargins(Enum):
    Minimum = 20
    Low = 50
    Medium = 75
    High = 100
    Max = 150
