import content_features as ctnfe
import url_features as urlfe
import external_features as trdfe
import feature_extractor as featex
import ml_models as models
import pandas as pd 
import urllib.parse
import tldextract
import requests
import json
import csv
import os
import re


from pandas2arff import pandas2arff
from urllib.parse import urlparse
from bs4 import BeautifulSoup

key = 'Add your OPR API key here'

import signal

if __name__=="__main__":
    url = "https://portal.ifrn.edu.br/campus/natalzonanorte/noticias/ifrn-divulga-1-196-vagas-para-cursos-tecnicos-subsequentes-ainda-em-2022"
    row = featex.extract_features(url, "?")
    print(row)