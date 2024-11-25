from typing import Annotated

from pydantic.types import StringConstraints

# username for User model
UsernameStr = Annotated[str, StringConstraints(min_length=5, max_length=50)]
