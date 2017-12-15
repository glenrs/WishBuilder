<h1><center>BiomarkerBenchmark_GSE67784</center></h1>
<h2><center> Status: In Progress </center></h2>


### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 100 characters

&#9989;	description.md contains a description.

#### Results: PASS
---
### Running Install . . .

Executing install.sh: Success

#### Results: PASS
---

### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

*Running user code . . .*

Executing download.sh: Success

Executing parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (8; min: 8)

&#10060;	Row 6 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 7 of "test_metadata.tsv" should contain exactly three columns.

&#10060;	Row 8 of "test_metadata.tsv" should contain exactly three columns.

&#9989;	test_metadata.tsv contains enough unique samples to test

&#10060;	"GSM1656050" does not have enough features to test (min: 2)

&#9989;	test_metadata.tsv contains enough test cases (8; min: 8)

#### Results: **<font color="red">FAIL</font>**
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	ENSG00000000003	|	ENSG00000000005	|	ENSG00000000419	|	ENSG00000000457	|
|	---	|	---	|	---	|	---	|	---	|
|	GSM1655822	|	-0.134786235833333	|	-0.17197239	|	1.45520826478261	|	1.19886235424242	|
|	GSM1655824	|	-0.0824956441666667	|	-0.138843961666667	|	1.52755358434783	|	1.23414307606061	|
|	GSM1655828	|	0.01410980625	|	-0.0497307604166667	|	1.87922163826087	|	1.37357742909091	|
|	GSM1655831	|	-0.14607886375	|	-0.0965413295833333	|	1.59259964304348	|	1.35120664515152	|

**Columns: 21615 Rows: 264**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#10060;	Row: 5 - Sample "GSM1656050" is not found in data.tsv.gz

&#10060;	Row: 6 - Sample "GSM1656050" is not found in data.tsv.gz

&#10060;	Row: 7 - Sample "GSM1656051" is not found in data.tsv.gz

&#10060;	Row: 8 - Sample "GSM1656051" is not found in data.tsv.gz

#### Results: **<font color="red">FAIL</font>**
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	GSM1655743	|	age	|	47	|
|	GSM1655743	|	treatment	|	Control	|
|	GSM1655743	|	gender	|	Female	|
|	GSM1655743	|	V30M_Carrier	|	Control	|

**Columns: 3 Rows: 1049**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#10060;	Row 5: Fail
- "GSM1656050	age	" is not found.

&#10060;	Row 6: Fail
- "GSM1656050	V30M_Carrier" is not found.

&#10060;	Row 7: Fail
- "GSM1656051	age" is not found.

&#10060;	Row 8: Fail
- "GSM1656051	V30M_Carrier" is not found.

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---