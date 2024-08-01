/**
 *  ht.c 
 *
 *  This file contains the source code for demoing a Hilbert transform in C, 
 *  using GSL (GNU Scientific Library)
 *
 *  The program prints x(t), H[x(t)], and the calculated and real instantaneous
 *  phase of x(t), over time 
 *  Where x(t) is the original signal, i.e. 5cos(2pi * 2 * t)
 *        H[x(t)] is the Hilbert transform of x(t)
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])
#define TWOPI 6.2831853

// Generate a cosine signal with given values
// * Presumes that data is of size 2*n 
void generate_cos(double f, double A, double period, double* data, int n) {
  double dt = period / n;
  for (int i = 0; i < n; i++)
  {
    REAL(data,i) = A * cos(TWOPI * f * dt * i); 
    IMAG(data,i) = 0;
  }
}

// Hilbert tranform function
void hilbert(double* data, int stride, int n) {
  gsl_fft_complex_radix2_forward (data, stride, n);

  // Remove negative frequencies
  for (int i = (n/2); i < n; i++) 
  {
    REAL(data, i) = 0;
  }

  gsl_fft_complex_radix2_inverse (data, stride, n);
}

int main(void) {
  // Information about original signal x(t)
  double f = 2.0;       // Hz
  double A = 5.0; 
  double period = 1.0;  // s
  int n = 64;           // # samples
  double dt = period / n;

  // Print num samples
  printf("%d\n", n);

  int i; 
  double data[2*n];

  // Initialize `data` with x(t)
  generate_cos(f, A, period, data, n);

  // Print initial `data` i.e. x(t)
  for (i = 0; i < n; i++)
  {
    printf ("%d %e\n", i,
      REAL(data,i)
    );
  }

  // Perform Hilbert transform on `data`
  hilbert (data, 1, n);

  // Print `data` i.e. H[x(t)]
  for (i = 0; i < n; i++)
  {
    printf ("%d %e %e\n", i,
      REAL(data,i),
      IMAG(data,i)
    );
  }

  // Print calculated phase over time,  
  // * Mapped from (-pi,pi] to (0, 2pi]
  for (i = 0; i < n; i++)
  {
    gsl_complex a = REAL(data,i) + IMAG(data,i)*I;
    printf ("%d %e\n", i,
      carg(a) + (TWOPI / 2)
    );
  }

  // Print actual phase over time
  const double phi_0 = TWOPI / 4; // pi / 2
  for (i = 0; i < n; i++)
  {
    double phi_t = (TWOPI * dt * i * f) + phi_0; 

    // shitty modulo
    while (phi_t > TWOPI) {
      phi_t -= TWOPI;
    }

    printf ("%d %e\n", i,
      phi_t 
    );
  }

  return 0;
}
