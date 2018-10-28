# -*- coding: utf-8 -*-
from Class.NiftyPython import NiftyCloudRequest


class NCMBManager:
    NCR_PATH = './nifty_cloud.yml'
    try:
        ncr = NiftyCloudRequest(NCR_PATH)
    except:
        print("NiftyCloudRequest NCR Exception")
    
    def __init__(self):
        if not(self.ncr is NiftyCloudRequest()):
            print("Didnt define ncr")

