import enum
import re

M_PI=3.14159

#
# https://wiki.freecadweb.org/Quantity#Unit
#
#

class UnitType(enum.Enum):
    U_NM = 0
    U_UM = 1
    U_MM = 2
    U_CM = 3
    U_DM = 4
    U_M  = 5
    U_KM = 6
    U_L  = 7
    U_UG = 8
    U_MG = 9
    U_G  = 10
    U_KG = 11
    U_T  = 12
    U_S  = 13
    U_MIN= 14
    U_H  = 15
    U_A  = 16
    U_MA = 17
    U_KA = 18
    U_MGA= 19
    U_K  = 20
    U_MK = 21
    U_UK = 22
    U_MOL= 23
    U_CD = 24
    U_DEG= 25
    U_RAD= 26
    U_GON= 27
    U_IN = 28
    U_IN2= 29
    U_FO = 30
    U_FO2= 31
    U_TH = 32
    U_YD = 33
    U_LB = 34
    U_OZ = 35
    U_ST = 36
    U_CWT= 37

UnitToken={
    'nm' : UnitType.U_NM,
    'µm' : UnitType.U_UM, 
    'mm' : UnitType.U_MM, 
    'cm' : UnitType.U_CM, 
    'dm' : UnitType.U_DM, 
    'm'  : UnitType.U_M,  
    'km' : UnitType.U_KM, 
    'l'  : UnitType.U_L,  
    'µg' : UnitType.U_UG, 
    'mg' : UnitType.U_MG, 
    'g'  : UnitType.U_G,  
    'kg' : UnitType.U_KG, 
    't'  : UnitType.U_T,  
    's'  : UnitType.U_S,  
    'min': UnitType.U_MIN,
    'h'  : UnitType.U_H,  
    'A'  : UnitType.U_A,  
    'mA' : UnitType.U_MA, 
    'kA' : UnitType.U_KA, 
    'MA' : UnitType.U_MGA, 
    'K'  : UnitType.U_K,  
    'mK' : UnitType.U_MK, 
    'µK' : UnitType.U_UK, 
    'mol': UnitType.U_MOL,
    'cd' : UnitType.U_CD, 
    'deg': UnitType.U_DEG,
    'rad': UnitType.U_RAD,
    'gon': UnitType.U_GON,
    'in' : UnitType.U_IN, 
    '"'  : UnitType.U_IN2,
    'ft' : UnitType.U_FO,
    '\'' : UnitType.U_FO2,
    'th' : UnitType.U_TH, 
    'yd' : UnitType.U_YD, 
    'lb' : UnitType.U_LB, 
    'oz' : UnitType.U_OZ, 
    'st' : UnitType.U_ST, 
    'cwt': UnitType.U_CWT,
}

QtyValue={
    UnitType.U_NM : 1.0e-6,
    UnitType.U_UM : 1.0e-3,
    UnitType.U_MM : 1.0,
    UnitType.U_CM : 10,
    UnitType.U_DM : 100,
    UnitType.U_M  : 1.0e3,
    UnitType.U_KM : 1.0e6,
    UnitType.U_L  : 1.0e6,
    UnitType.U_UG : 1.0e-9,
    UnitType.U_MG : 1.0e-6,
    UnitType.U_G  : 1.0e-3,
    UnitType.U_KG : 1.0,
    UnitType.U_T  : 1.0e3,
    UnitType.U_S  : 1.0,
    UnitType.U_MIN: 60.0,
    UnitType.U_H  : 3600.0,
    UnitType.U_A  : 1.0,
    UnitType.U_MA : 1.0e-3,
    UnitType.U_KA : 1.0e-6,
    UnitType.U_MGA: 1.0,
    UnitType.U_K  : 1.0,
    UnitType.U_MK : 1.0e-3,
    UnitType.U_UK : 1.0e-6,
    UnitType.U_MOL: 1.0,
    UnitType.U_CD : 1.0,
    UnitType.U_DEG: 1.0,
    UnitType.U_RAD: 180/M_PI,
    UnitType.U_GON: 360.0/400.0,
    UnitType.U_IN : 25.4,
    UnitType.U_IN2: 25.4,
    UnitType.U_FO : 304.8,
    UnitType.U_FO2: 304.8,
    UnitType.U_TH : 0.0254,
    UnitType.U_YD : 914.4,
    UnitType.U_LB : 0.45359237,
    UnitType.U_OZ : 0.0283495231,
    UnitType.U_ST : 6.35029318,
    UnitType.U_CWT: 50.80234544
}

class FCUnit:
    def __init__(self, unit_token):
        if unit_token in UnitToken.keys():
            self.token = unit_token
            self.token_type = UnitToken[unit_token]
            self.value = QtyValue[self.token_type]
        else:
            raise Exception(f'unknown unit: {unit_token}')



def isUnit(string):
    return string in UnitToken.keys()
        
        
        
