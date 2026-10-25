# Fun‑Sphere Engine — Mathematical Spine

Module 1: Reversible Operators & Algebraic Structure

---

1. Purpose
This module defines the formal mathematical structure of reversible operators in the Fun‑Sphere Engine.  
It establishes:

- Operator domains and codomains  
- Reversibility conditions  
- Commutation relations  
- Curvature contribution  
- Path composition rules  
- Identity and neutral elements  

This is the foundation for holonomy, Laplacian behavior, spectral ecology, and reversible quests.

---

2. Definitions

2.1 State Space
Let \( \mathcal{S} \) be the set of all valid engine states.

A state \( s \in \mathcal{S} \) is a structured object with:

- scalar fields  
- vector fields  
- spectral fields  
- curvature annotations  

All operators act on \( \mathcal{S} \).

---

2.2 Operators
An operator is a function:

\[
O : \mathcal{S} \rightarrow \mathcal{S}
\]

with the following constraints:

1. Deterministic  
   \[
   O(s1) = O(s2) \quad \text{whenever } s1 = s2
   \]

2. Non‑mutating  
   \[
   O(s) \neq s \quad \text{unless } O = I
   \]  
   and  
   \[
   s \text{ is never modified in place}
   \]

3. Reversible  
   There exists an inverse operator \( O^{-1} \) such that:

   \[
   O^{-1}(O(s)) = s
   \]

4. Closed under composition  
   For any operators \( O1, O2 \):

   \[
   O2 \circ O1 : \mathcal{S} \rightarrow \mathcal{S}
   \]

---

3. Identity Operator
The identity operator \( I \) satisfies:

\[
I(s) = s
\]

and is the neutral element of the operator algebra:

\[
O \circ I = I \circ O = O
\]

---

4. Composition Algebra
Operators form a group under composition:

\[
(\mathcal{O}, \circ)
\]

with:

- closure  
- associativity  
- identity  
- inverses  

4.1 Associativity
\[
(O3 \circ O2) \circ O1 = O3 \circ (O2 \circ O1)
\]

4.2 Inverses
\[
O^{-1} \circ O = I
\]

---

5. Commutation & Curvature
Operators may or may not commute.

5.1 Commuting Operators
\[
O2 \circ O1 = O1 \circ O2
\]

These produce zero holonomy.

5.2 Non‑commuting Operators
\[
O2 \circ O1 \neq O1 \circ O2
\]

These produce non‑zero holonomy, contributing to narrative curvature.

Define the holonomy curvature contribution:

\[
\Delta{\text{hol}}(O1, O2) = (O2 \circ O1)(s) - (O1 \circ O_2)(s)
\]

This is the fundamental curvature source in Fun‑Sphere.

---

6. Operator Paths
A reversible quest is a path:

\[
\gamma = (O1, O2, \ldots, O_n)
\]

Forward traversal:

\[
\gamma(s) = On(\cdots O2(O_1(s))\cdots)
\]

Reverse traversal:

\[
\gamma^{-1}(s) = O1^{-1}(O2^{-1}(\cdots O_n^{-1}(s)\cdots))
\]

---

7. Curvature Accumulation
Curvature along a path is:

\[
K(\gamma) = \sum{i < j} \Delta{\text{hol}}(Oi, Oj)
\]

This is the mathematical definition of narrative tension.

---

8. Operator Classes

8.1 Additive Operators
\[
O(s) = s + \alpha
\]

8.2 Multiplicative Operators
\[
O(s) = \beta s
\]

8.3 Spectral Operators
\[
O(\lambda) = f(\lambda)
\]

8.4 Curvature Operators
\[
O(s) = s + \kappa(s)
\]

---

9. Verification Requirements
All operators must satisfy:

- reversibility  
- determinism  
- non‑mutation  
- JSON‑safe representation  
- stable composition  
- stable inverse  

Wave‑T tests confirm these properties.

---

10. Status
This module is complete and ready for integration into:

- Laplacian spine  
- Holonomy spine  
- Spectral ecology spine  
- Reversible quest spine  
- Preprint.md  

---

