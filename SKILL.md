---
name: neural-network-html-dynamic-diagram
description: Create polished standalone HTML/CSS/JS dynamic diagrams for neural-network models and machine-learning algorithms. Use when the user asks to 绘制/制作/生成/复现 a “HTML 动态图示”, “动态图”, “动态计算过程”, “forward pass/前向计算”, “backpropagation/反向传播”, “网络结构图”, or similar visualization for algorithms such as CNN, RNN, LSTM, GRU, Transformer, attention, normalization, optimizers, loss functions, or any neural-network architecture; also use when the user provides or references a paper, formula, screenshot, or reference image that should guide the diagram.
---

# Neural Network HTML Dynamic Diagram

## Goal

Produce a self-contained `.html` file that teaches a neural-network algorithm through synchronized visual states: tensors/layers, formulas, numeric or symbolic values, arrows/data flow, and step-by-step animation.

Prefer a single standalone HTML file using inline CSS and JavaScript unless the user explicitly asks to modify an existing project.

## Workflow

1. **Collect source truth**
   - Use the user's description, uploaded/reference images, local PDFs, papers, formulas, screenshots, or existing code.
   - If details are ambiguous or likely to be misremembered, browse for authoritative sources before drawing. Prefer original papers, arXiv, official docs, framework docs, or reputable course notes.
   - If a local file is referenced, inspect it directly. For images, view the image and extract layout/labels visually. For papers/PDFs, extract text and render pages when useful.

2. **Decompose the algorithm**
   - Identify inputs, outputs, tensor shapes, recurrence/time steps, parameters, formulas, and state variables.
   - Split the process into animation phases such as input/tokenization, embedding, layer construction, gate computation, loss calculation, gradient flow, or parameter update.
   - For forward/backward diagrams, show both the mathematical equation and the visual data path.

3. **Plan the visual**
   - Match the user's reference image when provided: section order, labels, color families, hierarchy, and annotation style.
   - Choose SVG for precise diagrams, Canvas for dense particles/fields, and Three.js only when real 3D tensor/layer structure is central.
   - Include controls: play/pause, reset, previous/next step, and speed when the animation has multiple phases.
   - Make dynamic states synchronized across rows, formulas, arrows, and metrics.

4. **Implement**
   - Create a clearly named HTML file in the current workspace, such as `lstm_forward_visualization.html` or `transformer_attention_dynamic_diagram.html`.
   - Use semantic HTML sections, inline CSS variables, and JS data arrays for tokens/layers/phases instead of hard-coded duplicated DOM.
   - Keep the first viewport useful: the actual diagram should appear immediately, not a landing page.
   - Ensure text does not collapse into narrow columns, overlap, or get clipped at normal desktop widths.

5. **Validate**
   - Run syntax checks on inline JavaScript, for example with Node `new Function(...)`.
   - Run `scripts/validate_html_diagram.py <file.html>` for structural checks.
   - If a browser/runtime is available, open or screenshot the page and inspect the critical viewports. Fix overlap, blank SVG/canvas, broken controls, and cramped text.
   - If browser validation is unavailable, state that limitation briefly in the final response.

## Output Contract

The final HTML should include:

- A descriptive title and visible heading.
- The algorithm's main phases as animated steps.
- Formula panels synchronized with the current visual step.
- Arrows/particles/highlights that show data flow or gradient flow.
- Labels for tensor shapes, variables, gate names, layer names, or parameter updates.
- A short legend when symbols, colors, or operation nodes are used.
- Responsive constraints that preserve readability on desktop and avoid broken mobile layout.

## References

Read these only when needed:

- `references/design-principles.md` for visual and interaction rules.
- `references/neural-network-breakdown.md` for algorithm decomposition patterns.
- `references/quality-checklist.md` before final validation.

## Bundled Helpers

- `scripts/new_diagram_from_template.py`: copy the bundled standalone HTML template to a target path.
- `scripts/validate_html_diagram.py`: static checks for generated HTML diagrams.
- `assets/html-template/index.html`: minimal dynamic-diagram starter template.
