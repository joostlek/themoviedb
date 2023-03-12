from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas._partial import PartialEpisode
from themoviedb.schemas.credits import Cast, Crew


@dataclass
class Episode(PartialEpisode):
    crew: Optional[List[Crew]] = None
    guest_stars: Optional[List[Cast]] = None

    def __str__(self) -> str:
        return self.name

    def still_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.still_path}" if self.still_path else None
