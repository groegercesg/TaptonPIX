# Here is where I import all of the modules I require
import zipfile
import os
import requests
# Beginning Introduction of the program
print("Welcome to TaptonPIX Automated Data Packaging Program")
# The location of the question, this will decide what the user wants to do
# either run with defaults, edit those defaults or view information
#  about the program
user_option = int(input(
                        "What do you wish to do today? \n Type 1 to run  "
                        "with defaults \n Type 2 to edit defaults"
                        "\n Type 3 to view information \n"))

# Functions that will store commands to go with the user's response
# Number 1 does the defaults, a simple loading from file of the basic commands


def UsrOpt1():
    print("UsrOpt1")
    ###################
    # Data Collection #
    ###################
    # File Collection number count
    count = int(000)
    # number cycle iteration thingy
    for count in range(999):

        # This is the calling of the Pixelman API - directly,
        # following from a helpful guide on:
        # http://aladdin.utef.cvut.cz
        devID = 0  # Device number, this being the number, in array style
        # of sensors plugged into the computer
        acqTime = 1  # Time between Acquisitions, measured in seconds
        acqCount = 10  # Number of Acquisition
        for i in range(10):
            tp = 'TPIX-'
            name = tp + str(count)
            dir_name = os.path.join(
                                    'C:\\Users\\XXX\\Documents'
                                    '\\TaptonPIX\\TPIX', name)
            fileName = os.path.join(dir_name, "DatPIX-" + str(i) + ".txt")
            # Some automatic concatenation going on here, might not
            # entirely work with the Pixelman API
            pixelman.mpxCtrlPerformFrameAcq(devID, acqCount, acqTime,
                                            pixelman.FSAVE_ASCII |
                                            pixelman.FSAVE_SPARSEX, fileName)
    ##################
    # Data Packaging #
    ##################
        # This is the line that grabs the data from a certain location
        # and packes them up
        # Zip Name
        # zname = 'TPIX-' + count + '.zip'
        # Joining the two directory components together,
        # the location and the File Name
        dir_name_z = os.path.join(dir_name + ".zip")
        Imaginary_zip = zipfile.ZipFile(dir_name_z, 'w')

        # Change it here as well
        for folder, subfolders, files in os.walk(dir_name):

            for file in files:
                if file.endswith('.txt'):
                    # Some automatic concatenation going on here, might not
                    # fully work with zip writing so just preparing future me
                    Imaginary_zip.write(os.path.join(folder, file), file,
                                        compress_type=zipfile.ZIP_DEFLATED)

        Imaginary_zip.close()

    ################
    # Data Sending #
    ################

    # Demo borrowed from: https://github.com/InstituteForResearchInSchools/
    # tapas-api-demos/blob/master/uploading-zip-file.py - By Will Furnell

        file_path = dir_name_z  # The path to the ZIP file you want to upload.
        # Make sure it exists!

        # Use this when uploading to TAPAS, not the local development site
        API_BASE_URL = "https://tapas.researchinschools.org/"

        # Need to change this
        headers = {
            'Authorization': 'Token 5e865d620e7cc43ddb3b7ff8e3ee5728f27b258e',
            # You MUST include the 'Token' part here before the API token
        }

        # Fill out the payload fields,
        payload = {
            'name': 'TaptonPIX-' + count,  # Name of the upload,
            # can be whatever you like, but make it meaningful
            'project': '1',  # You MUST specify a project in ID form here!
                             # You can check all project IDs via the API too :)
            # These aren't super necessary but I guess it they can be put in
            # 'latitude': '1',  # Latitude of where data was taken,
            # needed if you choose RAY as a project
            # 'longitude': '1',  # Longitude of where data was taken,
            # needed if you choose RAY as a project
        }

        # The / at the end of upload is VERY important here!
        # You'll get an Internal Server Error without it.
        # .... I speak from experience
        r = requests.post(API_BASE_URL + "/api/v1/upload/",
                          files={"zipfile": open(file_path, 'rb')},
                          data=payload, headers=headers)

        print(r.text)


# Number 2 allows the user to edit any of the options necessary;
# <insert options here>
def UsrOpt2():
    print(
          "UsrOpt2 \n"
          "Not currently functional, maybe in a bit! \n"
          "Check the GitHub for updates")
    # break


# Number 3 allows the user to view information about the program
def UsrOpt3():
    print(
          "\n Here is some Useful Program Information"
          "\n \n Creator Name : Callum \n Creator Contact : groeger@c-e.sg \n"
          " Project Github : https://github.com/groegercesg/TaptonPIX \n"
          " Project Status : Non-Functional \n "
          "For all other enquiries please visit : groeger@c-e.sg \n"
          " Or see the GitHub page!")

# This is some simple validation for the user input to make sure that they
# only enter numbers, within the range I desire
try:
    if user_option == 1 or user_option == 2 or user_option == 3:
        print("Input Acceptable \n Proceding...")
    else:
        raise ValueError
except ValueError:
    print("Error \n Only enter the numbers listed")

# This runs the UsrOpt1 function when user_option is equal to 1'
# it loops it to continue the process
while user_option == 1:
    print("Proceding with User Option 1")
    UsrOpt1()
    # break

# This runs the UsrOpt2 function when user_option is equal to 2,
# it loops it to continue the process
while user_option == 2:
    print("Proceding with User Option 2")
    UsrOpt2()
    # Comment this out when the script is working, ok?
    break

# This runs the UsrOpt3 function when user_option is equal to 3.
while user_option == 3:
    print("Proceding with User Option 3")
    UsrOpt3()
    break
