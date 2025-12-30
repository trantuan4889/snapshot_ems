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
                import psse3504
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
    
from multiprocessing import Pool, cpu_count
from functools import partial # <--- Cần thêm thư viện này

# --- HÀM WORKER ---
def worker_task_data_file(file_info, file_py=None): # file_py nhận đường dẫn hoặc nội dung
    file_path, file_name = file_info
    
    # 1. Khởi tạo PSS/E
    # Lưu ý: run_psse() phải được import hoặc định nghĩa ở phạm vi toàn cục (global)
    # Nếu run_psse() nằm trong if __name__, worker sẽ không thấy nó -> Lỗi
    try:
        run_psse() 
    except NameError:
        pass # Giả định môi trường đã setup sẵn hoặc import từ module khác

    ps_api = pss_api()
    
    ps_api.hide_pg()
    ps_api.hide_rp()
    ps_api.hide_alert()

    pre, ext = os.path.splitext(file_name)
    case_key = pre[:16] 

    try:
        # 2. Load file
        if ext == '.sav':
            psspy.case(file_path)
        elif ext == '.raw':
            psspy.read(0, file_path)
        
        # 3. Chạy file script Python phụ (Fix lỗi exec)
        if file_py and os.path.exists(file_py):
            try:
                with open(file_py, 'r', encoding='utf-8') as f:
                    code_content = f.read()
                    # Chạy code python trong ngữ cảnh hiện tại
                    exec(code_content, globals(), locals())
                    psspy.fnsl([0,0,0,1,1,4,-1,0])
                    psspy.fnsl([0,0,0,1,1,0,99,0])

            except Exception as e:
                print(f"Lỗi khi chạy file script phụ {file_py}: {e}")

        # Thiết lập subsystem
        psspy.bsys(0, 1, [1.0, 500.], 0, [], 0, [], 0, [], 0, [])
        
        # 4. Lấy dữ liệu
        # Lưu ý: Class branch() phải import được ở đây
        list_branch = branch().data 

        extracted_data = []
        for brn in list_branch:
            ibus = brn[1]  
            jbus = brn[2]
            
            if ibus > 10000 and jbus > 10000:
                ckt = brn[5]
                iname = brn[3]
                jname = brn[4]
                meternumber = brn[14]
                
                flow_info = {
                    'length': brn[7], 'amps': brn[8], 'rate': brn[9],
                    'pcta': brn[10], 'pctmva': brn[11], 'mw': brn[12], 'mvar': brn[13]
                }
                static_info = {
                    'vol': brn[0], 'from_bus_number': ibus, 'to_bus_number': jbus,
                    'from_bus_name': iname, 'to_bus_name': jname, 'id': ckt,            
                    'meternumber': meternumber,
                    'name': iname.strip() + "-" + jname.strip() + "#" + ckt.strip()
                }

                extracted_data.append({
                    'unique_key': f"{ibus}_{jbus}_{ckt.strip()}",
                    'static': static_info,
                    'flow': flow_info
                })
        ps_api.show_pg()            
        ps_api.show_rp()
        ps_api.show_alert()
        
        return (case_key, extracted_data)

    except Exception as e:
        # Print lỗi chi tiết để debug
        import traceback
        print(f"Lỗi file {file_name}: {e}")
        # traceback.print_exc() # Bật dòng này nếu muốn xem full lỗi
        return (case_key, [])

