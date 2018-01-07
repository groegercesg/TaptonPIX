# TaptonPIX

This is a program for automated data collection using Pixelman, MX-10 and the TAPAS api; as well as some other stuff I guess.

## Getting Started

[//]: # (These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.)

### Prerequisites

[//]: # (What things you need to install the software and how to install them```Give examples```)
**Pixelman** - *Particulate Capturing* - [Download Location](http://aladdin.utef.cvut.cz/ofat/others/Pixelman/Pixelman_download.html) - Download from here as only this version solely works with the script

**Python** - *To Run the Script* - [Download Location](http://docs.python-guide.org/en/latest/starting/install3/win/#install3-windows) - Follow the instructions in the Installing Section.

**Requests** - *Used for the Tapas api* - [Download Location](http://docs.python-requests.org/en/master/user/install/#install) - Install using `pip`, instructions found below.



### Installing

#### Windows

1. Install [Pixelman](http://aladdin.utef.cvut.cz/ofat/others/Pixelman/Pixelman_download.html),  and verify it's running with the sensor attached.

2. Install the latest version of [Python](https://www.python.org/downloads/), with all the options. Especially the path variable. **If** this option doesn't arrive the first time round, then re-run the installer and select _Modify_ before selecting _pip_ in the Optional Features section and _Environment Variables_ in Advanced Options.

3. Then run `Win + R` and type `cmd` to open the command line. From there type:

> python -m pip install -U pip

  - To check that pip was correctly installed

4. Then use `pip` to install to install Pipenv:

> pip install --user pipenv

5. Then navigate to the TaptonPIX directory, using `cd` before typing:

> pipenv install requests

  - If this doesn't work then see below

6. Then you should ready to go.

7. In the Scenario that step 5 didn't work, them run this:

`py -m site --user-site`

  - The replace the section at the end, "site-packages" with "Scripts"
  - Then insert it into your Environment Variables [PATH](https://msdn.microsoft.com/en-us/library/windows/desktop/bb776899(v=vs.85).aspx)
  - Also you probably should restart after this, so do do that.


#### Mac OS X

This won't happen, ever.

#### Linux

Coming...


[//]: # (A step by step series of examples that tell you have to get a development env runningSay what the step will be```Give the example```And repeat```until finished```End with an example of getting some data out of the system or using it for a little demo)

## Built With

### Python Libraries

* [ZipFile](https://docs.python.org/2/library/zipfile.html) - For Zipping the Particle Data
* [OS](https://docs.python.org/2/tutorial/stdlib.html) - For properly interacting with the Operating System
* [Requests](http://docs.python-requests.org/en/master/) - For interacting with the TAPAS api, it's simply a requirement

## Contributing

[//]: # (Please read CONTRIBUTING.mdhttps://gist.github.com/PurpleBooth/b24679402957c63ec426 for details on our code of conduct, and the process for submitting pull requests to us.)

This might be filled in soon, but at the moment (as we're in development stage) we're not currently accepting and contributions/forks/pull requests.

## Project Progress

**Functionality Still Required:**
* Modification of Pixelman API options
* Storing of Pixelman options in json (**?**) for portability
* ~~Actually finish the main program functionality, so it works!~~
* Then complete UsrOpt2 function functionality
* Finish Mark Down install guide for Windows
* Finish Mark Down install guide for Linux
* ~~Make sure it complies with Pep 8~~
* Test program using sensor

**Functionality Desired:**
* Alterting system to notify if file stops running
* Consider finding some way to not miss gaps in the data collection, as I'm pretty sure there are gaps in the recording.
* Make it easier to run
* Running on Raspberry Pi Zero (w?)/ something light and ARM-based potentially (**?**)
* Remote website data thing, can't think of the words for it, but basically a control/data panel - using Grafana?

**Functionality That Will Never Happen But Is _Nice_ To Dream Of:**
* *The Cloud...*
* ^ No, no one wants that.




[//]: # (We use SemVerhttp://semver.org/ for versioning. For the versions available, see the tags on this repositoryhttps://github.com/your/project/tags.)

## Authors

* **Callum** - *Initial work* - [Groegercesg](https://www.c-e.sg/)

[//]: # (See also the list of contributors https://github.com/your/project/contributors who participated in this project.)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/groegercesg/TaptonPIX/blob/master/LICENSE) file for details

## Acknowledgments

* [IRIS](http://www.researchinschools.org/) - The Institute of Research In Schools
* [MX-10](http://www.particlecamera.com/index.php) - The MX-10 Digital Particle Camera
* [IEAP](http://aladdin.utef.cvut.cz/ofat/others/Pixelman/index.html) - Pixelman software developed by the Czech Technical University in Prague
