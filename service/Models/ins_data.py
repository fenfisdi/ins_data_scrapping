from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class INSData:
    file_id: str
    path: str 
    region: str 
    init_date: str
    final_date: str 