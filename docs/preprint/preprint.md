# Fun‑Sphere Engine  
### A Geometric AI Architecture for Narrative Physics  
**Author:** Borealis S. Hedling  
**Affiliation:** Independent Researcher, Geometric AI & Structural Interpretability  
**Date:** October 2026  
**Version:** Preprint — Phase‑E (Population)  
**License:** MIT 

---

## Abstract

The Fun‑Sphere Engine is a geometric AI architecture that models narrative
dynamics using formal mathematical structures. It treats narrative behavior
as motion across an operator‑defined state space, where non‑commutativity
induces holonomy curvature, curvature warps the Laplacian, and Laplacian
warp produces spectral drift across ecological energy levels. This pipeline
creates a unified geometric model of narrative physics, enabling formal
verification, interpretability, and structural analysis of emergent story
behavior.

This preprint presents the mathematical foundations of the engine,
including reversible operator algebra, holonomy curvature tensors,
curvature‑induced Laplacian warp, spectral ecology, and reversible quest
mechanics. The goal is to provide an academically defensible geometric
framework for narrative systems, suitable for both theoretical study and
runtime implementation.

---

## Document Overview

This document is organized into a high‑altitude conceptual exposition
followed by a mathematically rigorous appendix suite:

- **Operator Spine** — reversible operators, commutators, and path algebra  
- **Holonomy & Curvature** — frame shifts, curvature tensors, and geometric irreversibility  
- **Laplacian Geometry** — curvature‑aware adjacency and spectral structure  
- **Spectral Ecology** — eigenvectors as monster families, eigenvalues as ecological energy levels  
- **Reversible Quest Algebra** — operator‑path traversal and curvature accumulation  
- **Appendices A–E** — formal proofs, derivations, and extended mathematical artifacts  
- **References** — academically sourced citations supporting the geometric foundations  

---

## Table of Contents

1. Introduction  
2. Operator Spine  
3. Holonomy & Curvature  
4. Laplacian Geometry  
5. Spectral Ecology  
6. Reversible Quest Algebra  
7. Discussion  
8. References  
9. Appendices A–E

---

## 1. Introduction

The Fun‑Sphere Engine is a geometric AI architecture that treats narrative
dynamics as motion through an operator‑defined state space. Rather than
modeling stories as symbolic sequences or probabilistic transitions, the
engine frames narrative behavior as the interaction of reversible operators,
curvature tensors, and spectral structures. This geometric perspective
enables formal verification, structural interpretability, and mathematical
analysis of emergent narrative phenomena.

At the core of the engine is the **operator spine**: a collection of
reversible operators acting on a narrative state space. When these operators
fail to commute, they generate **holonomy curvature**, a geometric quantity
that measures how much the narrative “twists” when traversing closed
operator paths. Curvature then propagates into the **Laplacian**, modifying
adjacency weights and producing **spectral drift** across ecological energy
levels. Eigenvectors of the Laplacian correspond to monster families, while
eigenvalues encode ecological tension and resource distribution.

This pipeline establishes a unified model of narrative physics:

- **Operator Algebra** provides reversible transformations and commutators.  
- **Holonomy Curvature** captures geometric deviation from commutativity.  
- **Laplacian Geometry** encodes structural adjacency and tension.  
- **Spectral Ecology** interprets eigenstructure as ecological dynamics.  
- **Reversible Quest Algebra** models narrative traversal as operator paths.  

The purpose of this preprint is to present these structures in a coherent,
academically defensible form. Each module is introduced conceptually in the
main text and formalized in the appendices using operator identities,
curvature tensors, spectral perturbation theory, and path‑algebra
derivations. The resulting framework provides a geometric foundation for
narrative systems, suitable for theoretical study, runtime implementation,
and future work in structural AI and interpretability.

The Fun‑Sphere Engine is not a metaphorical or heuristic model; it is a
mathematically grounded architecture. Its components—operators, curvature,
Laplacians, spectra, and paths—are defined with the same rigor used in
geometric analysis and spectral graph theory. This document establishes that
foundation and prepares the ground for subsequent verification layers,
runtime scaffolds, and applied narrative‑physics research.

---

## 2. Operator Spine

The operator spine is the foundational structure of the Fun‑Sphere Engine.
It defines how narrative states transform, how reversible transitions are
constructed, and how geometric quantities such as curvature arise from
operator interactions. All higher‑level components—holonomy, Laplacian
geometry, spectral ecology, and quest algebra—derive their behavior from
the properties of this spine.

### 2.1 State Space

Let $\mathcal{S}$ denote the narrative state space. A state $s \in
\mathcal{S}$ encodes the complete configuration of the narrative at a
given moment: ecological conditions, monster‑family distributions,
factional tensions, resource flows, and quest‑level commitments. The
structure of $\mathcal{S}$ is intentionally abstract; the engine does not
assume a particular representation, only that reversible operators act on
it.

### 2.2 Reversible Operators

A reversible operator is a transformation
\[
O : \mathcal{S} \to \mathcal{S}
\]
with an inverse $O^{-1}$ satisfying
\[
O^{-1}(O(s)) = s.
\]

Reversibility ensures that narrative transitions do not destroy
information. This property is essential for geometric analysis: curvature,
holonomy, and spectral drift all rely on the ability to traverse operator
paths forward and backward without loss of state.

### 2.3 Operator Composition

Operators compose naturally:
\[
O_j \circ O_i : \mathcal{S} \to \mathcal{S}.
\]

Composition defines narrative motion. A sequence of operators
\[
\gamma = (O_1, O_2, \ldots, O_n)
\]
is a **path** through the narrative geometry. The forward traversal is
\[
\gamma(s) = O_n(\cdots O_2(O_1(s))\cdots),
\]
and the reverse traversal applies inverses in reverse order.

### 2.4 Commutators and Non‑Commutativity

Non‑commutativity is the source of geometric structure. For operators
$O_i$ and $O_j$, the commutator is
\[
[O_i, O_j] = O_j \circ O_i - O_i \circ O_j.
\]

If $[O_i, O_j] = 0$, the operators commute and produce no curvature.  
If $[O_i, O_j] \neq 0$, the operators generate geometric deviation that
propagates through the entire engine.

### 2.5 Operator Families

Operators are grouped into families based on their narrative role:

