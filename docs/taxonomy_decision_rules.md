# Taxonomy Decision Rules

This document describes the decision rules used to classify Visual Foundation Models (VFMs) in our task-centric taxonomy.

## Rule R1: Primary Output

A model is classified according to its primary output.

* If the output is newly synthesized visual content (image, video, or 3D asset), the model is classified as Generative.
* If the output is a structured interpretation of visual input (label, mask, embedding, depth map, correspondence), the model is classified as Discriminative.

## Rule R2: Unified Interface

If a single model combines visual understanding and generation through a shared multimodal interface, it is classified as Hybrid/Unified.

## Rule R3: Dominant Use

When a model is reused inside a larger pipeline, classification is determined by the model's standalone output rather than the output of the complete pipeline.

## Example Assignments

| Model                 | Category       |
| --------------------- | -------------- |
| Stable Diffusion      | Generative     |
| DALL-E                | Generative     |
| CLIP                  | Discriminative |
| DINOv2                | Discriminative |
| SAM                   | Discriminative |
| NeRF                  | Discriminative |
| 3D Gaussian Splatting | Discriminative |
| LLaVA                 | Hybrid/Unified |
| GPT-4V                | Hybrid/Unified |

## Purpose

The taxonomy is designed to organize visual foundation models according to their functional role in visual computing pipelines rather than architectural lineage.
