# Nadiifinta Xogta

**Cutubka:** 3aad - Hab-socodka Xogta  
**Casharka:** 3aad ee 6-da cashar  
**Dhammaadka casharkan:** Waxaad awoodi doontaa inaad goʼaamiso waxa laga qabanayo xogta soo noqnoqotay, qiimeyaasha maqan, iyo qiimeyaasha aan saxda ahayn.

## Dulmar

Marka falanqeeyayaasha la weydiiyo waxa waqtigooda ugu badan qaata, jawaabtu badanaa ma aha falanqaynta. Waqti badan waxay ku bixiyaan diyaarinta xogta si falanqayntu u suurtowdo.

Xogta dhabta ahi mar walba ma aha mid diyaarsan. Ka hor inta aan la falanqayn, badanaa waa in la nadiifiyaa. **Nadiifinta xogta (data cleaning)** waxay hagaajisaa tayada xogta iyada oo khaladaadka la saxayo, qiimeyaasha maqan wax laga qabanayo, qaababkana la mideynayo.

### Maxaa Xogta Loo Nadiifiyaa?

Falanqaynta xog aan nadiif ahayn waxay keeni kartaa natiijo khaldan.

Cutubka 1aad waxaan ku soo aragnay dhibaatooyinka tayada xogta, sida qiimeyaasha maqan, iyo xogta soo noqnoqotay. Nadiifinta xogtu waa waxa laga qabanayo dhibaatooyinkaas.

In dhibaatada la arko waa bilowga. Goʼaaminta waxa laga qabanayo ayaa u baahan taxaddar, laba falanqeeyana waxay si macquul ah xalal kala duwan ugu dooran karaan isla tiir (column) xogeed oo khaldan.

### Hawlaha Caamka ah ee Nadiifinta Xogta

| Hawsha | Tusaale |
|---|---|
| **Ka saarista xogta soo noqnoqotay** | Isla macmiilka oo laba jeer ku jira |
| **Wax ka qabashada qiimeyaasha maqan** | Daʼ ama email bannaan |
| **Saxidda qaababka** | Taariikho siyaabo kala duwan loo qoray |
| **Midaynta qaybaha (Standardizing categories)** | `Hargeysa`, `Hargeisa`, iyo `hargeysa` |
| **Saxidda qiimeyaasha aan saxda ahayn** | Daʼda oo ah `-3` ama `999` |

### Nadiifin Intee Leʼeg Ayaa Ku Filan?

Dhibaato kasta xal isku mid ah uma baahna.

Tusaalooyin:

- Jawaabaha survey-ga qaarkood oo maqan mararka qaarkood waa la aqbali karaa
- Diiwaannada maaliyadeed ee soo noqnoqday badanaa waa in laga saaraa
- Khalad ku jira magaca qayb waa in lagu saxo **midayn (standardization)**, si magac kasta oo magaalo ama alaab loogu qoro hal qaab

Xalka saxda ahi wuxuu ku xiran yahay suʼaasha xogta laga rabo inay ka jawaabto. Taasi waa sababta nadiifintu uga dambayso qeexidda suʼaasha.

### Tusaale

Liiska shaqaalaha ee ganacsi jumlo iibiya waxaa ku jira:

- Laba saf oo leh isla Employee ID
- Shaqaale qaarkood oo aan la diiwaangelin laanta (branch) ay ka shaqeeyaan
- Mushaharro loo kala qoray `$500`, `500`, iyo `500 USD`

Kahor intaadan isbarbar dhigin mushaharka laamaha oo dhan, waa inaad:

1. Ka saartaa safafka soo noqnoqday
2. Goʼaamisaa waxa laga qabanayo xogta laanta ee maqan
3. Mushaharrada u qortaa hal qaab

Haddii tallaabooyinkan laga boodo, waxaa soo bixi kara celcelis iyo kala-sarrayn khaldan.

Nadiifinta xogtu waa mawduuc ballaaran. Hadda waxa muhiimka ahi waa inaad garato in tallaabadani jirto iyo in ka boodisteedu ay natiijooyinka ka dambeeya ka dhigto kuwo aan lagu kalsoonaan karin.
