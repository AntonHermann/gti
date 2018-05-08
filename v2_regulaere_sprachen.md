# Reguläre Sprachen

## Problem

Schreibe r.A für alle Wörter über Σ={0,1}, die _nicht_
Teilstring '0110' enthalten.

Direkt => schwierig

Aber:

1. Schreibe NEA M1, der alle Wörter erkennt, die 0110 enthalten
2. Wandle M1 in DEA M2 um
3. Vertausche in M2 akzeptierende & nicht akzeptierende Zustände
    -> DEA M3 mit L(M3) = alle Wörter ohne Teilstring 0110
4. Finde r.A α mit L(α) = L(M3)

Schritt 2 muss vor Schritt 3 kommen, da Vertauschen nur bei DEA
das Komplement der Sprache ergibt, bei NEA gilt das nicht zwangsläufig
(da NEA akzeptiert ≡ min. 1 Zustand akzeptiert)

Def.: Sei Σ Alphabet. Eine Sprache L ⊆ Σ* heißt regulär, gdw. es existiert
    ein relärer Ausdruck α mit L = L(α)

Satz: Sei L ⊆ Σ* Sprache, dann gilt:

  1. L ist regulär          <=>
  2. ex. DEA M mit L = L(M) <=>
  3. ex. NEA M mit L = L(M)

Anwendung:
Satz: Seien L1, L2 ⊆ Σ* reguläre Sprachen
    Dann sind auch die Sprachen
    L1 ∘ L2, L1 ∪ L2, (L1)*, Σ*\L1 und L1 ∩ L2 regulär
Beweis:
    ∘, ∪, * : sehr einfach => Operationen bereits direkt für r.A definiert
    \       : Nimm DEA M1 für L1 und vertausche akzeptierende und nicht
              akzeptierende Zustände
    ∩       : Σ* \ ((Σ* \ L1) ∪ (Σ* \ L2))