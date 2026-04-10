---
lang: es
title: Tipo de agente de IA — Sistemas multiagente
slug: agent-type-multi-agent-systems
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [Open-Source, API, Cloude, OpenAI]
summary: Varios agentes especializados coordinados para resolver tareas complejas.
status: published
---

# Sistemas multiagente (MAS)

Los sistemas multiagente reparten el trabajo entre roles especializados (por ejemplo: planificador, investigador, ejecutor, revisor).

Es útil cuando un «agente general» se vuelve demasiado lento, caro o propenso a error en flujos complejos.

## Cómo funciona (arquitectura)

1. El orquestador recibe la tarea.
2. La tarea se descompone en subtareas.
3. Los agentes especialistas ejecutan en secuencia o en paralelo.
4. Un agente revisor/crítico valida salidas.
5. El orquestador fusiona el resultado final.

## Reparto típico de roles

- Planificador: convierte la petición en grafo de tareas
- Investigador: reúne evidencia y fuentes
- Constructor/ejecutor: realiza pasos de implementación
- Revisor: calidad, política y coherencia

## Mejores casos de uso

- Flujos complejos
- Subtareas en paralelo
- Separación de responsabilidades
- Procesos largos con bucles de revisión
- Operaciones multifunción (ops + legal + finanzas + producto)

## Compromisos

- Más sobrecarga de orquestación
- Depuración y evaluación más difíciles
- El coste puede subir rápido sin enrutado estricto

## Ejemplos en empresas y servicios

- Ecosistema OpenAI: muchos equipos implementan planificador + ejecutor con herramientas + crítico con llamadas a herramientas de la API.  
  Rango aproximado de API (según modelo): unos **0,20/1,25** a **2,50/15 USD** por 1M de tokens entrada/salida en niveles estándar habituales.
- Ecosistema Anthropic: flujos Claude multietapa con prompts especializados por rol y pipelines de herramientas.  
  Rango aproximado: a menudo **1/5** a **3/15 USD** por 1M de tokens entrada/salida en niveles habituales.
- Suites empresariales de automatización de procesos: orquestan agentes especializados para soporte, ops de ventas, informes y cumplimiento.  
  Modelo de precio habitual: asiento/suscripción + uso; a menudo **20–150+ USD por usuario/mes** más costes de API.

## Estrategia de gestión de costes

- Enruta subtareas simples a modelos de bajo coste.
- Reserva modelos premium solo para razonamiento difícil o revisión final.
- Cachea resultados intermedios.
- Fija máximo de rondas por agente (para evitar bucles).

## Estrategia de fiabilidad

- Contratos explícitos entre agentes (esquema entrada/salida).
- Exige citas de los agentes investigadores.
- Reglas de veto del revisor para errores de política y hechos.
- Mantén trazas completas de ejecución para depurar.

## Cuándo elegir MAS

Elige MAS cuando:
- Un pipeline de un solo agente falla en calidad o mantenibilidad.
- Necesitas flujos paralelos con propiedad clara.
- Necesitas auditoría y controles a nivel de rol.

Evita MAS cuando:
- La tarea es corta y determinista (usa reflejo o reflejo basado en modelo).
- El equipo no puede mantener orquestación e infraestructura de evaluación.
