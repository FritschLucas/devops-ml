from pydantic import BaseModel
from typing import List
from typing import Dict

class ClassificationResult(BaseModel):
    label: str
    confidence: float
    probabilities: Dict[str, float] 