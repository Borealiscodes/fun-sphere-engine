# Fun‑Sphere Engine — Mathematical Spine

Module 2: Laplacian Geometry & Spectral Structure

---

1. Purpose
This module defines the formal Laplacian framework used in the Fun‑Sphere Engine.  
It establishes:

- Discrete Laplacian construction  
- Spectral properties  
- Positive semi‑definiteness  
- Perturbation stability  
- Curvature interaction  
- Eigenstructure behavior  

This is the mathematical foundation for spectral ecology, holonomy interaction, and manifold‑based narrative physics.

---

2. Preliminaries

2.1 State Manifold
Let \( \mathcal{M} \) be the Fun‑Sphere narrative manifold.

Each point \( p \in \mathcal{M} \) contains:

- scalar fields \( f(p) \)  
- vector fields \( v(p) \)  
- curvature annotations \( \kappa(p) \)  
- spectral fields \( \lambda(p) \)  

---

2.2 Graph Structure
The manifold is discretized into a graph:

\[
G = (V, E)
\]

where:

- \( V \) are narrative zones  
- \( E \) are adjacency relations  
- weights encode curvature and operator bias  

---

3. Discrete Laplacian

3.1 Definition
For a scalar field \( f : V \rightarrow \mathbb{R} \), the Laplacian is:

\[
(\Delta f)(i) = f(i) - \frac{1}{di} \sum{j \sim i} w_{ij} f(j)
\]

where:

- \( di = \sum{j \sim i} w_{ij} \) is weighted degree  
- \( w_{ij} \) encodes curvature and operator influence  

---

3.2 Matrix Form
The Laplacian matrix is:

\[
L = D - W
\]

with:

- \( D \) diagonal degree matrix  
- \( W \) weighted adjacency matrix  

---

4. Properties

4.1 Symmetry
\[
L = L^\top
\]

4.2 Positive Semi‑Definiteness
\[
x^\top L x \ge 0
\]

This ensures spectral stability.

4.3 Zero Eigenvalue
\[
\lambda_0 = 0
\]

with eigenvector:

\[
\mathbf{1} = (1, 1, \ldots, 1)
\]

representing the neutral manifold.

---

5. Curvature Interaction

Curvature modifies weights:

\[
w{ij} = w{ij}^{(0)} + \kappa_{ij}
\]

where \( \kappa_{ij} \) is curvature induced by operator non‑commutativity.

Holonomy contributes:

\[
\kappa{ij} = \Delta{\text{hol}}(Oi, Oj)
\]

Thus:

- flat regions → standard Laplacian  
- curved regions → warped Laplacian  

This is the geometric basis of narrative tension.

---

6. Spectral Ecology

Eigenvectors of \( L \) define monster families:

\[
L uk = \lambdak u_k
\]

where:

- \( u_k \) is a spectral creature profile  
- \( \lambda_k \) is its ecological “energy level”  

6.1 Evolution
Perturbations in curvature cause eigenvalue drift:

\[
\lambdak' = \lambdak + \delta \lambda_k
\]

This models monster evolution.

---

7. Perturbation Stability

For small curvature perturbations \( \epsilon \):

\[
L' = L + \epsilon K
\]

Eigenvalues satisfy:

\[
|\lambdak' - \lambdak| \le \epsilon \|K\|
\]

This ensures:

- stable ecology  
- predictable spectral behavior  
- bounded narrative tension  

---

8. Laplacian in Reversible Quests

Quest paths modify curvature, which modifies weights, which modifies the Laplacian.

Thus:

- quests change spectral ecology  
- spectral ecology changes monster behavior  
- monster behavior changes narrative physics  

This is the full geometric feedback loop.

---

9. Verification Requirements

The Laplacian must satisfy:

- symmetry  
- positive semi‑definiteness  
- stable eigenstructure  
- JSON‑safe representation  
- deterministic construction  
- curvature‑aware weighting  

Wave‑T tests confirm these properties.

---

10. Status
This module is complete and ready for integration into:

- holonomy spine  
- spectral ecology spine  
- reversible quest spine  
- preprint.md  

---

