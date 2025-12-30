# -*- coding: utf-8-sig -*-
#-------------------------------------------------------------------------------
# Name:        PSS_E
# Purpose:
# Author:      TuanTNA
# Created:     20-02-2020
# Copyright:   (c) TuanTNA 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
__version__ = '2.0.0'


import sys  


#---------------------------------------------------     API PSSE      -----------------------------------------------------
class pss_api:
    def show_pg(self):
        psspy.progress_output(islct=1)
        return
    def hide_pg(self):
        psspy.progress_output(islct=6)
        return
    def clear_pg(self):
        psspy.clearprogressoutput()
        return
    def show_alert(self):
        psspy.alert_output(islct=1)
        return
    def hide_alert(self):
        psspy.alert_output(islct=6)
        return
    def clear_alert(self):
        psspy.clearalertoutput()
        return
    def show_rp(self):
        psspy.report_output(1)
        return
    def hide_rp(self):
        psspy.report_output(6)
        return
    def area(self,bus):  #--------------   BUS   ----------------
        bus=int(bus)
        return str(psspy.busint(bus,string = 'AREA')[1])
    def owner(self,bus):
        bus=int(bus)
        return str(psspy.busint(bus,string = 'OWNER')[1])
    def zone(self,bus):
        bus=int(bus)
        return str(psspy.busint(bus,string = 'ZONE')[1])
    def zone_name(self,bus):
        bus=int(bus)
        return str(psspy.zonnam(int(psspy.busint(bus,string = 'ZONE')[1]))[1])
    def vol(self,bus):
        bus=int(bus)
        return int(psspy.busdat(int(bus),'BASE')[1])
    def vol_pu(self,bus):
        bus=int(bus)
        return round(float(psspy.busdat(bus ,string='PU')[1]),3)
    def vol_kv(self,bus):
        bus=int(bus)
        return round(float(psspy.busdat(bus ,string='KV')[1]),1)
    def namebus(self,bus):
        bus=int(bus)
        name = psspy.notona(bus)[1]
        if name == None:
            return 'None'
        else:
            return psspy.notona(bus)[1][:12].replace(" ","")
    def sta_bus(self,bus):
        bus=int(bus)
        return int(psspy.busint(bus,string='TYPE')[1])
    #--------------   BRANCH   ----------------
    def r_branch(self,ibus,jbus,ickt): 
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndt2(ibus,jbus,ickt,string='RX')[1].real,7)
    def r0_branch(self,ibus,jbus,ickt): 
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndt2(ibus,jbus,ickt,string='RXZ')[1].real,7)
    def x_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndt2(ibus,jbus,ickt,string='RX')[1].imag,7)
    def x0_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndt2(ibus,jbus,ickt,string='RXZ')[1].imag,7)
    def b_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndat(ibus,jbus,ickt,string='CHARG')[1],7)
    def b0_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(psspy.brndat(ibus,jbus,ickt,string='CHARGZ')[1],7)
    def pcta_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(float(psspy.brnmsc(ibus,jbus,ickt,string='PCTRTA')[1]),1)
    def sta_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return int(psspy.brnint(ibus,jbus,ickt,string='STATUS')[1])
    def p_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(float(psspy.brnflo(ibus,jbus,ickt)[1].real),1)
    def q_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(float(psspy.brnflo(ibus,jbus,ickt)[1].imag),1)
    def length_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return round(float(psspy.brndat(ibus,jbus,ickt,string='LENGTH')[1]),2)
    def sbase_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        return int(psspy.brndat(ibus,jbus,ickt,string='RATE')[1])
    def amps_branch(self,ibus,jbus,ickt):
        ibus=int(ibus);jbus=int(jbus);ickt=str(ickt)
        mva = psspy.brndat(ibus,jbus,ickt,string='RATE')[1]
        kv = int(psspy.busdat(int(ibus),'BASE')[1])
        return int(mva*1000/((3**(0.5))*kv))
     #--------------   Tranformer 3 Windding   -------------
    def sta_trf3(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        return int(psspy.wndint(ibus, jbus, kbus,str(ickt), string='STATUS')[1])
    def pctmva_trf3(self,ibus,jbus,kbus,ickt): 
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        return round(float(psspy.wnddat(ibus, jbus, kbus, str(ickt), string='PCTMVA')[1]),1)
    def p_trf3(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        return round(float(psspy.wnddt2(ibus, jbus, kbus,str(ickt), string='FLOW')[1].real),1)
    def q_trf3(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        return round(float(psspy.wnddt2(ibus, jbus, kbus,ickt, string='FLOW')[1].imag),1)
    def tap_trf3_pu(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        return round(float(psspy.wnddat(ibus, jbus, kbus,ickt, string='RATIO')[1]),5)
    def tap_trf3_num(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        tap_pu = float(psspy.wnddat(ibus, jbus, kbus,ickt, string='RATIO')[1])
        pos = int(psspy.wndint(ibus, jbus, kbus,ickt, string='NTPOSN')[1])
        rmin = float(psspy.wnddat(ibus, jbus, kbus,ickt, string='RMIN')[1])
        vol = float(psspy.wnddat(ibus, jbus, kbus,ickt, string='NOMV')[1])
        k = round(((rmin*(220 if vol>200 else 110)/vol-1)/(((pos+1)/2)-pos)),4)
        return int(round(((1-(tap_pu*(220 if vol>200 else 110)/vol))/k) + ((pos+1)/2),0))

    def sbase(self,ibus,jbus,kbus,ickt):
        ibus=int(ibus);jbus=int(jbus);kbus=int(kbus);ickt=str(ickt)
        s1_base = int(psspy.wnddat(ibus, jbus, kbus ,ickt, string='SBASE')[1])
        s2_base = int(psspy.wnddat(jbus, ibus, kbus ,ickt, string='SBASE')[1])
        if s1_base < s2_base:
            return s2_base
        else:
            return s1_base
        #--------------   Machine   -------------
    def p_machine(self,bus,id):  
        bus=int(bus);id=str(id)
        return float(psspy.macdat(bus,id,string='P')[1])
    def pmax_machine(self,bus,id):
        bus=int(bus);id=str(id)
        return float(psspy.macdat(bus,id,string='PMAX')[1])
    def sta_machine(self,bus,id):
        bus=int(bus);id=str(id)
        return int(psspy.macint(bus, id, string='STATUS')[1])
    #--------------   Load   ----------------
    def area_load(self,bus,id):
        bus=int(bus);id=str(id)
        return str(psspy.lodint(bus,id,string = 'AREA')[1])
    def owner_load(self,bus,id):
        bus=int(bus);id=str(id)
        return str(psspy.lodint(bus,id,string = 'OWNER')[1])
    def zone_load(self,bus,id):
        bus=int(bus);id=str(id)
        return str(psspy.lodint(bus,id,string = 'ZONE')[1])
    def p_load(self,bus,id):
        bus=int(bus);id=str(id)
        try:
            return round(float(psspy.loddt2(bus,id,'MVA','ACT')[1].real),2)
        except:
            print (bus)
    
    def q_load(self,bus,id):
        bus=int(bus);id=str(id)
        return round(float(psspy.loddt2(bus,id,'MVA','ACT')[1].imag),2)
    def sta_load(self,bus,id):
        bus=int(bus);id=str(id)
        return psspy.lodint(bus, id, string='STATUS')[1]
    def nxtbrn(self,bus):
        ibus = int(bus)
        vol = self.vol(ibus)
        nxtbrn =[]
        ierr = psspy.inibrn(ibus,2)
        while ierr==0:
            ierr,jbus,kbus,ickt = psspy.nxtbrn3(ibus)
            if ierr==0:
                vol2 = self.vol(jbus)
                if vol2 >= vol:
                    vol = vol2
                else:
                    vol = self.vol(ibus)           
                dev_type = "UNKNOWN"
                
                if kbus != 0:
                    # Nếu kbus khác 0 -> Chắc chắn là Máy biến áp 3 cuộn dây (hoặc node sao)
                    dev_type = "TRF3"
                else:
                    # Nếu kbus == 0 -> Có thể là Line hoặc Transformer 2 cuộn dây
                    # Cách kiểm tra: Thử đọc dữ liệu RATIO của Transformer
                    ierr_xfr, _ = psspy.xfrdat(bus, jbus, ickt, 'RATIO')
                    
                    if ierr_xfr == 0:
                        dev_type = "TRF2"
                    else:
                        dev_type = "LINE"
                nxtbrn.append([ibus,jbus,kbus,ickt,vol,dev_type])
        return nxtbrn        
    def nxtmac(self,bus):
        ibus = int(bus)
        nxtmac =[]
        ierr = psspy.inimac(ibus)
        while ierr==0:
            ierr,id = psspy.nxtmac(ibus)
            if ierr==0:
                nxtmac.append([ibus,id])
        return nxtmac
    def mba_load(self,bus):
        bus=int(bus)
        brn = self.nxtbrn(bus)
        if len(brn) == 1:
            id = brn [0]
            ibus = id[0]
            jbus = id[1]
            kbus = id[2]
            ickt  = id[3]
            if kbus != 0:
                return float(self.sbase(ibus,jbus,kbus,ickt))
            else:
                return float(self.sbase_branch(ibus,jbus,ickt))
        elif len(brn) > 1:
            mva = 0
            for ids in brn:
                ibus = ids[0]
                jbus = ids[1]
                kbus = ids[2]
                ickt  = ids[3]
                if kbus != 0:
                    return float(self.sbase(ibus,jbus,kbus,ickt))
                else:
                    if mva > 0:
                        mva = float(self.sbase_branch(ibus,jbus,ickt))
            return mva
        else:
            return None
        
    def check_type(self,bus):
        bus=int(bus)
        nxtbrn =[]
        ierr = psspy.inibrn(bus,2)
        while ierr==0:
            ierr,jbus,kbus,ickt = psspy.nxtbrn3(bus)
            if ierr==0:
                nxtbrn.append([bus,jbus,kbus,ickt])
        if len(nxtbrn) == 0:
            if psspy.inilod(bus) == 0:
                return 'lod'   # Load Bus
            elif psspy.inimac(bus) == 0 :
                return 'mac'   # Machine Bus
            elif psspy.inibrn(bus) == 0 :
                return 'brn'   # Branch Bus
            elif psspy.inifxs(bus) == 0:
                return 'fxs'    # FixShunt Bus
            else:
                return 'iso'    # Isolated Bus
        else:
            if psspy.inilod(bus) == 0:
                return 'brn_lod'   # Load Bus
            elif psspy.inimac(bus) == 0:
                return 'brn_mac'   # Machine Bus
            elif psspy.inibrn(bus) == 0:
                return 'brn_brn'   # Branch Bus
            elif psspy.inifxs(bus) == 0:
                return 'brn_fxs'    # FixShunt Bus
            else:
                return 'iso_brn'    # Isolated Bus

##########-------------------------------------Bus----------------------------------###########
class bus:
    def __init__(self):
        # Bus Data - Integer
        inum = psspy.abusint(0, 2, string='number')[1]
        izones = psspy.abusint(0, 2, string='zone')[1]
        iarea = psspy.abusint(0, 2, string='area')[1]
        iowner = psspy.abusint(0, 2, string='owner')[1]
        # Name Bus Data - Character
        cname = psspy.abuschar(0, 2, string= 'name')[1]
        #Name Bus Data - Real
        rvol = psspy.abusreal(0, 2, string = 'base')[1]
        #Name Bus Data - Real
        code = psspy.abusint(0, 2, string='TYPE')[1]

        data = []
        for i in range(0,len(inum[0])):
            data.append([i,inum[0][i],cname[0][i],int(rvol[0][i]),iarea[0][i],izones[0][i],iowner[0][i],code[0][i]])
        self.title = ['Stt','Bus_number','Bus_name','Voltage','Area','Zone','Owner', 'Type']

        self.bus_220 = [i[1] for i in data if i[3] == 220]
        self.data = data

##########-------------------------------------Machine----------------------------------###########
class machine:
    def __init__(self):
        # Machine Data - Integer
        inum = psspy.amachint(0, 4, string='number')[1]
        istatus = psspy.amachint(0, 4, string='status')[1]

        # Name Machine Data - Character
        cname = psspy.amachchar(0, 4, string= 'name')[1]
        cid = psspy.amachchar(0, 4, string= 'ID')[1]

        #Name Machine Data - Real
        rpgen = psspy.amachreal(0, 4, string = 'PGEN')[1]
        rpmax = psspy.amachreal(0, 4, string = 'PMAX')[1]
        rpmin = psspy.amachreal(0, 4, string = 'PMIN')[1]

        self.title = ['Stt','Bus_number','Bus_name','ID','Status','PGEN','PMax','PMin','NumOwner','Owner','NumZone','Zone']
        data = []
        for i in range(0,len(inum[0])):
            ibus = int(inum[0][i])
            obusint = psspy.busint(ibus,string = 'OWNER')[1]
            cownnam = psspy.ownnam(obusint)[1]
            zbusint = psspy.busint(ibus,string = 'ZONE')[1]
            czonnam = psspy.zonnam(zbusint)[1]
            data.append([i,inum[0][i],cname[0][i],cid[0][i],istatus[0][i],rpgen[0][i],rpmax[0][i],rpmin[0][i],obusint,cownnam,zbusint,czonnam])
        self.data = data

##########-------------------------------------Shunt----------------------------------###########
class shunt:
    def __init__(self):
        # Shunt Data - Integer
        inum = psspy.aswshint(0, 4, string='number')[1]
        istatus = psspy.aswshint(0, 4, string='status')[1]
        izones = psspy.aswshint(0, 4, string='zone')[1]
        iowner = psspy.aswshint(0, 4, string='owner')[1]

        # Name Shunt Data - Character
        cname = psspy.aswshchar(0, 4, string= 'name')[1]

        #Name Shunt Data - Real
        rvol = psspy.aswshreal(0, 4, string = 'BASE')[1]
        rmvar = psspy.aswshreal(0, 4, string = 'BSWNOM')[1]
        rstep1 = psspy.aswshreal(0, 4, string = 'BSTPBLOCK1')[1]

        self.title = ['Stt','Bus_number','Bus_name','Status','Zone','Owner','Voltage','MVAR', 'Step1' ]
        data = []
        for i in range(0,len(inum[0])):
            data.append([i,inum[0][i],cname[0][i],istatus[0][i],izones[0][i],iowner[0][i],rvol[0][i],rmvar[0][i],rstep1[0][i]])
            self.data = data

##########-------------------------------------Branch----------------------------------###########
class branch:
    def __init__(self):
        self.pss_api = pss_api()
        sid = 0
        owner = 1
        ties = 3
        flag = 2
        entry = 1
        # Branch Data - Integer
        ifromnum = psspy.abrnint(sid,owner,ties,flag,entry, string='FROMNUMBER')[1]
        itonum = psspy.abrnint(sid,owner,ties,flag,entry, string='TONUMBER')[1]
        istatus = psspy.abrnint(sid,owner,ties,flag,entry, string='STATUS')[1]
        imeternumber = psspy.abrnint(sid,owner,ties,flag,entry, string='METERNUMBER')[1]

        # Name Branch Data - Character
        icid = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'ID')[1]
        cfromname = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'FROMNAME')[1]
        ctoname = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'TONAME')[1]

        # Name Branch Data - Real
        rmw = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'P')[1]
        rmvar = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'Q')[1]
        rlength = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'LENGTH')[1]
        rrate= psspy.abrnreal(sid,owner,ties,flag,entry, string = 'RATE')[1]
        ramps = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'AMPS')[1]
        rpctamp = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'PCTRATE')[1]
        rpctmva = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'PCTMVARATE')[1]
 
        
        self.title = ['Vol','From_bus_number','To_bus_number','From_bus_name','To_bus_name','ID','Status','Length',  \
                        'Amps','Rate','PctA','PctMVA','MW','MVAr', 'METERNUMBER','Name','Từ Tỉnh', 'Đến Tỉnh'  ]
        data= []
        for i in range(0,len(ifromnum[0])):
            ibus = int(ifromnum[0][i])
            jbus = int(itonum[0][i])
            ivol = int(psspy.busdat(ibus,'BASE')[1])       
        
            inums = str(ifromnum[0][i]) + "_" + str(itonum[0][i]) + "_" + str(int(icid[0][i]))
            
            name = self.pss_api.namebus(ibus)
            
            data.append([ivol,ifromnum[0][i],itonum[0][i],cfromname[0][i],ctoname[0][i],icid[0][i],istatus[0][i], \
                        rlength[0][i],ramps[0][i],rrate[0][i],rpctamp[0][i],rpctmva[0][i],rmw[0][i],rmvar[0][i],imeternumber[0][i],inums, name])

        self.data = data
