# Nadiifinta Xogta

**Cutubka:** 3aad - Hab-socodka Xogta
**Casharka:** 3aad ee 6-da cashar
**Dhammaadka casharkan:** Waxaad awoodi doontaa inaad doorato tallaabo ku habboon xogta soo noqnoqotay, qiimeyaasha maqan, iyo qaababka ama qiimeyaasha khaldan.

## Dulmar

Casharkii hore waxaan soo ururinnay xogta iibka bariiska ee Luulyo iyo Agoosto. Hadda waxaan diyaarinaynaa xogtaas si laamaha si sax ah loogu barbar dhigo.

**Nadiifinta xogta (data cleaning)** waa saxidda khaladaadka, wax ka qabashada qiimeyaasha maqan, iyo midaynta qaababka xogta.

Casharkii tayada xogta waxaad ku baratay aqoonsiga dhibaatooyinka; halkan waxaad ku baranaysaa waxa laga qabanayo.

### Dhibaatada Hubi, Kadibna Tallaabo Qaad

Kaydi xogtii asalka ahayd, ku shaqee nuqul, kuna qor isbeddellada aad samaysay iyo sababtooda.

| Dhibaatada | Waxa la hubinayo | Tallaabada |
|---|---|---|
| Safaf soo noqnoqda | Ma isla diiwaankii baa laba jeer la geliyey, mise waa iibyo kala duwan? | Ka saar nuqulka dheeraadka ah marka soo noqnoqoshada la xaqiijiyo |
| Qiime maqan | Ma laga heli karaa diiwaankii asalka ahaa? | Ku buuxi xog la xaqiijiyey; haddii aan la helin, calaamadee inuu maqan yahay |
| Magacyo kala qoran | Ma isla laantii baa magacyo kala duwan loo qoray? | U qor hal magac oo la isla oggol yahay |
| Taariikho qaabab kala duwan leh | Ma caddahay maalinta, bisha, iyo sannadku? | U beddel hal qaab marka macnaha taariikhda la xaqiijiyo |
| Halbeegyo kala duwan | Ma la yaqaan sida loogu beddelo halbeeg isku mid ah? | U beddel kg marka miisaanka la xaqiijiyo |
| Qiime laga shakiyo | Ma khalad gelin baa, mise wuxuu leeyahay sharaxaad sax ah? | Ka hubi isha oo sax haddii khalad la xaqiijiyo |

Isla macmiilka oo laba jeer wax iibsaday ma aha xog si khaldan u soo noqnoqotay. Sidoo kale, tiro aad u weyn keliya ma caddaynayso khalad.

### Tusaale: Nadiifinta Diiwaanka Iibka Bariiska

Qayb ka mid ah xogtii la soo ururiyey ayaa sidan u qoran. Tusaalahan, saf kasta waxaa loogu talagalay hal iib oo bariis ah, iib kastana wuxuu leeyahay aqoonsi u gaar ah.

| Aqoonsiga iibka | Taariikhda | Laanta | Tirada | Halbeegga |
|---|---|---|---|---|
| B-101 | 2026-07-05 | Hodan | 50 | kg |
| B-101 | 2026-07-05 | Hodan | 50 | kg |
| B-102 | 2026-07-06 | hodan | 2 | jawaan |
| B-103 | 2026-08-03 | | 25 | kg |

Ka hor isbarbardhigga laamaha:

1. **Hubi B-101:** Haddii diiwaanka asalka ahi xaqiijiyo inuu yahay hal iib oo laba jeer la geliyey, hal saf ka saar. Haddii labadaba la tiriyo, iibkaas wuxuu noqonayaa 100 kg halkii uu ka ahaan lahaa 50 kg.
2. **Midee magaca laanta:** Marka la xaqiijiyo in `hodan` iyo `Hodan` yihiin isla laanta, labadaba u qor `Hodan`.
3. **Xaqiiji miisaanka jawaanka:** Haddii jawaan kasta oo iibka B-102 ahi yahay 50 kg, labada jawaan u beddel 100 kg. Ha qiyaasin miisaanka adigoon hubin.
4. **Raadi laanta B-103:** Ka hubi diiwaanka asalka ah ama qofka xogta geliyey; magaca laanta ha iska qiyaasin.

### Haddii Xogta Maqan Aan La Helin

Qiime maqan si toos ah eber ha uga dhigin. Tirada iibka oo maqan iyo iib eber ahi isku macne ma aha.

Haddii laanta B-103 la waayo, ku calaamadee “Laan aan la garanayn”. 25-ka kg waxaa lagu dari karaa wadarta guud ee iibka, laakiin looma nisbayn karo laan gaar ah.

Marka natiijada la gudbinayo, sheeg in iib aan laantiisa la garanayn uu jiro, taasina ay xaddidayso isbarbardhigga laamaha.

### Hubi Natiijada Nadiifinta

Dib u eeg in nuqulladii la xaqiijiyey laga saaray, magacyadu isku qaab yihiin, iyo tirooyinka la isu geynayo ay isku halbeeg yihiin. Isbarbar dhig xogtii hore iyo tan la nadiifiyey si aad u sharxi karto wixii isbeddelay.

### Qodobka Muhiimka ah

**Hubi dhibaatada → ku sax xog la xaqiijiyey → diiwaangeli isbeddelka → dib u hubi.**

Xogta aan la sixi karin xaddidaaddeeda caddee ka hor intaadan u gudbin falanqaynta.
