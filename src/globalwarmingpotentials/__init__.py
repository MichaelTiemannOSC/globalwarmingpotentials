"""
globalwarmingpotentials
-----------------------

"""

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


def as_frame():
    """Return Global Warming Potentials as a Pandas DataFrame."""
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas is required for reading global warming "
            "potentials as a Data Frame."
        ) from None

    from importlib.resources import files

    return pd.read_csv(
        files("globalwarmingpotentials").joinpath("globalwarmingpotentials.csv").open('r', encoding="utf-8"),
        index_col=0,
        comment="#",
    )


data = {
    "SARGWP100": {
        "CH4": 21.0,
        "N2O": 310.0,
        "CFC11": 3800.0,
        "CFC12": 8100.0,
        "CFC113": 4800.0,
        "Halon1301": 5400.0,
        "CCl4": 1400.0,
        "CH3CCl3": 100.0,
        "HCFC22": 1500.0,
        "HCFC123": 90.0,
        "HCFC124": 470.0,
        "HCFC141b": 600.0,
        "HCFC142b": 1800.0,
        "HFC23": 11700.0,
        "HFC32": 650.0,
        "HFC41": 150.0,
        "HFC125": 2800.0,
        "HFC134": 1000.0,
        "HFC134a": 1300.0,
        "HFC143": 300.0,
        "HFC143a": 3800.0,
        "HFC152a": 140.0,
        "HFC227ea": 2900.0,
        "HFC236fa": 6300.0,
        "HFC245ca": 560.0,
        "HFC4310mee": 1300.0,
        "SF6": 23900.0,
        "CF4": 6500.0,
        "C2F6": 9200.0,
        "C3F8": 7000.0,
        "cC4F8": 8700.0,
        "C4F10": 7000.0,
        "C5F12": 7500.0,
        "C6F14": 7400.0,
        "CHCl3": 4.0,
        "CH2Cl2": 9.0,
    },
    "AR4GWP100": {
        "CH4": 25.0,
        "N2O": 298.0,
        "CFC11": 4750.0,
        "CFC12": 10900.0,
        "CFC13": 14400.0,
        "CFC113": 6130.0,
        "CFC114": 10000.0,
        "CFC115": 7370.0,
        "Halon1301": 7140.0,
        "Halon1211": 1890.0,
        "Halon2402": 1640.0,
        "CCl4": 1400.0,
        "CH3Br": 5.0,
        "CH3CCl3": 146.0,
        "HCFC22": 1810.0,
        "HCFC123": 77.0,
        "HCFC124": 609.0,
        "HCFC141b": 725.0,
        "HCFC142b": 2310.0,
        "HCFC225ca": 122.0,
        "HCFC225cb": 595.0,
        "HFC23": 14800.0,
        "HFC32": 675.0,
        "HFC125": 3500.0,
        "HFC134a": 1430.0,
        "HFC143a": 4470.0,
        "HFC152a": 124.0,
        "HFC227ea": 3220.0,
        "HFC236fa": 9810.0,
        "HFC245fa": 1030.0,
        "HFC365mfc": 794.0,
        "HFC4310mee": 1640.0,
        "SF6": 22800.0,
        "NF3": 17200.0,
        "CF4": 7390.0,
        "C2F6": 12200.0,
        "C3F8": 8830.0,
        "cC4F8": 10300.0,
        "C4F10": 8860.0,
        "C5F12": 9160.0,
        "C6F14": 9300.0,
        "SF5CF3": 17700.0,
        "HFE125": 14900.0,
        "HFE134": 6320.0,
        "HFE143a": 756.0,
        "HCFE235da2": 350.0,
        "HFE245cb2": 708.0,
        "HFE245fa2": 659.0,
        "HFE347mcc3": 575.0,
        "HFE347pcf2": 580.0,
        "HFE356pcc3": 110.0,
        "HFE569sf2": 59.0,
        "HFE4310pccc124": 1870.0,
        "HFE236ca12": 2800.0,
        "HFE338pcc13": 1500.0,
        "PFPMIE": 10300.0,
        "CH2Cl2": 8.7,
        "CH3Cl": 13.0,
    },
    "AR5GWP100": {
        "CH4": 28.0,
        "N2O": 265.0,
        "CFC11": 4660.0,
        "CFC12": 10200.0,
        "CFC13": 13900.0,
        "CFC113": 5820.0,
        "CFC114": 8590.0,
        "CFC115": 7670.0,
        "Halon1301": 6290.0,
        "Halon1211": 1750.0,
        "Halon2402": 1470.0,
        "CCl4": 1730.0,
        "CH3Br": 2.0,
        "CH3CCl3": 160.0,
        "HCFC21": 148.0,
        "HCFC22": 1760.0,
        "HCFC123": 79.0,
        "HCFC124": 527.0,
        "HCFC141b": 782.0,
        "HCFC142b": 1980.0,
        "HCFC225ca": 127.0,
        "HCFC225cb": 525.0,
        "HFC23": 12400.0,
        "HFC32": 677.0,
        "HFC41": 116.0,
        "HFC125": 3170.0,
        "HFC134": 1120.0,
        "HFC134a": 1300.0,
        "HFC143": 328.0,
        "HFC143a": 4800.0,
        "HFC152": 16.0,
        "HFC152a": 138.0,
        "HFC161": 4.0,
        "HFC227ea": 3350.0,
        "HFC236cb": 1210.0,
        "HFC236ea": 1330.0,
        "HFC236fa": 8060.0,
        "HFC245ca": 716.0,
        "HFC245fa": 858.0,
        "HFC365mfc": 804.0,
        "HFC4310mee": 1650.0,
        "SO2F2": 4090.0,
        "SF6": 23500.0,
        "NF3": 16100.0,
        "CF4": 6630.0,
        "C2F6": 11100.0,
        "C3F8": 8900.0,
        "cC4F8": 9540.0,
        "C4F10": 9200.0,
        "C5F12": 8550.0,
        "C6F14": 7910.0,
        "C7F16": 7820.0,
        "C8F18": 7620.0,
        "C10F18": 7190.0,
        "SF5CF3": 17400.0,
        "cC3F6": 9200.0,
        "HFE125": 12400.0,
        "HFE134": 5560.0,
        "HFE143a": 523.0,
        "HCFE235da2": 491.0,
        "HFE245cb2": 654.0,
        "HFE245fa2": 812.0,
        "HFE347mcc3": 530.0,
        "HFE347pcf2": 889.0,
        "HFE356pcc3": 413.0,
        "HFE569sf2": 57.0,
        "HFE4310pccc124": 2820.0,
        "HFE236ca12": 5350.0,
        "HFE338pcc13": 2910.0,
        "HFE227ea": 6450.0,
        "HFE236ea2": 1790.0,
        "HFE236fa": 979.0,
        "HFE245fa1": 828.0,
        "HFE263fb2": 1.0,
        "HFE329mcc2": 3070.0,
        "HFE338mcf2": 929.0,
        "HFE347mcf2": 854.0,
        "HFE356mec3": 387.0,
        "HFE356pcf2": 719.0,
        "HFE356pcf3": 446.0,
        "HFE374pc2": 627.0,
        "PFPMIE": 9710.0,
        "CHCl3": 16.0,
        "CH2Cl2": 9.0,
        "CH3Cl": 12.0,
        "Halon1201": 376.0,
    },
    "AR5CCFGWP100": {
        "CH4": 34,
        "N2O": 298,
        "CFC11": 5352,
        "CFC12": 11547,
        "CFC13": 15451,
        "CFC113": 6586,
        "CFC114": 9615,
        "CFC115": 8516,
        "Halon1301": 7154,
        "Halon1211": 2070,
        "Halon2402": 1734,
        "Halon1202": 280,
        "CCl4": 2019,
        "CH3Br": 3,
        "CH3CCl3": 193,
        "HCFC21": 179,
        "HCFC22": 2106,
        "HCFC123": 96,
        "HCFC124": 635,
        "HCFC141b": 938,
        "HCFC142b": 2345,
        "HCFC225ca": 155,
        "HCFC225cb": 633,
        "HFC23": 13856,
        "HFC32": 817,
        "HFC41": 141,
        "HFC125": 3691,
        "HFC134": 1337,
        "HFC134a": 1549,
        "HFC143": 397,
        "HFC143a": 5508,
        "HFC152": 20,
        "HFC152a": 167,
        "HFC161": 4,
        "HFC227ea": 3860,
        "HFC236cb": 1438,
        "HFC236ea": 1596,
        "HFC236fa": 8998,
        "HFC245ca": 863,
        "HFC245fa": 1032,
        "HFC365mfc": 966,
        "HFC4310mee": 1952,
        "SO2F2": 4732,
        "SF6": 26087,
        "NF3": 17885,
        "CF4": 7349,
        "C2F6": 12340,
        "C3F8": 9878,
        "cC4F8": 10592,
        "C4F10": 10213,
        "C5F12": 9484,
        "C6F14": 8780,
        "C7F16": 8681,
        "C8F18": 8456,
        "C10F18": 7977,
        "SF5CF3": 19396,
        "cC3F6": 10208,
        "HFE125": 13951,
        "HFE134": 6512,
        "HFE143a": 632,
        "HCFE235da2": 595,
        "HFE245cb2": 790,
        "HFE245fa2": 981,
        "HFE347mcc3": 641,
        "HFE347pcf2": 1072,
        "HFE356pcc3": 500,
        "HFE569sf2": 69,
        "HFE4310pccc124": 3353,
        "HFE236ca12": 6260,
        "HFE338pcc13": 3466,
        "HFE227ea": 7377,
        "HFE236ea2": 2143,
        "HFE236fa": 1177,
        "HFE245fa1": 997,
        "HFE263fb2": 2,
        "HFE329mcc2": 3598,
        "HFE338mcf2": 1118,
        "HFE347mcf2": 1028,
        "HFE356mec3": 468,
        "HFE356pcf2": 867,
        "HFE356pcf3": 540,
        "HFE365mcf3": 1,
        "HFE374pc2": 758,
        "PFPMIE": 10789,
        "CHCl3": 20,
        "CH2Cl2": 11,
        "CH3Cl": 15,
        "Halon1201": 454,
    },
    "AR6GWP100": {
        "CH4": 27.9,
        "N2O": 273.0,
        "CFC11": 6230.0,
        "CFC12": 12500.0,
        "CFC13": 16200.0,
        "CFC113": 6520.0,
        "CFC114": 9430.0,
        "CFC115": 9600.0,
        "Halon1301": 7200.0,
        "Halon1211": 1930.0,
        "Halon2402": 2170.0,
        "Halon1202": 216.0,
        "CCl4": 2200.0,
        "CH3Br": 2.43,
        "CH3CCl3": 161.0,
        "HCFC21": 160.0,
        "HCFC22": 1960.0,
        "HCFC123": 90.4,
        "HCFC124": 597.0,
        "HCFC141b": 860.0,
        "HCFC142b": 2300.0,
        "HCFC225ca": 137.0,
        "HCFC225cb": 568.0,
        "HFC23": 14600.0,
        "HFC32": 771.0,
        "HFC41": 135.0,
        "HFC125": 3740.0,
        "HFC134": 1260.0,
        "HFC134a": 1530.0,
        "HFC143": 364.0,
        "HFC143a": 5810.0,
        "HFC152": 21.5,
        "HFC152a": 164.0,
        "HFC161": 4.84,
        "HFC227ea": 3600.0,
        "HFC236cb": 1350.0,
        "HFC236ea": 1500.0,
        "HFC236fa": 8690.0,
        "HFC245ca": 787.0,
        "HFC245fa": 962.0,
        "HFC365mfc": 914.0,
        "HFC4310mee": 1600.0,
        "SO2F2": 4630.0,
        "SF6": 25200.0,
        "NF3": 17400.0,
        "CF4": 7380.0,
        "C2F6": 12400.0,
        "C3F8": 9290.0,
        "cC4F8": 10200.0,
        "C4F10": 10000.0,
        "C5F12": 9220.0,
        "C6F14": 8620.0,
        "C7F16": 8410.0,
        "C8F18": 8260.0,
        "C10F18": 7480.0,
        "SF5CF3": 18500.0,
        "HFE125": 14300.0,
        "HFE134": 6630.0,
        "HFE143a": 616.0,
        "HCFE235da2": 539.0,
        "HFE245cb2": 747.0,
        "HFE245fa2": 878.0,
        "HFE347mcc3": 576.0,
        "HFE347pcf2": 980.0,
        "HFE356pcc3": 277.0,
        "HFE569sf2": 60.7,
        "HFE4310pccc124": 3220.0,
        "HFE236ca12": 6060.0,
        "HFE338pcc13": 3320.0,
        "HFE227ea": 7520.0,
        "HFE236ea2": 2590.0,
        "HFE236fa": 1100.0,
        "HFE245fa1": 934.0,
        "HFE329mcc2": 3770.0,
        "HFE338mcf2": 1040.0,
        "HFE347mcf2": 963.0,
        "HFE356mec3": 264.0,
        "HFE356pcf2": 831.0,
        "HFE356pcf3": 484.0,
        "HFE365mcf3": 1.6,
        "HFE374pc2": 12.5,
        "PFPMIE": 10300.0,
        "CHCl3": 20.6,
        "CH2Cl2": 11.2,
        "CH3Cl": 5.54,
        "Halon1201": 380.0,
    },
    "AR6GWP20": {
        "CH4": 81.2,
        "N2O": 273.0,
        "CFC11": 8320.0,
        "CFC12": 12700.0,
        "CFC13": 12400.0,
        "CFC113": 6860.0,
        "CFC114": 8260.0,
        "CFC115": 7410.0,
        "Halon1301": 8320.0,
        "Halon1211": 4920.0,
        "Halon2402": 4070.0,
        "Halon1202": 775.0,
        "CCl4": 3810.0,
        "CH3Br": 8.74,
        "CH3CCl3": 567.0,
        "HCFC21": 575.0,
        "HCFC22": 5690.0,
        "HCFC123": 325.0,
        "HCFC124": 2070.0,
        "HCFC141b": 2710.0,
        "HCFC142b": 5510.0,
        "HCFC225ca": 491.0,
        "HCFC225cb": 1960.0,
        "HFC23": 12400.0,
        "HFC32": 2690.0,
        "HFC41": 485.0,
        "HFC125": 6740.0,
        "HFC134": 3900.0,
        "HFC134a": 4140.0,
        "HFC143": 1300.0,
        "HFC143a": 7840.0,
        "HFC152": 77.6,
        "HFC152a": 591.0,
        "HFC161": 17.4,
        "HFC227ea": 5850.0,
        "HFC236cb": 3750.0,
        "HFC236ea": 4420.0,
        "HFC236fa": 7450.0,
        "HFC245ca": 2680.0,
        "HFC245fa": 3170.0,
        "HFC365mfc": 2920.0,
        "HFC4310mee": 3960.0,
        "SO2F2": 7510.0,
        "SF6": 18300.0,
        "NF3": 13400.0,
        "CF4": 5300.0,
        "C2F6": 8940.0,
        "C3F8": 6770.0,
        "cC4F8": 7400.0,
        "C4F10": 7300.0,
        "C5F12": 6680.0,
        "C6F14": 6260.0,
        "C7F16": 6120.0,
        "C8F18": 6010.0,
        "C10F18": 5480.0,
        "SF5CF3": 13900.0,
        "HFE125": 13500.0,
        "HFE134": 12700.0,
        "HFE143a": 2170.0,
        "HCFE235da2": 1930.0,
        "HFE245cb2": 2630.0,
        "HFE245fa2": 3060.0,
        "HFE347mcc3": 2020.0,
        "HFE347pcf2": 3370.0,
        "HFE356pcc3": 995.0,
        "HFE569sf2": 219.0,
        "HFE4310pccc124": 8720.0,
        "HFE236ca12": 11700.0,
        "HFE338pcc13": 9180.0,
        "HFE227ea": 9800.0,
        "HFE236ea2": 7020.0,
        "HFE236fa": 3670.0,
        "HFE245fa1": 3170.0,
        "HFE329mcc2": 7550.0,
        "HFE338mcf2": 3460.0,
        "HFE347mcf2": 3270.0,
        "HFE356mec3": 949.0,
        "HFE356pcf2": 2870.0,
        "HFE356pcf3": 1730.0,
        "HFE365mcf3": 5.77,
        "HFE374pc2": 45.0,
        "PFPMIE": 7750.0,
        "CHCl3": 74.2,
        "CH2Cl2": 40.2,
        "CH3Cl": 19.9,
        "Halon1201": 1340.0,
    },
    "AR6GWP500": {
        "CH4": 7.95,
        "N2O": 130.0,
        "CFC11": 2090.0,
        "CFC12": 5710.0,
        "CFC13": 17500.0,
        "CFC113": 2830.0,
        "CFC114": 6150.0,
        "CFC115": 9880.0,
        "Halon1301": 2750.0,
        "Halon1211": 552.0,
        "Halon2402": 639.0,
        "Halon1202": 61.5,
        "CCl4": 658.0,
        "CH3Br": 0.692,
        "CH3CCl3": 46.0,
        "HCFC21": 45.6,
        "HCFC22": 560.0,
        "HCFC123": 25.8,
        "HCFC124": 170.0,
        "HCFC141b": 246.0,
        "HCFC142b": 658.0,
        "HCFC225ca": 39.0,
        "HCFC225cb": 162.0,
        "HFC23": 10500.0,
        "HFC32": 220.0,
        "HFC41": 38.6,
        "HFC125": 1110.0,
        "HFC134": 361.0,
        "HFC134a": 436.0,
        "HFC143": 104.0,
        "HFC143a": 1940.0,
        "HFC152": 6.14,
        "HFC152a": 46.8,
        "HFC161": 1.38,
        "HFC227ea": 1100.0,
        "HFC236cb": 387.0,
        "HFC236ea": 428.0,
        "HFC236fa": 6040.0,
        "HFC245ca": 225.0,
        "HFC245fa": 274.0,
        "HFC365mfc": 261.0,
        "HFC4310mee": 458.0,
        "SO2F2": 1410.0,
        "SF6": 34100.0,
        "NF3": 18200.0,
        "CF4": 10600.0,
        "C2F6": 17500.0,
        "C3F8": 12400.0,
        "cC4F8": 13800.0,
        "C4F10": 13400.0,
        "C5F12": 12700.0,
        "C6F14": 11600.0,
        "C7F16": 11300.0,
        "C8F18": 11100.0,
        "C10F18": 9780.0,
        "SF5CF3": 21100.0,
        "HFE125": 7680.0,
        "HFE134": 1940.0,
        "HFE143a": 176.0,
        "HCFE235da2": 154.0,
        "HFE245cb2": 213.0,
        "HFE245fa2": 251.0,
        "HFE347mcc3": 164.0,
        "HFE347pcf2": 279.0,
        "HFE356pcc3": 79.0,
        "HFE569sf2": 17.3,
        "HFE4310pccc124": 920.0,
        "HFE236ca12": 1770.0,
        "HFE338pcc13": 948.0,
        "HFE227ea": 2570.0,
        "HFE236ea2": 741.0,
        "HFE236fa": 315.0,
        "HFE245fa1": 266.0,
        "HFE329mcc2": 1100.0,
        "HFE338mcf2": 297.0,
        "HFE347mcf2": 275.0,
        "HFE356mec3": 75.3,
        "HFE356pcf2": 237.0,
        "HFE356pcf3": 138.0,
        "HFE365mcf3": 0.457,
        "HFE374pc2": 3.56,
        "PFPMIE": 11700.0,
        "CHCl3": 5.87,
        "CH2Cl2": 3.18,
        "CH3Cl": 1.58,
        "Halon1201": 108.0,
    },
    "AR6GTP100": {
        "CH4": 5.38,
        "N2O": 233.0,
        "CFC11": 3540.0,
        "CFC12": 10400.0,
        "CFC13": 18800.0,
        "CFC113": 5210.0,
        "CFC114": 9410.0,
        "CFC115": 11000.0,
        "Halon1301": 5060.0,
        "Halon1211": 406.0,
        "Halon2402": 702.0,
        "Halon1202": 39.3,
        "CCl4": 810.0,
        "CH3Br": 0.438,
        "CH3CCl3": 29.7,
        "HCFC21": 29.0,
        "HCFC22": 379.0,
        "HCFC123": 16.4,
        "HCFC124": 110.0,
        "HCFC141b": 162.0,
        "HCFC142b": 514.0,
        "HCFC225ca": 24.8,
        "HCFC225cb": 105.0,
        "HFC23": 15100.0,
        "HFC32": 142.0,
        "HFC41": 24.6,
        "HFC125": 1300.0,
        "HFC134": 239.0,
        "HFC134a": 306.0,
        "HFC143": 66.6,
        "HFC143a": 3250.0,
        "HFC152": 3.89,
        "HFC152a": 29.8,
        "HFC161": 0.872,
        "HFC227ea": 1490.0,
        "HFC236cb": 268.0,
        "HFC236ea": 288.0,
        "HFC236fa": 8870.0,
        "HFC245ca": 146.0,
        "HFC245fa": 180.0,
        "HFC365mfc": 172.0,
        "HFC4310mee": 347.0,
        "SO2F2": 1920.0,
        "SF6": 30600.0,
        "NF3": 20000.0,
        "CF4": 9050.0,
        "C2F6": 15200.0,
        "C3F8": 11200.0,
        "cC4F8": 12400.0,
        "C4F10": 12100.0,
        "C5F12": 11200.0,
        "C6F14": 10500.0,
        "C7F16": 10200.0,
        "C8F18": 10000.0,
        "C10F18": 9010.0,
        "SF5CF3": 21600.0,
        "HFE125": 13100.0,
        "HFE134": 2060.0,
        "HFE143a": 113.0,
        "HCFE235da2": 98.4,
        "HFE245cb2": 137.0,
        "HFE245fa2": 162.0,
        "HFE347mcc3": 106.0,
        "HFE347pcf2": 181.0,
        "HFE356pcc3": 50.4,
        "HFE569sf2": 11.0,
        "HFE4310pccc124": 647.0,
        "HFE236ca12": 1860.0,
        "HFE338pcc13": 657.0,
        "HFE227ea": 4440.0,
        "HFE236ea2": 521.0,
        "HFE236fa": 205.0,
        "HFE245fa1": 173.0,
        "HFE329mcc2": 1090.0,
        "HFE338mcf2": 194.0,
        "HFE347mcf2": 179.0,
        "HFE356mec3": 48.0,
        "HFE356pcf2": 154.0,
        "HFE356pcf3": 88.4,
        "HFE365mcf3": 0.289,
        "HFE374pc2": 2.25,
        "PFPMIE": 12000.0,
        "CHCl3": 3.72,
        "CH2Cl2": 2.01,
        "CH3Cl": 1.0,
        "Halon1201": 69.8,
    },
}
