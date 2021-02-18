import sys
import ROOT

f = ROOT.TFile.Open('hist_ggH.root')

hdata = f.Get("ggH_pt_1")

print(len(hdata.GetNbinsX()))
