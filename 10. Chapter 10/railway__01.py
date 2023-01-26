import pandas as pd

pd.DataFrame()

class RailwayForm:
    formType ="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        

# Object below
RoysApplication = RailwayForm()
RoysApplication.name ="Soham"
RoysApplication.train = "Rajdhani Express"
RoysApplication.printData()
