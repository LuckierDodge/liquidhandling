# liquidhandling

This repository contains the source code for a python library developed to allow programmatic control of the Hudson Robotics systems installed in Argonne National Laboratory's Secure BIO Lab.

This library is currently in **active development**. As such, there are no guarantess of API stability, feature completeness, or test coverage. Any code generated by this library should be considered untested, and when run on the physical lab automation systems should be carefully monitored.

## Documentation

Documentation for the interfaces contained in this library can be found in the `docs` directory. In addition, example code is available under `example`.

## Development

### Installing For Development/Testing

1. Install [Python 3.8.5+](https://www.python.org/downloads/), making sure to include pip in the install
1. Git clone this repository: `git clone https://xgitlab.cels.anl.gov/rarvind/liquidhandling.git`
1. Run `pip install -r requirements.txt` in the repository root
1. Run `pip install -e .` in the repository root
1. Use python to run the `example/solosoft/solo_soft_example.py` and open the `example.hso` file it generates in SoloSoft to test that your setup is functioning properly.

### Tests

* Run all: `python -m pytest ./test` in the repo's root directory (or with the last argument adjusted to point to the `test` directory)

### Formatting the Code

To automatically format the code for style and readability, run `black .` in the repo's root directory. This keeps all python code stylistically consistent.

### Recommended Visual Studio Code Extensions

* Better Comments by Aaron Bond
* GitLens by Eric Amodio
* Pylance by Microsoft
* Python by Microsoft
* Visual Studio IntelliCode by Microsoft