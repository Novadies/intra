from typing import List, Optional, Union, Literal, Any
from pydantic import BaseModel, Field


class Item(BaseModel):    # если будет передано меньше полей на проверку, то в словаре будут 'attr': None
    numberlist: Optional[Union[int, float]]    # todo сделать алиасы для полей
    id_fabrics: Optional[str]
    id_work: Optional[Union[int, str]] #= Field(validation_alias='Цех')
    id_insta: Optional[str]
    id_contract: Optional[str]
    id_execut: Optional[str]
    id_object: Optional[str]
    id_cat: Optional[Union[int, str]]
    id_med: Optional[str]
    rectangular: Optional[Union[int, str]]
    flanconnect: Optional[Union[int, str]]
    flanthick: Optional[Union[int, float, Literal[""]]]
    dismantling: Optional[str]
    mounting: Optional[str]
    gostansi: Optional[int]

class Item1(BaseModel):
    # Tут рандомная валидация
    rectangular: Optional[Union[int, str]]
    flanconnect: Optional[Union[int, float, Literal[""]]]
    flanthick: Optional[Union[int, float, Literal[""]]]
    dismantling: Optional[str]
    mounting: Optional[str]
    gostansi: Optional[int]
    different: Optional[str]
    id_diam: Optional[str]
    id_diamsi: Optional[str]