# --- HÀM CHÍNH ---
def data_file_multicore(source_folder, file_py_path=''):
    name = os.path.basename(file_py_path) 
    output_json_path = os.path.join(source_folder, 'branch_data'+name[:-3]+'.json')
    master_branch_data = {}

    if not os.path.exists(source_folder):
        print(f"Thư mục không tồn tại: {source_folder}")
        return {}

    files = [f for f in os.listdir(source_folder) if f.endswith(('.sav', '.raw'))]
    tasks = [(os.path.join(source_folder, f), f) for f in files]
    
    print(f"Bắt đầu xử lý {len(files)} files trên {cpu_count()} nhân CPU...")

    num_processes = max(1, cpu_count() - 1)
    
    # --- SỬA LỖI Ở ĐÂY: Dùng partial ---
    # Partial giúp tạo ra một hàm mới đã được điền sẵn tham số file_py
    worker_with_arg = partial(worker_task_data_file, file_py=file_py_path)

    with Pool(processes=num_processes) as pool:
        # map giờ chỉ cần nhận danh sách tasks
        results = pool.map(worker_with_arg, tasks)

    print("Đang tổng hợp dữ liệu...")
    for case_key, data_list in results:
        if not data_list: continue 
        
        for item in data_list:
            u_key = item['unique_key']
            if u_key not in master_branch_data:
                master_branch_data[u_key] = item['static']
                master_branch_data[u_key]['flows'] = {}
            master_branch_data[u_key]['flows'][case_key] = item['flow']


    # try:
    #     with open(output_json_path, 'w', encoding='utf-8') as f:
    #         json.dump(master_branch_data, f, indent=4, ensure_ascii=False)
    #     print(f"Hoàn thành! Đã xuất: {output_json_path}")
    # except Exception as e:
    #     print(f"Lỗi ghi JSON: {e}")

    return master_branch_data

# Trong file Snapshot_cal_branch.py
# Thêm hoặc sửa hàm so sánh để trả về dữ liệu trực tiếp

def compare_data_in_memory(data_base, data_new):
    """
    Hàm so sánh 2 bộ dữ liệu dictionary trong bộ nhớ
    data_base: Dữ liệu GỐC (File 2)
    data_new: Dữ liệu MỚI (File 1 - Có Script)
    """
    comparison_result = []

    for u_key, info_new in data_new.items():
        if u_key not in data_base:
            continue 

        info_base = data_base[u_key]
        
        flows_new_sorted = sorted(info_new.get('flows', {}).items())
        flows_base_sorted = sorted(info_base.get('flows', {}).items())

        min_len = min(len(flows_new_sorted), len(flows_base_sorted))
        
        max_delta_val = 0.0
        at_time_display = ""
        
        # Khởi tạo giá trị mặc định để tránh lỗi reference
        at_val_new = 0.0
        at_val_base = 0.0

        for i in range(min_len):
            key_new, flow_n = flows_new_sorted[i]
            key_base, flow_b = flows_base_sorted[i]

            val_new = flow_n.get('pctmva', 0.0) 
            val_base = flow_b.get('pctmva', 0.0)
            
            diff = val_new - val_base
            
            # Tìm thời điểm có độ lệch lớn nhất
            if abs(diff) > abs(max_delta_val):
                max_delta_val = diff
                at_time_display = key_new 
                at_val_new = val_new    # Giá trị Sau khi chạy Script
                at_val_base = val_base  # Giá trị Gốc

        if abs(max_delta_val) > 1.0: 
            sign = "+" if max_delta_val > 0 else ""
            comparison_result.append({
                "key": u_key,
                "name": info_new['name'],
                "delta_raw": abs(max_delta_val),
                "delta": f"{sign}{max_delta_val:.2f}%", 
                "at": at_time_display,
                "pct": at_val_base,           # Mang tải gốc
                "pct_after": at_val_new       # Mang tải sau sự cố (QUAN TRỌNG)
            })

    comparison_result.sort(key=lambda x: x['delta_raw'], reverse=True)

    final_dict = {}
    for item in comparison_result:
        final_dict[item['key']] = {
            "delta": item['delta'],
            "name": item['name'],
            "pct": item['pct'],            
            "pct_after": item['pct_after'], # Server trả về giá trị này cho Web
            "at": item['at']
        }
    
    return final_dict


# if __name__ == '__main__':  

    # output_folder = r'D:/'
       
    # file_py = r'D:\123.py'
    # data_file_multicore(output_folder+'/2025_12_24',file_py)

    # data_file_multicore(output_folder+'/2025_12_24')
    # file_goc = 'D:/2025_12_28/branch_data.json'      # File chạy bình thường
    # file_moi = 'D:/2025_12_28/branch_data123.json' # File chạy code 123.py (ví dụ)
    # file_out = 'D:/2025_12_28/comparison_delta.json' # File kết quả
    
    # # Kiểm tra file tồn tại trước khi chạy
    # if os.path.exists(file_goc) and os.path.exists(file_moi):
        # compare_json_files_by_order(file_goc, file_moi, file_out)
    # else:
        # print("Không tìm thấy đủ 2 file input để so sánh.")