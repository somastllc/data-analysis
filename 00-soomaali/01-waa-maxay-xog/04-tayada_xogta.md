# Tayada Xogta

**Cutubka:** 1aad - Waa maxay xog?  
**Casharka:** 4aad ee 5-ta cashar  
**Dhammaadka casharkan:** Waxaad awoodi doontaa inaad jadwal (table) eegto oo aad aqoonsato dhibaatooyinka ku jira xogta.

## Dulmar

Maamule ayaa kuu soo diray liiska macaamiisha, wuxuuna kaa codsaday inaad xisaabiso celceliska daʼdooda. Markaad jadwalka eegto, waxaad markiiba arkaysaa dhowr sababood oo natiijada ka dhigi kara mid khaldan.

Xog xun waxay keentaa goʼaanno xun. Xitaa falanqayn (analysis) fudud way khaldami kartaa haddii xogtu ay dhammaystirnayn, khaldan tahay, ama aanay isku mid ahayn.

### Maxay Tayada Xogtu Muhiim u Tahay?

**Tayada xogta (data quality)** waxay kuu sheegaysaa in dataset-ku ku habboon yahay shaqada laga rabo iyo in kale. Goʼaan lagu dhisay tirooyin maqan, xog soo noqnoqotay, ama si khaldan loo qoray wuxuu u muuqan karaa mid sax ah, laakiin natiijadiisu way khaldan tahay. Khaladku wuxuu ku jiraa xogta la geliyey (input).

Fikraddan waxaa lagu soo koobaa **Garbage In, Garbage Out (GIGO)**, oo macnaheedu yahay: xog xun oo la geliyo (input) waxay keentaa natiijo xun (output). Xitaa haddii xisaabinta ama qalabku si sax ah u shaqeeyo, natiijadu way khaldamaysaa haddii xogta la geliyey ay khaldan tahay.

Taasi waa sababta xirfadlayaasha xogta (data professionals) ay u hubiyaan xogta ka hor falanqaynta.

### Dhibaatooyinka Caamka ah ee Tayada Xogta

Khaladaadka inta badan laga helo xogta waxaa ka mid ah:

- **Qiimeyaal maqan (missing values):** meelo bannaan
- **Xog soo noqnoqotay (duplicates):** isla diiwaankii oo hal mar ka badan muuqda
- **Qiimeyaal khaldan (incorrect values):** khaladaad qoraal, halbeegyo khaldan, ama tirooyin aan macquul ahayn
- **Habayn aan isku mid ahayn (inconsistent formatting):** xog isku nooc ah oo siyaabo kala duwan loo qoray, sida `01/05/2024` iyo `2024-05-01`
- **Xog duug ah (outdated data):** xog aan hadda ka tarjumayn xaaladda jirta

Waxaa caam ah in dataset laga helo hal ama dhowr ka mid ah dhibaatooyinkan.

### Cabbirrada Tayada Xogta

| Cabbirka | Suʼaasha lagu hubiyo |
|---|---|
| **Saxnaan (accuracy)** | Xogtu ma sax baa? |
| **Dhammaystirnaan (completeness)** | Wax miyaa ka maqan? |
| **Isku mid ahaansho (consistency)** | Habayntu ma isku mid baa? |
| **Cusboonaansho (timeliness)** | Xogtu ma cusub tahay? |
| **Ku habboonaansho (relevance)** | Xogtu ma ka jawaabaysaa suʼaasha? |

Uma baahnid qalab horumarsan (advanced tools) si aad u bilowdo hubinta tayada xogta. Mararka qaarkood jadwal si taxaddar leh loo eego ayaa muujinaya qiimeyaal maqan, ama safaf soo noqnoqda (duplicate rows).

### Tusaale: Liiska Macaamiisha

Maamuluhu wuxuu rabaa celceliska daʼda macaamiisha. Marka hore jadwalka eeg. Waxaa ku jira afar dhibaato.

| Customer ID | Magaca | Daʼda | Magaalada | Iimayl |
|---|---|---|---|---|
| `C-101` | Hodan Warsame | `34` | `Hargeisa` | `hodan@example.com` |
| `C-102` | Farah Guled | `27` | `Muqdisho` | `farah@example.com` |
| `C-103` | Sagal Ibrahim | | `hargeisa` | `sagal@example.com` |
| `C-104` | Liibaan Cabdi | `200` | `Muqdisho` | `liibaan@example.com` |
| `C-102` | Farah Guled | `27` | `Muqdisho` | `farah@example.com` |

### Isla Xogtii, Celcelisyo Kala Duwan

Saddex ka mid ah afarta dhibaato ayaa beddelaya celceliska daʼda, mid kastaana si gaar ah ayuu u beddelaa:

- Daʼda Liibaan waa `200`. Waa **qiime khaldan (incorrect value)**, sababtoo ah waa tiro aan macquul ahayn oo celceliska kor u qaadaysa.
- Daʼda Sagal way bannaan tahay. Waa **qiime maqan (missing value)**, taas oo xogta ka dhigaysa mid aan dhammaystirnayn. Waa inaad goʼaansataa in Sagal laga reebo celceliska ama daʼdeeda eber loo tiriyo. Labadaas doorasho waxay keenayaan jawaabo kala duwan.
- `C-102` laba jeer ayuu soo muuqday. Waa **xog soo noqnoqotay (duplicate)**. Labada saf xogtoodu waa sax, laakiin Farah waxaa loo tirinayaa laba macmiil.

Haddii daʼaha jadwalka sida ay yihiin loo xisaabiyo, meesha bannaanna aan tiro ahaan loo tirin, celcelisku wuxuu noqonayaa **72**. Marka qiimaha `200` laga saaro, Farah hal mar la tiriyo, meesha bannaan ee Sagalna aan lagu darin xisaabinta, celcelisku wuxuu noqonayaa **30.5**.

Waa isla faylkii, isla suʼaashii, iyo isla xisaabintii, laakiin dhibaatooyinka tayada xogtu waxay keeneen laba jawaabood oo aad u kala duwan.

Dhibaatada afraad celceliska ma beddelayso. `Hargeisa` iyo `hargeisa` waa **habayn aan isku mid ahayn (inconsistent formatting)**. Waxay muhiim noqon lahayd haddii suʼaashu magaalooyinka ku saabsan tahay. Dhibaatada muhiimka ahi waxay ku xiran tahay suʼaasha aad rabto inaad ka jawaabto.
