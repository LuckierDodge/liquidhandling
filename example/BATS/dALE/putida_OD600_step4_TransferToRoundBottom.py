""" 
Putida.OD600.step4.TransferToRoundBottom

Steps: 
- Transfer 20uL supernatant from Corning 3635 - Columns 1-12 to Round Bottom Storage - Columns 1-12 
    - make sure to keep 2mm clearance from the bottom

Deck Layout:
1 -> 
2 -> Empty (HEATING NEST)
3 -> 
4 -> 
5 -> 
6 -> 
7 -> 
8 -> 


"""

import os
import sys
from liquidhandling import SoloSoft
from liquidhandling import *

# Program Variables
transfer_volume = 20 
blowoff_volume = 10
clearance_from_bottom = 2

soloSoft = SoloSoft(
    filename="putida_OD600_step4_TransferToRoundBottom.hso",
      plateList=[
        "TipBox.200uL.Corning-4864.orangebox",
        "Empty",
        "Reservoir.12col.Agilent-201256-100.BATSgroup",
        "Plate.96.Agilent-5043-9310.RoundBottomStorage",
        "DeepBlock.96.VWR-75870-792.sterile",
        "Plate.96.Corning-3635.ClearUVAssay",
        "Empty",
        "Empty",
    ],
)


for i in range(1,13): # i = 1,2,..., 12
    soloSoft.getTip()  # need to get new tips every time 
    soloSoft.aspirate(
        position="Position6", 
        aspirate_volumes=Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        aspirate_shift=[0,0,clearance_from_bottom], 
        pre_aspirate=blowoff_volume,
    )
    soloSoft.dispense(
        position="Position4", 
        dispense_volumes=Plate_96_Agilent_5043_9310_RoundBottomStorage().setColumn(i, transfer_volume), 
        dispense_shift=[0,0,clearance_from_bottom], 
        blowoff=blowoff_volume,
    )

soloSoft.shuckTip()
soloSoft.savePipeline()

# UNCOMMENT FOLLOWING CODE TO GENERATE SOFTLINX .AHK FILE FOR THIS STEP ALONE

softLinx = SoftLinx("Putida.OD600.step4.TransferToRoundBottom", "putida_OD600_step4_TransferToRoundBottom.slvp")
softLinx.soloSoftRun( "C:\\Users\\svcaibio\\Dev\\liquidhandling\\example\\BATS\\dALE\\putida_OD600_step4_TransferToRoundBottom.hso")
softLinx.saveProtocol()
