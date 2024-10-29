# Data sources, IDs of Google Sheets where the core date is stored.
# Specific for swift.
five_day_ux_sheets = "1doFll5_L6URN8Chc9TODblvjiDHIh-5lDY1jhtIQtGc"
swift_sheets = "1wxigdxuKSzgut4jfOyefdmcySvZnrswbJHrwm7hzP2A"
C_swift_surveys = "1t5y2V7Z4e8IKJ2Na-hn9fzzRc4uBF3_iYa7q9ysNFIE"  #"1XLDv84qWWlXSpnAuQIjymascOdrBxpMQ"
swift_survey_config = "130h8-YX7X0mrUHU-7BgfV7_cg6PzUMazYscL79aZ0zo" #"1lOHCCuAsUoQ-O-eI76D987obZNlMGZ0IsTNPVcuw104"


# Shared with all deployments.
# Multiple content index for different types of content.
T_content = "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU"
N_onboarding_data = "1Y09xDjs3jHRDaNaNpAOLmCMa5N0bwcqHiyah3RgzCyA"
T_onboarding = "1Sl0Jl_N4cGQi2INmE_EnX_aYUMUrUB6cKbuWVPzirtY"
C_ltp_activities = "1xF-nqhYH-De5T08cIVHrxVBgfQ56mK-gu0RgNAXmTO4"
C_modules_teen = "1P17piJfRAL_Llknjh5vkbdVmjq3qT4A3rqFARy_749A"
C_modules_child = "1WXDv6kSkWG9-dio3vPFajA39JljudvhT5VUFTBD44wo"
C_modules_all_ages = "1zayzI3-mSGL3FO6jxCDoVJk3fi_ZqrhNEA73uHOmTuQ"
C_goal_checkin = "1osdl2DJsAO2rtm8Tqmk6uDl84SPoL5qaH4_1hlKuPIo"
N_safeguarding_data = "1cBq9sFH-MyGWJehfiAOvJTYTlCia02SFuYMOi7us9Po"
T_safeguarding = "1bWOyM5yShTTJSaxwqRCrjUzkwbp7DF6_nSF_96YcZ2c"
T_delivery = "1q6E2c4Bg_UvqTmhxAsTIQngwAtj0aFoqu8wsPHnqmaU"
N_delivery_data = "11ngXU85ezCin3zrurum2yzIJSWUP175p-6QvJ8svwVw"
T_menu = "1lIiFjZKS0eXzzo6XwDdqYv4e1A73WFCpWZg5ju-tCZE"
N_menu_data = "1hN9eK78o4ZpTm-36PciGSSGjt2xM9k-a6M2BLjAv20Q"
T_survey = "13aLV7tgTO6GNlI0zFG8gdq3BEl8PdX7kH5VEIXN5ssc"
T_trial = "1BifL5eSoEo3b7WS8KsrnXDYg3t36yYLqzr75Y8V9Vhw"

# "filename" is how it will be generally named in the pipeline.
#
# "crowdin_name" will be the name of the file that is produced to send to the
# translators.
#
# "tags" are used to identify flows to be process. Possible values for tag 1:
#   onboarding
#   dev_assess
#   ltp_activity
#   home_activity_checkin
#   module
#   goal_checkin
#   safeguarding
#   menu
#   delivery
#
# "split_no" is used to divide the file at the final step to get it to a manageable
# size that can be uploaded to RapidPro.
sources = [
    {
        "filename": "parenttext_all",
        "spreadsheet_ids": [
            N_onboarding_data,
            T_onboarding,
            C_ltp_activities,
            C_modules_all_ages,
            C_modules_teen,
            C_modules_child,
            C_goal_checkin,
            T_content,
            N_safeguarding_data,
            T_safeguarding,
            N_delivery_data,
            T_delivery,
            N_menu_data,
            T_menu,
            T_trial,
            five_day_ux_sheets,
            swift_sheets#,
            #C_swift_surveys,
            #swift_survey_config
        ],
        # "archive": "parenttext_all.zip",
        #"archive": "https://drive.usercontent.google.com/download?id=1V9fQZ9ZrzwRkQWBtlHJ1it0Fe3hdtHs2&export=download&authuser=0&confirm=t&uuid=f9d65ff1-b210-4b61-a030-cd4a231c22ca&at=APZUnTVzz2FLSi1riCmRjCFI5vCx:1696348063599",  # noqa: E501
        "crowdin_name": "navigation",
        "tags": [1,"module"],
        #"tags":[1,"ret"],
        #"tags": [1, "delivery",1 ,"menu",1,"onboarding",1,"safeguarding"],
        # "tags": [1,"goal_checkin",4,"course"],
       # "tags": [1,"module",1,"ltp_activity",1,"goal_checkin"],
        "split_no": 2
    },
]

