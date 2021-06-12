from dataclasses import dataclass

@dataclass
class INSData:
    file_id: str
    path: str
    region: str
    init_date: str
    final_date: str
