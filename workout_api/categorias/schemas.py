from workout_api.contrib.schemasC import BaseSchema
from typing import Annotated
from pydantic import UUID4, Field


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example = 'Scale', max_length=10)]
class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')] 