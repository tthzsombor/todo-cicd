# Dokumentáció váz – CI/CD pipeline projekt
(Címlap: név, Neptun-kód, tantárgy, dátum, repository link, éles URL)

## 1. A feladat és a cél
Rövid összefoglaló: mini alkalmazás + teljes CI/CD, Definition of Done.

## 2. Az alkalmazás
- Funkciók, REST végpontok táblázata (GET/POST /api/todos, PUT /api/todos/{id}/toggle, DELETE /api/todos/{id}, GET /health)
- Technológia: Python 3.12, Flask, Gunicorn
- Képernyőkép a UI-ról

## 3. Architektúra és eszközök
- Diagram: Fejlesztő → git push → GitHub → Actions (test → docker → deploy) → GHCR → Render
- Miért ezeket az eszközöket választottuk (ingyenes, git-integráció, konténer)

## 4. Verziókezelés
- Repo felépítése, main branch, commit üzenetek, (opcionális) PR-ok

## 5. A pipeline lépésről lépésre
- Trigger, jobok, a workflow kulcsrészletei, secrets kezelése
- Képernyőkép: sikeres zöld pipeline futás

## 6. Telepítés (deploy)
- Dockerfile magyarázata
- Render beállítás (Web Service, Docker, deploy hook)
- Smoke test szerepe

## 7. Bizonyíték a Definition of Done-ra
- Élő URL, /health válasz, a UI működés képernyőképei

## 8. Tapasztalatok, nehézségek, továbbfejlesztés
- Pl. adatbázis, staging környezet, lint/security scan, verziózott release

## Mellékletek
- Repository link, Dockerfile, ci-cd.yml