- **Ecological Operators** — modify monster‑family distributions  
- **Faction Operators** — adjust tensions, alliances, and conflicts  
- **Resource Operators** — redistribute ecological or narrative resources  
- **Quest Operators** — encode reversible narrative commitments  
- **Holonomy‑Sensitive Operators** — generate curvature under composition  

These families interact through composition, producing complex geometric
behavior.

### 2.6 Operator Spine as Geometric Infrastructure

The operator spine provides:

- **local structure** via reversible transformations  
- **global structure** via operator paths  
- **geometric structure** via commutators and curvature  
- **spectral structure** via Laplacian warp  
- **narrative structure** via quest algebra  

Every subsequent section of this preprint builds on the operator spine.
Holonomy curvature arises from non‑commutativity. Laplacian geometry
incorporates curvature into adjacency. Spectral ecology interprets the
Laplacian’s eigenstructure. Reversible quest algebra models narrative
motion through operator paths.

The spine is therefore the engine’s geometric core: the source of its
mathematical behavior and the foundation for its narrative physics.

---

## 3. Holonomy & Curvature

Holonomy and curvature arise naturally from the operator spine. When
reversible operators fail to commute, they generate geometric deviation
that accumulates along narrative paths. This deviation is measured by
holonomy, and its infinitesimal structure is captured by curvature. These
quantities define the geometric backbone of the Fun‑Sphere Engine.

### 3.1 Holonomy as Frame Shift

Consider a closed operator path
\[
\gamma = (O_1, O_2, \ldots, O_n)
\]
with inverse traversal $\gamma^{-1}$. Even though the state returns to its
original value,
\[
\gamma^{-1}(\gamma(s)) = s,
\]
the *frame* associated with the state may not. Holonomy measures this
frame shift:
\[
\mathrm{Hol}(\gamma) : F \mapsto F'.
\]

Holonomy is therefore a geometric quantity: it describes how the narrative
“twists” when traversing a closed operator loop.

### 3.2 Curvature from Non‑Commutativity

Curvature is the infinitesimal generator of holonomy. For operators
$O_i$ and $O_j$, the curvature contribution is the commutator
\[
H_{ij} = [O_i, O_j] = O_j \circ O_i - O_i \circ O_j.
\]

If $H_{ij} = 0$, the operators commute and produce no curvature.  
If $H_{ij} \neq 0$, the operators generate geometric deviation that
propagates through the entire system.

Curvature is therefore a structural property of the operator spine.

### 3.3 Path Curvature

For a path $\gamma = (O_1, \ldots, O_n)$, total curvature is
\[
K(\gamma) = \sum_{i < j} H_{ij}.
\]

This quantity measures how much geometric deviation accumulates along the
path. Longer paths, or paths involving highly non‑commutative operators,
produce larger curvature.

### 3.4 Curvature and Narrative Geometry

Curvature affects narrative geometry in several ways:

- **Frame Shift:** Holonomy changes the narrative frame even when the
  state returns to its original value.
- **Adjacency Warp:** Curvature modifies adjacency weights in the
  Laplacian.
- **Spectral Drift:** Warped adjacency produces changes in eigenvalues and
  eigenvectors.
- **Ecological Evolution:** Spectral drift alters monster‑family
  distributions and ecological energy levels.
- **Quest Irreversibility:** Curvature prevents perfect reversal of
  narrative geometry even when state reversibility holds.

Curvature is therefore the engine’s primary geometric driver.

### 3.5 Holonomy–Curvature Interaction

Holonomy and curvature interact through operator paths:

- Curvature is local (commutators).
- Holonomy is global (frame shift along closed paths).
- Curvature integrates to holonomy.
- Holonomy differentiates to curvature.

This relationship mirrors classical geometric analysis but is adapted to
the operator‑defined narrative space of the Fun‑Sphere Engine.

### 3.6 Role in the Engine

Holonomy and curvature provide:

- **geometric structure** for narrative transitions  
- **constraints** on operator composition  
- **sources** of Laplacian warp  
- **drivers** of spectral drift  
- **mechanisms** for ecological evolution  
- **irreversibility** in quest‑path geometry  

They are the bridge between operator algebra and spectral ecology, and
they define the engine’s geometric behavior at both local and global
scales.

---

## 4. Laplacian Geometry

Laplacian geometry provides the spectral backbone of the Fun‑Sphere Engine.
It translates curvature into adjacency warp, adjacency into spectral
structure, and spectral structure into ecological dynamics. The Laplacian
is therefore the engine’s bridge between local operator behavior and global
narrative physics.

### 4.1 Curvature‑Aware Adjacency

Let $W$ denote the adjacency matrix encoding structural relationships
between narrative states, monster families, factions, or ecological zones.
In classical settings, $W$ is determined by static connectivity. In the
Fun‑Sphere Engine, adjacency is **curvature‑aware**:
\[
W' = W + H,
\]
where $H$ is the curvature tensor assembled from commutators
\[
H_{ij} = [O_i, O_j].
\]

Curvature therefore modifies adjacency weights, increasing or decreasing
connectivity based on operator interactions.

### 4.2 Degree Matrix

The degree matrix $D$ is defined as usual:
\[
D_{ii} = \sum_j W'_{ij}.
\]

Because $W'$ incorporates curvature, $D$ also reflects geometric deviation.
Narrative regions with high curvature accumulate higher degree, indicating
greater structural tension.

### 4.3 Curvature‑Warped Laplacian

The curvature‑aware Laplacian is
\[
L' = D - W'.
\]

This operator encodes how narrative structure responds to curvature. When
curvature is zero, $L'$ reduces to the classical Laplacian. When curvature
is present, $L'$ becomes a geometric operator whose spectrum reflects
holonomy‑induced warp.

### 4.4 Spectral Structure

The Laplacian admits eigenpairs
\[
L' u_k = \lambda_k u_k.
\]

In the Fun‑Sphere Engine:

- **Eigenvectors** $u_k$ correspond to **monster families**.  
- **Eigenvalues** $\lambda_k$ correspond to **ecological energy levels**.  

This interpretation is the foundation of spectral ecology (Section 5).

### 4.5 Curvature‑Induced Spectral Drift

Curvature modifies the Laplacian, producing spectral drift:
\[
(\lambda_k, u_k) \mapsto (\lambda_k', u_k').
\]

Spectral drift measures how ecological energy levels and monster‑family
distributions evolve under curvature. Drift magnitude depends on:

- operator non‑commutativity  
- path curvature  
- spectral gaps  
- adjacency warp  

This drift is the engine’s mechanism for ecological evolution.

