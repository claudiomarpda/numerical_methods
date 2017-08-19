<h2>2. Equations Resolution </h2>
<h3> Find root of non-trivial equations with the following methods: </h3>

1. Bissection
2. False position
3. Newton-Raphson
4. Secant

We can do that in two steps:

* Root insulation
  * consists of determining an interval [a, b] that has one root of the equation inside it.
* Refinement
  * consists in redefining the interval [a, b] to obtain a new shorter interval that still has a root of the equation inside it.

To do that, we need the Bolzano theorem:
> If f(x) is continuous in an interval [a, b] such that f(a)f(b) < 0 (f(a) and f(b) has counter signs), then the equation f(x) = 0 has at least one root inside this interval.
