# Neural Network HTML Dynamic Diagram

A Codex skill for creating polished, standalone HTML/CSS/JS dynamic diagrams for neural-network models and machine-learning algorithms.

Use it when you want Codex to turn an algorithm, paper, formula, screenshot, or short description into an interactive visual explanation, especially for:

- Forward pass / 前向计算
- Backpropagation / 反向传播
- Network architecture construction
- Tensor shape flow
- RNN/LSTM/GRU recurrence
- Transformer attention
- CNN convolution / pooling / normalization
- Optimizers, losses, and update rules

## Trigger Examples

After installing the skill, prompts like these should trigger it:

```text
帮我绘制 LSTM 前向计算的 HTML 动态图示。
```

```text
根据这张参考图，生成 Transformer Self-Attention 的 HTML 动态演示。
```

```text
我正在学 BatchNorm，请画一个前向计算和反向传播的动态图。
```

```text
复现 AlexNet 原论文网络结构图，并用 HTML 展示动态构建过程。
```

## What The Skill Produces

The skill guides Codex to produce a self-contained `.html` file with:

- Inline HTML/CSS/JS, no build step by default
- Step-by-step animation phases
- Play/pause, reset, previous/next, and speed controls when useful
- Formula panels synchronized with visual highlights
- Tensor/layer/state labels and shapes
- Animated arrows, particles, or highlighted paths for data flow or gradient flow
- Responsive layout checks for common desktop and mobile widths

## Installation

Clone or copy this folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/La0bALanG/neural-network-html-dynamic-diagram.git \
  ~/.codex/skills/neural-network-html-dynamic-diagram
```

If you already cloned it elsewhere, copy it:

```bash
cp -R neural-network-html-dynamic-diagram ~/.codex/skills/
```

Then start a new Codex session so the skill metadata can be discovered.

## Repository Structure

```text
neural-network-html-dynamic-diagram/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── html-template/
│       └── index.html
├── references/
│   ├── design-principles.md
│   ├── neural-network-breakdown.md
│   └── quality-checklist.md
└── scripts/
    ├── new_diagram_from_template.py
    └── validate_html_diagram.py
```

## Helper Scripts

Create a starter HTML file from the bundled template:

```bash
python3 scripts/new_diagram_from_template.py ./demo_diagram.html \
  --title "Demo Neural Network Dynamic Diagram"
```

Run static checks on a generated HTML diagram:

```bash
python3 scripts/validate_html_diagram.py ./demo_diagram.html
```

These checks look for basic standalone HTML structure, viewport metadata, inline script presence, visual surfaces such as SVG/canvas, and obvious animation controls.

## Workflow Encoded In The Skill

The skill tells Codex to:

1. Gather source truth from the user's request, uploaded reference images, papers, PDFs, formulas, or web research.
2. Decompose the algorithm into inputs, outputs, tensor shapes, phases, formulas, and state variables.
3. Plan a teaching-oriented visual that matches any reference image when provided.
4. Implement a standalone HTML/CSS/JS dynamic diagram.
5. Validate JavaScript syntax and layout quality before returning the file path.

## License

MIT License. See [LICENSE](LICENSE).
