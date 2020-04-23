This repository is a collection of scripts for practicing Natural Language Processing. Each directory is a separate project.

## basic-pipeline

Follows instruction at [Natural Language Processing is Fun!](https://medium.com/@ageitgey/natural-language-processing-is-fun-9a0bff37854e), contains code for basic English NLP pipeline.

We will give this code some paragraphs about an object (for example: London, Eiffel Tower). It will tell us what is its understanding about that object.

### Installation

Install spaCy

```shell
$ pip3 install --upgrade spacy
```

Download the large English model for spaCy, which is 828MB in April 2020.

```shell
$ python3 -m spacy download en_core_web_lg
```

Install textacy which will also be useful

```shell
$ pip3 install --upgrade textacy
```

Change directory

```shell
$ cd basic-pipeline
```

### Extract entities and entity types

```shell
$ python3 extract_entities.py london.txt
London (GPE)
England (GPE)
the United Kingdom (GPE)
the River Thames (LOC)
the south east (LOC)
Great Britain (GPE)
London (GPE)
two millennia (DATE)
Romans (NORP)
Londinium (ORG)

$ python3 extract_entities.py eiffel_tower.txt
The Eiffel Tower (FAC)
the Champ de Mars (FAC)
Paris (GPE)
France (GPE)
Gustave Eiffel (PERSON)
1887 to 1889 (DATE)
1889 (DATE)
World's Fair (EVENT)
France (GPE)
France (GPE)
one (CARDINAL)
The Eiffel Tower (FAC)
6.91 million (CARDINAL)
2015 (DATE)
324 metres (QUANTITY)
1,063 ft) (QUANTITY)
Paris (GPE)
125 metres (QUANTITY)
410 ft (QUANTITY)
the Eiffel Tower (FAC)
the Washington Monument (FAC)
41 years (DATE)
the Chrysler Building (FAC)
New York City (GPE)
1930 (DATE)
first (ORDINAL)
300 metres (QUANTITY)
1957 (DATE)
Chrysler (ORG)
5.2 metres (QUANTITY)
17 ft (QUANTITY)
the Eiffel Tower (FAC)
second (ORDINAL)
France (GPE)
the Millau Viaduct (FAC)
```

You can look up what each of those [entity codes means here](https://spacy.io/usage/linguistic-features#entity-types).

### Detect and remove names

```shell
$ python3 scrub.py names.txt
In 1950, [REDACTED] published his famous article "Computing Machinery and Intelligence". In 1957, [REDACTED] Syntactic Structures revolutionized Linguistics with 'universal grammar', a rule based system of syntactic structures.

$ python3 scrub.py bill_gates.txt
[REDACTED] (born October 28, 1955) is an American business magnate, software developer, investor, and philanthropist. He is best known as the co-founder of Microsoft Corporation.[2][3] During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president and chief software architect, while also being the largest individual shareholder until May 2014. He is one of the best-known entrepreneurs and pioneers of the microcomputer revolution of the 1970s and 1980s.

Born and raised in Seattle, Washington, Gates co-founded Microsoft with childhood friend [REDACTED] in 1975, in Albuquerque, New Mexico; it went on to become the world's largest personal computer software company.[4][a] [REDACTED] led the company as chairman and CEO until stepping down as CEO in January 2000, but he remained chairman and became chief software architect.[7] During the late 1990s, [REDACTED] had been criticized for his business tactics, which have been considered anti-competitive. This opinion has been upheld by numerous court rulings.[8] In June 2006, [REDACTED] announced that he would be transitioning to a part-time role at Microsoft and full-time work at the Bill & Melinda Gates Foundation, the private charitable foundation that he and his wife, [REDACTED] , established in 2000.[9] He gradually transferred his duties to [REDACTED] and [REDACTED] Mundie.[10] He stepped down as chairman of Microsoft in February 2014 and assumed a new post as technology adviser to support the newly appointed CEO [REDACTED]

Since 1987, he has been included in the Forbes list of the world's wealthiest people.[12][13] From 1995 to 2017, he held the [REDACTED] title of the richest person in the world all but four of those years.[1] In October 2017, he was surpassed by Amazon founder and CEO [REDACTED] , who had an estimated net worth of US$90.6 billion compared to [REDACTED] ' net worth of US$89.9 billion at the time.[14] As of November 2019, [REDACTED] had an estimated net worth of US$107.1 billion, making him the second-wealthiest person in the world, behind Bezos.[b]
```

### Extract facts

```shell
$ python3 extract_facts.py london.txt London
Here are the things I know about London:
 - the capital and most populous city of England and the United Kingdom
 - a major settlement for two millennia

$ python3 extract_facts.py eiffel_tower.txt "Eiffel Tower"
Here are the things I know about Eiffel Tower:
 - a wrought-iron lattice tower on the Champ de Mars in Paris, France
 - the most-visited paid monument in the world
 - the second tallest free-standing structure in France after the Millau Viaduct.
```

### Extract frequently-mentioned noun chunks

```shell
$ python3 extract_noun_chunks.py london_wiki.txt
river thames
bbc history
regent's park
original (pdf
roman london
30 april
anglo-saxon england
south bank
city centre
king's college london
imperial college london
cable car
13 may
25 may
national statistics
european city
(press release
other city
east london
met office
2011 census
office space
west london
"2011 census
royal exchange
median age
26 april
6 july
west end
20 june
national gallery
canary wharf
natural history museum
royal albert hall
official website
south kensington
main article
london assembly
greater london's population
london evening standard
london's population
international olympic committee
united kingdom
central london
trafalgar square
29 august
london luton airport
new york
" (pdf
london business school
local government
greater london authority
royal opera house
inner london
primrose hill
daily telegraph
3 april
hampstead heath
27 april
st paul's cathedral
london borough
oxford street
royal parks
main articles
thames barrier
new york city
epping forest
18 may
london underground
local authorities
greater london
national portrait gallery
key statistics
1 may
major centre
second world war
city status
british library
royal college
hyde park
london government
25 june
bbc news
london eye
sadiq khan
square kilometre
tower hamlets
great fire
24 january
29 april
6 december
tate modern
financial times
outer london
east end
ethnic groups
london boroughs
british museum
northern ireland
11 may
new york times
london school
population density
science museum
english civil war
south london
27 may
open spaces
25 april
wayback machine
```

## text-classification

Follows instruction at [Text Classification is Your New Secret Weapon](https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788), contains code for classifying texts into: like/dislike, positive/negative, rate 1 to 5 stars... about a subject.

### Install fastText and 

Follow [these instructions](https://fasttext.cc/docs/en/support.html).

### Download Yelp data

Download [Yelp research dataset of 4.7 million user reviews](https://www.yelp.com/dataset/download), it is a 4.5GB compressed, 9.8GB uncompressed JSON file. Note that you cannot use Yelp data for commercial purposes.
