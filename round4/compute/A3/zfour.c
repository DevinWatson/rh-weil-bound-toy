// zfour.c : exact iterated additive Fourier transforms on F_{q^n}, q = p^u, p in {2,3}.
// Integer arithmetic only (Z[omega], omega a primitive cube root of unity, coordinates a+b*omega in __int128).
// G_1 = t, Ghat_i(y) = sum_x G_i(x) psi(Tr(b_i x y)), G_{i+1}(y) = t(y) Ghat_i(y),  t(y) = chi(f(y)), f = prod (x - z_j).
// p=3: chi quadratic (q=3), psi(a)=omega^a.   p=2: chi cubic (q=4), psi(a)=(-1)^a.
// usage: zfour p u n poly_digits cfgfile
//   poly_digits: N=u*n digits (low to high) of m_0..m_{N-1}; field = F_p[X]/(X^N + sum m_i X^i), X primitive.
// cfg line: id h nz z_1..z_nz K c_1..c_K nw w_1..w_nw    (element code: -1 = zero, a>=0 = xi^a, xi = g^((Q-1)/(q-1)))
// output line: R id n i w a b      (Ghat_i(w) = a + b*omega)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#ifdef _WIN32
#include <windows.h>
#endif
typedef __int128 i128;
typedef struct { i128 a, b; } zw;
static int p, u, n, N, e;
static uint64_t Q, q;
static uint32_t *EXP; static int32_t *LOG;
static uint64_t pw[40];
static int mpoly[40];

static void pr128(i128 x, char *buf) {
  char t[64]; int k = 0; int neg = 0;
  if (x < 0) { neg = 1; x = -x; }
  if (x == 0) t[k++] = '0';
  while (x > 0) { t[k++] = '0' + (int)(x % 10); x /= 10; }
  int j = 0; if (neg) buf[j++] = '-';
  while (k > 0) buf[j++] = t[--k];
  buf[j] = 0;
}
static inline zw zadd(zw x, zw y) { zw r = { x.a + y.a, x.b + y.b }; return r; }
static inline zw zmulw(zw x) { zw r = { -x.b, x.a - x.b }; return r; }          // * omega
static inline zw zmulw2(zw x) { zw r = { x.b - x.a, -x.a }; return r; }         // * omega^2

