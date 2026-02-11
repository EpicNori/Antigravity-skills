---
name: antigravity-ralfwiggum-loop
description: Implementiert einen autonomen Agenten-Loop für Google Antigravity, der Aufgaben iterativ ausführt, bis alle Anforderungen erfüllt sind.
---

# Antigravity RalfWiggum Loop

Dieser Skill ermöglicht es einem Agenten, in einer kontinuierlichen Schleife zu arbeiten, um komplexe Programmieraufgaben autonom zu lösen. Der Name "Ralph Wiggum" bezieht sich auf das Muster des "helfenden" Agenten, der so lange iteriert, bis das Ziel erreicht ist.

## Funktionsweise

Der Loop basiert auf einem Bash-Skript, das die Antigravity CLI (`ag`) aufruft. In jeder Iteration wird der aktuelle Zustand des Projekts und die verbleibenden Aufgaben aus dem PRD (Product Requirements Document) an den Agenten übergeben.

## Implementierung

Erstellen Sie eine Datei namens `ralph.sh` in Ihrem Projektverzeichnis:

```bash
#!/bin/bash

# Der RalfWiggum Loop für Antigravity
# Verwendung: ./ralph.sh "Erstelle eine Todo-App mit React"

GOAL=$1

while true; do
  echo "🚀 Starte Iteration... Ziel: $GOAL"
  
  # Rufe den Antigravity Agenten auf
  # --non-interactive sorgt dafür, dass der Agent autonom arbeitet
  ag task "$GOAL" --non-interactive --verify
  
  # Überprüfe den Exit-Status oder ob der Agent "DONE" signalisiert hat
  if [ $? -eq 0 ]; then
    echo "✅ Aufgabe erfolgreich abgeschlossen!"
    break
  else
    echo "🔄 Iteration beendet, starte erneut zur Verfeinerung..."
    sleep 2
  fi
done
```

## Best Practices

1. **Strukturierte Anforderungen**: Stellen Sie sicher, dass eine `AGENTS.md` oder `PRD.md` im Root-Verzeichnis existiert, damit der Agent den Fortschritt verfolgen kann.
2. **Kontext-Management**: Der Loop nutzt die "Artifacts"-Funktion von Antigravity, um den Zustand zwischen den Iterationen zu speichern.
3. **Sicherheitschecks**: Verwenden Sie den `--verify` Flag, damit der Agent Tests ausführt, bevor er eine Iteration als erfolgreich markiert.

## Wann dieser Skill zu verwenden ist

- Bei großen Refactorings, die mehrere Dateien betreffen.
- Wenn eine neue Funktion von Grund auf implementiert werden soll.
- Zur automatischen Fehlerbehebung in CI/CD-Pipelines.
