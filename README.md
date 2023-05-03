# Vacation Itinerary Planner


# Project’s Functionality and Technologies:
* This project is a backend machine learning system implemented in python, that helps users to search and plan their movement in choicy locations during vacations/visits. Interactions with this would be based on a terminal‘s command line interface.
* For the technologies, it makes use of Google’s Places API, Google Directions API and Google’s Geocoding API to enable access to the millions of locations, directions and addresses google uses, for itinerary planning. An unsupervised Machine Learning (ML) model (K-means clustering) has been trained from web-scraped data about places visited and reviewed by tons of users (at least a few tens of thousands of such reviews) on Google reviews.
* 12 different destination categories were selected for the final ML training in the following order: movie theaters, art galleries, clothing stores, universities, bars, shopping malls, museums, stadia, zoos, point of interest, tourist attraction and park.
* These categories were selected from the numerous classifications of locations Google places API has in its documentation, and selection choices were made based on the frequency of reviewed data scraped from the web.


## Automated Testing Infrastructure:
**“GitHub Actions”** was used for the implementation of automated testing of code.
This includes the implementation of unit and integration tests, and the generation of a test coverage report.
To implement this:
1.	A YAML (.yml) file was created to implement testing on GitHub actions. It is run of the latest version of windows with python 3.9 version for the setup. 
2.	This workflow is triggered for any push on the main branch in the GitHub repository and the **“.yml”** file is saved in a **“.github\workflows”** folder in the local repository.
3.	Thereafter, a key dependency, pip, is installed or upgraded if a newer version is available, as it would be useful for installing other relevant python libraries.
4.	The python application for this project relies on several external modules that are not installed by default in python, hence they are installed. These include googlemaps, scikit-learn, pandas and coverage which are all installed with pip. Googlemaps module is used to interface with relevant google APIs for getting information about locations, surrounding venues and directions. Whereas pandas and scikit-learn are scientific libraries which were used in creating the machine learning model that is used in recommending location categories to new users based on their preferences.
5.	Coverage is eventually used for running all unit/integration tests in the testing file, and thereafter generating a coverage report.
6.	Whenever changes to code are pushed to the main branch, this “test” job is automatically triggered and the process flows sequentially as stated in steps 2 – 5. These can be seen on the GitHub repository in the **“Actions”** tab each time code changes are pushed.
7.	The contents of the .yml file for the automated testing process described above is as shown below:

```
name: Python App CI/CD with Docker and Testing

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: windows-latest

    steps:
      - name: Checkout the repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          
      - name: Run tests
        run: |
          pip install googlemaps scikit-learn pandas coverage
          coverage run TestRecommender.py 
          
      - name: Coverage report
        run: |
          coverage report -m
```


## Build and Deploy Infrastructure:
**Docker** was used for automated building and deployment of my code infrastructure.
Docker Hub was the registry used to store the docker images that were created which was integrated with Github actions and is triggered immediately after the automated testing for code changes to the main branch.
To implement this:
1.	A **Dockerfile** was created for the implementation of the building of the main.py file which integrates the various methods from the Recommender.py file for the application.
2.	The Dockerfile contains a sequence of steps that uses same python version 3.9 and adds the main.py file and copies any other relevant file to the root folder of the image.
3.	Thereafter, relevant libraries similar to those used in the testing file for running the application are installed. These include googlemaps, scikit-learn and pandas. Thereafter the *“CMD”* command runs the main.py python file once the docker container is started.
4.	Secret variables were created with credentials for my Docker Hub login details from the **Settings** Tab of my Github repository. Here, two repository *“secrets”* were added to the **“Actions”** sub-category of **“Secrets and Variables”**; one for docker username and the other for password.
5.	Afterwards the docker build and deployment process was included in the YAML file as a separate job that depends on and runs after the automated testing process is successfully completed.
6.	This was configured to run on the latest available version of ubuntu and first logins to my Docker Hub account with the Github secret variables earlier created. Afterwards, it sets up Docker **Buildx** which is Github required to successfully execute, before building the image and pushing (whose tag I assigned in the file) to a Docker repository I already made.
7.	The concluding part of the YAML file (which follows from the automated testing job) is as shown below:

```
  build-and-deploy:
    runs-on: ubuntu-latest
    
    needs: test

    steps:
      - name: Checkout the repository
        uses: actions/checkout@v2
      
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v1
        
      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Build and push the Docker image
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: johansono/vacation-planner:v1.0.1
```

#### Consequently, once code is pushed to the main branch on Github, the testing process executes first and then the docker build and deployment, all in an automated sequence. This pushed docker image can be subsequently pulled by anyone and run locally.