# Data used when modifying expiration times.
special_expiration = "./edits/specific_expiration.json"
default_expiration = 1440

# Model that is used as part of the process when the data is extracted from sheets.
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the
# 3-letter code used in RapidPro, "code" is the 2 letter code used in CrowdIn.
# hausa is used in RapidPro instead of Xhosa because the language is not supported for Whatsapp templates
languages = [
    {"language": "afr", "code": "af"},
    {"language": "hau", "code": "xh"}
]

# Location where translations are stored, at the moment pointing to a locally cloned
# repo, should maybe be adapted so we can provide a link to an online repo.
translation_repo = "https://github.com/IDEMSInternational/plh-digital-content"
folder_within_repo = "translations/parenttext_5day_south_africa"

# In one of the latter stages we have the option to modify the quick replies:
# 1 - We may want to remove the quick replies and add them to message text and give
#     numerical prompts to allow basic phone users to use the app - for this use
#     reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the
#     message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat_whatsapp"

# This is the default phrase we want to add in if the quick replies are being moved to
# message text.
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick
# replies back in, if so we need to specify add_selectors as True
add_selectors = "yes"

# Words we always want to keep as full quick replies are specified in this file.
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the
# quick replies.
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is
# shorter than or equal to the length_threshold then the QR are to be left in place
# the node will not be changed.
# In places where the QR are too long. We will make the changes to make the QRs
# numbers and add the number references to the message text as example 1.
count_threshold = "3"
length_threshold = "18"

# Google Sheet ID containing AB testing data.
# Same for all deployments.
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s"
#  specific.
localisation_sheet_ID = "1C0lxVtiBw8kuJ9z4CAtW5BYesskYbQaSylqg6k3-ebw" 

# Google Sheet ID containing dict edits data.
# Same for all deployments.
eng_edits_sheet_ID = "1Ab8H_s26EuOiS4nZ6HGADjD4CZw55586LL66fl8tEWI"
# 5day ux SA specific specific.
transl_edits_sheet_ID = "1FYevYZZjTByCPA6dF0NgYvfYqtUNDzlz03tkQE_j5dM"

# Data used in safeguarding script.
#SG_flow_ID = "b83315a6-b25c-413a-9aa0-953bf60f223c"
#SG_flow_name = "safeguarding_wfr_interaction"

# Path to file containing translated safeguarding words.
SG_path = "./output/safeguarding_words.json"

# Names of redirect flows to be modified as part of safeguarding process.
redirect_flow_names = (
    '['
    '    "safeguarding_redirect_to_topic_all", '
    '    "safeguarding_redirect_to_topic_start", '
    '    "safeguarding_redirect_to_topic_trigger"'
    ']'
)

def create_config():
    return {
        "ab_testing_sheet_id": ab_testing_sheet_ID,
        "add_selectors": add_selectors,
        "count_threshold": count_threshold,
        "default_expiration": default_expiration,
        "eng_edits_sheet_id": eng_edits_sheet_ID,
        "folder_within_repo": folder_within_repo,
        "languages": languages,
        "length_threshold": length_threshold,
        "localisation_sheet_id": localisation_sheet_ID,
        "model": model,
        "qr_treatment": qr_treatment,
        "redirect_flow_names": redirect_flow_names,
        "select_phrases": select_phrases,
        "replace_phrases": "",
        #"sg_flow_id": SG_flow_ID,
        #"sg_flow_name": SG_flow_name,
        "sg_path": SG_path,
        "sg_sources": [
            {
               "key": "hau",
               "path": "excel_files/safeguarding xhosa.xlsx",
            },
            {
               "key": "afr",
               "path": "excel_files/safeguarding afr.xlsx",
            }
        ],
        "sources": sources,
        "special_expiration": special_expiration,
        "special_words": special_words,
        "translation_repo": translation_repo,
        "transl_edits_sheet_id": transl_edits_sheet_ID,
    }