##########-------------------------------------Tranformer Two Winding----------------------------------###########
class two_winding:
    def __init__(self):
        sid = 0
        owner = 1
        ties = 3
        flag = 6
        entry = 1
        # Tranformer Two Winding Data - Integer
        ifromnum = psspy.abrnint(sid,owner,ties,flag,entry, string='FROMNUMBER')[1]
        itonum = psspy.abrnint(sid,owner,ties,flag,entry, string='TONUMBER')[1]
        istatus = psspy.abrnint(sid,owner,ties,flag,entry, string='STATUS')[1]
        imeternumber = psspy.abrnint(sid,owner,ties,flag,entry, string='METERNUMBER')[1]

        # Name Tranformer Two Winding Data - Character
        cid = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'ID')[1]
        cfromname = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'FROMNAME')[1]
        ctoname = psspy.abrnchar(sid,owner,ties,flag,entry, string= 'TONAME')[1]

        # Name Tranformer Two Winding Data - Real
        rmw = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'P')[1]
        rmvar = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'Q')[1]
        rrate= psspy.abrnreal(sid,owner,ties,flag,entry, string = 'RATE')[1]
        ramps = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'AMPS')[1]
        rpctamp = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'PCTRATE')[1]
        rpctmva = psspy.abrnreal(sid,owner,ties,flag,entry, string = 'PCTMVARATE')[1]

        self.title = ['Vol','From_bus_number','To_bus_number','From_bus_name','To_bus_name','ID','Status',\
                        'Amps','Rate','PctA','PctMVA','MW','MVAr','METERNUMBER','NUMBER'  ]
        data = []
        data_load =[]
        for i in range(0,len(ifromnum[0])):
            ibus = int(ifromnum[0][i])
            jbus = int(itonum[0][i])
            inums = str(ifromnum[0][i]) + "_" + str(itonum[0][i]) + "_" + str(cid[0][i])
            ivol_w1 = int(psspy.busdat(ibus,'BASE')[1])
            ivol_w2 = int(psspy.busdat(jbus,'BASE')[1])
            if ivol_w1 > ivol_w2:
                ivol = ivol_w1
            else:
                ivol = ivol_w2
            data.append([ivol,ifromnum[0][i],itonum[0][i],cfromname[0][i],ctoname[0][i],cid[0][i],istatus[0][i], \
                        ramps[0][i],rrate[0][i],rpctamp[0][i],rpctmva[0][i],rmw[0][i],rmvar[0][i],imeternumber[0][i],inums])
            data_load.append([ifromnum[0][i],itonum[0][i],rrate[0][i]])

        self.data = data
        self.data_load = data_load
