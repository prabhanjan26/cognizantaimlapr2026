#create pipeline runner to display the customer data from txt file using pipline runner 

class PipeLineRunner:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)
    def run(self,**kwargs):
        for stage in self.stages:
            data = stage(**kwargs)
        return data 