from typing import List, Optional, Union, Literal
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    numberlist: Optional[Union[int, float]]
    id_fabrics: Optional[str]
    id_work: Optional[Union[int, str]]
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

class Item2(BaseModel):

    id_object: Optional[str]
    id_cat: Optional[Union[int, str]]
    id_med: Optional[str]
    rectangular: Optional[Union[int, str]]
    flanconnect: Optional[Union[int, str]]
    flanthick: Optional[Union[int, float, Literal[""]]]
    dismantling: Optional[str]
    mounting: Optional[str]
    gostansi: Optional[int]