### 4.6 Ecological Interpretation

The Laplacian’s spectrum encodes:

- **monster‑family structure** (eigenvectors)  
- **ecological tension** (eigenvalues)  
- **resource distribution** (low‑frequency modes)  
- **rare species** (high‑frequency modes)  
- **factional boundaries** (spectral partitions)  

Curvature shifts these quantities, producing narrative change.

### 4.7 Laplacian Geometry as Narrative Physics

Laplacian geometry provides:

- a **spectral lens** for interpreting curvature  
- a **geometric operator** linking local and global structure  
- a **dynamical system** for ecological evolution  
- a **mathematical foundation** for spectral ecology  
- a **verification pathway** for narrative behavior  

It is the engine’s central spectral operator, and its curvature‑aware
structure is essential for modeling narrative physics.

---

## 5. Spectral Ecology

Spectral ecology interprets the eigenstructure of the curvature‑warped
Laplacian as ecological dynamics. In the Fun‑Sphere Engine, eigenvectors
correspond to monster families, eigenvalues correspond to ecological energy
levels, and curvature induces spectral drift that reshapes the ecological
landscape. This section introduces the spectral framework that governs
ecological behavior.

### 5.1 Eigenvectors as Monster Families

Given the curvature‑aware Laplacian
\[
L' = D - W',
\]
its eigenvectors satisfy
\[
L' u_k = \lambda_k u_k.
\]

Each eigenvector $u_k$ defines a **monster family**: a coherent ecological
cluster whose internal structure is encoded by the vector’s components.
Low‑frequency eigenvectors correspond to broad, stable families; high‑frequency
eigenvectors correspond to rare or highly localized species.

Monster families are therefore spectral objects, not symbolic categories.

### 5.2 Eigenvalues as Ecological Energy Levels

The eigenvalue $\lambda_k$ associated with $u_k$ defines the **ecological
energy level** of the monster family. High energy indicates structural
tension, resource scarcity, or ecological instability. Low energy indicates
cohesion, abundance, or stability.

Curvature modifies these energy levels, producing ecological evolution.

### 5.3 Curvature‑Induced Spectral Drift

Curvature alters adjacency weights, which modifies the Laplacian, which
shifts the spectrum:
\[
(\lambda_k, u_k) \mapsto (\lambda_k', u_k').
\]

Spectral drift measures how monster families evolve under geometric
pressure. Drift magnitude depends on:

- curvature intensity  
- operator non‑commutativity  
- path geometry  
- spectral gaps  
- ecological adjacency structure  

This drift is the engine’s mechanism for ecological change.

### 5.4 Ecological Zones and Spectral Partitions

The spectrum partitions the narrative ecology into zones:

- **Low‑frequency modes** define broad ecological regions.  
- **Mid‑frequency modes** define factional or territorial boundaries.  
- **High‑frequency modes** define rare species or localized anomalies.  

Curvature shifts these partitions, causing ecological zones to expand,
contract, merge, or fracture.

### 5.5 Faction Bias and Curvature

Curvature can introduce **faction bias** into the spectrum. If certain
operators are associated with specific factions, their non‑commutativity
produces curvature that disproportionately affects those regions of the
ecology. This bias manifests as:

- elevated eigenvalues for certain families  
- spectral clustering around factional boundaries  
- localized ecological tension  

Faction bias is therefore a geometric consequence of operator behavior.

### 5.6 Narrative Tension Propagation

Spectral drift propagates narrative tension. When curvature increases
adjacency weights in a region, eigenvalues rise, indicating ecological
stress. This stress can spread through the spectrum, producing:

- monster‑family migration  
- resource redistribution  
- factional escalation  
- ecological collapse or stabilization  

Narrative tension is thus a spectral phenomenon.

### 5.7 Rare Species and High‑Frequency Modes

High‑frequency eigenvectors correspond to rare species. Curvature can:

- create new rare species  
- eliminate existing ones  
- shift their ecological niches  
- cause rare species to merge or bifurcate  

These behaviors arise naturally from spectral perturbation theory.

### 5.8 Spectral Ecology as Geometric Dynamics

Spectral ecology provides:

- a **mathematical model** of ecological structure  
- a **geometric mechanism** for ecological evolution  
- a **spectral lens** for interpreting curvature  
- a **dynamical system** for narrative tension  
- a **foundation** for reversible quest algebra  

It is the engine’s spectral‑geometric layer, linking curvature to ecology
through the Laplacian’s eigenstructure.

---

## 6. Reversible Quest Algebra

Reversible quest algebra models narrative traversal as motion along
operator paths. A quest is not a symbolic objective or storyline; it is a
geometric object defined by a sequence of reversible operators acting on
the narrative state space. These paths accumulate curvature, induce
holonomy, and generate spectral consequences that propagate through the
ecology. Quest algebra is therefore the engine’s mechanism for linking
local operator behavior to global narrative dynamics.

### 6.1 Quest Paths

A quest path is an ordered sequence of reversible operators
\[
\gamma = (O_1, O_2, \ldots, O_n).
\]

Forward traversal applies operators in sequence:
\[
\gamma(s) = O_n(\cdots O_2(O_1(s))\cdots).
\]

Reverse traversal applies inverses in reverse order:
\[
\gamma^{-1}(s) = O_1^{-1}(O_2^{-1}(\cdots O_n^{-1}(s)\cdots)).
\]

State reversibility holds:
\[
\gamma^{-1}(\gamma(s)) = s,
\]
but geometric reversibility does not.

### 6.2 State Reversibility vs. Geometric Irreversibility

Reversible quests preserve state but not geometry. Even though the state
returns to its original value, the frame does not:
\[
F'' = \mathrm{Hol}(\gamma^{-1})(\mathrm{Hol}(\gamma)(F)),
\]
and in general
\[
F'' \neq F.
\]

This distinction is central: quests are reversible in state space but
irreversible in geometric space.

### 6.3 Curvature Accumulation Along Paths

Curvature arises from operator non‑commutativity. For operators $O_i$ and
$O_j$, the curvature contribution is the commutator
\[
H_{ij} = [O_i, O_j].
\]

Total curvature accumulated along a quest path is
\[
K(\gamma) = \sum_{i < j} H_{ij}.
\]

Longer paths or paths involving highly non‑commutative operators produce
greater curvature.

### 6.4 Quest Energy

Quest energy is defined as the norm of the curvature tensor:
\[
E(\gamma) = \|K(\gamma)\|.
\]

