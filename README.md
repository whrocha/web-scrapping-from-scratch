# TECHNICAL CHALLENGE

## The Challenge

We want to build a reference map on a website and understand which will be the most viewed by users when browsing.

For this we will make a crawler to help us get this information. Then, with the data obtained, we will train a model against historical data.

A crawler is a tool that allows us to enter a link and obtain information about it, for example, if the link is active or not.

In the case of this exercise, this software will allow us to evaluate the HTML response, parse it and obtain the links that are referenced within it.

In addition, this crawler will re-execute this procedure for each link it finds after this process, putting together a map like the following:

![picture 1](images/854731ea7f96e0a8c518ddd5f3c5e5ce7077b277a76d97dbedf0420461bb99da.png)  

Our challenge will be to count the number of references (“appearences”) that we find of a link from other sources.

In the example case, the link https://www.google.com/doodles/ it has 2 "appearences", while https://google.com/ has 0 "appearences" (since no other page is referencing it).

Understanding that the growth of this process is exponential (and potentially infinite), at the beginning of the process will be defined a maximum degree of depth N, which we can reach. 

That is, we will stop the process when reaching the referenced link more than N steps after the initial link.

### First Part: Generation of Features

In the first instance, the objective is to build a project that has the ability to crawl the different links from a base set and persist, for each link, **how many different references (appearences)** of external pages were found. 

The maximum level, N, of depth of the crawler is defined at the beginning of the process:

![picture 2](images/dab11824e73f82c0df9dd00063da1d86cbddf49374235969b7007b85bd3c7b01.png)  

In addition, this information can be enriched for each link with the information that it deems necessary to store.

Once the map is finished, for each link of the base set it is required to build a vector with at least 10 numerical characteristics based on said map, using the enrichment information previously obtained.

An example of a characteristic is "the number of characters in the link." 

These characteristics should only depend on information that can be obtained from the link -to be able to dynamically load them later-.

This vector must be saved in a new storage instance (table, document, file, etc):

![picture 3](images/63819b93d826e3fd065f676bf3d33de0569b815e77a9606e1fa01212209359c4.png)  

Each of these vectors must be persisted in the type of persistence that the user defines -unless it is forced by the conditions of the exercise-.

Finally, a REST API will be built such that it uses the defined storage and allows **obtaining the vector of features associated with a link**:

- If the link is in the database, answer the precalculated vector.
- If the link is not found in the database, the values corresponding to the vector must be calculated, inserted into the database and then returned. This vector will not have the number of external references calculated.

## My Achievements

I build the crawler from scratch, this crawler can be access in [crawler.py](./crawler.py) file.

**There are some warnings about this crawler script.**

- The crawler script is slow and supports no parallelism. As can be seen from the timestamps, it takes about one second to crawl each URL. Each time the crawler makes a request it waits for the request to be resolved and no work is done in between.
- There is no retry mechanism, the URL queue is not a real queue and not very efficient with a high number of URLs.
- The link extraction logic doesn’t support standardizing URLs by removing URL query string parameters, doesn’t handle URLs starting with #, doesn’t support filtering URLs by domain or filtering out requests to static files.
- The crawler doesn’t identify itself and ignores the robots.txt file.

All of this limitation could be solved by using Scrapy, I have an example of crawler using Scrapy that can be access [here](https://github.com/whrocha/web-scrapping-challenge).

I don't built the REST API yet, but I created a Jupyter Notebook to analyse extracted links and to create Vectors.

Jupyter Notebook can be access in [vector-analytics.ipynb](./vector-analytics.ipynb).

### Run locally

To run this project locally.

**Create virtual environment**

```
virtualenv -p python3.8 venv
```

**Active Virtual Environment**

```
source venv/bin/activate
```

**Install necessary libs**

```
pip install -r requirements.txt
```

**Run crawler**

```
python crawler.py
```

The final output should be

```
2021-05-16 22:31:53,106 INFO:Crawling: https://scrapethissite.com/
2021-05-16 22:31:53,973 INFO:Crawling: https://scrapethissite.com/
2021-05-16 22:31:54,708 INFO:Crawling: https://scrapethissite.com/pages/
2021-05-16 22:31:55,581 INFO:Crawling: https://scrapethissite.com/lessons/
2021-05-16 22:31:57,456 INFO:Crawling: https://scrapethissite.com/faq/
2021-05-16 22:31:58,287 INFO:Crawling: https://scrapethissite.com/login/
2021-05-16 22:31:59,119 INFO:Crawling: https://scrapethissite.com/pages/
2021-05-16 22:31:59,948 INFO:Crawling: https://scrapethissite.com/pages/simple/
2021-05-16 22:32:02,796 INFO:Crawling: https://scrapethissite.com/pages/forms/
2021-05-16 22:32:04,158 INFO:Crawling: https://scrapethissite.com/pages/ajax-javascript/
2021-05-16 22:32:05,579 INFO:Crawling: https://scrapethissite.com/pages/frames/
2021-05-16 22:32:06,629 INFO:Crawling: https://scrapethissite.com/pages/advanced/
2021-05-16 22:32:07,594 INFO:Crawling: https://scrapethissite.com/lessons/
2021-05-16 22:32:09,631 INFO:Crawling: https://gum.co/oLpqb?wanted=true
2021-05-16 22:32:11,738 INFO:Crawling: https://gum.co/oLpqb/LASTCHANCE?wanted=true
2021-05-16 22:32:13,434 INFO:Crawling: https://scrapethissite.com/faq/
2021-05-16 22:32:14,297 INFO:Crawling: https://scrapethissite.com/robots.txt
2021-05-16 22:32:14,781 INFO:Crawling: https://scrapethissite.com/login/
2021-05-16 22:32:15,688 INFO:Crawling: https://peric.github.io/GetCountries/
2021-05-16 22:32:16,347 INFO:Crawling: http://www.opensourcesports.com/hockey/
```

Check items file in [items.jl](./items.jl)  

**Checking Results**

Go to [Jupyter Notebook](./vector-analytics.ipynb) to see the Results.

### TO-DO List

- Build the challenge REST API.