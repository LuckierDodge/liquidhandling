import sys
import os
from liquidhandling import SoftLinx
from liquidhandling import SoloSoft

soloSoft = SoloSoft.SoloSoft("example.hso")

soloSoft.moveArm("Position1")
soloSoft.savePipeline()


softLinx = SoftLinx.SoftLinx("ExampleProtocol", "example_protocol.slvp")
softLinx.setPlates({"SoftLinx.PlateCrane.Stack1": "PlateOne 96 V-Bottom"})
softLinx.plateCraneMovePlate(
    ["SoftLinx.PlateCrane.Stack1"], ["SoftLinx.Solo.Position6"]
)
softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
softLinx.soloSoftRun(
    "C:\\Users\\svcaibio\\Dev\\liquidhandling\\example\\softlinx\\example.hso"
)
softLinx.saveProtocol()