##########-------------------------------------Tranformer Three Winding----------------------------------###########
class three_winding:
    def __init__(self):
        # Tranformer Three Winding- Data - Integer
        sid = 0;owner = 2;ties = 1;flag = 3;entry = 2
        iwind1num = psspy.awndint(sid,owner,ties,flag,entry, string='WIND1NUMBER')[1]
        iwind2num = psspy.awndint(sid,owner,ties,flag,entry, string='WIND2NUMBER')[1]
        iwind3num = psspy.awndint(sid,owner,ties,flag,entry, string='WIND3NUMBER')[1]
        ictrbus = psspy.awndint(sid,owner,ties,flag,entry, string='ICONTNUMBER')[1]
        itap = psspy.awndint(sid,owner,ties,flag,entry, string='NTPOSN')[1]
        istatus = psspy.awndint(sid,owner,ties,flag,entry, string='STATUS')[1]
        inonmeternumber = psspy.awndint(sid,owner,ties,flag,entry, string='NMETERNUMBER') [1]
        iwind = psspy.awndint(sid,owner,ties,flag,entry, string = 'WNDNUM')[1]
        # Name Tranformer Three Winding- Data - Character
        ccid = psspy.awndchar(sid,owner,ties,flag,entry, string= 'ID')[1]
        cname = psspy.awndchar(sid,owner,ties,flag,entry, string= 'WNDBUSNAME')[1]
        cwind1name = psspy.awndchar(sid,owner,ties,flag,entry, string= 'WIND1NAME')[1]
        cwind2name = psspy.awndchar(sid,owner,ties,flag,entry, string= 'WIND2NAME')[1]
        cwind3name = psspy.awndchar(sid,owner,ties,flag,entry, string= 'WIND3NAME')[1]

        # Name Tranformer Three Winding- Data - Real
        rmw = psspy.awndreal(sid,owner,ties,flag,entry, string = 'P')[1]
        rmvar = psspy.awndreal(sid,owner,ties,flag,entry, string = 'Q')[1]
        rmva = psspy.awndreal(sid,owner,ties,flag,entry, string = 'MVA')[1]
        rrate= psspy.awndreal(sid,owner,ties,flag,entry, string = 'RATE')[1]
        ramps = psspy.awndreal(sid,owner,ties,flag,entry, string = 'AMPS')[1]
        rpctamp = psspy.awndreal(sid,owner,ties,flag,entry, string = 'PCTRATE')[1]
        rpctmva = psspy.awndreal(sid,owner,ties,flag,entry, string = 'PCTMVARATE')[1]
        rrmax = psspy.awndreal(sid,owner,ties,flag,entry, string = 'RMAX')[1]
        rrmin = psspy.awndreal(sid,owner,ties,flag,entry, string = 'RMIN')[1]
        rnvol = psspy.awndreal(sid,owner,ties,flag,entry, string = 'NOMV')[1]
        rstep = psspy.awndreal(sid,owner,ties,flag,entry, string = 'RATIO')[1]
        rploss = psspy.awndreal(sid,owner,ties,flag,entry, string = 'PLOSS')[1]
        rqloss = psspy.awndreal(sid,owner,ties,flag,entry, string = 'QLOSS')[1]
    #            inor_vol_w2 = psspy.awndreal(sid,owner,ties,flag,entry, string = 'STEP')[1]

        self.title = ['Stt','Name_MBA','W1_number','W2_number','W3_number','ID','Sta','Ctr Bus','Rate','Vol', \
                    'Vol2','Rmax','Rmin','TAP','Step','Amps','MVA','PctA','PctMVA','MW','MVAr', 'NMETER', 'NUMBER' ]
        data = []
        data_load=[]
        for i in  range(0, len(iwind1num[0])):
            ibus = int(iwind1num[0][i])
            jbus = int(iwind2num[0][i])
            kbus = int(iwind3num[0][i])
            wind_trf3num = int(iwind[0][i])
            if wind_trf3num == 1:
                inor_vol_w2 = int(rnvol[0][i+1])
                inums = str(ibus) + "_" + str(jbus) + "_" + str(kbus) + "_" + str(int(ccid[0][i]))
                basevol_w1 = int(psspy.busdat(ibus,'BASE')[1])
                basevol_w2 = int(psspy.busdat(jbus,'BASE')[1])
                if basevol_w1 > basevol_w2:
                    basevol = basevol_w1
                else:
                    basevol = basevol_w2
                data.append([i,cname[0][i],iwind1num[0][i],iwind2num[0][i],iwind3num[0][i],ccid[0][i],istatus[0][i], \
                            basevol,rrate[0][i],rnvol[0][i],inor_vol_w2,rrmax[0][i],rrmin[0][i],itap[0][i],rstep[0][i],ramps[0][i], \
                            rmva[0][i],rpctamp[0][i],rpctmva[0][i],rmw[0][i],rmvar[0][i],inonmeternumber[0][i],inums,wind_trf3num])
                data_load.append([iwind2num[0][i],iwind3num[0][i],rrate[0][i]])

        self.data = data

        self.trf_220 = [i for i in data if i[7]== 220]
        self.data_load = data_load
