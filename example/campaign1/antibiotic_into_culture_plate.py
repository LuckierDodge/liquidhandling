"""
CAMPAIGN 1, STEP 3: 

ADD ANTIBIOTIC TO CULTURE PLATES

Deck Layout:
Deck Layout:
1 -> Tips ("TipBox-Corning 200uL")
2 -> Growth plate (Corning 3383 or Falcon - ref 353916)
3 -> Lb media well, antibiotic stock solution well (12 channel reservoir) -> column 1 = lb media; column 3 = antibiotic stock solution 
4 -> HEATING NEST
5 -> Culture plate from freezer (96 deep well round bottom)
6 -> Antibiotic serial dilution plate (Corning 3383 or Falcon - ref 353916)
7 -> Empty
8 -> Empty


Idea: 
-Transfer set volume from Column1 of antibiotic dilution plate to Column 1 of inoculated growth media plate
-Transfer set volume from Colum 2 of antibiotic dilution plate to Column 2 of inoculated growth media plate
. . . ect. 


"""

import os
import sys

# Change this path to point to the location of the repository, if neccessary
sys.path.append(
    os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../src"))
)
import SoloSoft
from Plates import GenericPlate96Well, NinetySixDeepWell, ZAgilentReservoir_1row   # TODO: determine which plate types you will actually need

#* Program Variables
blowoff_volume = 20
num_mixes = 5
# Step 3 variables
antibiotic_transfer_volume_s3 = 90
antibiotic_mix_volume_s3 = 90  
destination_mix_volume_s3 = 120

soloSoft = SoloSoft.SoloSoft(
    filename="antibiotic_into_culture_plate.hso",
    plateList=[
        "TipBox-Corning 200uL",
        "Corning 3383",
        "12 Channel Reservoir",
        "Empty",
        "96 Deep Protein",
        "Corning 3383",
        "Empty",
        "Empty",
    ],
)

# no need to get tips (just ended at smallest serial dilution) -> work backwards in growth plate
soloSoft.getTip()
for i in range(6,0,-1):
    soloSoft.aspirate(
        position="Position6", 
        aspirate_volumes=GenericPlate96Well().setColumn(i, antibiotic_transfer_volume_s3), 
        mix_at_start=True, 
        mix_cycles=num_mixes, 
        mix_volume=antibiotic_mix_volume_s3,
        dispense_height=2, 
        aspirate_shift=[0,0,2], 
    )
    soloSoft.dispense(
        position="Position2", 
        dispense_volumes=GenericPlate96Well().setColumn(i, antibiotic_transfer_volume_s3),
        mix_at_finish=True,
        mix_cycles=num_mixes,
        mix_volume=destination_mix_volume_s3, 
        aspirate_height=2, 
        dispense_shift=[0,0,2], 
    )

soloSoft.shuckTip()
soloSoft.savePipeline() 