#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jeolpaul

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 9844066))
    API_HASH = os.environ.get("API_HASH", "0d3f74056f1e60388d3317548799ee17")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5358931750:AAG7tgS-t5t22_pWPwSqb8gDRoAIJyZ0Rhc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1770455672")
    SESSION = os.environ.get("SESSION", "BQCWNWIAKrD5-x1C5_Aa3tlG_gkiFbXiXN22VP6Hi5rm8NZMkoSQtP1H-Q4OOZW98b1niJ4LnDgJy_z5K85kjgcrnYrZX5JGNTAGyVcLQUEPirCIuQjIdgbdWOxVzthfjAab9NN3hHdD3v6480iwvhbeXDWwPidoD36R3lEgmRXxBJp2gTyy4Yx0TaFYW7CSHamvQIhGJTrMiwsYu1YwBdgsNk5aiO8cCgJOUgsuLuBVg8i2l6qXGeLEIpRH23FoKIPJCX_CRX3dmTimbOLg9LAtyemU8cCstpOQvwlyJtm5kZLb3cJEk_WNiVVuxItHmI3WYrLDNsvD1kDrbWyiSlYIGvbxOwAAAABphwJ4AA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