static void build_tables(void) {
  EXP = (uint32_t*)malloc(sizeof(uint32_t) * Q);
  LOG = (int32_t*)malloc(sizeof(int32_t) * Q);
  for (uint64_t i = 0; i < Q; i++) LOG[i] = -2;
  int cur[40]; memset(cur, 0, sizeof(cur)); cur[0] = 1;
  uint64_t idx = 1;
  for (uint64_t k = 0; k < Q - 1; k++) {
    EXP[k] = (uint32_t)idx;
    if (LOG[idx] != -2) { fprintf(stderr, "poly not primitive (repeat at %llu)\n", (unsigned long long)k); exit(2); }
    LOG[idx] = (int32_t)k;
    int lead = cur[N - 1];
    for (int i = N - 1; i >= 1; i--) cur[i] = cur[i - 1];
    cur[0] = 0;
    if (lead) for (int i = 0; i < N; i++) { cur[i] = ((cur[i] - lead * mpoly[i]) % p + p) % p; }
    idx = 0; for (int i = 0; i < N; i++) idx += (uint64_t)cur[i] * pw[i];
  }
  if (idx != 1) { fprintf(stderr, "poly not primitive (no return)\n"); exit(2); }
  LOG[0] = -1;
}
static inline uint64_t elem_pow_log(int64_t lg) { // element g^lg
  int64_t m = (int64_t)(Q - 1); lg %= m; if (lg < 0) lg += m; return EXP[lg];
}
static uint64_t code_to_idx(int code) { // F_q element code -> index
  if (code < 0) return 0;
  return EXP[(uint64_t)code * ((Q - 1) / (q - 1)) % (Q - 1)];
}
static void digits_of(uint64_t x, int *d) { for (int i = 0; i < N; i++) { d[i] = x % p; x /= p; } }
static uint64_t idx_of(const int *d) { uint64_t x = 0; for (int i = 0; i < N; i++) x += (uint64_t)d[i] * pw[i]; return x; }
static uint64_t addidx(uint64_t a, uint64_t b) { int da[40], db[40]; digits_of(a, da); digits_of(b, db); for (int i = 0; i < N; i++) da[i] = (da[i] + db[i]) % p; return idx_of(da); }
static int trace_of(uint64_t z) { // Tr_{K/F_p}(z) in 0..p-1
  if (z == 0) return 0;
  uint64_t acc = 0; int64_t lg = LOG[z]; uint64_t m = Q - 1;
  uint64_t ppow = 1;
  for (int i = 0; i < N; i++) {
    uint64_t l2 = (uint64_t)lg * ppow % m;   // lg<2^28, ppow<2^28 ok
    acc = addidx(acc, EXP[l2]);
    ppow = ppow * p % m;
  }
  int d[40]; digits_of(acc, d);
  for (int i = 1; i < N; i++) if (d[i] != 0) { fprintf(stderr, "trace not in prime field\n"); exit(3); }
  return d[0];
}
// B columns for b: col[l] = vector (digits) with col[l][j] = T_{j+l}, T_m = Tr(b X^m)
static int colv[40][40];
static void build_cols(uint64_t b) {
  int T[80];
  for (int m = 0; m <= 2 * N - 2; m++) T[m] = trace_of(elem_pow_log((int64_t)LOG[b] + m));
  for (int l = 0; l < N; l++) for (int j = 0; j < N; j++) colv[l][j] = T[j + l];
}
static uint64_t vec_of(uint64_t y) { // B y as index
  int d[40], v[40]; digits_of(y, d); for (int j = 0; j < N; j++) v[j] = 0;
  for (int l = 0; l < N; l++) if (d[l]) for (int j = 0; j < N; j++) v[j] = (v[j] + d[l] * colv[l][j]) % p;
  return idx_of(v);
}
static uint32_t *VMAP;
static void build_vmap(void) {
  if (!VMAP) VMAP = (uint32_t*)malloc(sizeof(uint32_t) * Q);
  uint64_t colidx[40];
  for (int l = 0; l < N; l++) colidx[l] = idx_of(colv[l]);
  if (p == 2) {
    VMAP[0] = 0;
    for (uint64_t y = 1; y < Q; y++) VMAP[y] = VMAP[y & (y - 1)] ^ (uint32_t)colidx[__builtin_ctzll(y)];
  } else {
    int d[40], v[40]; for (int i = 0; i < N; i++) { d[i] = 0; v[i] = 0; }
    uint64_t vi = 0; VMAP[0] = 0;
    for (uint64_t y = 1; y < Q; y++) {
      int l = 0;
      while (1) {
        d[l] = (d[l] + 1) % 3;
        for (int j = 0; j < N; j++) if (colv[l][j]) { int nv = (v[j] + colv[l][j]) % 3; vi += (uint64_t)((nv - v[j] + 3) % 3 == 0 ? 0 : 0); v[j] = nv; }
        if (d[l] != 0) break;
        l++;
      }
      vi = 0; for (int j = 0; j < N; j++) vi += (uint64_t)v[j] * pw[j];
      VMAP[y] = (uint32_t)vi;
    }
  }
}
static void dft(zw *A) {
  if (p == 2) {
    for (int j = 0; j < N; j++) {
      uint64_t s = 1ULL << j;
      for (uint64_t base = 0; base < Q; base += 2 * s)
        for (uint64_t k = base; k < base + s; k++) {
          zw x = A[k], y = A[k + s];
          A[k].a = x.a + y.a; A[k].b = x.b + y.b; A[k + s].a = x.a - y.a; A[k + s].b = x.b - y.b;
        }
    }
  } else {
    for (int j = 0; j < N; j++) {
      uint64_t s = pw[j];
      for (uint64_t base = 0; base < Q; base += 3 * s)
        for (uint64_t k = base; k < base + s; k++) {
          zw x0 = A[k], x1 = A[k + s], x2 = A[k + 2 * s];
          zw y0 = zadd(zadd(x0, x1), x2);
          zw y1 = zadd(zadd(x0, zmulw(x1)), zmulw2(x2));
          zw y2 = zadd(zadd(x0, zmulw2(x1)), zmulw(x2));
          A[k] = y0; A[k + s] = y1; A[k + 2 * s] = y2;
        }
    }
  }
}
static int maxbits(const zw *A) {
  i128 mx = 0;
  for (uint64_t i = 0; i < Q; i++) { i128 x = A[i].a < 0 ? -A[i].a : A[i].a, y = A[i].b < 0 ? -A[i].b : A[i].b; if (x > mx) mx = x; if (y > mx) mx = y; }
  int bits = 0; while (mx > 0) { bits++; mx >>= 1; }
  return bits;
}
int main(int argc, char **argv) {
#ifdef _WIN32
  SetPriorityClass(GetCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS);
#endif
  if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
  p = atoi(argv[1]); u = atoi(argv[2]); n = atoi(argv[3]);
  N = u * n; pw[0] = 1; for (int i = 1; i < 40; i++) pw[i] = pw[i - 1] * p;
  Q = pw[N]; q = pw[u];
  e = (p == 3) ? 2 : 3;
  if (strlen(argv[4]) != (size_t)N) { fprintf(stderr, "poly length\n"); return 1; }
  for (int i = 0; i < N; i++) mpoly[i] = argv[4][i] - '0';
  build_tables();
  FILE *fc = fopen(argv[5], "r");
  if (!fc) { fprintf(stderr, "cfg open\n"); return 1; }
  uint8_t *texp = (uint8_t*)malloc(Q);
  zw *A = (zw*)malloc(sizeof(zw) * Q), *Bv = (zw*)malloc(sizeof(zw) * Q);
  if (!A || !Bv) { fprintf(stderr, "alloc\n"); return 4; }
  char id[64];
  while (fscanf(fc, "%63s", id) == 1) {
    int h, nz, z[16], K, c[16], nw, w[64];
    fscanf(fc, "%d %d", &h, &nz);
    for (int i = 0; i < nz; i++) fscanf(fc, "%d", &z[i]);
    fscanf(fc, "%d", &K);
    for (int i = 0; i < K; i++) fscanf(fc, "%d", &c[i]);
    fscanf(fc, "%d", &nw);
    for (int i = 0; i < nw; i++) fscanf(fc, "%d", &w[i]);
    uint64_t zi[16]; for (int i = 0; i < nz; i++) zi[i] = code_to_idx(z[i]);
    // t array
    for (uint64_t y = 0; y < Q; y++) {
      int64_t s = 0; int zero = 0;
      for (int j = 0; j < nz; j++) {
        uint64_t yy;
        if (p == 2) yy = y ^ zi[j];
        else { int d0 = y % 3; int nd = ((d0 - (int)zi[j]) % 3 + 3) % 3; yy = y - d0 + nd; }
        if (yy == 0) { zero = 1; break; }
        s += LOG[yy];
      }
      texp[y] = zero ? 255 : (uint8_t)((s % (int64_t)(Q - 1)) % e);
    }
    for (uint64_t y = 0; y < Q; y++) {
      zw v = {0, 0}; uint8_t t = texp[y];
      if (t != 255) {
        if (p == 3) { v.a = (t == 0) ? 1 : -1; }
        else { if (t == 0) { v.a = 1; } else if (t == 1) { v.b = 1; } else { v.a = -1; v.b = -1; } }
      }
      A[y] = v;
    }
    for (int i = 1; i <= K; i++) {
      // b_i = h * c_i
      uint64_t bidx;
      int64_t lb = (int64_t)LOG[code_to_idx(h)] + (int64_t)LOG[code_to_idx(c[i - 1])];
      bidx = elem_pow_log(lb);
      build_cols(bidx);
      build_vmap();
      dft(A);
      int mb = maxbits(A);
      if (mb > 118) { fprintf(stderr, "OVERFLOW RISK bits=%d\n", mb); return 5; }
      for (int k = 0; k < nw; k++) {
        uint64_t widx = code_to_idx(w[k]);
        uint64_t vw = VMAP[widx];
        char b1[64], b2[64]; pr128(A[vw].a, b1); pr128(A[vw].b, b2);
        printf("R %s %d %d %d %s %s\n", id, n, i, w[k], b1, b2);
      }
      fprintf(stderr, "cfg %s n=%d stage %d maxbits %d\n", id, n, i, mb);
      if (i < K) {
        // G_{i+1}(y) = t(y) * Ghat_i(y), Ghat_i(y) = A[B y]
        for (uint64_t y = 0; y < Q; y++) {
          uint8_t t = texp[y];
          zw v = {0, 0};
          if (t != 255) {
            zw x = A[VMAP[y]];
            if (p == 3) { v = (t == 0) ? x : (zw){ -x.a, -x.b }; }
            else { v = (t == 0) ? x : (t == 1 ? zmulw(x) : zmulw2(x)); }
          }
          Bv[y] = v;
        }
        zw *tmp = A; A = Bv; Bv = tmp;
      }
    }
    fflush(stdout);
  }
  return 0;
}
