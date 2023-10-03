from typing import List, Optional

from pydantic import BaseModel


class BashDagRequest(BaseModel):
    """Request for Bash Generating."""

    steps: List[tuple[str, str]]
    connections: List[tuple[str, str]]
    dag_id: str
    start_year: int
    start_month: int
    start_day: int
    schedule_interval: Optional[str] = None
