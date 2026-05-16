# Neural-Network Breakdown Patterns

Use this checklist to transform an algorithm into a dynamic diagram.

## Core Questions

- What is the input object? Example: image tensor, token sequence, hidden state, graph, batch.
- What are the intermediate tensors and their shapes?
- What equations define each step?
- Which variables persist over time? Example: `c_t`, `h_t`, optimizer moments, running mean/variance.
- Which parameters are learned? Example: `W_q`, `W_k`, `W_v`, convolution kernels, gates, affine scale/shift.
- What is the final output?
- What is the minimum example that makes the process concrete?

## Forward Pass

Typical phases:

1. Input preparation.
2. Parameter lookup or layer construction.
3. Core operation, such as convolution, attention score, gate computation, normalization, recurrence, or activation.
4. Combination/update step.
5. Output generation and transfer to next layer/time step.

Show formulas next to the visual state. Highlight the formula line being executed.

## Backpropagation

Typical phases:

1. Loss signal starts at the output.
2. Local derivative at the current node/layer.
3. Chain-rule multiplication through edges.
4. Gradient accumulation where branches merge.
5. Parameter gradient computation.
6. Optimizer update.

Use a second visual direction for gradients and label `dL/d...` or `∂L/∂...` values.

## Architecture Construction

Typical phases:

1. Input tensor.
2. Each layer appears in order.
3. Connections animate after target layer appears.
4. Pooling/normalization/dropout/residual/skip connections appear where specified.
5. Final classifier/head/output appears.

Use authoritative shapes and hyperparameters from the source paper or user-provided material.

## Sequence Models

For RNN/LSTM/GRU/Transformer sequence diagrams:

- Show tokens, IDs, embeddings, and time positions when relevant.
- Keep a zoomed single-cell view for internals.
- Keep the expanded sequence view for recurrence or attention flow.
- Synchronize token highlight with current equation and current cell/layer.

## Numeric Examples

Use small illustrative values only when they help. Mark them as examples. Do not invent source-specific hyperparameters; research or ask when exact values matter.
