# One-Eval

One-Eval is a graph-based evaluation framework built on top of DataFlow-Agent, designed to transform model evaluation from a static endpoint into a dynamic, traceable, and interactive process.

It reuses the serving and infrastructure layers of dataflow_agent, while introducing three core abstractions — Graph, Node, and State to describe a complete evaluation workflow, from natural-language task specification (NL-to-Bench) to metric planning and final report generation.

This repository is in its early stage, focusing on a minimal working One-Eval Graph as the foundation for future human-in-the-loop and multi-model evaluation capabilities.