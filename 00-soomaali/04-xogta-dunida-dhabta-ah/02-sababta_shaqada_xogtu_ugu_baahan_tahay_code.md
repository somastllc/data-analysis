# Sababta Shaqada Xogtu Ugu Baahan Tahay Code

**Cutubka:** 4aad - Xogta Dunida Dhabta ah  
**Casharka:** 2aad ee 3-da cashar  
**Dhammaadka casharkan:** Waxaad awoodi doontaa inaad sharaxdo sababta code loo isticmaalo halkii spreadsheets oo keliya lagu ekaan lahaa.

## Dulmar

Spreadsheets-ku si fiican ayay u shaqeeyaan ilaa saddex arrimood dhacaan: xogtu aad ayay u badataa, isla report-ka ayaa toddobaad kasta loo baahan yahay, ama qof ayaa kaa codsada inaad caddeyso sida tirada loo soo saaray.

### Waxa Code-ku Xalliyo

**Code** waa amarro qoran oo kombiyuutarka u sheegaya tallaabooyinka uu fulinayo.

Code-ku wuxuu xalliyaa saddexdaas arrimood:

- Wuxuu la shaqayn karaa xog badan
- Hawsha ayaa mar kale la socodsiin karaa marka loo baahdo
- Wuxuu reebaa diiwaan qoran oo muujinaya tallaabo kasta oo la qaaday

Qodobka ugu dambeeya ayaa ka muhiimsan inta qofka bilowga ahi filan karo. Spreadsheet-ku wuxuu ku tusayaa tiro. Code-ku wuxuu si taxane ah u muujinayaa tallaabooyinkii tiradaas lagu soo saaray. Taasi waa farqiga u dhexeeya natiijo la hubin karo iyo mid la aqbalo iyada oo aan la garanayn sida lagu helay.

Code mar walba qasab ma aha. Falanqeeye wuxuu qaban karaa shaqo waxtar leh isaga oo aan code adeegsan. Laakiin marka xogtu weynaato, hawshu soo noqnoqoto, ama loo baahdo in tallaabo kasta la hubiyo, code-ku wuxuu noqdaa mid waxtar badan.

Lagama rabo inaad hadda fahanto code-ka tusaalooyinka soo socda. Ujeeddadu waa inaad aragto sida ay shaqadani u muuqato.

### SQL oo Suʼaal u Diraya Database-ka

**SQL** wuxuu database-ka u diraa suʼaal:

```sql
SELECT city, SUM(sales) AS total_sales
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY city;
```

Query-gani wuxuu database-ka weydiinayaa: “Laga bilaabo 1-da Janaayo 2024, magaalo kasta iibkeedu waa imisa?” Afar sadar oo SQL ah ayaa jawaabta suʼaashaas soo saaraya.

### Python oo Xogta Tallaabo Tallaabo Uga Shaqaynaya

**Python** wuxuu furaa xogta, kadibna tallaabo tallaabo ayuu uga shaqeeyaa:

```python
import pandas as pd

orders = pd.read_csv("orders.csv")
average_by_city = orders.groupby("city")["sales"].mean()
print(average_by_city)
```

Code-kani wuxuu:

1. Furayaa faylka `orders.csv`
2. Xogta u kala kooxaynayaa magaalo
3. Xisaabinayaa celceliska iibka magaalo kasta
4. Soo bandhigayaa natiijada

Labada tusaale waxaa sidoo kale gacanta loogu samayn karaa spreadsheet. Farqigu waa in code-ku malaayiin saf kaga shaqayn karo ilbidhiqsiyo gudahood, mar kastana uu tallaabooyinka si isku mid ah u fulin karo. Tallaabooyinku sidoo kale way qoran yihiin, waana dib loo hubin karaa.
