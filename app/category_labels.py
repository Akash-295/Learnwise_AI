
CATEGORY_LABELS = {

    "Marital status": {
        1: "Single",
        2: "Married",
        3: "Widower",
        4: "Divorced",
        5: "Facto union",
        6: "Legally separated"
    },

    "Application mode": {
        1: "1st phase - general contingent",
        2: "Ordinance No. 612/93",
        5: "1st phase - special contingent (Azores)",
        7: "Holders of other higher courses",
        10: "Ordinance No. 854-B/99",
        15: "International student (bachelor)",
        16: "1st phase - special contingent (Madeira)",
        17: "2nd phase - general contingent",
        18: "3rd phase - general contingent",
        26: "Ordinance No. 533-A/99 (Different Plan)",
        27: "Ordinance No. 533-A/99 (Other Institution)",
        39: "Over 23 years old",
        42: "Transfer",
        43: "Change of course",
        44: "Technological specialization diploma holders",
        51: "Change of institution/course",
        53: "Short cycle diploma holders",
        57: "Change of institution/course (International)"
    },

    "Application order": {
        0: "1st choice",
        1: "2nd choice",
        2: "3rd choice",
        3: "4th choice",
        4: "5th choice",
        5: "6th choice",
        6: "7th choice",
        7: "8th choice",
        8: "9th choice",
        9: "10th choice"
    },

    "Course": {
        33: "Biofuel Production Technologies",
        171: "Animation and Multimedia Design",
        8014: "Social Service (Evening)",
        9003: "Agronomy",
        9070: "Communication Design",
        9085: "Veterinary Nursing",
        9119: "Informatics Engineering",
        9130: "Equinculture",
        9147: "Management",
        9238: "Social Service",
        9254: "Tourism",
        9500: "Nursing",
        9556: "Oral Hygiene",
        9670: "Advertising and Marketing Management",
        9773: "Journalism and Communication",
        9853: "Basic Education",
        9991: "Management (Evening)"
    },

    "Previous qualification": {
        1: "Secondary education",
        2: "Higher education - bachelor's degree",
        3: "Higher education - degree",
        4: "Higher education - master's",
        5: "Higher education - doctorate",
        6: "Frequency of higher education",
        9: "12th year - not completed",
        10: "11th year - not completed",
        12: "Other - 11th year",
        14: "10th year",
        15: "10th year - not completed",
        19: "Basic education 3rd cycle",
        38: "Basic education 2nd cycle",
        39: "Technological specialization course",
        40: "Higher education - degree (1st cycle)",
        42: "Professional higher technical course",
        43: "Higher education - master's (2nd cycle)"
    },

    "Nacionality": {
        1: "Portuguese",
        2: "German",
        6: "Spanish",
        11: "Italian",
        13: "Dutch",
        14: "English",
        17: "Lithuanian",
        21: "Angolan",
        22: "Cape Verdean",
        24: "Guinean",
        25: "Mozambican",
        26: "Santomean",
        32: "Turkish",
        41: "Brazilian",
        62: "Romanian",
        100: "Moldovan",
        101: "Mexican",
        103: "Ukrainian",
        105: "Russian",
        108: "Cuban",
        109: "Colombian"
    }
}


# Shared parent qualification labels
PARENT_QUALIFICATION_LABELS = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year - not completed",
    10: "11th year - not completed",
    11: "7th year (old)",
    12: "Other - 11th year",
    13: "2nd year complementary high school",
    14: "10th year",
    18: "General commerce course",
    19: "Basic education 3rd cycle",
    20: "Complementary high school course",
    22: "Technical-professional course",
    25: "Complementary high school - not completed",
    26: "7th year of schooling",
    27: "2nd cycle general high school",
    29: "9th year - not completed",
    30: "8th year of schooling",
    31: "General administration and commerce",
    33: "Supplementary accounting and administration",
    34: "Unknown",
    35: "Cannot read or write",
    36: "Can read without 4th year",
    37: "Basic education 1st cycle",
    38: "Basic education 2nd cycle",
    39: "Technological specialization course",
    40: "Higher education - degree",
    41: "Specialized higher studies",
    42: "Professional higher technical course",
    43: "Higher education - master's",
    44: "Higher education - doctorate"
}

CATEGORY_LABELS["Mother's qualification"] = PARENT_QUALIFICATION_LABELS
CATEGORY_LABELS["Father's qualification"] = PARENT_QUALIFICATION_LABELS


# Binary features
BINARY_LABELS = {
    "Displaced": {
        0: "No",
        1: "Yes"
    },
    "Educational special needs": {
        0: "No",
        1: "Yes"
    },
    "Debtor": {
        0: "No",
        1: "Yes"
    },
    "Tuition fees up to date": {
        0: "No",
        1: "Yes"
    },
    "Gender": {
        0: "Female",
        1: "Male"
    },
    "Scholarship holder": {
        0: "No",
        1: "Yes"
    },
    "International": {
        0: "No",
        1: "Yes"
    }
}

OCCUPATION_LABELS = {
    0: "Student",
    1: "Legislative and executive officials, directors and managers",
    2: "Intellectual and scientific professionals",
    3: "Intermediate-level technicians and professionals",
    4: "Administrative staff",
    5: "Personal services, security and sales workers",
    6: "Farmers and skilled agricultural workers",
    7: "Industry, construction and craft workers",
    8: "Machine operators and assembly workers",
    9: "Unskilled workers",
    10: "Armed forces professions",
    90: "Other situation",
    99: "Not specified",
    101: "Armed forces officers",
    102: "Armed forces sergeants",
    103: "Other armed forces personnel",
    112: "Administrative and commercial service directors",
    114: "Hotel, catering, trade and service directors",
    121: "Physical science, mathematics and engineering specialists",
    122: "Health professionals",
    123: "Teachers",
    124: "Finance and accounting specialists",
    125: "ICT specialists",
    131: "Science and engineering technicians",
    132: "Health technicians",
    134: "Legal, social, sports and cultural service technicians",
    135: "ICT technicians",
    141: "Office workers and secretaries",
    143: "Accounting and financial service operators",
    144: "Other administrative support staff",
    151: "Personal service workers",
    152: "Sellers",
    153: "Personal care workers",
    154: "Security service personnel",
    161: "Market-oriented farmers",
    163: "Subsistence farmers, fishers and hunters",
    171: "Skilled construction workers",
    172: "Metalworking workers",
    173: "Printing and precision instrument workers",
    174: "Electrical and electronics workers",
    175: "Food, woodworking and clothing industry workers",
    181: "Fixed plant and machine operators",
    182: "Assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    191: "Cleaning workers",
    192: "Unskilled agricultural and fisheries workers",
    193: "Unskilled construction and manufacturing workers",
    194: "Meal preparation assistants",
    195: "Street vendors and service providers"
}

CATEGORY_LABELS["Mother's occupation"] = OCCUPATION_LABELS
CATEGORY_LABELS["Father's occupation"] = OCCUPATION_LABELS