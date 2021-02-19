import sys
import ROOT

def test_bins() :
    f = ROOT.TFile.Open('hist_ggH.root')

    hdata = f.Get("ggH_pt_1")

    # print(hdata.GetNbinsX())
    assert hdata.GetNbinsX() == 30
