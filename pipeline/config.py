from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT_DIR / "data" / "df" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "df" / "processed"
OUTPUT_DIR = ROOT_DIR / "data" / "df" /"output" / "pdad"
#GEOJSON_PATH = ROOT_DIR / "geojson" / "distrito_federal.geo.json"

MORADORES_FILE = RAW_DIR / "moradores.csv"
DOMICILIOS_FILE = RAW_DIR / "domicilios.csv"

REGION_COLUMN = "localidade"
MOR_WEIGHT_COLUMN = "peso_mor"
DOM_WEIGHT_COLUMN = "peso_dom"

SPECIAL_CODES = {77777, 88888, 99999}
MIN_CELL_SIZE = 8

MORADORES_VARIABLES = {
    "E02_3": {
        "source": "moradores", "column": "E02_3",
        "description": "Age", "kind": "numeric",
        "unit": "years", "special_codes": [],
        "valid_min": 0, "valid_max": 120,
    },
    "E03": {
        "source": "moradores", "column": "E03",
        "description": "Sex", "kind": "categorical",
        "special_codes": [],
        "labels": {1: "Male", 2: "Female"},
    },
    "E03_2": {
        "source": "moradores", "column": "E03_2",
        "description": "Identified sexual orientation",
        "kind": "categorical", "special_codes": [77777, 88888, 99999],
        "labels": {
            1: "Asexual", 2: "Bisexual", 3: "Gay", 4: "Lesbian",
            5: "Heterosexual", 6: "Homosexual", 7: "Pansexual",
            8: "I have relationships with men",
            9: "I have relationships with men and women",
            10: "I have relationships with women", 11: "Other",
        },
    },
    "E05": {
        "source": "moradores", "column": "E05",
        "description": "Skin colour/Race", "kind": "categorical",
        "special_codes": [],
        "labels": {1: "White", 2: "Black", 3: "Yellow", 4: "Pardo(Mixed)", 5: "Indigenous"},
    },
    "E06": {
        "source": "moradores", "column": "E06",
        "description": "Religion", "kind": "categorical",
        "special_codes": [88888],
        "labels": {
            1: "Catholic",
            2: "Evangelical", # originally pentecostal
            3: "Evangelical", # originally non-pentecostal
            4: "Evangelical", 
            5: "Spiritism",
            6: "African-derived religions",
            7: "Islam", 8: "Judaism", 9: "Indigenous Traditions",
            10: "Atheism", # originally "agnostic"
            11: "Atheism", 
            12: "Atheism", # originally "no religion"
            13: "Other",
        },
    },
    "E15_A": {
        "source": "moradores", "column": "E15_A",
        "description": "Country of birth",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            76: "Brazil", 4: "Afghanistan", 8: "Albania", 10: "Antarctica",
            12: "Algeria", 16: "American Samoa", 20: "Andorra",
            24: "Angola", 28: "Antigua and Barbuda", 31: "Azerbaijan",
            32: "Argentina", 36: "Australia", 40: "Austria", 44: "Bahamas",
            48: "Bahrain", 50: "Bangladesh", 51: "Armenia", 52: "Barbados",
            56: "Belgium", 60: "Bermuda", 64: "Bhutan", 68: "Bolivia",
            70: "Bosnia and Herzegovina", 72: "Botswana", 84: "Belize",
            90: "Solomon Islands", 96: "Brunei", 100: "Bulgaria",
            104: "Myanmar", 108: "Burundi", 112: "Belarus",
            116: "Cambodia", 120: "Cameroon", 124: "Canada",
            132: "Cape Verde", 140: "Central African Republic",
            144: "Sri Lanka", 148: "Chad", 152: "Chile", 156: "China",
            170: "Colombia", 178: "Congo", 180: "Democratic Republic of the Congo",
            188: "Costa Rica", 191: "Croatia", 192: "Cuba", 196: "Cyprus",
            203: "Czechia", 204: "Benin", 208: "Denmark", 212: "Dominica",
            214: "Dominican Republic", 218: "Ecuador", 222: "El Salvador",
            231: "Ethiopia", 232: "Eritrea", 233: "Estonia",
            242: "Fiji", 246: "Finland", 250: "France",
            254: "French Guiana", 262: "Djibouti", 266: "Gabon",
            268: "Georgia", 270: "Gambia", 275: "State of Palestine",
            276: "Germany", 288: "Ghana", 300: "Greece", 308: "Grenada",
            320: "Guatemala", 324: "Guinea", 328: "Guyana", 332: "Haiti",
            336: "Holy See (Vatican City)", 340: "Honduras", 344: "China (Hong Kong)",
            348: "Hungary", 352: "Iceland", 356: "India", 360: "Indonesia",
            364: "Iran", 368: "Iraq", 372: "Ireland", 376: "Israel",
            380: "Italy", 384: "Ivory Coast", 388: "Jamaica",
            392: "Japan", 398: "Kazakhstan", 400: "Jordan",
            404: "Kenya", 408: "North Korea", 410: "South Korea",
            414: "Kuwait", 418: "Laos", 422: "Lebanon", 426: "Lesotho",
            428: "Latvia", 430: "Liberia", 434: "Libya", 438: "Liechtenstein",
            440: "Lithuania", 442: "Luxembourg", 450: "Madagascar",
            454: "Malawi", 458: "Malaysia", 462: "Maldives", 466: "Mali",
            470: "Malta", 474: "Martinique", 478: "Mauritania",
            480: "Mauritius", 484: "Mexico", 492: "Monaco", 496: "Mongolia",
            498: "Moldova", 499: "Montenegro", 504: "Morocco",
            508: "Mozambique", 512: "Oman", 516: "Namibia", 520: "Nauru",
            524: "Nepal", 528: "Netherlands", 531: "Curaçao",
            533: "Aruba", 534: "Sint Maarten", 540: "New Caledonia",
            548: "Vanuatu", 554: "New Zealand", 558: "Nicaragua",
            562: "Niger", 566: "Nigeria", 578: "Norway",
            583: "Federated States of Micronesia", 584: "Marshall Islands",
            585: "Palau", 586: "Pakistan", 591: "Panama",
            598: "Papua New Guinea", 600: "Paraguay", 604: "Peru",
            608: "Philippines", 616: "Poland", 620: "Portugal",
            624: "Guinea-Bissau", 626: "Timor-Leste", 630: "Puerto Rico",
            634: "Qatar", 642: "Romania", 643: "Russian Federation",
            646: "Rwanda", 659: "Saint Kitts and Nevis", 662: "Saint Lucia",
            670: "Saint Vincent and the Grenadines", 674: "San Marino",
            678: "São Tomé and Príncipe", 682: "Saudi Arabia",
            686: "Senegal", 688: "Serbia", 690: "Seychelles",
            694: "Sierra Leone", 702: "Singapore", 703: "Slovakia",
            704: "Vietnam", 705: "Slovenia", 706: "Somalia",
            710: "South Africa", 716: "Zimbabwe", 724: "Spain",
            728: "South Sudan", 729: "Sudan", 740: "Suriname",
            748: "Eswatini", 752: "Sweden", 756: "Switzerland",
            1760: "Syria", 1762: "Tajikistan", 1764: "Thailand",
            1768: "Togo", 780: "Trinidad and Tobago",
            784: "United Arab Emirates", 788: "Tunisia",
            792: "Turkey", 795: "Turkmenistan", 800: "Uganda",
            804: "Ukraine", 818: "Egypt", 826: "United Kingdom",
            834: "Tanzania", 840: "United States of America",
            854: "Burkina Faso", 858: "Uruguay", 860: "Uzbekistan",
            862: "Venezuela", 882: "Samoa", 887: "Yemen", 894: "Zambia",
        },
    },
    "E15_B": {
        "source": "moradores", "column": "E15_B",
        "description": "State of birth",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            11: "Rondônia", 12: "Acre", 13: "Amazonas", 14: "Roraima",
            15: "Pará", 16: "Amapá", 17: "Tocantins",
            21: "Maranhão", 22: "Piauí", 23: "Ceará",
            24: "Rio Grande do Norte", 25: "Paraíba", 26: "Pernambuco",
            27: "Alagoas", 28: "Sergipe", 29: "Bahia",
            31: "Minas Gerais", 32: "Espírito Santo", 33: "Rio de Janeiro",
            35: "São Paulo", 41: "Paraná", 42: "Santa Catarina",
            43: "Rio Grande do Sul", 50: "Mato Grosso do Sul",
            51: "Mato Grosso", 52: "Goiás", 53: "Distrito Federal/Brasília",
        },
    },
    "F01": {
        "source": "moradores", "column": "F01",
        "description": "How many cellphones for personal use",
        "kind": "numeric", "unit": "phones", "special_codes": [88888],
        "valid_min": 0, "valid_max": 100,
    },
    "G02": {
        "source": "moradores", "column": "G02",
        "description": "medical consultations/services involve general check-ups or preventive care?",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "public", 2: "private",
            3: "public/private", 4: "none",
        },
    },
    "G03": {
        "source": "moradores", "column": "G03",
        "description": "medical consultations involved emergency?",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "public", 2: "private",
            3: "public/private", 4: "none",
        },
    },
    "H01": {
        "source": "moradores", "column": "H01",
        "description": "Knows how to read/write", "kind": "categorical",
        "special_codes": [88888, 99999], "labels": {1: "Yes", 2: "No"},
    },
    "H05_11": {
        "source": "moradores", "column": "H05_11",
        "description": "Most used mode of transportation",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "Bus", 2: "Public school bus", 3: "Private school bus",
            4: "Private (apps, taxi etc.)", 5: "Car",
            6: "Metro", 7: "Motorbike", 8: "Bicycle",
            9: "On foot", 10: "Horse/Horse wagon",
        },
    },
    "H11": {
        "source": "moradores", "column": "H11",
        "description": "Highest level of education attained", "kind": "categorical",
        "special_codes": [88888, 99999],
        "labels": {
            1: "Daycare", 2: "Early childhood education", 3: "EJA",
            4: "EJA", 5: "Primary",
            6: "Primary", 7: "Primary",
            8: "Primary", 9: "Secondary",
            10: "Secondary",
            11: "Secondary",
            12: "EJA", 13: "EJA", #program for people who did not complete school at a regular age
            14: "Undergraduate", 15: "Postgraduate",
            16: "Masters", 17: "Phd",
        },
    },
    "I04": {
        "source": "moradores", "column": "I04",
        "description": "Has worked in the last 30 days", "kind": "categorical",
        "special_codes": [88888, 99999], "labels": {1: "Yes", 2: "No"},
    },
    "I10": {
        "source": "moradores", "column": "I10",
        "description": "Commutting times",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "Less than 30 minutes", 2: "Less than 30 minutes",
            3: "Between 30 minutes and 1 hour", 4: "Between 30 minutes and 1 hour",
            5: "Between 1 hour and 1h30", 6: "Between 1 hour and 1h30",
            7: "Between 1h30 and 2 hours", 8: "Between 1h30 and 2 hours",
            9: "More than 2 hours",
        },
    },
    "I13": {
        "source": "moradores", "column": "I13",
        "description": "Position in occupation", "kind": "categorical",
        "special_codes": [88888, 99999],
        "labels": {
            1: "Public sector employee",
            2: "Military / police / firemen",
            3: "Private sector employee",
            4: "Domestic worker", 5: "Paid intern",
            6: "Apprentice", 7: "Self-employed",
            8: "Employer", 9: "Mandatory military service",
            10: "Unpaid worker assisting a household member",
        },
    },
    "I23": {
        "source": "moradores", "column": "I23",
        "description": "Weekly hours dedicated to household chores",
        "kind": "numeric", "unit": "hours/week",
        "special_codes": [88888, 99999], "valid_min": 0, "valid_max": 168,
    },
}