##########-------------------------------------Load----------------------------------###########
class load:
    def __init__(self):
        load_trf_trf3 = three_winding().data_load
        load_trf_trf2 = two_winding().data_load
        # Load Data - Integer
        inum = psspy.aloadint(0, 4, string='number')[1]
        istatus = psspy.aloadint(0, 4, string='status')[1]
        izones = psspy.aloadint(0, 4, string='zone')[1]
        iowner = psspy.aloadint(0, 4, string='owner')[1]
        # Name Load Data - Character
        cname = psspy.aloadchar(0, 4, string= 'name')[1]
        ccid = psspy.aloadchar(0, 4, string= 'ID')[1]
        #Name Load Data - Complex
        xload = psspy.aloadcplx(0, 4, string = 'mvaact')[1]

        self.title = ['Stt','Bus_number','Bus_name','ID','Status','Zone','Rate','PLoad','QLoad']
        data = []
        for i in range(0,len(inum[0])):
            ibus = int(inum[0][i])
            if str(ibus)[-1:] != '0':
                xloadp = float(xload[0][i].real)
                xloadq = float(xload[0][i].imag)
                load_rate = ''
                try:
                    load_rate = int(load_trf_trf2[list([j[1] for j in load_trf_trf2]).index(ibus)][2])
                except ValueError:
                    try:
                        load_rate = int(load_trf_trf3[list([j[0] for j in load_trf_trf3]).index(ibus)][2])
                    except ValueError:
                        try:
                            load_rate = int(load_trf_trf3[list([j[1] for j in load_trf_trf3]).index(ibus)][2])
                        except ValueError:
                            load_rate = ''
                data.append([i+1,ibus,cname[0][i],istatus[0][i],ccid[0][i],izones[0][i],load_rate,xloadp,xloadq])
        self.data = data

def run_psse():
    global psspy, PSSEVERSION,_i,_f,_s
    try:
        import psspy
        PSSEVERSION = psspy.psseversion()[1]
    except:
        try:
            import psse3506
        except:
            try:
                import psse34
            except:
                pass

        import psspy
        PSSEVERSION = psspy.psseversion()[1]
        psspy.psseinit(50000)
        _i=psspy.getdefaultint()
        _f=psspy.getdefaultreal()
        _s=psspy.getdefaultchar()

