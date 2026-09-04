# Eexda iyo Caddaaladda

**Cutubka:** 5aad - Anshaxa iyo Asturnaanta Xogta  
**Casharka:** 3aad ee 4-ta cashar  
**Dhammaadka casharkan:** Waxaad awoodi doontaa inaad dataset-ka ka dhex aqoonsato doorsoomayaasha wakiilka ah (proxy variables), isla markaana aad sharaxdo sida nidaam eex leh uu eexda u sii xoojin karo.

## Dulmar

Model-ku wuxuu si dadban u kala garan karaa ragga iyo dumarka, xitaa haddii dataset-ku aanu lahayn field si toos ah u sheegaya jinsiga (gender). Tani ma aha arrin naadir ah. Fields kale ayaa si dadban u muujin kara macluumaad la xiriira jinsiga.

**Eexda (bias)** waa caddaalad-darro nidaamsan oo keenta natiijooyin aan caddaalad ahayn. Xogtu waxay u ekaan kartaa mid dhexdhexaad ah, laakiin waxay xambaarsanaan kartaa goʼaannadii dadka iyo sinnaan-laʼaantii hore.

### Noocyada Eexda

| Nooca | Macnaha |
|---|---|
| **Eexda muunadda (sampling bias)** | Xogtu si caddaalad ah uma metelayso dhammaan dadka uu nidaamku saamaynayo |
| **Eexda cabbirka (measurement bias)** | Xogta kooxaha qaarkood si ka duwan ayaa loo cabbiraa |
| **Eexda taariikhiga ah (historical bias)** | Caddaalad-darradii hore ayaa xogta ku dhex jirta |
| **Eexda warbixinta (reporting bias)** | Dhacdooyinka qaarkood ayaa laga diiwaangeliyaa in ka badan kuwa kale |

### Eexda Mashruuca Amaahda

Kooxdu waxay model-ka qiimaynta amaahda ku tababaraysaa diiwaannada amaahihii ay shirkaddu gacanta ku ansixisay saddexdii sano ee la soo dhaafay. Diiwaannadu waxay muujinayaan amaah kasta oo la bixiyey iyo in dib loo bixiyey iyo in kale.

Tani waa xogta ugu dhow ee shirkaddu u hayso arrinta ay rabto inay saadaaliso. Laakiin isla xogtaas ayaa sidoo kale xambaarsan dhibaatada.

Amaahihii hore badankood waxaa la siiyey macaamiil tagay laanta shirkadda, haystay ganacsi diiwaangashan, isla markaana lahaa cinwaan rasmi ah. Dadkaas badankood waxay ahaayeen ganacsato ku nool caasimadda, rag ayaana u badnaa. Ganacsatada suuqa, macaamiisha miyiga, iyo haweenka guryahooda ku ganacsada si yar ayay amaah u codsadeen. Xitaa markii ay codsadeen, codsiyadooda si ka yar ayaa loo ansixiyey.

Dataset-ku wuxuu hayaa natiijada dadkii amaahda la siiyey, laakiin ma hayo waxa dhici lahaa haddii dadkii la diiday amaah la siin lahaa. Sidaas darteed, nidaamku ma haysto caddayn ku filan oo ku saabsan dhammaan macaamiisha uu goʼaanka ka gaarayo. Wuxuu qaabkii hore ee ansixinta ku khaldi karaa awoodda dhabta ah ee dib-u-bixinta.

### Proxy Variables

Kooxdu field-ka jinsiga kuma darin dataset-ka. Taasi keliya kama hor istaagayso nidaamka inuu jinsiga si dadban u garto.

| Field-ka | Waxa uu si dadban u muujin karo |
|---|---|
| **Degmada telefoonku ka diiwaangashan yahay** | Magaalo ama miyi |
| **In lacag-bixin ganacsi la helay** | Ganacsi rasmi ah ama aan rasmi ahayn |
| **Daʼda akoonka** | Cidda waqti hore awood u lahayd telefoon iyo adeegga mobile money-ga |

