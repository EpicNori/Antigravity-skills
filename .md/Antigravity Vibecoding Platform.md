---
name: antigravity-vibecoding-platform
description: Leitfaden zur Erstellung einer eigenen Vibecoding-Plattform, die auf der Antigravity-Infrastruktur basiert.
---

# Antigravity Vibecoding Platform

Vibecoding ist ein Paradigma, bei dem der Entwickler durch High-Level-Intentionen ("Vibes") und visuelles Feedback steuert, während die KI die gesamte Implementierung übernimmt. Dieser Skill beschreibt, wie man eine solche Plattform aufbaut.

## Architektur einer Vibecoding-Plattform

Eine moderne Vibecoding-Plattform besteht aus drei Hauptkomponenten:

1. **Vibe-Interface**: Ein Frontend (oft mit Canvas oder Chat), das Intentionen, Screenshots oder Skizzen aufnimmt.
2. **Antigravity Orchestrator**: Ein Backend, das diese "Vibes" in Agent-Tasks übersetzt.
3. **Live-Preview-Engine**: Ein System, das den vom Agenten generierten Code sofort rendert und für den Benutzer sichtbar macht.

## Implementierungsschritte

### 1. Vibe-to-Task Translation
Nutzen Sie ein LLM (z.B. Gemini 3 Pro), um vage Benutzerwünsche in strukturierte Antigravity-Tasks zu übersetzen.

```python
# Beispiel für die Übersetzung eines "Vibes"
vibe = "Mach es wie Airbnb, aber für Hundehütten. Viel Weißraum, abgerundete Ecken."
task = antigravity.translate_vibe_to_task(vibe)
# Resultat: "Create a React landing page with Tailwind CSS, using a minimalist design, 
# specific color palette #FFFFFF, and border-radius: 1rem..."
```

### 2. Integration der Antigravity Manager Surface
Binden Sie die Antigravity Manager Surface über ein Iframe oder eine API ein, damit Benutzer den Fortschritt der Agenten in Echtzeit sehen können.

### 3. Artifact-basiertes Feedback
Implementieren Sie eine Funktion, mit der Benutzer direkt auf den generierten Artifacts (z.B. Screenshots der UI) Feedback geben können. Dieses Feedback wird sofort als neuer Task in den RalfWiggum-Loop eingespeist.

## Beispiel-Workflow
1. **Input**: Benutzer lädt einen Screenshot einer Website hoch und sagt: "Bau das nach, aber in Dunkelblau."
2. **Processing**: Ein Antigravity-Agent analysiert das Bild (Vision) und erstellt ein technisches PRD.
3. **Execution**: Der RalfWiggum-Loop startet und baut die Seite Komponente für Komponente auf.
4. **Feedback**: Der Benutzer sieht die Live-Preview, klickt auf einen Button und sagt: "Der Button muss größer sein."
5. **Refinement**: Der Agent korrigiert den Code sofort.

## Tools & Technologien
- **Frontend**: Next.js, Tailwind CSS, Framer Motion.
- **Backend**: Python FastAPI mit Antigravity SDK.
- **Deployment**: Google Cloud Run oder Vercel.

## Best Practices
- **Scope Limiting**: Zwingen Sie den Agenten, sich auf eine Design-System-Bibliothek (z.B. Shadcn UI) zu konzentrieren, um Konsistenz zu wahren.
- **Live API Checks**: Lassen Sie den Agenten echten Code gegen Live-APIs testen, anstatt nur Mocks zu erstellen.
- **Vibe-History**: Speichern Sie alle Iterationen, damit der Benutzer zu einem früheren "Vibe" zurückkehren kann.