DOMICILIO_VARIABLES = {
    "B01": {
        "source": "domicilios", "column": "B01",
        "description": "Type of dwelling",
        "kind": "categorical", "special_codes": [],
        "labels": {
            1: "Permanent",
            2: "Improvised",
        },
    },
    "B04": {
        "source": "domicilios", "column": "B04",
        "description": "Monthly instalment amount paid in the last month",
        "kind": "numeric",
        "unit": "BRL/month",
        "special_codes": [77777, 88888, 99999],
    },
    "B05": {
        "source": "domicilios", "column": "B05",
        "description": "Monthly rent paid in the last month",
        "kind": "numeric",
        "unit": "BRL/month",
        "special_codes": [77777, 88888, 99999],
    },
    "B10": {
        "source": "domicilios", "column": "B10",
        "description": "Number of rooms",
        "kind": "numeric", "unit": "rooms",
        "special_codes": [],
    },
    "B14": {
        "source": "domicilios", "column": "B14",
        "description": "Access to general sewage collection network",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "B16": {
        "source": "domicilios", "column": "B16",
        "description": "Public waste collection service collects household waste",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "B17_1_1": {
        "source": "domicilios", "column": "B17_1_1",
        "description": "Urban infrastructure: Road asphalt quality rating",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "Excellent",
            2: "Good",
            3: "Regular",
            4: "Poor",
            5: "Very poor",
        },
    },
    "B17_2_2": {
        "source": "domicilios", "column": "B17_2_2",
        "description": "Urban infrastructure: Sidewalk quality rating",
        "kind": "categorical", "special_codes": [88888, 99999],
        "labels": {
            1: "Excellent",
            2: "Good",
            3: "Regular",
            4: "Poor",
            5: "Very poor",
        },
    },
    "B19_1": {
        "source": "domicilios", "column": "B19_1",
        "description": "Trees in the surrounding area",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "B19_2": {
        "source": "domicilios", "column": "B19_2",
        "description": "Parks or squares in the surrounding area",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "B20": {
        "source": "domicilios", "column": "B20",
        "description": "Regular police presence in the surrounding area",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "C01_1": {
        "source": "domicilios", "column": "C01_1",
        "description": "Number of cars",
        "kind": "numeric", "unit": "cars",
        "special_codes": [88888, 99999],
    },
    "C05": {
        "source": "domicilios", "column": "C05",
        "description": "Household internet access in the last month",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes, own connection",
            2: "Yes, shared with other household(s)",
            3: "No",
        },
    },
    "C07_11": {
        "source": "domicilios", "column": "C07_11",
        "description": "Number of laptops, notebooks or desktop computers",
        "kind": "numeric", "unit": "computers",
        "special_codes": [88888],
        "valid_min": 0,
    },
    "C07_12": {
        "source": "domicilios", "column": "C07_12",
        "description": "Number of air conditioning units",
        "kind": "numeric", "unit": "units",
        "special_codes": [88888],
        "valid_min": 0,
    },
    "C08": {
        "source": "domicilios", "column": "C08",
        "description": "Hired a non-resident monthly domestic worker in the last month",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "C11": {
        "source": "domicilios", "column": "C11",
        "description": "Has any pets",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "C11_1": {
        "source": "domicilios", "column": "C11_1",
        "description": "Number of cats",
        "kind": "numeric", "unit": "cats",
        "special_codes": [88888, 99999],
        "valid_min": 0,
    },
    "C11_2": {
        "source": "domicilios", "column": "C11_2",
        "description": "Number of dogs",
        "kind": "numeric", "unit": "dogs",
        "special_codes": [88888, 99999],
        "valid_min": 0,
    },
    "D15": {
        "source": "domicilios", "column": "D15",
        "description": "Any household member received a social benefit from DF or Goiás in the last month",
        "kind": "categorical", "special_codes": [88888],
        "labels": {
            1: "Yes",
            2: "No",
        },
    },
    "grupo_ped": {
        "source": "domicilios", "column": "grupo_ped",
        "description": "PED administrative region income group (derived)",
        "kind": "categorical", "special_codes": [],
        "labels": {
            1: "High income",
            2: "Upper-middle income",
            3: "Lower-middle income",
            4: "Low income",
        },
    },
    "renda_domiciliar_pc": {
        "source": "domicilios", "column": "renda_domiciliar_pc",
        "description": "Household per capita income (derived)",
        "kind": "numeric",
        "unit": "BRL",
        "special_codes": [],
    },
}

