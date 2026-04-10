---
lang: es
title: Tipo de agente de IA — Agentes de reflejo basados en modelo
slug: agent-type-model-based-reflex
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [Open-Source, API, Cloude]
summary: Agentes reflexivos con estado interno para entornos parcialmente observables.
status: published
---

# Agentes de reflejo basados en modelo

Los agentes de reflejo basados en modelo amplían el reflejo simple con un modelo de estado interno.

Guardan memoria breve del entorno (qué ocurrió antes) y siguen usando reglas de estilo reflexivo para actuar.

## Cómo funciona (arquitectura)

1. Observar la entrada actual.
2. Actualizar el estado interno (contexto reciente, estado, últimas acciones).
3. Aplicar reglas usando entrada y estado.
4. Ejecutar la acción.

Es habitual en bots de soporte, bots de flujo y asistentes con estado cuando «solo el mensaje actual» no basta.

## Mejores casos de uso

- Entornos donde no todo es visible a la vez
- Sistemas que necesitan memoria corta
- Flujos con estado
- Asistentes conscientes de la sesión
- Gestión de incidentes con transiciones de estado

## Compromisos

- Mejor que sistemas puramente reflexivos
- Aún más débiles que planificadores basados en objetivos/utilidad para tareas complejas
- El diseño del estado puede volverse frágil si no se versiona

## Ejemplos en empresas y servicios

Ejemplos donde el comportamiento reflexivo con estado es común:

- OpenAI — flujos de la API Responses con llamadas a herramientas que mantienen estado de conversación y salidas de herramientas en contexto.  
  Rango aproximado de API: de unos **0,20 USD entrada / 1,25 USD salida** hasta **2,50 USD entrada / 15 USD salida por 1M de tokens** según la clase de modelo.
- API de Anthropic Claude — chat y sesiones con herramientas donde las decisiones dependen de turnos anteriores.  
  Rango aproximado: unos **1 USD entrada / 5 USD salida** a **3 USD entrada / 15 USD salida por 1M de tokens** en muchos niveles habituales.
- Plataformas de soporte (Salesforce, complementos IA de Zendesk, Intercom AI) — el estado del ticket y los pasos previos influyen en la siguiente acción.  
  Precio habitual: suscripción o por asiento; a menudo **decenas o cientos de USD por asiento/mes** más uso.

## Consejos de diseño

- Mantén el estado mínimo y explícito (`etapa`, `ultima_accion`, `confianza`).
- Añade tiempo de caducidad para estado obsoleto.
- Guarda el estado crítico en servidor, no solo en prompts.
- Añade respaldo: si el estado es inconsistente, deriva a humano o reinicia con seguridad.

## Cuándo elegir este tipo

Elige reflejo basado en modelo antes que basado en objetivos si:
- El proceso es mayormente determinista.
- Necesitas memoria corta pero no planificación completa.
- Quieres baja latencia y baja complejidad operativa.
