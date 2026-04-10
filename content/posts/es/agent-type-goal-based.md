---
lang: es
title: Tipo de agente de IA — Agentes basados en objetivos
slug: agent-type-goal-based
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [OpenAI, API, ChatGPT]
summary: Agentes que evalúan acciones según si acercan a un objetivo definido.
status: published
---

# Agentes basados en objetivos

Los agentes basados en objetivos no solo reaccionan: eligen acciones que ayudan a alcanzar un estado meta.

Es la mentalidad del «planificador»: definir un objetivo, evaluar posibles pasos siguientes y ejecutar el mejor camino.

## Cómo funciona (arquitectura)

1. Definir objetivo y restricciones.
2. Generar candidatos de plan.
3. Seleccionar la siguiente acción hacia el objetivo.
4. Ejecutar y observar el resultado.
5. Replanificar hasta lograr el objetivo o abortar.

## Ejemplos típicos de objetivos

- «Crear un informe de mercado en 30 minutos con fuentes.»
- «Automatizar el emparejamiento de facturas con menos del 1 % de error.»
- «Concertar reuniones con leads cualificados esta semana.»

## Mejores casos de uso

- Flujos de finalización de tareas
- Planificación en varios pasos
- Comportamiento asistente estructurado
- Pipelines de investigación y síntesis
- Codificación y refactorización asistida por agentes

## Compromisos

- Requiere definición clara del objetivo
- El coste de planificación puede crecer rápido
- Objetivos mal definidos generan errores con confianza

## Ejemplos en empresas y servicios

- OpenAI — asistentes orientados a objetivo con la API Responses + herramientas (búsqueda web, archivos, ejecución de código, APIs externas).  
  Rango aproximado de API: **0,20/1,25** a **2,50/15 USD** por 1M de tokens entrada/salida en muchos niveles estándar.
- Anthropic Claude — flujos de planificación con herramientas para investigación, redacción y operaciones.  
  Rango aproximado: a menudo **1/5** a **3/15 USD** por 1M de tokens entrada/salida en niveles habituales.
- Microsoft Copilot / GitHub Copilot — flujos de completar tareas (objetivo = «producir resultado, no solo responder»).  
  Precio habitual: unos **10–39 USD por usuario/mes** según el producto.

## Referencias prácticas de precios (consumidor + API)

- ChatGPT Plus: unos **20 USD/mes** (suscripción web; la API se factura aparte).
- Claude Pro: unos **20 USD/mes** mensual, o equivalente anual de unos **17 USD/mes** en algunas regiones.
- El coste API puede ser menor que las suscripciones con uso ligero, pero mayor con cargas automatizadas intensas.

## Cómo hacer fiables los agentes basados en objetivos

- Escribe criterios explícitos de éxito («terminado significa X»).
- Impón límites de presupuesto (tokens, tiempo, llamadas a herramientas).
- Añade puntos de control tras cada paso importante.
- Exige citas/evidencia en tareas factuales.
- Añade aprobación humana para acciones de alto riesgo.

## Cuándo evitarlos

Evita configuraciones puramente basadas en objetivos cuando:
- Necesitas optimización estricta bajo varios objetivos en conflicto (usa utilidad).
- El entorno cambia continuamente y el modelo debe adaptarse con feedback (añade componentes de aprendizaje).
