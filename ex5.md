# AVL Puu

AVL puu on nimetatud Adelsoni, Velski ja Landise järgi.

See on üks tüüp binaarsetest otsingupuudest, mis on isebalanseeriv.

AVL puu jälgib "tasakaalufaktorit" ning pöörab sõlmi, et säilitada tasakaalu. Tasakaalufaktor on vasaku ja parema alampuu kõrguse vahe.

Iga sõlm sisaldab mingit võrdlust ja viiteid vasakule/paremale alampuule.

# AVL puu vs punane-must puu

AVL puu nõuab tavaliselt rohkem pööramisi kui punase-musta puu.

AVL puu kõrgus võib olla lühem ning seega ka saab teha kiiremaid otsinguid.

AVL puu võib kasutada rohkem mälu, kuna ta peab hoidma ka tasakaalufaktoreid.

# Rakendused

AVL puu on sobilik rakendustes, kus otsingud on sagedasemad kui sisestamised või kustutamised Näiteks andmebaasid ja failisüsteemid, kus otsingukiirus on kriitiline.

Punase-musta puu sobib hästi rakendustesse, kus esineb rohkem sisestamisi ja kustutamisi, ning otsinguid vähem.

Kasutatakse sageli raamatukogude andmestruktuurides (nt Javas TreeMap/TreeSet).






