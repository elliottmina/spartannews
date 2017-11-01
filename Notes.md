# Spartan news

* for indexes, use URL as ID
	* remove ID parsers from meta modules?
* for indexes, use meta updated value with treshold
* run meta extractor on feed item
* add site to DB
* add image to DB
* Soupify everything
* remove htmldom (pip)
* switch to dateutil isntead of mail lib
* filter headlines separately from body
* limit description length

## Collector features
* Allow sources to define filters

### serving
* Fetch time slice
* Fetch all
* fetcher headers
* fetch sections
* fetch sources
* fetch keywords

### source type
* index (new site, HN)

### filters
* Blacklist authors
* Blacklist websites
* Blacklist keywords

## client features
* Display content
* Track last requested date so we can get what is fresh
* Record what items have been read
  * purge from server
  * add and configure sources
    * preview configuration effects

