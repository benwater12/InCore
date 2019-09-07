from service.analyticService.core.analyticAlgo.analyticBase import analytic
import numpy as np
from service.visualizeService.core.analyticVizAlgo.dotLine import dotLine

class regression(analytic):
    def __init__(self, algoInfo, fid, action='train', mid=None):
        super().__init__(algoInfo, fid, action, mid)
    
    def test(self):
        self.txtRes = ""
        for k, v in self.outputData.items():
            self.txtRes += f"{self.outputDict[k]}:\n"
            self.txtRes += f"  MAE: {(np.abs(v-self.result[k])).mean()}\n"
            self.txtRes += f"  MSE: {((v-self.result[k])**2).mean()}\n"
            self.txtRes += f"  RMSE: {np.sqrt(((v-self.result[k])**2).mean())}\n"
        self.visualize()
        return {"text": self.txtRes, "fig": self.vizRes}

    def projectVisualize(self):
        allInputCols = {}
        allRealCols = {}
        allPredictCols = {}
        figs = {}
        for k, v in self.inputDict.items():
            for col in v:
                if self.colType[col] == 'float' or self.colType[col] == 'int':
                    allInputCols[col] = self.dataDf[col]
        for k, v in self.outputDict.items():
            if self.colType[v] == 'float' or self.colType[v] == 'int':
                allRealCols[v] = self.dataDf[v]
                allPredictCols[v] = self.result[k]
        for ink, inv in allInputCols.items():
            for outk, outv in allRealCols.items():
                tmpData = {"x": inv, "y_dot": outv, "y_line": allPredictCols[outk]}
                tmpColName={"x":ink,"y":outk}
                figName=f"{ink}-{outk}"
                algo=dotLine(tmpData,tmpColName,figName)
                algo.doBokehViz()
                algo.getComp()
                figs[figName]=algo.component
        #TODO: use dotLineSelect
        return figs
             
        

            