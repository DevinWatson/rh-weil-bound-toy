#!/bin/bash
# lean_check.sh Module.Name [Module.Name ...]
#
# Compiles the named modules of the toy-case Lean tree, in the order given, against the Mathlib of ~/mlslice
# (Lean 4.34.1). One Lean process at a time (shared lock with rh-silicon/open/tools/build.sh), two threads,
# low priority, 15 minute limit per module. Module ToyWeil.Foo lives at toy-case/lean/ToyWeil/Foo.lean.
# A module may import earlier modules of this tree once they have been compiled here.
#
# Call from PowerShell:
#   wsl.exe -d Ubuntu -- bash ./tools/lean_check.sh ToyWeil.Foo
# The full compiler output is in toy-case/lean/logs/<Module>.log
export PATH=$HOME/.elan/bin:$PATH
ROOT=./lean
OUT=$HOME/toyweil-build
LOGS=$ROOT/logs
[ $# -ge 1 ] || { echo "usage: lean_check.sh Module.Name [...]"; exit 2; }
mkdir -p "$OUT" "$LOGS" || exit 2
exec 9>"$HOME/.rh-open-build.lock"
flock -w 1800 9 || { echo "LEANCHECK: the build lock was busy for 30 minutes"; exit 99; }
cd "$HOME/mlslice" || { echo "LEANCHECK: no ~/mlslice"; exit 2; }
BASE_LP=$(lake env printenv LEAN_PATH </dev/null 2>/dev/null)
for mod in "$@"; do
  rel=${mod//.//}
  src="$ROOT/$rel.lean"
  [ -f "$src" ] || { echo "LEANCHECK: no source file $src"; exit 2; }
  for i in $(seq 1 120); do
    mem=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
    [ "${mem:-0}" -ge $((6*1024*1024)) ] && break
    sleep 5
  done
  mkdir -p "$(dirname "$OUT/$rel.olean")"
  log="$LOGS/$mod.log"
  start=$(date +%s)
  LEAN_PATH="$BASE_LP:$OUT" LEAN_NUM_THREADS=2 nice -n 10 timeout 900 \
    lean --root="$ROOT" -o "$OUT/$rel.olean" -i "$OUT/$rel.ilean" "$src" >"$log" 2>&1 </dev/null
  rc=$?
  echo "LEANCHECK $mod exit=$rc secs=$(( $(date +%s) - start )) log=toy-case/lean/logs/$mod.log"
  head -c 5000 "$log"
  if [ $rc -ne 0 ]; then
    [ $rc -eq 124 ] && echo "LEANCHECK: timed out after 900 s"
    exit $rc
  fi
done
echo "LEANCHECK OK"
