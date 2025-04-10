# USPS_zip_to_city
This is a python script that uses csv files with city/state to obtain the 5-digit postcode from the USPS API. Created with development assistance from ChatGPT. This tool is designated for free use and distribution.


Ensure that the csv file to be used as input is in the following format:

```csv
state,city
IA,ADAIR
IA,BRIDGEWATER
IA,CASEY
IA,FONTANELLE
IA,GREENFIELD
IA,ORIENT
IA,STUART
IA,UNINCORPORATED
IA,CARBON
IA,CORNING
IA,LENOX
IA,NODAWAY
IA,PRESCOTT
IA,UNINCORPORATED
IA,HARPERS FERRY
IA,FRASER
...
```

The output file will be named the same as the input file, with "_results" appended to it. It will be in the following format:

```csv
state,city,zip_code
IA,ADAIR,50002
IA,BRIDGEWATER,50837
IA,CASEY,50048
IA,FONTANELLE,50846
IA,GREENFIELD,50849
IA,ORIENT,50858
IA,STUART,50250
IA,UNINCORPORATED,NOT FOUND
IA,CARBON,50839
IA,CORNING,50841
IA,LENOX,50851
IA,NODAWAY,50857
IA,PRESCOTT,50859
IA,UNINCORPORATED,NOT FOUND
IA,HARPERS FERRY,52146
IA,HARPERS FERRY,52151
IA,FRASER,NOT FOUND
...
```

* Notice that for cities that span more than one zip code, one line will be created for each zip code.
   * Ex: IA,HARPER'S FERRY
* Notice that for census-designated-places, or other such towns/villages/etc, that do not have a zip code according to USPS, the zip code will be listed as NOT FOUND.
    * Ex: IA,FRASER