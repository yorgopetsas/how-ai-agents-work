---
lang: es
title: Tipo de agente de IA — Agentes de reflejo simple
slug: agent-type-simple-reflex
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [Open-Source, API, ChatGPT]
summary: Agentes basados en reglas que reaccionan solo a la entrada actual, sin memoria.
status: published
---

# Agentes de reflejo simple

Los agentes de reflejo simple siguen reglas condición–acción:

- Si ocurre la condición A, haz la acción B.
- Sin memoria de estados anteriores.
- Sin planificación.

En resumen: es el estilo de agente más rápido y fácil de poner en producción cuando el entorno es estable y las reglas son claras.

## Cómo funciona (arquitectura)

1. Recibir entrada o evento.
2. Comparar la entrada con reglas fijas.
3. Ejecutar la acción predefinida.
4. Fin del ciclo.

A menudo se implementa con disparadores de eventos, manejadores de webhooks o enrutado por políticas sin memoria a largo plazo.

## Mejores casos de uso

- Automatización determinista
- Alertas y umbrales
- Entornos muy estables
- Enrutado básico de leads
- Filtros de seguridad y cumplimiento de políticas

## Ejemplos en empresas y servicios

Estos productos no siempre se etiquetan como «reflejo simple», pero muchas funciones se comportan así internamente:

- OpenAI — `omni-moderation-latest` (comprobaciones de política, decisiones tipo permitir/bloquear).  
  Precio aproximado: **gratis** (endpoint de moderación de la API; revisa los límites actuales).
- Anthropic — comprobaciones de guardrails o capa de política delante de las llamadas al modelo.  
  Precio aproximado: depende del modelo; en producción suele rondar **1–15 USD por 1M de tokens de salida** en muchos modelos.
- Automatizaciones estilo Zapier / Make — flujos «si disparador entonces acción».  
  Precio aproximado: habitualmente **0–20+ USD/mes** según plan y volumen de tareas.

## Perfil de coste (orientativo)

- Complejidad de construcción: **baja**
- Coste en ejecución: **bajo**
- Latencia típica: **muy baja**
- Ideal para: tareas de alto volumen y baja complejidad

## Limitaciones

- Fallan con la ambigüedad
- No razonan en tareas largas
- Repiten errores
- No se adaptan salvo que humanos actualicen las reglas

## Cuándo usar o evitar

Úsalos cuando:
- Necesitas fiabilidad frente a creatividad.
- La política se puede escribir como reglas claras.
- Cumplimiento y predictibilidad son lo principal.

Evítalos cuando:
- La tarea exige planificación, memoria u optimización.
- Las entradas son difusas, incompletas o cambian a menudo.

## Patrón rápido de implementación

- Pon primero una puerta reflex (reglas baratas).
- Escala solo los casos dudosos a un agente basado en objetivos o en utilidad más fuerte.
- Registra semanalmente los fallos de reglas para mejorar la cobertura.
