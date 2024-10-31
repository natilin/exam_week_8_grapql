from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .countries import Countries
from .cities import Cities
from .missions import Missions
from .targets import Targets
from .targettypes import TargetTypes