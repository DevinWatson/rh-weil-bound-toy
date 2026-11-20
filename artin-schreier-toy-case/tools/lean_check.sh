#!/bin/bash
# lean_check.sh Module.Name [Module.Name ...]
# Compiles modules of artin-schreier-toy-case/lean against a Mathlib workspace
# (defaults to $HOME/mlslice; override with MATHLIB_DIR=/path/to/mathlib/project).
export PATH="$HOME/.elan/bin:$PATH"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../lean" && pwd)"
OUT="${ASTOY_OUT:-$HOME/astoy-build}"
LOGS="$ROOT/logs"
MATHLIB_DIR="${MATHLIB_DIR:-$HOME/mlslice}"
[ $# -ge 1 ] || { echo "usage: lean_check.sh Module.Name [...]"; exit 2; }
mkdir -p "$OUT" "$LOGS" || exit 2
cd "$MATHLIB_DIR" || { echo "LEANCHECK: no Mathlib workspace at $MATHLIB_DIR"; exit 2; }
BASE_LP=$(lake env printenv LEAN_PATH </dev/null 2>/dev/null)
for mod in "$@"; do
  rel=${mod//.//}
  src="$ROOT/$rel.lean"
  [ -f "$src" ] || { echo "LEANCHECK: no source file $src"; exit 2; }
  mkdir -p "$(dirname "$OUT/$rel.olean")"
  log="$LOGS/$mod.log"
  start=$(date +%s)
  LEAN_PATH="$BASE_LP:$OUT" LEAN_NUM_THREADS=4 nice -n 10 timeout 900 \
    lean --root="$ROOT" -o "$OUT/$rel.olean" -i "$OUT/$rel.ilean" "$src" >"$log" 2>&1 </dev/null
  rc=$?
  echo "LEANCHECK $mod exit=$rc secs=$(( $(date +%s) - start )) log=artin-schreier-toy-case/lean/logs/$mod.log"
  head -c 5000 "$log"
  if [ $rc -ne 0 ]; then
    [ $rc -eq 124 ] && echo "LEANCHECK: timed out after 900 s"
    exit $rc
  fi
done
echo "LEANCHECK OK"