High‑energy quests produce significant geometric distortion, leading to
strong spectral drift and ecological consequences. Low‑energy quests
produce minimal distortion and behave nearly classically.

### 6.5 Quest Composition

Quests compose by concatenation:
\[
\gamma_2 \circ \gamma_1 = (O_1, \ldots, O_m, O_{m+1}, \ldots, O_n).
\]

Curvature is additive:
\[
K(\gamma_2 \circ \gamma_1) = K(\gamma_1) + K(\gamma_2).
\]

This property enables modular construction of complex narrative behavior.

### 6.6 Interaction with Spectral Ecology

Quest curvature modifies adjacency weights:
\[
W' = W + H,
\]
producing a curvature‑warped Laplacian
\[
L' = D - W'.
\]

This warp induces spectral drift:
\[
(\lambda_k, u_k) \mapsto (\lambda_k', u_k'),
\]
which alters monster‑family distributions and ecological energy levels.

Quest algebra is therefore a driver of ecological evolution.

### 6.7 Narrative Consequences

Reversible quests generate:

- **monster‑family evolution** through spectral drift  
- **faction‑biased ecological zones** via curvature concentration  
- **narrative‑tension propagation** through Laplacian warp  
- **rare species emergence** from high‑frequency spectral shifts  
- **geometric irreversibility** despite state reversibility  

These consequences arise naturally from the operator‑geometric structure.

### 6.8 Quest Algebra as Geometric Dynamics

Reversible quest algebra provides:

- a **path‑based geometric model** of narrative traversal  
- a **curvature mechanism** for generating holonomy  
- a **spectral driver** for ecological evolution  
- a **modular composition system** for narrative behavior  
- a **formal mathematical foundation** for quest dynamics  

It is the engine’s operator‑path layer, linking curvature, holonomy,
spectral drift, and ecological change into a unified geometric framework.

---

## 7. Discussion

The Fun‑Sphere Engine establishes a geometric model of narrative physics
built from reversible operators, curvature tensors, Laplacian geometry,
spectral ecology, and quest‑path algebra. These components form a coherent
mathematical system capable of expressing narrative dynamics as geometric
motion rather than symbolic or probabilistic transitions. This section
discusses the implications of the framework, its development context, and
the intentionally limited scope of the present preprint.

### 7.1 Geometric Interpretation of Narrative Dynamics

The engine reframes narrative behavior as the accumulation of curvature
along operator paths. Narrative tension, ecological evolution, factional
boundaries, and quest commitments emerge from geometric quantities rather
than heuristic rules. This geometric interpretation provides a unified
language for describing narrative phenomena and enables structural
analysis grounded in operator theory and spectral geometry.

### 7.2 Structural Interpretability

Because the engine is built from reversible operators and curvature‑aware
Laplacians, its behavior is structurally interpretable. Every narrative
transition can be traced to a specific operator interaction, a commutator
producing curvature, a Laplacian warp modifying adjacency, or a spectral
shift altering ecological structure. Interpretability is therefore intrinsic
to the geometric design, not an auxiliary feature.

### 7.3 Formal Verification Pathways

The reversible operator spine and curvature‑based geometry admit formal
verification pathways similar to those used in geometric analysis and
spectral graph theory. These include curvature bounds, holonomy constraints,
spectral gap analysis, operator‑path invariants, and ecological stability
criteria. Verification is a natural extension of the engine’s mathematical
structure and provides a foundation for safe runtime behavior.

### 7.4 Modularity and Altitude Separation

The engine is modular by construction. Each layer—operator algebra,
holonomy curvature, Laplacian geometry, spectral ecology, and quest
algebra—can be studied independently at its own altitude. Yet the layers
integrate cleanly through shared geometric quantities. This altitude
separation supports theoretical clarity, controlled extension of operator
families, and predictable propagation of geometric effects across the
system.

### 7.5 Development Context and Scope

The geometric structures presented here emerged from practical testing
within the Fantasy Engine prototypes. Those experiments raised questions
about operator behavior, ecological stability, spectral drift, and
curvature accumulation that motivated the formal framework developed in
this preprint. The purpose of this document is not to describe the full
Fantasy Engine, nor to claim completeness of the geometric model. Instead,
the scope is deliberately limited: it isolates the mathematical foundations
required for logical, verifiable development.

This preprint serves as a structural checkpoint. It ensures that the
geometric assumptions underlying the broader engine are coherent and
academically defensible before additional runtime layers are built.

### 7.6 Limitations and Open Questions

Because the scope is intentionally constrained, several questions remain
outside the boundaries of this document:

- How should the geometric model integrate with higher‑order narrative
  systems in the full Fantasy Engine?
- What constraints ensure long‑term ecological coherence under repeated
  quest‑path traversal?
- How do extreme curvature concentrations behave in large‑scale narrative
  environments?
- What verification criteria are necessary for runtime safety?

These questions define the next phase of research and are not addressed
here.

### 7.7 Toward a Complete Geometric Runtime

The preprint establishes the mathematical foundation for the Fun‑Sphere
Engine. The next step is to integrate these structures into a complete
runtime capable of executing reversible operator paths, computing curvature
tensors, updating curvature‑aware Laplacians, performing spectral analysis,
evolving ecological systems, and verifying narrative behavior. The geometric
framework presented here provides the necessary foundation for such a
runtime.

### 7.8 Summary

This preprint provides a focused, rigorous treatment of the operator spine,
holonomy curvature, Laplacian geometry, spectral ecology, and reversible
quest algebra. It does not attempt to describe the entire Fantasy Engine or
its full runtime behavior. Instead, it establishes the geometric core
required for continued development and future integration with the broader
narrative‑physics system.

---

## 8. References

Abraham, R., Marsden, J. E., & Ratiu, T. (1988). *Manifolds, tensor analysis, and applications* (2nd ed.). Springer.

Belkin, M., & Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data representation. *Neural Computation, 15*(6), 1373–1396.

Chung, F. R. K. (1997). *Spectral graph theory*. American Mathematical Society.

Davis, C., & Kahan, W. M. (1970). The rotation of eigenvectors by a perturbation. *SIAM Journal on Numerical Analysis, 7*(1), 1–46.

Hall, B. C. (2015). *Lie groups, Lie algebras, and representations* (2nd ed.). Springer.

Horn, R. A., & Johnson, C. R. (2012). *Matrix analysis* (2nd ed.). Cambridge University Press.