#---------------------------------------------------     Export TXT file      -----------------------------------------------------
def export_txt(link,text):
    file = open(link, "w")
    #text = str(text.encode('utf-8'))
    #print (text)
    file.write(text)
    file.close()

import os
import json
#---------------------------------------------------     Select zone      -----------------------------------------------------
class select_zone:
    def all(self,minkv,maxkv):
        psspy.bsys(0,1,[minkv, maxkv],1,[],0,[],0,[],0,[])
    def nam(self,minkv,maxkv):
        psspy.bsys(0,1,[minkv, maxkv],1,[3],0,[],0,[],0,[])
    def bac(self,minkv,maxkv):
        psspy.bsys(0,1,[minkv, maxkv],1,[1],0,[],0,[],0,[])
    def trung(self,minkv,maxkv):
        psspy.bsys(0,1,[minkv, maxkv],1,[2],0,[],0,[],0,[])

class fnsl_solved:
    def __init__(self, solved='fnsl'):
        self.island_busnum = []
        pss_api().hide_pg()
        if solved == 'fnsl':
            ierr_newton = psspy.fnsl([0,0,0,1,1,0,99,0])
        elif solved == 'fdns':
            ierr_newton = psspy.fdns([0,0,0,1,1,0,99,0])
        
        ierr_solved = psspy.solved()
        pss_api().show_pg()
        if ierr_newton== 0 and ierr_solved == 0:
            self.ierr = 0
            self.ntf='Bai toan Hoi tu'
            return
        elif ierr_newton == 4 :
            self.ierr = 4
            self.ntf = '\nBài toán bị tách đảo'
            treeobj = psspy.treedat()
            self.island_busnum = treeobj['island_busnum']
            return
        else:
            self.ierr = 9
            self.ntf = '\nBài toán không hội tụ'
            return

# Hàm hỗ trợ nếu chưa có
def array2dict(keys, values):
    return dict(zip(keys, values))
    
