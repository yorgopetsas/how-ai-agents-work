---
lang: es
title: Tipo de agente de IA — Agentes basados en utilidad
slug: agent-type-utility-based
date: 2026-04-10
section: agent-type
category: Agent Types
tags: [API, OpenAI, Cloude]
summary: Agentes que puntúan resultados y eligen la acción con mejor equilibrio de utilidad.
status: published
---

# Agentes basados en utilidad

Los agentes basados en utilidad ordenan opciones por preferencia, coste, riesgo o recompensa y eligen la acción de mayor utilidad esperada.

A diferencia de los basados en objetivos (que preguntan «¿esto alcanza el objetivo?»), los basados en utilidad preguntan «¿qué opción da el mejor valor global?».

## Cómo funciona (arquitectura)

1. Definir función de utilidad (fórmula de puntuación).
2. Generar acciones candidatas.
3. Estimar la utilidad de cada candidata.
4. Elegir la de mayor utilidad esperada.
5. Actualizar pesos según los resultados.

## Ejemplo de función de utilidad

`utilidad = 0,5 * calidad + 0,3 * velocidad + 0,2 * eficiencia_coste - penalizacion_riesgo`

Puedes ajustar pesos para cada contexto de negocio.

## Mejores casos de uso

- Optimización de compromisos (velocidad frente a calidad, coste frente a fiabilidad)
- Priorización bajo restricciones
- Sistemas de decisión con objetivos medibles
- Enrutado de modelos consciente del presupuesto
- Clasificación de anuncios y recomendaciones

## Compromisos

- Diseñar la utilidad es difícil
- Métricas equivocadas producen comportamiento equivocado
- Requiere buena telemetría y monitorización

## Ejemplos en empresas y servicios

- Enrutado de modelos OpenAI / Anthropic en producción — elegir nivel de modelo por petición según coste, latencia y calidad.  
  Ejemplos aproximados de API: OpenAI a menudo de **0,20/1,25** hasta **2,50/15 USD** por 1M de tokens; Anthropic de **1/5** a **3/15 USD** en niveles habituales.
- IA en centros de contacto en la nube — enrutar conversaciones por valor/riesgo (autoservicio frente a escalado humano).  
  Precio habitual: asiento + uso; frecuentemente **30–150+ USD por asiento/mes** según plataforma.
- Sistemas de recomendación en comercio — maximizar conversión controlando margen y riesgo de devoluciones.  
  Perfil de coste: infraestructura + uso de modelos; muy variable por tráfico.

## Dimensiones de utilidad que conviene seguir

- Puntuación de calidad de respuesta
- Tiempo hasta completar
- Coste total por tarea exitosa
- Tasa de escalado humano
- Tasa de error / rollback

## Modos de fallo habituales

- Optimizar una métrica mientras se daña otra (por ejemplo, coste mínimo pero mal resultado para el usuario).
- «Juego» de la utilidad (atajos que inflan la puntuación pero perjudican el valor de negocio).
- Faltan penalizaciones por cumplimiento o riesgo de marca.

## Lista de implementación

- Empieza solo con 3–5 dimensiones de utilidad.
- Normaliza puntuaciones a rangos comparables.
- Añade restricciones duras antes de puntuar (política, legal, seguridad).
- Recalibra pesos mensualmente con datos reales de producción.
