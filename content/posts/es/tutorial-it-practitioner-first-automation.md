---
lang: es
title: Carril IT — Primer agente de automatización (poco código)
slug: tutorial-it-practitioner-first-automation
date: 2026-04-09
section: tutorial
difficulty: it-ops
category: Tutorial
tags: [IT, Automation, APIs, Ops]
summary: Carril de marcador para operaciones IT: integraciones, runbooks y scripting ligero. Tutoriales estilo ops sustituirán este esqueleto.
status: published
---

## Para qué es este carril

El **carril IT** va dirigido a personas con **experiencia en IT** (redes, administración SaaS, tickets, incidencias) cómodas con **poco código**: scripts, APIs y configuración, no ingeniería de producto completa.

> **Estado:** contenido provisional. Aquí irán tutoriales estilo operaciones (runbooks, listas de comprobación y patrones de integración).

---

## Resultados (borrador)

Los tutoriales futuros deberían permitir:

- Conectar un agente a **herramientas internas** con seguridad (solo lectura al principio)
- Usar **claves API y variables de entorno** sin filtrarlas en tickets
- Bocetar un **runbook**: disparador → paso del agente → aprobación humana → registro
- Medir **coste y modos de fallo** como cualquier otro servicio

---

## Esqueleto de runbook (marcador)

### R1 — Entorno

- *Marcador:* endpoint de modelo aprobado (local vs. proveedor)
- *Marcador:* listas de permitidos de red y comprobaciones DNS

### R2 — Identidad y secretos

- *Marcador:* cuenta de servicio vs. tokens personales
- *Marcador:* rotación y almacenamiento en vault

### R3 — Primera automatización

- *Marcador:* «carpeta vigilada / webhook → el agente resume → publica en Slack»
- *Marcador:* modo simulación y reversión

### R4 — Operaciones

- *Marcador:* registro, límites de tasa y alertas
- *Marcador:* respuesta a incidentes cuando el agente entra en bucle o alucina

---

## Siguiente paso

Empareja este carril con la **ruta de código** en **Construye tu primer agente de IA (2 rutas gratuitas)** (Python + Ollama) y extiéndelo a tu stack real (ticketing, CMDB, CLI cloud) con la misma disciplina que en cualquier integración en producción.
