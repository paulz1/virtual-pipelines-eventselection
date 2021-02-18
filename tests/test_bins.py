import sys
import ROOT

f = ROOT.TFile.Open('hist_ggH.root')

hdata = f.Get("z_pt")

print(len(hdata.GetNbinsX()))
