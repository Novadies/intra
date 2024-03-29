from typing import List, Optional, Union, Literal, Any
from pydantic import BaseModel, Field


class ItemN(BaseModel):
    numberlist: Optional[Union[int, float]]
    id_fabrics: Optional[str]
    id_work: Optional[Union[int, str]]
    id_insta: Optional[str]
    id_contract: Optional[str]
    id_execut: Optional[str]
    id_object: Optional[str]
    id_cat: Optional[Union[int, str]]
    id_med: Optional[str]
    rectangular: Optional[int]
    flanconnect: Optional[Union[int, str]]
    flanthick: Any
    dismantling: Optional[str]
    mounting: Optional[str]
    gostansi: Optional[int]
    different: Any
    id_diam: Any
    id_diamsi: Any
    otherflange: Any
    rectanga: Any
    rectangb: Any
    id_press: Any
    id_presan: Any
    hydratestpress: Any
    workpress: Any
    opertemp: Any
    calcpress: Any
    calctemp: Any
    flan1: Any
    materialf1: Any
    dentdeff1: Any
    protectcover: Any
    protectcover1: Any
    defflan1: Any
    transdeff1: Any
    longdeff1: Any
    ulcercorf1: Any
    wearsurff1: Any
    violgeomf1: Any
    seasurff1: Any
    whyf: Any
    whyf1: Any
    flan2: Any
    materialf2: Any
    dentdeff2: Any
    defflan2: Any
    transdeff2: Any
    longdeff2: Any
    ulcercorf2: Any
    wearsurff2: Any
    violgeomf2: Any
    seasurff2: Any
    typesurf: Any
    typesurfANSI: Any
    diffdesig: Any
    diffdesig1: Any
    typegasket: Any
    gasket1: Any
    gasketoht: Any
    gasket2: Any
    gasket3: Any
    gasket4: Any
    gasket5: Any
    gasket6: Any
    gasket7: Any
    gasketdiam: Any
    gasketwidth: Any
    gasketthick: Any
    clampedpart: Any
    typefast: Any
    threadpitch: Any
    threadpitchansi: Any
    fastmater: Any
    fastener_vid_inst: Any
    fastinstdiam: Any
    fastinstdiamansi: Any
    fastinstlen: Any
    fastener_vid_need: Any
    fastneeddia: Any
    fastneeddiansi: Any
    fastneedlen: Any
    numberfast: Any
    fastreject: Any
    fastrepl: Any
    fastrecom: Any
    fastcondit: Any
    deffast1: Any
    deffast2: Any
    deffast3: Any
    deffast4: Any
    mnogo: Any
    inconsist1: Any
    inconsist2: Any
    inconsist3: Any
    inconsist4: Any
    inconsist5: Any
    inconsist6: Any
    inconsist7: Any
    inconsist8: Any
    inconsist9: Any
    inconsist10: Any
    typenut: Any
    lubricfast: Any
    tightshem1: Any
    tightshem2: Any
    lubricfast1: Any
    tighttorq: Any
    loosefast: Any
    remarkfast1: Any
    remfastdate1: Any
    remarkfast2: Any
    remfastdate2: Any
    coaxiality: Any
    coaxiality1: Any
    parallel: Any
    parallel1: Any
    tools: Any
    succgidro: Any
    countgidro: Any
    dategidro: Any
    commgidro: Any
    tag1: Any
    tag2: Any
    usesiz: Any
    workingtool: Any
    generalquest: Any
    reactremark: Any
    mechanic: Any
    datemech: Any
    supervisor: Any
    datesuper: Any
    commcheck1: Any
    commcheck: Any
    sxemafile: Any
    edit: Any
    created: Any
