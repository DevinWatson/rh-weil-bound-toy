#!/bin/bash
# Probe the WSL Lean setup used for small standalone builds. Read-only.
export PATH=$HOME/.elan/bin:$PATH
cd "$HOME/mlslice" || { echo "no ~/mlslice"; exit 2; }
pwd
ls | head -20
echo "toolchain: $(cat lean-toolchain 2>/dev/null)"
lean --version 2>/dev/null | head -1
echo "packages: $(ls .lake/packages 2>/dev/null | tr '\n' ' ')"
for m in Mathlib Mathlib/NumberTheory/GaussSum Mathlib/Algebra/Group/AddChar Mathlib/LinearAlgebra/Vandermonde \
         Mathlib/Analysis/InnerProductSpace/Basic Mathlib/NumberTheory/LegendreSymbol/AddCharacter \
         Mathlib/Analysis/Fourier/FiniteAbelian/Orthogonality Mathlib/Analysis/Fourier/ZMod \
         Mathlib/FieldTheory/Finite/Basic Mathlib/Analysis/SpecialFunctions/Pow/Real \
         Mathlib/Analysis/CStarAlgebra/Matrix Mathlib/NumberTheory/LegendreSymbol/QuadraticChar/Basic; do
  f=$(find . -path "*/$m.olean" 2>/dev/null | head -1)
  echo "$m -> ${f:-MISSING}"
done
echo "olean count: $(find . -name '*.olean' 2>/dev/null | wc -l)"
echo "cpus: $(nproc)"
free -g | head -2
df -h "$HOME" | tail -1
