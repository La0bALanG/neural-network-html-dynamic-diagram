# Design Principles

Use these rules when building neural-network HTML dynamic diagrams.

## Layout

- Put the usable diagram first. Do not create a marketing hero page.
- Prefer clear teaching bands: source/input, mapping/embedding, main computation, formulas, legend.
- For sequence models, use horizontal token/time-step lanes and a separate zoomed cell when the internal operation is complex.
- For architectures, show layers in construction order and animate the connecting edges.
- For forward/backward passes, use opposite colors or directions for activations and gradients.
- Keep section cards shallow. Do not nest decorative cards inside cards unless the inner element is a repeated item or formula panel.

## Visual Encoding

- Use SVG for architecture diagrams, gates, equations, arrows, tensor blocks, and timelines.
- Use Canvas when many moving particles or continuous fields are needed.
- Use Three.js for meaningful 3D tensors/cubes/layer stacks; verify the canvas is nonblank.
- Use color consistently:
  - Inputs/tokens: blue.
  - IDs/lookup/state maps: green.
  - Embeddings/formulas: purple.
  - Main computation/current step: amber/orange.
  - Gradients/errors: red/rose.
  - Outputs/final state: pink or bright green.

## Animation

- Model animation as explicit phases in a JS data array.
- Update all linked visuals from one state object: active token/layer, formula, metrics, arrows, and notes.
- Include play/pause, reset, previous/next, and speed controls for multi-step diagrams.
- Use particles or dashed strokes only to clarify data flow; keep them subtle enough that labels remain readable.
- Support manual stepping so the user can study a single phase.

## Typography And Fit

- Avoid viewport-scaled font sizes except for top-level headings.
- Use `minmax(0, 1fr)`, `overflow-x: auto`, `white-space` deliberately, and `word-break: normal` for formula/status panels.
- Do not let explanatory text collapse into a narrow vertical column.
- Check long Chinese labels and formula text at desktop and mobile widths.

## Reference Images

When the user provides a reference image:

- Preserve the conceptual structure and labels.
- Recreate the teaching intent, not pixel-perfect decoration.
- Match section order, color semantics, and annotation density.
- Improve defects if the reference has cramped text or ambiguous arrows.
