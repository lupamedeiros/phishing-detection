# phishing-detection

This project is a machine learning experiment to detect phishing websites by url.
The dataset is available [here](https://data.mendeley.com/datasets/c2gw7fy2j4/3).

## Setup up the environment

This project is developed using Anaconda for manage the environment. To setup your environment follow the steps:

    conda env create --file environment.yml
    conda activate phishing-detection
    pip install -r requirements.txt

To exit the envoriment:

    conda deactivate

## From Data to Model

The model's creation is developed according to the workflow model presented by Ivanovitch.

![Ivanovitch's Model](images/ivanovicth_workflow.png)

Each task is developed in a Jupyter Notebook file. The files are numbered according to the workflouw sequence. They're avaliable at the directory source/creating_model.

* **01_fetch_data.ipynb:** In this notebook we read the data from a CSV file and upload it to WandB.
* **02_eda.ipynb:** In this notebook we perform an exploratory analysis of the data. From here is produced [report.html](./source/creating_model/report.html)
* **03_preprocessing.ipynb:** Fix missing or incorrect data on dataset.
* **04_check_data.ipynb:** Perform unitary tests over the dataset in order to identify problems like missing data, duplicated samples, wrong data type, etc.
* **05_data_segregation.ipynb:** Splits the dataset into two artifacts. The train subset and the test subset.
* **06_train.ipynb:** Here we create the pipeline to deliver the data to the model, train the model and valitade it.
* **07_test.ipynb:** Usesthe test subset to validate the inference model.

## The API

This stage of the project was based on Ivanovitch's [colab2mlops repo](https://github.com/ivanovitchm/colab2mlops).

![Ivanovitch's Deploy](./images/deploy.png)

The file [main.py](./source/api/main.py) implements an API using FastAPI. To run it:

    uvircorn source.api.main:app --reload

The file [test_main.py](./source/api/test_main.py) contains unit test to API. It is used to validate the projects when it is updated.

This file is executed every time we update the main branch.

This project is deployed as an App in Heroku. The deployment is configured on a CI/CD patern. The file [Profile](./Procfile) containd the instruction to Heroku run the app.