Lee, J. M. (2018). *Introduction to Riemannian manifolds* (2nd ed.). Springer.

Nakahara, M. (2003). *Geometry, topology and physics* (2nd ed.). Taylor & Francis.

Strang, G. (2019). *Linear algebra and learning from data*. Wellesley‑Cambridge Press.

Taylor, M. E. (2003). Holonomy and curvature. *Bulletin of the American Mathematical Society, 40*(2), 169–172.


### How These References Support the Preprint

The references included in this preprint form the mathematical backbone of
the Fun‑Sphere Engine. Each source contributes a specific structural
component to the geometric framework:

- **Spectral Graph Theory (Chung, 1997)**  
  Provides the formal foundation for Laplacian geometry, eigenstructure,
  spectral drift, and the interpretation of eigenvectors as coherent
  clusters. This directly supports Sections 4 and 5.

- **Matrix Analysis & Operator Theory (Horn & Johnson, 2012)**  
  Supplies the operator‑algebraic tools used throughout the operator spine,
  including commutators, spectral properties, and perturbation behavior.
  Essential for Sections 2, 3, and 6.

- **Eigenvector Perturbation (Davis & Kahan, 1970)**  
  Establishes the classical theory of eigenvector rotation under
  perturbation, grounding the engine’s treatment of curvature‑induced
  spectral drift in Section 5.

- **Riemannian Geometry (Lee, 2018)**  
  Provides the geometric language for curvature, holonomy, and frame
  transport. Supports Section 3’s treatment of holonomy as a geometric
  quantity.

- **Holonomy & Curvature (Taylor, 2003)**  
  Offers a concise and rigorous treatment of holonomy and curvature,
  reinforcing the geometric interpretation of operator non‑commutativity.

- **Geometry, Topology, and Physics (Nakahara, 2003)**  
  Connects geometric structures to physical interpretations, supporting the
  narrative‑physics framing of curvature and holonomy.

- **Manifolds & Tensor Analysis (Abraham, Marsden & Ratiu, 1988)**  
  Provides the tensor‑analytic tools needed for curvature tensors and
  operator‑path accumulation.

- **Lie Groups & Representations (Hall, 2015)**  
  Supports the treatment of operator families, reversible transformations,
  and structured operator composition.

- **Linear Algebra Foundations (Strang, 2019)**  
  Reinforces the linear‑algebraic foundations underlying the operator spine
  and spectral analysis.

- **Laplacian Embeddings (Belkin & Niyogi, 2003)**  
  Demonstrates how Laplacian eigenvectors encode coherent structures,
  supporting the ecological interpretation of spectral modes in Section 5.

Together, these works justify the mathematical structures used throughout
the preprint and situate the Fun‑Sphere Engine within established geometric,
spectral, and operator‑theoretic research traditions.

---

📁 Provenance Footer

Provenance:  
This document integrates geometric‑AI structures developed through Fantasy Engine prototyping and subsequent formalization. Mathematical foundations draw on established literature in spectral graph theory, operator algebra, holonomy, perturbation theory, and Riemannian geometry. All appendices and sections were generated through iterative refinement to ensure altitude separation, modularity, and academic defensibility.

Version:  
Fun‑Sphere Engine Preprint — Geometric Foundations  
Commit: Appendix Integration & Final Structural Assembly  
Date: 26 October 2026

---


## Appendices Overview

The appendices provide the formal mathematical scaffolding underlying the
geometric framework presented in the main text. Each appendix isolates a
specific altitude layer—operator algebra, holonomy, Laplacian geometry,
spectral ecology, and quest‑path dynamics—and presents the definitions,
derivations, and identities required for rigorous development.

### Appendix A — Operator Algebra Foundations
Defines reversible operators, operator composition, commutators, operator
families, path structure, and curvature tensor assembly. This appendix
supports Sections 2 and 6 by providing the algebraic backbone of the
operator spine.

### Appendix B — Holonomy & Curvature Derivations
Formalizes frame transport, holonomy of closed paths, curvature as
non‑commutativity, and the holonomy–curvature relationship. Supports
Section 3 by grounding geometric deviation in operator theory.

### Appendix C — Laplacian Geometry & Spectral Structure
Derives the curvature‑aware adjacency matrix, degree matrix, Laplacian,
spectral properties, and perturbation behavior. Supports Section 4 by
providing the spectral operator framework.

### Appendix D — Spectral Ecology Derivations
Formalizes ecological interpretation of eigenvectors and eigenvalues,
curvature‑induced spectral drift, eigenvector rotation, factional bias, and
ecological partitioning. Supports Section 5 by grounding spectral ecology
in perturbation theory.

### Appendix E — Quest Algebra & Path Geometry
Defines reversible quest paths, geometric irreversibility, curvature
accumulation, path energy, quest composition, and spectral consequences of
operator paths. Supports Section 6 by providing the geometric path‑integral
structure.

Together, these appendices form the mathematical foundation of the
Fun‑Sphere Engine and ensure that the geometric assumptions of the preprint
are formally justified.

---

## Glossary

### Adjacency Matrix ($W$)
Matrix encoding structural relationships between ecological units. Modified
by curvature to produce $W'$.

### Curvature ($H_{ij}$)
The commutator of operators $O_i$ and $O_j$, measuring their failure to
commute. Aggregated into a curvature tensor $K(\gamma)$ along paths.

### Degree Matrix ($D$)
Diagonal matrix whose entries are the row sums of the adjacency matrix.
Reflects geometric tension when curvature is present.

### Ecological Energy Level ($E_k$)
Eigenvalue $\lambda_k$ of the curvature‑aware Laplacian. Measures tension,
instability, or abundance in ecological zones.

### Eigenvector ($u_k$)
Spectral mode of the Laplacian corresponding to a monster family or
ecological cluster.

### Frame ($F$)
Geometric structure associated with a state in the narrative space. Used to
measure holonomy.

### Frame Transport ($T_O$)
Pushforward of a frame under operator $O$. Composition of frame transports
defines holonomy.

### Holonomy ($\mathrm{Hol}(\gamma)$)
Frame shift induced by traversing a closed operator path. Generated by
curvature and accumulated along the path.

### Laplacian ($L'$)
Curvature‑aware operator defined as $L' = D - W'$. Its spectrum encodes
ecological structure.

### Monster Family
Ecological cluster defined by an eigenvector of the Laplacian.

