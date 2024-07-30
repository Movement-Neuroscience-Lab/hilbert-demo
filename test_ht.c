#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])
#define TWOPI 6.2831853

// Hilbert tranform function
void hilbert(double* data, int stride, int n) {
  gsl_fft_complex_radix2_forward (data, stride, n);

  for (int i = (n/2); i < n; i++) 
    {
      REAL(data, i) = 0;
    }

  gsl_fft_complex_radix2_inverse (data, stride, n);
}

// Instantaneous phase function 
// analogous to `angle()` in MATLAB/Python
double angle(double real, double imag) {
  return atan2(imag, real);
}

int main(void) {
  // Information about original signal x(t)
  double f = 2.5;       // Hz
  double A = 5.0; 
  double period = 2.0;  // s
  int n = 2048;         // # samples
  double dt = period / n;

  // Print num samples
  printf("%d\n", n);

  int i; 
  double data[2*n];
  double transformed_data[2*n];

  // Initialize `data` and `transformed_data` with x(t)
  for (i = 0; i < n; i++)
    {
      REAL(data,i) = A * sin(TWOPI * f * dt * i); 
      IMAG(data,i) = 0;
      REAL(transformed_data,i) = A * sin(TWOPI * f * dt * i); 
      IMAG(transformed_data,i) = 0;
    }

  // Print initial `data` i.e. x(t)
  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
        REAL(data,i), IMAG(data,i)
      );
    }

  // Store Hilbert transformed data in `transformed_data`
  hilbert (transformed_data, 1, n);

  // Print `transformed_data` i.e. H[x(t)]
  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
        REAL(transformed_data,i),
        IMAG(transformed_data,i)
      );
    }

  // Print phase over time
  for (i = 0; i < n; i++)
    {
      printf ("%d %e\n", i,
        angle(REAL(data,i), IMAG(transformed_data,i))
      );
    }

  return 0;
}
