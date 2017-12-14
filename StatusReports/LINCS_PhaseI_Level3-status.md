<h1><center>LINCS_PhaseI_Level3</center></h1>
<h2><center> Status: In Progress </center></h2>


### Testing Directory . . .

#### Results: PASS
---
### Testing Description File . . .

&#9989;	Title is less than 100 characters

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

*Running user code . . .*

Executing download.sh: Success

Executing parse.sh: Success

&#9989;	data.tsv.gz was created and zipped correctly.

&#9989;	metadata.tsv.gz was created and zipped correctly.

#### Results: PASS
---
### Testing Key Files:

&#9989;	test_data.tsv contains enough unique samples to test

&#9989;	test_data.tsv contains enough test cases (12; min: 8)

&#9989;	test_metadata.tsv contains enough unique samples to test

&#9989;	test_metadata.tsv contains enough test cases (39; min: 8)

#### Results: PASS
---

### First 5 columns and 5 rows of data.tsv.gz:

|	Sample	|	PSME1	|	ATF1	|	RHEB	|	FOXO3	|
|	---	|	---	|	---	|	---	|	---	|
|	CPC001_HA1E_24H_X1_B3_DUO52HI53LO:H01	|	11.464849472	|	7.20182514191	|	12.3978500366	|	8.41334915161	|
|	CPC001_HA1E_24H_X2_B3_DUO52HI53LO:H01	|	11.6028995514	|	7.60437488556	|	12.4033002853	|	8.67430019379	|
|	CPC001_HA1E_24H_X3_B3_DUO52HI53LO:H01	|	11.4104747772	|	7.36237573624	|	12.3866500854	|	8.18389987946	|
|	CPC001_HA1E_24H_X1_B3_DUO52HI53LO:F22	|	11.7382497787	|	7.14995002747	|	12.4792499542	|	9.08315086365	|

**Columns: 12329 Rows: 1317822**

---
### "data.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#9989;	Row 11: Success

&#9989;	Row 12: Success

#### Results: PASS
---
### First 3 columns and 5 rows of metadata.tsv.gz:

|	Sample	|	Variable	|	Value	|
|	---	|	---	|	---	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	rna_plate	|	ASG001_MCF7_24H_X1	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	rna_well	|	F13	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	pert_id	|	DMSO	|
|	ASG001_MCF7_24H_X1_B7_DUO52HI53LO:F13	|	is_touchstone	|	1	|

**Columns: 3 Rows: 31226018**

---
### "metadata.tsv.gz" Test Cases (from rows in test file). . .

&#9989;	First column of file is titled "Sample"

&#10060;	The value for variable "pert_time_unit" for all samples is the same ("h").

&#10060;	The value for variable "donor_ethnicity" for all samples is the same ("Caucasian").

&#9989;	Row 1: Success

&#9989;	Row 2: Success

&#9989;	Row 3: Success

&#9989;	Row 4: Success

&#9989;	Row 5: Success

&#9989;	Row 6: Success

&#9989;	Row 7: Success

&#9989;	Row 8: Success

&#9989;	Row 9: Success

&#9989;	Row 10: Success

&#10060;	Row 11: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	rna_plate	PCLB002_MCF7_24H_X3" is not found.

&#10060;	Row 12: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	pert_id	BRD-A75409952" is not found.

&#10060;	Row 13: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	is_touchstone	0" is not found.

&#10060;	Row 14: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	canonical_smiles	COCC1OC(=O)c2coc3c2C1(C)C1=C(C2CCC(=O)C2(C)CC1OC(C)=O)C3=O" is not found.

&#10060;	Row 15: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	tas_q75	0.41063425" is not found.

&#10060;	Row 16: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	icc	0.478662326931953" is not found.

&#10060;	Row 17: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	pert_iname	wortmannin" is not found.

&#10060;	Row 18: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	cell_id	MCF7" is not found.

&#10060;	Row 19: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	cell_type	cell line" is not found.

&#10060;	Row 20: Fail
- "PCLB002_MCF7_24H_X3_B13:P24	donor_ethnicity	Caucasian" is not found.

&#9989;	Row 21: Success

&#9989;	Row 22: Success

&#9989;	Row 23: Success

&#9989;	Row 24: Success

&#9989;	Row 25: Success

&#9989;	Row 26: Success

&#9989;	Row 27: Success

&#9989;	Row 28: Success

&#9989;	Row 29: Success

&#9989;	Row 30: Success

&#9989;	Row 31: Success

&#9989;	Row 32: Success

&#9989;	Row 33: Success

&#9989;	Row 34: Success

&#9989;	Row 35: Success

&#9989;	Row 36: Success

&#9989;	Row 37: Success

&#9989;	Row 38: Success

&#9989;	Row 39: Success

#### Results: **<font color="red">FAIL</font>**
---
### Making sure no commas exist in either file . . .

&#10060;	Comma(s) exist in "metadata.tsv.gz"

#### Results: **<font color="red">FAIL</font>**
---
### Comparing samples in both files . . .

&#9989;	Samples are the same in both "data.tsv.gz" & "metadata.tsv.gz"

#### Results: PASS

---
### Testing Directory after cleanup . . .

#### Results: PASS
---