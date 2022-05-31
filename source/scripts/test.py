import external_features as trdfe
import pandas as pd 
import urllib
import tldextract

key = 'Add your OPR API key here'

import signal

def get_domain(url):
    o = urllib.parse.urlsplit(url)
    return o.hostname, tldextract.extract(url).domain, o.path

if __name__=="__main__":
    url = "https://portal.ifrn.edu.br/campus/natalzonanorte/noticias/ifrn-divulga-1-196-vagas-para-cursos-tecnicos-subsequentes-ainda-em-2022"
    hostname, domain, path = get_domain(url)
    extracted_domain = tldextract.extract(url)
    domain = extracted_domain.domain+'.'+extracted_domain.suffix
    row = {
        "whois_registered_domain": trdfe.whois_registered_domain(domain),
        "domain_registration_length": trdfe.domain_registration_length(domain),
        "domain_age": trdfe.domain_age(domain),
        "web_traffic": trdfe.web_traffic(url),
        "dns_record": trdfe.dns_record(domain),
        "google_index": trdfe.google_index(url)#,
        #"page_rank": trdfe.page_rank(key,domain)
    }
    print(row)