# TaptonPIX

This is a program for automated data collection using Pixelman, MX-10 and the TAPAS api; as well as some other stuff I guess.

## Getting Started

[//]: # (These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.)

### Prerequisites

[//]: # (What things you need to install the software and how to install them```Give examples```)
**Pixelman** - *Particulate Capturing* - [Download Location](http://aladdin.utef.cvut.cz/ofat/others/Pixelman/Pixelman_download.html) - Download from here as only this version solely works with the script
**Python** - *To Run the Script* - [Download Location](https://www.python.org/downloads/release/python-2713/) - It may work with newer versions, but I haven't tested it with anything newer


### Installing

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

Functionality Still Required:
* Modification of Pixelman API options
* Storing of Pixelman options in json (**?**) for portability
* Actually finish the program, so it works!
* Then complete UsrOpt2 function functionality

Functionality Desired:
* Alterting system to notify if file stops running
* Consider finding some way to not miss gaps in the data collection, as I'm pretty sure there are gaps in the recording.
* Make it easier to run
* Running on Raspberry Pi Zero (w?)/ something light and ARM-based potentially (**?**)
* Remote website data thing, can't think of the words for it, but basically a control/data panel - using Grafana?

Functionality That Will Never Happen But Is Nice To Dream Of:
* *The Cloud...*
* ^ No, no one wants that.




[//]: # (We use SemVerhttp://semver.org/ for versioning. For the versions available, see the tags on this repositoryhttps://github.com/your/project/tags.)

## Authors

* **Callum** - *Initial work* - [Groegercesg](https://www.c-e.sg/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/groegercesg/TaptonPIX/blob/master/LICENSE) file for details

## Acknowledgments

* [IRIS](http://www.researchinschools.org/) - The Institute of Research In Schools
