# USPS_zip_to_city

This Python script takes a CSV file containing `city` and `state` values, queries the USPS ZIP Code Lookup API, and returns the corresponding 5-digit ZIP codes.  

Created with development assistance from ChatGPT. This tool is designated for free use and distribution.

---

## 📥 Input Format

The script expects a CSV file with two columns: `state` and `city`.  
**Column names must match exactly** (case-insensitive; leading/trailing spaces are stripped).

**Example:**

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
IA,HARPERS FERRY
IA,FRASER
...
```

## 📥 Output Format

The script creates a new CSV file with `_results` appended to the original filename.
Each ZIP code match is output as a separate row:

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
IA,HARPERS FERRY,52146
IA,HARPERS FERRY,52151
IA,FRASER,NOT FOUND
...
```

## 🔹 Notes:
* If a city has multiple ZIP codes, a row will be created for each ZIP.

* If USPS does not return a ZIP code for a city (e.g. unincorporated areas, CDPs, or unsupported names), NOT FOUND will be used as the ZIP code.

* If the API times out or returns an error, TIMEOUT or ERROR will appear in the zip_code column.

## 🚀 Usage
1. Run the script:

```bash
python usps_city_state_to_zip.py
```

2. When prompted, enter the name of your input file (e.g. input.csv).

3. The script will generate a new file (e.g. input_results.csv) in the same folder.

## 📄 License
This script is designated for free use and distribution under an open license. No attribution required.