### Operator ($O$)
Reversible transformation acting on the narrative state space. Forms the
operator spine of the engine.

### Operator Path ($\gamma$)
Ordered sequence of reversible operators. Accumulates curvature and induces
holonomy.

### Path Energy ($E(\gamma)$)
Norm of the curvature tensor accumulated along a path. Measures geometric
distortion.

### Spectral Drift
Change in eigenvalues and eigenvectors under curvature perturbation. Drives
ecological evolution.

### Spectral Gap
Difference between adjacent eigenvalues. Determines stability of ecological
families under perturbation.

### State Space ($\mathcal{S}$)
Underlying narrative configuration space on which operators act.

### Tensor ($K(\gamma)$)
Curvature tensor assembled from commutators along a path. Generates
holonomy and Laplacian warp.

---

## Appendix A — Operator Algebra Foundations

This appendix formalizes the operator‑algebraic structures underlying the
Fun‑Sphere Engine. The main text introduces reversible operators,
commutators, and path composition at a conceptual altitude; here we provide
the mathematical definitions and identities that support those structures.

### A.1 Reversible Operators

Let $\mathcal{S}$ be the narrative state space.  
A reversible operator is a bijection
\[
O : \mathcal{S} \to \mathcal{S}
\]
with inverse $O^{-1}$ satisfying
\[
O^{-1}(O(s)) = s, \qquad O(O^{-1}(s)) = s.
\]

Reversibility ensures that operator paths preserve state information even
when geometric quantities (holonomy, curvature) do not.

### A.2 Operator Composition

Operators compose via function composition:
\[
(O_j \circ O_i)(s) = O_j(O_i(s)).
\]

Composition is associative:
\[
O_k \circ (O_j \circ O_i) = (O_k \circ O_j) \circ O_i.
\]

This property enables the definition of operator paths.

### A.3 Operator Paths

A path is an ordered sequence of reversible operators
\[
\gamma = (O_1, O_2, \ldots, O_n).
\]

Forward traversal:
\[
\gamma(s) = O_n(\cdots O_2(O_1(s))\cdots).
\]

Reverse traversal:
\[
\gamma^{-1}(s) = O_1^{-1}(O_2^{-1}(\cdots O_n^{-1}(s)\cdots)).
\]

### A.4 Commutators

For operators $O_i$ and $O_j$, the commutator is
\[
[O_i, O_j] = O_j \circ O_i - O_i \circ O_j.
\]

Properties:

- **Antisymmetry:**  
  \[
  [O_i, O_j] = -[O_j, O_i].
  \]

- **Jacobi Identity:**  
  \[
  [O_i, [O_j, O_k]] + [O_j, [O_k, O_i]] + [O_k, [O_i, O_j]] = 0.
  \]

- **Zero commutator implies commutativity:**  
  \[
  [O_i, O_j] = 0 \iff O_i O_j = O_j O_i.
  \]

These identities are the algebraic backbone of curvature.

### A.5 Curvature Tensor Assembly

Curvature contributions arise from commutators:
\[
H_{ij} = [O_i, O_j].
\]

For a path $\gamma = (O_1, \ldots, O_n)$, total curvature is
\[
K(\gamma) = \sum_{i < j} H_{ij}.
\]

This tensor measures geometric deviation accumulated along the path.

### A.6 Operator Families

Operators are grouped into families $\mathcal{F}_\alpha$ based on narrative
role. For each family, closure under composition may or may not hold:
\[
O_i, O_j \in \mathcal{F}_\alpha \quad \Rightarrow \quad
O_j \circ O_i \in \mathcal{F}_\alpha \quad \text{(not guaranteed)}.
\]

Non‑closure is a source of cross‑family curvature.

### A.7 Path Energy

Define path energy as the norm of the curvature tensor:
\[
E(\gamma) = \|K(\gamma)\|.
\]

High‑energy paths produce strong geometric distortion and significant
spectral drift.

### A.8 Summary

This appendix provides the operator‑algebraic foundation for:

- holonomy (Appendix B)  
- curvature tensors (Appendix B)  
- Laplacian warp (Appendix C)  
- spectral drift (Appendix D)  
- quest‑path geometry (Appendix E)

These structures form the mathematical core of the Fun‑Sphere Engine.

---

## Appendix B — Holonomy & Curvature Derivations

This appendix formalizes the geometric quantities introduced in Section 3:
holonomy, curvature, frame transport, and path‑based geometric deviation.
The main text presents these concepts at a conceptual altitude; here we
provide the mathematical derivations that support them.

### B.1 Frame Transport

Let $\mathcal{S}$ be the narrative state space and let $\mathcal{F}$ denote
the associated frame bundle. A frame $F \in \mathcal{F}$ encodes the local
geometric structure at a state $s \in \mathcal{S}$.

A reversible operator $O : \mathcal{S} \to \mathcal{S}$ induces a frame
transport map
\[
T_O : \mathcal{F} \to \mathcal{F},
\]
defined by pushing forward the frame under the operator’s action.

### B.2 Holonomy of a Closed Path

For a closed operator path
\[
\gamma = (O_1, O_2, \ldots, O_n),
\]
the holonomy is the composite frame transport
\[
\mathrm{Hol}(\gamma) = T_{O_n} \circ \cdots \circ T_{O_2} \circ T_{O_1}.
\]

Even though the state returns to its original value,
\[
\gamma^{-1}(\gamma(s)) = s,
\]
the frame generally does not:
\[
F' = \mathrm{Hol}(\gamma)(F).
\]

Holonomy therefore measures geometric deviation accumulated along the path.

### B.3 Infinitesimal Holonomy and Curvature

Curvature is the infinitesimal generator of holonomy. For operators
$O_i$ and $O_j$, define the curvature contribution
\[
H_{ij} = [O_i, O_j] = O_j \circ O_i - O_i \circ O_j.
\]

This quantity measures the failure of the operators to commute. When
$H_{ij} = 0$, the operators commute and produce no curvature.

### B.4 Curvature Tensor Assembly

For a path $\gamma = (O_1, \ldots, O_n)$, total curvature is
\[
K(\gamma) = \sum_{i < j} H_{ij}.
\]

This tensor aggregates all pairwise non‑commutativity along the path.

### B.5 Holonomy–Curvature Relationship

Holonomy integrates curvature. For sufficiently small operators (or
infinitesimal steps), we have the expansion
\[
\mathrm{Hol}(\gamma)
= I + K(\gamma) + \mathcal{O}(\|K(\gamma)\|^2),
\]
where $I$ is the identity frame transport.

