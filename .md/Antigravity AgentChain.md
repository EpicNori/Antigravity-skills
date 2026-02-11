---
name: antigravity-agentchain
description: Anleitung zur Implementierung von Agent-Chains im eigenen Code unter Verwendung des Antigravity SDKs.
---

# Antigravity AgentChain

Agent-Chaining ist das Muster, bei dem mehrere spezialisierte Agenten nacheinander oder parallel arbeiten, um eine komplexe Aufgabe zu lösen. Dieser Skill zeigt, wie man dies programmatisch mit dem Antigravity SDK umsetzt.

## Kernkonzept

Eine Agent-Chain besteht aus:
1. **Planner Agent**: Erstellt einen detaillierten Ausführungsplan.
2. **Worker Agents**: Führen spezifische Teilaufgaben aus (z.B. Frontend, Backend, Testing).
3. **Reviewer Agent**: Validiert die Ergebnisse gegen die ursprünglichen Anforderungen.

## Code-Beispiel (Python)

Verwenden Sie das `antigravity` Paket, um Agenten in Ihrem eigenen Code zu verketten:

```python
from antigravity import Agent, Chain

def run_agent_chain(user_request):
    # 1. Spezialisierte Agenten definieren
    planner = Agent(role="Architect", goal="Create a technical plan")
    coder = Agent(role="Developer", goal="Implement the code based on the plan")
    tester = Agent(role="QA", goal="Verify the implementation")

    # 2. Die Kette (Chain) definieren
    # Der Output eines Agenten wird automatisch der Input des nächsten
    chain = Chain([planner, coder, tester])

    # 3. Kette ausführen
    result = chain.run(input=user_request)
    
    return result

if __name__ == "__main__":
    request = "Baue eine API-Endpunkt für Benutzer-Authentifizierung"
    final_output = run_agent_chain(request)
    print(f"Chain abgeschlossen: {final_output}")
```

## Fortgeschrittene Muster

### Bedingte Verzweigung
Sie können Logik hinzufügen, um basierend auf dem Output eines Agenten zu entscheiden, welcher Agent als nächstes aufgerufen wird:

```python
if "error" in coder_output:
    fixer_agent.run(coder_output)
else:
    tester_agent.run(coder_output)
```

### Gemeinsamer Speicher (Shared Memory)
Nutzen Sie den `State` von Antigravity, um Kontext über die gesamte Kette hinweg zu teilen, ohne dass jeder Agent den gesamten Verlauf lesen muss.

## Best Practices
- **Kleine Schritte**: Halten Sie die Aufgaben pro Agent so klein wie möglich.
- **Klare Schnittstellen**: Definieren Sie genau, in welchem Format (z.B. JSON) die Agenten kommunizieren sollen.
- **Fehlerbehandlung**: Implementieren Sie Retries für einzelne Glieder der Kette.