**Proxy variable** waa field si dadban u metela xog kale oo aan dataset-ka si toos ah ugu jirin. Tusaalahan, fields-ku ma sheegayaan jinsiga qofka, laakiin waxay la xiriiri karaan fursadihii kala duwanaa ee ay ragga iyo dumarku hore u haysteen.

Sidaas darteed, in shirkaddu tiraahdo “ma aanan ururin xogta jinsiga” ma caddaynayso in nidaamku eex laʼaan yahay. Waxay muujin kartaa oo keliya in aan la hubin waxa fields-ka kale metelayaan.

### Proxy Variable iyo Cabbir Toos ah

Nidaamku wuxuu sidoo kale adeegsadaa inta lacag ah ee akoonka soo marta bil kasta. Field-kani si toos ah ayuu u cabbirayaa dhaqdhaqaaqa ganacsiga amaahda loo codsanayo. Qof ay lacag ganacsi akoonkiisa soo marto wuxuu hayaa ganacsi, xitaa haddii aanu lahayn cinwaan rasmi ah ama shirkad diiwaangashan.

Tani waa farqiga u dhexeeya **proxy variable** iyo **cabbir toos ah (direct measure)**:

- Proxy variable-ku wuxuu suʼaasha uga jawaabaa isagoo adeegsanaya wax kale oo la xiriira
- Cabbirka tooska ahi wuxuu cabbiraa waxa aad dhab ahaan rabto inaad ogaato

Marka aad eegayso fields-ka dataset, mid kasta iska weydii: **Field-kani ma cabbirayaa waxa aan rabno, mise wuxuu si dadban u metelayaa wax kale?**

### Sida Eexdu Isu Sii Xoojiso

```mermaid
flowchart LR
    pastNode["Goʼaannadii hore"] --> dataNode["Xogta tababarka"]
    dataNode --> modelNode["Model"]
    modelNode --> decisionNode["Goʼaanno cusub"]
    decisionNode --> pastNode
```

Wareeggan waxaa loo yaqaan **wareeg is-xoojinaya (feedback loop)**. Goʼaannada model-ku gaaro waxay qayb ka noqdaan xogta loo adeegsan doono goʼaannada mustaqbalka.

Nidaamku wuxuu diidi karaa ganacsatada suuqa sababtoo ah xogta tababarka waxaa ku yar ganacsato suuqa oo hore amaah loo siiyey. Marka la diido, ma samaysmaan diiwaanno cusub oo muujinaya sida ay amaahda u bixin lahaayeen haddii fursad la siin lahaa.

Marka xogta sannadka xiga la ururiyo, ganacsatadaas weli si fiican uguma muuqdaan dataset-ka. Nidaamkuna mar kale ayuu u badan yahay inuu diido.

Sidaas ayay eexdu isu sii xoojin kartaa.

Nidaam eex leh khaladkiisu halkiisii kuma ekaado. Haddii aan la hubin, wareeg kasta ayuu dhibaatada sii xoojin karaa.

### Waa Maxay Caddaaladdu?

Caddaaladdu macnaheedu ma aha in kiis kasta si isku mid ah loola dhaqmo. Waxay ka dhigan tahay in laga fogaado waxyeello aan caddaalad ahayn, lana hubiyo in goʼaannadu kooxaha qaarkood si gaar ah u dhibayn.

Si taas loo sameeyo:

- Hubi in dataset-ku metelayo dhammaan kooxaha uu goʼaanku saamaynayo
- Isbarbardhig natiijooyinka kooxaha, hana eegin saxnaanta guud (overall accuracy) oo keliya
- Goʼaannada ku tijaabi tiro yar ka hor inta aan si ballaaran loo adeegsan
- Si joogto ah u hubi in koox gaar ahi aanay la kulmayn natiijooyin aan caddaalad ahayn

Tallaabooyinkani dhammaantood uma baahna aqoon tirakoob oo heer sare ah. Waxa ay u baahan yihiin in si cad loo qeexo cidda nidaamka la soconaysa, cidda go’aannada dib u eegaysa, iyo cidda mas’uuliyadda qaadaysa marka dhibaato dhacdo.