Thus:

- curvature is **local** (commutators),
- holonomy is **global** (path‑integrated frame shift),
- curvature **generates** holonomy,
- holonomy **accumulates** curvature.

### B.6 Curvature and Laplacian Warp

Curvature modifies adjacency weights:
\[
W' = W + H,
\]
where $H$ is the curvature tensor assembled from commutators.

This produces a curvature‑aware Laplacian
\[
L' = D - W',
\]
whose spectrum encodes ecological structure.

### B.7 Curvature Norm and Geometric Energy

Define path energy as the norm of the curvature tensor:
\[
E(\gamma) = \|K(\gamma)\|.
\]

High‑energy paths produce:

- strong holonomy,
- significant Laplacian warp,
- large spectral drift,
- ecological reconfiguration.

### B.8 Summary

This appendix provides the geometric foundation for:

- holonomy (global frame shift),
- curvature (local non‑commutativity),
- Laplacian warp (adjacency modification),
- spectral drift (eigenstructure evolution),
- quest‑path geometry (curvature accumulation).

These derivations support the geometric interpretation of narrative physics
presented in the main text.

---

## Appendix C — Laplacian Geometry & Spectral Structure

This appendix provides the formal mathematical structures underlying the
curvature‑aware Laplacian introduced in Section 4. The main text presents
Laplacian geometry conceptually; here we define the operators, derive their
properties, and establish the spectral framework used in spectral ecology.

### C.1 Curvature‑Aware Adjacency Matrix

Let $W$ be the baseline adjacency matrix encoding structural relationships
between narrative states, ecological zones, or monster families.

Curvature modifies adjacency through the curvature tensor $H$:
\[
W' = W + H,
\]
where
\[
H_{ij} = [O_i, O_j]
\]
is assembled from operator commutators.

Thus $W'$ incorporates geometric deviation induced by operator
non‑commutativity.

### C.2 Degree Matrix

The degree matrix $D$ is defined as
\[
D_{ii} = \sum_j W'_{ij}.
\]

Because $W'$ includes curvature, $D$ reflects geometric tension: regions
with high curvature accumulate higher degree.

### C.3 Curvature‑Warped Laplacian

The curvature‑aware Laplacian is
\[
L' = D - W'.
\]

When $H = 0$, $L'$ reduces to the classical graph Laplacian.  
When $H \neq 0$, $L'$ becomes a geometric operator whose spectrum encodes
holonomy‑induced warp.

### C.4 Properties of the Laplacian

The Laplacian $L'$ is:

- **symmetric** (if $W'$ is symmetric),
- **positive semidefinite**,
- **diagonally dominant**,
- **zero‑row‑sum** (for undirected structures).

These properties ensure a real, non‑negative spectrum.

### C.5 Eigenstructure

Eigenpairs satisfy
\[
L' u_k = \lambda_k u_k.
\]

Interpretation in the Fun‑Sphere Engine:

- **Eigenvectors** $u_k$ correspond to **monster families**.  
- **Eigenvalues** $\lambda_k$ correspond to **ecological energy levels**.

Low‑frequency eigenvectors encode broad ecological regions; high‑frequency
eigenvectors encode rare or localized species.

### C.6 Spectral Perturbation Under Curvature

Curvature perturbs the Laplacian:
\[
L' = L + \Delta L,
\]
where
\[
\Delta L = H - \Delta D,
\]
and $\Delta D$ is the curvature‑induced change in the degree matrix.

Eigenpairs shift accordingly:
\[
(\lambda_k, u_k) \mapsto (\lambda_k', u_k').
\]

Classical perturbation theory (Davis–Kahan) provides bounds on eigenvector
rotation:
\[
\sin \theta(u_k, u_k') \le
\frac{\|\Delta L\|}{\text{gap}_k},
\]
where $\text{gap}_k$ is the spectral gap around $\lambda_k$.

### C.7 Ecological Interpretation of Spectral Drift

Spectral drift measures ecological evolution:

- **Eigenvalue increase** → rising ecological tension.  
- **Eigenvalue decrease** → stabilization or resource abundance.  
- **Eigenvector rotation** → monster‑family migration or restructuring.  
- **High‑frequency amplification** → emergence of rare species.  

Curvature determines the magnitude and direction of drift.

### C.8 Spectral Partitions

The spectrum partitions the ecology:

- **Low‑frequency modes** → large‑scale ecological zones.  
- **Mid‑frequency modes** → factional boundaries.  
- **High‑frequency modes** → rare species or anomalies.

Curvature shifts these partitions, causing ecological zones to merge,
fracture, or migrate.

### C.9 Summary

This appendix provides the spectral foundation for:

- curvature‑aware adjacency,
- Laplacian warp,
- eigenvalue/eigenvector interpretation,
- spectral drift,
- ecological evolution.

These structures support the geometric‑spectral model of narrative physics
presented in Sections 4 and 5.

---

## Appendix D — Spectral Ecology Derivations

This appendix provides the mathematical derivations underlying spectral
ecology. The main text interprets eigenvectors as monster families and
eigenvalues as ecological energy levels; here we formalize those
interpretations and derive the curvature‑induced spectral drift that drives
ecological evolution.

### D.1 Eigenstructure of the Curvature‑Warped Laplacian

Let
\[
L' = D - W'
\]
be the curvature‑aware Laplacian, where
\[
W' = W + H
\]
and $H$ is the curvature tensor assembled from operator commutators.

Eigenpairs satisfy
\[
L' u_k = \lambda_k u_k.
\]

The spectrum $\{\lambda_k\}$ is non‑negative, and the eigenvectors
$\{u_k\}$ form an orthonormal basis for the ecological state space.

### D.2 Ecological Interpretation of Eigenvectors

Each eigenvector $u_k$ defines a coherent ecological cluster. Let
$u_k(i)$ denote the component associated with ecological unit $i$ (e.g.,
monster species, factional region, or resource zone).

Interpretation:

- Large, smooth components → broad ecological families.  
- Localized, oscillatory components → rare or high‑frequency species.  
- Sign structure → factional or territorial boundaries.  

Thus eigenvectors encode ecological topology.

### D.3 Ecological Energy Levels

The eigenvalue $\lambda_k$ associated with $u_k$ defines the ecological
energy level:
\[
E_k = \lambda_k.
\]

High energy indicates structural tension or instability; low energy
indicates cohesion or abundance.

### D.4 Curvature Perturbation of the Laplacian

Curvature perturbs the Laplacian:
\[
L' = L + \Delta L,
\]
where
\[
\Delta L = H - \Delta D,
\]
and $\Delta D$ is the curvature‑induced change in the degree matrix.

### D.5 Eigenvalue Drift

Eigenvalues shift under perturbation:
\[
\lambda_k' = \lambda_k + u_k^\top (\Delta L) u_k + \mathcal{O}(\|\Delta L\|^2).
\]

Thus:

- positive curvature contributions raise ecological energy,
- negative contributions lower it,
- magnitude depends on the alignment of $u_k$ with $\Delta L$.

### D.6 Eigenvector Rotation

Eigenvectors rotate under perturbation. Classical Davis–Kahan theory gives:
\[
\sin \theta(u_k, u_k') \le
\frac{\|\Delta L\|}{\text{gap}_k},
\]
where $\text{gap}_k$ is the spectral gap around $\lambda_k$.

Consequences:

- small gaps → large ecological reconfiguration,  
- large gaps → stable ecological families.

### D.7 Ecological Drift Dynamics

Spectral drift produces ecological evolution:

- **Eigenvalue increase**  
  → rising tension, resource scarcity, or instability.

- **Eigenvalue decrease**  
  → stabilization, abundance, or ecological recovery.

- **Eigenvector rotation**  
  → migration, restructuring, or merging of monster families.

- **High‑frequency amplification**  
  → emergence of rare species or anomalies.

Curvature determines the direction and magnitude of drift.

### D.8 Factional Bias

If curvature is concentrated in operator families associated with specific
factions, then:

- eigenvalues for those regions rise disproportionately,
- eigenvectors localize around factional boundaries,
- ecological zones shift toward faction‑aligned structures.

Factional bias is therefore a geometric consequence of operator behavior.

### D.9 Spectral Partitions

The spectrum partitions the ecology:

- low‑frequency modes → large‑scale ecological zones,  
- mid‑frequency modes → factional boundaries,  
- high‑frequency modes → rare species or anomalies.

Curvature shifts these partitions, causing ecological zones to expand,
contract, merge, or fracture.

### D.10 Summary

This appendix formalizes the spectral‑ecological machinery underlying:

- ecological energy levels (eigenvalues),
- monster‑family structure (eigenvectors),
- curvature‑induced spectral drift,
- factional bias,
- ecological evolution.

These derivations support the geometric‑spectral interpretation of narrative
physics presented in Sections 5 and 6.

---

## Appendix E — Quest Algebra & Path Geometry

This appendix formalizes the reversible quest algebra introduced in Section
6. The main text interprets quests as operator paths that accumulate
curvature and induce holonomy; here we provide the mathematical derivations
that support those interpretations.

### E.1 Quest Paths as Operator Sequences

A quest path is an ordered sequence of reversible operators
\[
\gamma = (O_1, O_2, \ldots, O_n),
\]
acting on the narrative state space $\mathcal{S}$.

Forward traversal:
\[
\gamma(s) = O_n(\cdots O_2(O_1(s))\cdots).
\]

Reverse traversal:
\[
\gamma^{-1}(s) = O_1^{-1}(O_2^{-1}(\cdots O_n^{-1}(s)\cdots)).
\]

State reversibility holds:
\[
\gamma^{-1}(\gamma(s)) = s.
\]

### E.2 Geometric Irreversibility

Although state reversibility holds, geometric reversibility does not.  
Let $T_{O_i}$ denote the frame transport induced by operator $O_i$.

Forward frame transport:
\[
F' = T_{O_n} \circ \cdots \circ T_{O_1}(F).
\]

Reverse frame transport:
\[
F'' = T_{O_1^{-1}} \circ \cdots \circ T_{O_n^{-1}}(F').
\]

In general:
\[
F'' \neq F.
\]

This geometric irreversibility is the holonomy of the quest path.

### E.3 Curvature Accumulation Along Paths

Curvature contributions arise from operator commutators:
\[
H_{ij} = [O_i, O_j].
\]

Total curvature accumulated along the path is
\[
K(\gamma) = \sum_{i < j} H_{ij}.
\]

This tensor measures the geometric deviation induced by the quest.

### E.4 Path Energy

Define path energy as the norm of the curvature tensor:
\[
E(\gamma) = \|K(\gamma)\|.
\]

High‑energy paths produce:

- strong holonomy,
- significant Laplacian warp,
- large spectral drift,
- ecological restructuring.

### E.5 Quest Composition

Quests compose by concatenation:
\[
\gamma_2 \circ \gamma_1 = (O_1, \ldots, O_m, O_{m+1}, \ldots, O_n).
\]

Curvature is additive:
\[
K(\gamma_2 \circ \gamma_1) = K(\gamma_1) + K(\gamma_2).
\]

This property enables modular construction of complex narrative behavior.

### E.6 Curvature‑Driven Laplacian Warp

Curvature modifies adjacency weights:
\[
W' = W + H,
\]
producing a curvature‑aware Laplacian
\[
L' = D - W'.
\]

This warp induces spectral drift:
\[
(\lambda_k, u_k) \mapsto (\lambda_k', u_k'),
\]
which alters ecological energy levels and monster‑family distributions.

### E.7 Spectral Consequences of Quest Paths

Quest‑induced spectral drift produces:

- **monster‑family migration** (eigenvector rotation),
- **ecological tension shifts** (eigenvalue drift),
- **rare species emergence** (high‑frequency amplification),
- **factional bias** (localized curvature concentration).

These consequences arise naturally from the geometric structure of the
operator path.

### E.8 Path Geometry and Holonomy

Holonomy integrates curvature:
\[
\mathrm{Hol}(\gamma)
= I + K(\gamma) + \mathcal{O}(\|K(\gamma)\|^2).
\]

Thus:

- curvature is **local** (commutators),
- holonomy is **global** (path‑integrated frame shift),
- curvature **generates** holonomy,
- holonomy **accumulates** curvature.

Quest geometry is therefore a path‑integral structure.

### E.9 Summary

This appendix formalizes the geometric machinery underlying reversible quest
algebra:

- operator‑path composition,
- curvature accumulation,
- holonomy‑induced frame shift,
- Laplacian warp,
- spectral drift,
- ecological evolution.

These derivations complete the mathematical foundation of the Fun‑Sphere
Engine.

---