#---------------------------------------------------     Fix Code 4      -----------------------------------------------------
def fix_code_4(source_folder = r'C:\Users\tuantna\Desktop', output_folder = r'D:\PSSE_Fix_Code_4'):
    run_psse()
    ps_api = pss_api()

    # --- PHẦN 1: KHỞI TẠO VÀ LẤY DỮ LIỆU ---
    # 1. Cấu hình đường dẫn

    history_file = output_folder + '/processed_history.txt' # File lưu lịch sử nằm cùng thư mục với file code python
    
    target_suffix = 'output_Hoi Tu Roi.raw'

    # Tạo thư mục đích nếu chưa có
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 2. Load lịch sử đã chạy từ file JSON
    processed_files = []
    if os.path.exists(history_file):
        print (history_file)
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                processed_files = [line.strip().strip('"') for line in f if line.strip()]
        except Exception as e:
            print(f"Lỗi đọc file lịch sử: {e}. Sẽ tạo mới.")
            processed_files = []
    else:
        print("Chưa có file lịch sử. Sẽ tạo mới.")

    # 3. Quét file và xử lý
    files_in_dir = os.listdir(source_folder)
    newly_processed_count = 0

    for file_name in files_in_dir:
        # Kiểm tra đuôi file
        if file_name.endswith(target_suffix):
            
            # Kiểm tra xem đã xử lý chưa
            if file_name in processed_files:
                print(f"Bỏ qua (đã chạy trước đó): {file_name}")
                continue
            
            if hasattr(ps_api, 'hide_pg'):
                ps_api.hide_pg()
                ps_api.hide_rp()
                ps_api.hide_alert()

            # Đường dẫn đầy đủ tới file raw
            file_psse = os.path.join(source_folder, file_name)

            path = os.path.dirname(file_psse)
            pre_base, ext_base = os.path.splitext(file_psse)
            
            if ext_base == '.sav':
                case_base = psspy.case(file_psse)
            elif ext_base == '.raw':
                case_base = psspy.read(0, file_psse)
                print('Load Raw file: OK')

            psspy.bsys(0, 1, [1.0, 500.], 0, [], 0, [], 0, [], 0, [])

            list_bus = bus().data
            
            # Dict tra cứu Type gốc
            bus_code_dict = {ibus[1]: ibus[7] for ibus in list_bus}

            # [MODIFIED] Thêm phần tử thứ 3 là 'area' vào danh sách để phục vụ sắp xếp
            name_vol_1 = [] 
            name_vol_2 = [] 
            name_vol_3 = []
            name_vol_4 = [] 
            name_vol_41 = []
            name_vol_4_psse = []

            for ibus in list_bus:
                bus_number = ibus[1]
                bus_name = ibus[2]
                bus_vol = ibus[3]
                area = ibus[4] # Lấy thông tin Area
                
                # Format tên: Name_Vol_Area (để phân biệt rõ ràng)
                name_vol = bus_name + '_' + str(bus_vol) + '_' + str(area)
                bus_code = ibus[7]
                
                # Cấu trúc lưu trữ: [BUS_ID, NAME_VOL, AREA]
                if bus_code == 4:
                    bus_type_str = ps_api.check_type(bus_number)
                    if bus_type_str in ['mac', 'lod', 'fxs', 'brn_mac', 'brn_lod', 'brn_fxs']:
                        name_vol_4.append([bus_number, name_vol, area])
                    elif bus_type_str in ['iso'] and bus_number >= 10000:
                        name_vol_4_psse.append([bus_number, name_vol, area])
                    elif bus_type_str in ['iso_brn']:
                        name_vol_41.append([bus_number, name_vol, area])
                elif bus_code == 3:
                    name_vol_3.append([bus_number, name_vol, area])
                elif bus_code == 1:
                    name_vol_1.append([bus_number, name_vol, area])
                elif bus_code in [2, -2]:
                    name_vol_2.append([bus_number, name_vol, area])

            # [NEW] Sắp xếp danh sách trước khi xử lý để đảm bảo trình tự thực hiện (Execution Order)
            # Ưu tiên 1: Area (x[2]), Ưu tiên 2: Tên (x[1])
            sort_key = lambda x: (x[2], x[1])
            name_vol_4.sort(key=sort_key)
            name_vol_1.sort(key=sort_key)
            name_vol_2.sort(key=sort_key)
            name_vol_3.sort(key=sort_key)
            name_vol_41.sort(key=sort_key)

            print("-" * 30)
            print("Bắt đầu xử lý (đã sắp xếp theo Area)...")
            
            txt_log_header = ""
            log_buffer = {} # Dictionary chứa nội dung log
            
            # [NEW] Dictionary ánh xạ tên -> Area để phục vụ sắp xếp file log cuối cùng
            name_to_area_map = {}

            deleted_buses = set()

            # -----------------------------------------------------------
            # BƯỚC 1: RECN VÀ GHÉP NỘI BỘ CÁC BUS TRONG NAME_VOL_4
            # -----------------------------------------------------------
            print(">>> BƯỚC 1: RECN và GHÉP NỘI BỘ danh sách Type 4...")
            
            # 1.2 Gom nhóm nội bộ Type 4
            dict_internal_4 = {}
            
            # [MODIFIED] Unpack 3 biến (bao gồm area)
            for b_id, b_name, b_area in name_vol_4:
                # Lưu area vào map để dùng sau này
                name_to_area_map[b_name] = b_area
                
                base_name = b_name.rsplit('_', 2)[0] # Cắt bớt phần _Vol_Area
                if base_name.strip() == '0': continue

                if b_name not in dict_internal_4:
                    dict_internal_4[b_name] = []
                dict_internal_4[b_name].append(b_id)

            # 1.3 Thực hiện ghép nội bộ
            # Do dict_internal_4 được tạo từ name_vol_4 đã sắp xếp, 
            # nên thứ tự duyệt keys ở đây cũng sẽ theo Area -> Name (Python 3.7+)
            count_internal = 0
            for b_name, list_ids in dict_internal_4.items():
                if len(list_ids) < 2: continue

                sorted_ids = sorted(list_ids, reverse=True)
                target = sorted_ids[0]
                sources = sorted_ids[1:]

                for src in sources:
                    block_log = ""
                    block_log += f"# Bus type 4 is {src}\npsspy.recn({src})\n"
                    block_log += f"# Bus type 4 is {target}\npsspy.recn({target})\n"
                    
                    psspy.recn(src)
                    psspy.recn(target)
                    
                    msg = f"# [NOI BO 4] Ghep: {target} <--- {src} (Name: {b_name})\npsspy.join({target}, {src}, 1)\n"
                    block_log += msg

                    ierr_join = psspy.join(target, src, 1)
                    
                    if ierr_join == 0:
                        deleted_buses.add(src)
                        count_internal += 1
                    else:
                        block_log += f"# -> LOI JOIN NOI BO {target}, {src}: {ierr_join}\n"
                    
                    if b_name not in log_buffer: log_buffer[b_name] = []
                    log_buffer[b_name].append(block_log)
            
            # 1.2 Gom nhóm nội bộ Type 1 (Code tương tự Type 4)
            dict_internal_1 = {}
            # Gộp tất cả các list lại để duyệt
            all_vol_lists = name_vol_1 + name_vol_2 + name_vol_3 + name_vol_41 + name_vol_4_psse
            # Sắp xếp lại list tổng hợp này theo Area để đảm bảo thứ tự
            all_vol_lists.sort(key=sort_key)

            for b_id, b_name, b_area in all_vol_lists:
                name_to_area_map[b_name] = b_area
                
                base_name = b_name.rsplit('_', 2)[0]
                if base_name.strip() in ['0', '1']: continue

                if b_name == 'HOA_BINH    _220_26':
                    b_name = 'HOA_BINH    _220_90'

                if b_name not in dict_internal_1:
                    dict_internal_1[b_name] = []
                dict_internal_1[b_name].append(b_id)

            export_txt('D:/debug_internal_1.json', json.dumps(dict_internal_1, indent=4))

            # 1.3 Thực hiện ghép nội bộ Type 1
            for b_name, list_ids in dict_internal_1.items():
                if len(list_ids) < 2: continue

                sorted_ids = sorted(list_ids, reverse=True)
                target = sorted_ids[0]
                sources = sorted_ids[1:]

                for src in sources:
                    block_log = "" 
                    if target >= 10000 and src >= 10000:
                        if target >= 100000 and src >= 100000 and (str(target)[-1:] in ['6','7'] or str(src)[-1:] in ['6','7']):
                            pass
                        else:
                            if psspy.brnint(src,target,'1',string='STATUS')[1] == None:
                                psspy.branch_data(src,target,str(1),[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]) 
                                psspy.branch_chng(src,target,str(1),[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
                                block_log += f"psspy.branch_data({src},{target},'1',[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]\n"
                                block_log += f"psspy.branch_chng({src},{target},'1',[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])\n"
                            elif psspy.brnint(src,target,'2',string='STATUS')[1] == None:
                                psspy.branch_data(src,target,str(2),[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]) 
                                psspy.branch_chng(src,target,str(2),[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
                                block_log += f"psspy.branch_data({src},{target},'2',[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]\n"
                                block_log += f"psspy.branch_chng({src},{target},'2',[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])\n"
                            else:
                                psspy.branch_data(src,target,str(3),[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]) 
                                psspy.branch_chng(src,target,str(3),[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
                                block_log += f"psspy.branch_data({src},{target},'3',[_i,_i,_i,_i,_i,_i],[0.0,0.0001,0.0,0.0,0.0,0.0,_f,_f,_f,_f,0.0,_f,_f,_f,_f]\n"
                                block_log += f"psspy.branch_chng({src},{target},'3',[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])\n"
                            continue
                    # Logic kiểm tra thiết bị nối vào (giữ nguyên logic cũ của bạn)
                    src_list = ps_api.nxtbrn(src)
                    tgt_list = ps_api.nxtbrn(target)
                    src_k0 = ([brn for brn in src_list if brn[5] == 'TRF3'])
                    tgt_k0 = ([brn for brn in tgt_list if brn[5] == 'TRF3'])

                    if  ((ps_api.check_type(src) == 'iso_brn' or ps_api.check_type(target) == 'iso_brn') or \
                        (ps_api.check_type(src) in ['brn_mac', 'brn_lod', 'brn_fxs'] and len(src_list) == 1 and len(tgt_k0) == 0 ) or \
                        (ps_api.check_type(target) in ['brn_mac', 'brn_lod', 'brn_fxs'] and len(tgt_list) == 1 and len(src_k0) == 0)) and \
                        (len(src_k0) == 0 or len(tgt_k0) == 0 or not (len(src_k0) == len(tgt_k0) ==  len(src_list) == len(tgt_list) == 1)):
                    
                
                        
                        block_log += f"# Bus type 1 is {src}\npsspy.recn({src})\n"
                        block_log += f"# Bus type 1 is {target}\npsspy.recn({target})\n"
                        
                        psspy.recn(src)
                        psspy.recn(target)
                        
                        # ... (Phần logic tìm thiết bị txt_log_all giữ nguyên như code cũ) ...
                        txt_log_all = []
                        if len(src_k0) > 0:
                            ibus, jbus, kbus, ckt, dev_type = src_k0[0][0], src_k0[0][1], src_k0[0][2], src_k0[0][3], src_k0[0][5]
                            if ps_api.sta_trf3(ibus, jbus, kbus, ckt) == 0: txt_log_all.append([ibus, jbus, kbus, ckt,dev_type])
                        elif len(tgt_k0) > 0:
                            ibus, jbus, kbus, ckt, dev_type = tgt_k0[0][0], tgt_k0[0][1], tgt_k0[0][2], tgt_k0[0][3], tgt_k0[0][5]
                            if ps_api.sta_trf3(ibus, jbus, kbus, ckt) == 0: txt_log_all.append([ibus, jbus, kbus, ckt,dev_type])
                        else:
                            check_src = ([brn for brn in src_list if brn[2] == 0])
                            check_tgt = ([brn for brn in tgt_list if brn[2] == 0])
                            for i in check_src + check_tgt:
                                ibus, jbus, kbus, ckt, dev_type = i[0], i[1], i[2], i[3], i[5]
                                if ps_api.sta_branch(ibus, jbus, ckt) == 0: txt_log_all.append([ibus, jbus, kbus, ckt,dev_type])

                        msg = f"# [NOI BO 1] Ghep: {target} <--- {src} (Name: {b_name})\npsspy.join({target}, {src}, 1)\n"
                        block_log += msg
                        ierr_join = psspy.join(target, src, 1)

                        if ierr_join == 0:
                            deleted_buses.add(src)
                            count_internal += 1

                        # Logic xử lý thiết bị đi kèm (Move branches/transformers)
                        for item in txt_log_all:
                            ibus = item[0]
                            jbus = item[1]
                            kbus = item[2]
                            ckt = item[3]
                            dev_type = item[4]

                            block_log += f"# Bus {jbus}\npsspy.recn({jbus})\n"
                            psspy.recn(jbus)
                            if dev_type == 'LINE': # Đường dây
                                psspy.branch_chng(target,jbus,ckt,[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])
                                block_log += f"psspy.branch_chng({target},{jbus},'{ckt}',[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f])\n"
                            elif dev_type == 'TRF2': # Biến áp
                                _src_list = ps_api.nxtbrn(jbus)
                                if len(_src_list) < 2:
                                    block_log += f"# Bus {jbus}\npsspy.dscn({jbus})\n"
                                    psspy.dscn(jbus)
                                    psspy.two_winding_chng_6(target,jbus,ckt,[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)
                                    block_log += f"psspy.two_winding_chng_6({target},{jbus},'{ckt}',[0,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)\n"
                                else:
                                    psspy.two_winding_chng_6(target,jbus,ckt,[1,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)
                                    block_log += f"psspy.two_winding_chng_6({target},{jbus},'{ckt}',[1,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)\n"
                            elif dev_type == 'TRF3': # MBA 3 cuộn
                                block_log += f"# Bus {kbus}\npsspy.recn({kbus})\n"
                                psspy.recn(kbus)
                                try:
                                    psspy.three_wnd_imped_chng_4(target,jbus,kbus,ckt,[_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)
                                    block_log += f"psspy.three_wnd_imped_chng_4({target},{jbus},{kbus},'{ckt}',[_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)\n"
                                except:
                                    print (type(target), type(jbus), type(kbus), type(ckt)  )
                                    print(f"Lỗi thay đổi MBA 3 cuộn: {target}, {jbus}, {kbus}, {ckt}")
                                
                        else:
                            if ierr_join != 0:
                                block_log += f"# -> LOI JOIN NOI BO {target}, {src}: {ierr_join}\n"
                        
                        if b_name not in log_buffer: log_buffer[b_name] = []
                        log_buffer[b_name].append(block_log)
                        
            # -----------------------------------------------------------
            # BƯỚC 2: GHÉP TYPE 4 (CÒN SỐNG) VÀO TYPE 1 / TYPE 2
            # -----------------------------------------------------------
            print(">>> BƯỚC 2: Ghép Type 4 vào Type 1/Type 2...")

            # Tạo từ điển Online
            dict_online = {}
            for b_id, b_name, b_area in all_vol_lists: 
                if b_name not in dict_online: dict_online[b_name] = []
                dict_online[b_name].append(b_id)

            count_cross = 0

            # Duyệt name_vol_4 (đã sort theo Area)
            for item_4 in name_vol_4:
                bus_4_id = item_4[0]
                bus_name_key = item_4[1]
                bus_4_area = item_4[2]
                
                # Cập nhật map cho chắc chắn (dù đã có ở trên)
                name_to_area_map[bus_name_key] = bus_4_area

                if bus_4_id in deleted_buses: continue
                
                base_name = bus_name_key.rsplit('_', 2)[0]
                if base_name.strip() == '0': continue

                if bus_name_key in dict_online:
                    list_target_ids = dict_online[bus_name_key]
                    valid_targets = [bid for bid in list_target_ids if bid not in deleted_buses]
                    if not valid_targets: continue

                    bus_online_id = max(valid_targets)
                    
                    # Logic Keep/Move
                    bus_keep, bus_move = None, None
                    if bus_online_id >= 10000 and bus_4_id < 10000:
                        bus_keep, bus_move = bus_online_id, bus_4_id
                    elif bus_4_id >= 10000 and bus_online_id < 10000:
                        bus_keep, bus_move = bus_4_id, bus_online_id
                    else:
                        if bus_online_id > bus_4_id:
                            bus_keep, bus_move = bus_online_id, bus_4_id
                        else:
                            bus_keep, bus_move = bus_4_id, bus_online_id

                    if bus_move in deleted_buses or bus_keep in deleted_buses: continue

                    try:
                        block_log = ""
                        block_log += f"# Bus type 4 is {bus_keep}\npsspy.recn({bus_keep})\n"
                        block_log += f"# Bus type 4 is {bus_move}\npsspy.recn({bus_move})\n"
                        
                        psspy.recn(bus_keep)
                        psspy.recn(bus_move)
                        
                        msg_join = f"# Da Ghep: {bus_keep} <--- {bus_move} (Name: {bus_name_key})\npsspy.join({bus_keep}, {bus_move}, 1)\n"
                        block_log += msg_join + "\n"

                        ierr_join = psspy.join(bus_keep, bus_move, 1)

                        if ierr_join == 0:
                            count_cross += 1
                            deleted_buses.add(bus_move)
                        
                        # Logic dscn nếu cần
                        _src_list = ps_api.nxtbrn(bus_keep)                
                        _src_list_trf = ([brn for brn in _src_list if brn[5] == 'TRF3'])
                        _src_list_line = ([brn for brn in _src_list if brn[5] != 'TRF3'])
                        if len(_src_list_line) == 1 and len(_src_list_trf) == 0:
                            block_log += f"# Bus keep {bus_keep}\npsspy.dscn({bus_keep})\n"
                            psspy.dscn(bus_keep)
                        
                        # if bus_keep in bus_code_dict and bus_code_dict[bus_keep] == 4 and bus_code_dict[bus_move] == 4:
                        #        block_log += f"psspy.dscn({bus_keep})\n"
                        
                        if ierr_join != 0:
                            block_log += f"# -> LOI JOIN {bus_keep}, {bus_move}: {ierr_join}\n"
                        
                        if bus_name_key not in log_buffer: log_buffer[bus_name_key] = []
                        log_buffer[bus_name_key].append(block_log)

                    except Exception as e:
                        print(f"Lỗi ngoại lệ: {e}")
                        if bus_name_key not in log_buffer: log_buffer[bus_name_key] = []
                        log_buffer[bus_name_key].append(f"# Exception: {e}\n")

            print("-" * 30)
            print(f"HOÀN THÀNH TOÀN BỘ.")
            
            # [MODIFIED] TỔNG HỢP VÀ GHI FILE TỪ BUFFER THEO THỨ TỰ AREA -> NAME
            final_log_content = txt_log_header
            
            # Tạo danh sách các Key đã sắp xếp theo tiêu chí: (Area, Name)
            # name_to_area_map.get(name, 9999) phòng trường hợp không tìm thấy area thì đẩy xuống cuối
            sorted_log_keys = sorted(log_buffer.keys(), key=lambda name: (name_to_area_map.get(name, 9999), name))
            
            current_area = -1
            
            for name in sorted_log_keys:
                area = name_to_area_map.get(name, 9999)
                
                # In tiêu đề Area nếu chuyển sang vùng mới
                if area != current_area:
                    final_log_content += "\n" + "#" * 80 + "\n"
                    final_log_content += f"# AREA: {area}\n"
                    final_log_content += "#" * 80 + "\n"
                    current_area = area

                final_log_content += "\n" + "#" * 60 + "\n"
                final_log_content += f"# GROUP NAME: {name}\n"
                final_log_content += "#" * 60 + "\n"
                
                for block in log_buffer[name]:
                    final_log_content += block


            # final_log_content += '\npsspy.fdns([0,0,0,1,1,0,99,0])\npsspy.fdns([0,0,0,1,1,0,99,0])'
            # psspy.fdns([0,0,0,1,1,0,99,0])
            # psspy.fdns([0,0,0,1,1,0,99,0])

            solved = fnsl_solved('fdns')
            if solved.ierr == 0:
                print(f"\n# -> KET QUA FNSL/SOLVED: {solved.ntf}\n")
            elif solved.ierr == 4:
                ps_api.hide_pg()
                for buss in (solved.island_busnum):
                    for bus_id in buss:
                        nxtbrn = ps_api.nxtbrn(bus_id)
                        if len(nxtbrn) == 0:
                            psspy.dscn(bus_id)
                            final_log_content += f"# Bus {bus_id}\npsspy.dscn({bus_id})\n"
                            continue
                        for brn in nxtbrn:
                            ibus = brn[0]
                            jbus = brn[1]
                            kbus = brn[2]
                            ckt = brn[3]
                            dev_type = brn[5]
                            if ps_api.sta_bus(jbus) == 4:
                                psspy.recn(jbus)
                                final_log_content += f"# Bus {jbus}\npsspy.recn({jbus})\n"
                            if dev_type == 'LINE':
                                psspy.branch_chng_3(ibus,jbus,ckt,[1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)                    
                                final_log_content += f"psspy.branch_chng_3({ibus},{jbus},'{ckt}',[1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s)\n"
                            elif dev_type == 'TRF2':
                                psspy.two_winding_chng_6(ibus,jbus,ckt,[1,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)
                                final_log_content += f"psspy.two_winding_chng_6({ibus},{jbus},'{ckt}',[1,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)\n"
                            elif dev_type == 'TRF3':
                                if ps_api.sta_bus(kbus) == 4:
                                    psspy.recn(kbus)
                                    final_log_content += f"# Bus {kbus}\npsspy.recn({kbus})\n"
                                psspy.three_wnd_imped_chng_4(ibus,jbus,kbus,ckt,[_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)
                                
                                final_log_content += f"psspy.three_wnd_imped_chng_4({ibus},{jbus},{kbus},'{ckt}',[_i,_i,_i,_i,_i,_i,_i,1,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f],_s,_s)\n"
                    
                final_log_content += '\npsspy.fdns([0,0,0,1,1,4,-1,0])\npsspy.fdns([0,0,0,1,1,0,99,0])\npsspy.fnsl([0,0,0,1,1,0,99,0])\n'
                
                psspy.fnsl([0,0,0,1,1,4,-1,0])
                psspy.fnsl([0,0,0,1,1,0,99,0])
                ps_api.show_pg()     
                solved = fnsl_solved('fnsl')
                print (f"\n# -> KET QUA FNSL/SOLVED: {solved.ntf}\n")
            else:
                print(f"\n# -> KET QUA FNSL/SOLVED: {solved.ntf}\n")
            

            # fnsl_solved('fnsl')
            with open(r'D:\log_ghep_bus.py', 'w', encoding='utf-8') as f:
                f.write(final_log_content)
                print(f"Đã ghi file log: D:\\log_ghep_bus.py")
             
            name = os.path.basename(file_psse) 
            pre, ext = os.path.splitext(name)
            _date = name[:10].replace('-','_')     
            # Tạo thư mục đích nếu chưa có
            if not os.path.exists(output_folder + "/" + _date+ "/"):
                os.makedirs(output_folder + "/" + _date+ "/")


            if solved.ierr == 0:   
                full_file = output_folder + "/" + _date+ "/" + pre + ".sav"
                psspy.save(full_file)
                print(f"Đã ghi file: {full_file}")
            else:
                full_file= output_folder + "/" + _date+ "/" + pre + "_Khong_hoi_tu.sav"
                psspy.save(full_file)
                print(f"Đã ghi file Không hội tụ: {full_file}")
                


            with open(history_file, 'a', encoding='utf-8') as f:
                # json.dumps(file_name) tạo chuỗi "tenfile.raw"
                # + "\n" để xuống dòng cho lần ghi sau
                f.write("\n"+json.dumps(file_name))

            if not os.path.exists(file_psse):
                print(f"File không tồn tại: {file_psse}")
                return

        if hasattr(ps_api, 'show_pg'):
            ps_api.show_pg()            
            ps_api.show_rp()
            ps_api.show_alert()

if __name__ == '__main__':  

    output_folder = r'D:/'
       
    source_folder = r'\\PhongPhuongThuc\Trao doi du lieu\Phuong thuc A0-Ax\Tinh toan che do A0-Ax\A0\Snapshot' 
    fix = fix_code_4(source_folder,output_folder)    
    print ("Finish")
