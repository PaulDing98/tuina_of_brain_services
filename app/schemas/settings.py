'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-03 11:30:13
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-04-18 19:35:02
FilePath: /services/app/schemas/settings.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from pydantic import BaseModel


class ColorOption(BaseModel):
    value: int
    label: str    
    
class SchulteSettings(BaseModel):
    highlightOnCorrect: bool = True
    borderColor: ColorOption
    fontColor: ColorOption
    penaltyTime: int = 2500    
    
    
class SequenceSettings(BaseModel):
    sequenceLength: int = 5
    displayTime: int = 800
    intervalTime: int = 400
    
    
class SettingsResponseData(BaseModel):
    schulte: SchulteSettings
    sequence: SequenceSettings
    
class UpdateSettingsRequest(BaseModel):
    schulte: SchulteSettings
    sequence: SequenceSettings
        