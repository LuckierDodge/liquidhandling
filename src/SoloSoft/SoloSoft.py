class SoloSoft:

    file = None
    plateList = []
    pipeline = []
    STEP_DELIMITER = "!@#$"

    def __init__(self, filename=None, plateList=None, pipeline=None):
        # *Open protocol file for editing
        try:
            if filename != None:
                self.setFile(open(filename, "x"))
        except:
            print("Error creating SoloSoft protocol with filename %s" % filename)
        # *Set plate list
        try:
            if plateList != None:
                self.setPlates(plateList)
            else:
                self.setPlates(
                    [
                        "Empty",
                        "Empty",
                        "Empty",
                        "Empty",
                        "Empty",
                        "Empty",
                        "Empty",
                        "Empty",
                    ]
                )
        except:
            print("Error setting Plate List")
        # *Set pipeline, if we're expanding on an existing pipeline
        try:
            if pipeline != None:
                self.setPipeline(pipeline)
        except:
            print("Error setting pipeline")

    def setFile(self, filename):
        self.file = open(filename, "x")

    def setPlates(self, plateList):
        if not isinstance(plateList, list):
            raise TypeError("plateList must be a list of strings.")
        else:
            for plate in plateList:
                if not isinstance(plate, str):
                    raise TypeError("plate must be a string.")

    def setPipeline(self, pipeline):
        if not isinstance(pipeline, list):
            raise TypeError("pipeline should be a list")
        else:
            self.pipeline = pipeline

    def initializePipeline(self):
        self.setPipeline([self.plateList])

    def removeStep(self, position=None):
        if position != None:
            self.pipeline.remove(position)
        else:
            self.pipeline.pop()

    def getTips(
        self,
        position="Position1",
        disposal="TipDisposal",
        num_tips=8,
        auto_tip_selection=True,
        count_tips_from_last_channel=False,
        index=None,
    ):  # TODO Need to figure out rest of parameters
        properties_list = ["GetTip"]
        properties_list.append(position)
        properties_list.append(disposal)
        properties_list.append(num_tips)
        if auto_tip_selection:
            properties_list.append(1)
        else:
            properties_list.append(0)
        properties_list.append(
            0
        )  # ? Likely unused, but we'll keep it in for consistency
        properties_list.append(count_tips_from_last_channel)
        properties_list.append(self.STEP_DELIMITER)
        if index != None:
            self.pipeline.insert(index, properties_list)
        else:
            self.pipeline.append(properties_list)

    def startLoop(self, iterations=-1):
        properties_list = ["Loop"]
        properties_list.append(iterations)
        properties_list.append(self.STEP_DELIMITER)
        self.pipeline.append(properties_list)

    def endLoop(self):
        properties_list = ["EndLoop"]
        properties_list.append(self.STEP_DELIMITER)
        self.pipeline.append(properties_list)

    # TODO
    def aspirate(
        self,
        position="Position1",
        aspirate_volume_named=None,
        syringe_speed=100,
        start_by_emptying_syringe=0,
        increment_column_order=None,
        aspirate_point="Position1",
        aspirate_shift=[0, 0, 1],
        do_tip_touch=0,
        tip_touch_shift=[0, 0, 0],
        file_data_path="",
        multiple_wells=1,
        backlash=0,
        move_distance=[0, 0, 0],
        pre_aspirate=0,
        mix_at_start=0,
        mix_cycles=1,
        mix_volume=0,
    ):
        properties_list = ["Aspirate"]
        properties_list.append(position)
        if aspirate_volume_named != None:
            properties_list.append(position)
        else:
            properties_list.append("")
        properties_list.append(2)  # ? Mysterious integer value
        properties_list.append(syringe_speed)
        properties_list.append(start_by_emptying_syringe)
        if aspirate_volume_named != None:
            properties_list.append("True")
            properties_list.append("False")
        else:
            properties_list.append("False")
            properties_list.append("True")
        if increment_column_order != None:
            properties_list.append("True")
            properties_list.append("False")
        else:
            properties_list.append("False")
            properties_list.append("True")
        properties_list.append(aspirate_point)
        properties_list.append(aspirate_shift)
        properties_list.append(do_tip_touch)
        properties_list.append(tip_touch_shift)
        properties_list.append(file_data_path)
        properties_list.append(multiple_wells)
        properties_list.append(backlash)
        properties_list.append(mix_at_start)
        properties_list.append(mix_cycles)
        properties_list.append(mix_volume)
        properties_list.append(self.STEP_DELIMITER)

    # TODO
    def dispense(self):
        return

    # TODO
    def hitPicking(self):
        return

    # TODO
    def operateAccessory(self):
        return

    # TODO
    def pause(self):
        return

    # TODO
    def getBottom(self):
        return

    # TODO
    def setSpeed(self):
        return

    # TODO
    def moveArm(self):
        return