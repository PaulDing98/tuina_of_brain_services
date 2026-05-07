'''
Author: PaulDing 1031071856@qq.com
Date: 2026-04-19 01:58:20
LastEditors: PaulDing 1031071856@qq.com
LastEditTime: 2026-05-04 12:02:33
FilePath: /services/app/services/settings.py
Description: 

Copyright (c) 2026 by ${git_name_email}, All Rights Reserved. 
'''
from app.models import Settings
from sqlalchemy.orm import Session
from app.schemas.settings import SettingsResponseData, SchulteSettings, SequenceSettings, ColorOption, UpdateSettingsRequest
from app.db.crud import get_one_by, save

def get_color_label(value: int) -> str:
    color_map = {
        0: "默认",
        3: "三色",
        5: "五色",
        7: "七色",
    }
    return color_map.get(value, "默认")

#  
def build_settings_response(db_settings: Settings) -> SettingsResponseData:
    return SettingsResponseData(
        schulte = SchulteSettings(
            highlightOnCorrect= db_settings.schulte_highlight_on_correct,
            borderColor=ColorOption(
                value=db_settings.schulte_border_color_value,
                label=get_color_label(db_settings.schulte_border_color_value),
            ),
            fontColor=ColorOption(
                value=db_settings.schulte_font_color_value,
                label=get_color_label(db_settings.schulte_font_color_value),
            ),
            penaltyTime=db_settings.schulte_penalty_time,
        ),
        sequence=SequenceSettings(
            sequenceLength=db_settings.sequence_sequence_length,
            displayTime=db_settings.sequence_display_time,
            intervalTime=db_settings.sequence_interval_time,
        ),
    )
    
def json_to_models(data: UpdateSettingsRequest)  -> dict[str, int | bool]:
    return dict(
        schulte_highlight_on_correct=data.schulte.highlightOnCorrect,
        schulte_border_color_value=data.schulte.borderColor.value,
        schulte_font_color_value=data.schulte.fontColor.value,
        schulte_penalty_time=data.schulte.penaltyTime,
        sequence_sequence_length=data.sequence.sequenceLength,
        sequence_display_time=data.sequence.displayTime,
        sequence_interval_time=data.sequence.intervalTime,
    )
    # return settings

def get_settings(current_user, db: Session ) -> SettingsResponseData:
    user_settings = get_one_by(db, Settings, user_id=current_user.id)
    if not user_settings:
        user_settings = Settings(user_id=current_user.id)
        save(db, user_settings)
    return build_settings_response(user_settings)

def edit_settings(data: UpdateSettingsRequest, current_user, db: Session ) -> SettingsResponseData:
    settings = get_one_by(db, Settings, user_id=current_user.id) or Settings(user_id=current_user.id)
    formed_data = json_to_models(data)
    for key, value in formed_data.items():
        setattr(settings, key, value)
    save(db, settings)
    return build_settings_response(settings)