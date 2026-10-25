# Fun‑Sphere Engine — Mathematical Spine

Module 5: Reversible Quest Algebra, Path Geometry, and Curvature Accumulation

---

1. Purpose
This module defines the reversible quest algebra of the Fun‑Sphere Engine.  
It establishes:

- operator‑path formalization  
- forward and reverse traversal invariants  
- curvature accumulation rules  
- holonomy‑induced frame shifts  
- narrative tension propagation  
- spectral ecology interaction  

Reversible quests are the narrative geometry layer that ties together all previous Phase‑D modules.

---

2. Preliminaries

2.1 Operator Group
From the Operator Spine:

\[
O : \mathcal{S} \rightarrow \mathcal{S}, \quad O^{-1} \text{ exists}
\]

Operators form a group under composition.

---

2.2 Paths
A quest is a path:

\[
\gamma = (O1, O2, \ldots, O_n)
\]

Forward traversal applies operators in sequence.  
Reverse traversal applies inverses in reverse order.

---

3. Forward Traversal

Given initial state \( s \):

\[
\gamma(s) = On(\cdots O2(O_1(s))\cdots)
\]

Forward traversal:

- modifies the state  
- accumulates curvature  
- shifts the narrative frame  
- perturbs spectral ecology  

---

4. Reverse Traversal

Reverse traversal is:

\[
\gamma^{-1}(s) = O1^{-1}(O2^{-1}(\cdots O_n^{-1}(s)\cdots))
\]

Reverse traversal:

- restores the original state  
- does not undo curvature  
- does not undo spectral drift  
- does not undo frame shifts  

Thus quests are:

- state‑reversible  
- geometry‑irreversible  

This is the core Fun‑Sphere narrative physics principle.

---

5. Curvature Accumulation

Curvature arises from operator non‑commutativity:

\[
H{ij} = \Delta{\text{hol}}(Oi, Oj)
\]

Total curvature along a quest path:

\[
K(\gamma) = \sum{i < j} H{ij}
\]

Curvature is:

- additive  
- path‑dependent  
- frame‑shifting  
- ecology‑perturbing  

---

6. Frame Shift

Holonomy transforms the narrative frame:

\[
F' = \text{Hol}(\gamma)(F)
\]

Even though:

\[
\gamma^{-1}(\gamma(s)) = s
\]

the frame satisfies:

\[
F' \neq F
\]

Thus:

- quests change the geometry  
- even when they do not change the state  

---

7. Quest Energy

Define quest energy:

\[
E(\gamma) = \|K(\gamma)\|
\]

Interpretation:

- low energy → simple quests  
- medium energy → faction‑biased quests  
- high energy → ecology‑shifting quests  
- extreme energy → spectral‑catastrophic quests  

---

8. Interaction with Spectral Ecology

Curvature modifies Laplacian weights:

\[
w{ij}' = w{ij} + H_{ij}
\]

Thus quests:

- warp the Laplacian  
- shift eigenvalues  
- evolve monster families  
- alter faction ecology  
- propagate narrative tension  

This is the quest‑ecology feedback loop.

---

9. Quest Composition

Quests compose:

\[
\gamma2 \circ \gamma1 = (O1, \ldots, Om, O{m+1}, \ldots, On)
\]

Curvature is additive:

\[
K(\gamma2 \circ \gamma1) = K(\gamma1) + K(\gamma2)
\]

Quest energy is likewise additive.

---

10. Reversible Quest Algebra

Define the algebra:

- Elements: operator paths  
- Operation: path concatenation  
- Identity: empty path  
- Inverse: reverse traversal  

This forms a groupoid, not a group:

- identity exists  
- inverses exist  
- composition is partially defined  
- curvature is non‑zero  

---

11. Verification Requirements

Reversible quests must satisfy:

- state reversibility  
- deterministic curvature accumulation  
- stable frame shift  
- JSON‑safe representation  
- bounded spectral drift  
- deterministic operator sequencing  

Wave‑T tests confirm these properties.

---

12. Status
This module is complete and ready for integration into:

- preprint.md  
- quest appendix  
- narrative physics section  
- Phase‑D milestone E  

---

