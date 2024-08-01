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

  // Remove negative frequencies
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
  double f = 2.0;       // Hz
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
    REAL(data,i) = A * cos(TWOPI * f * dt * i); 
    IMAG(data,i) = 0;
    REAL(transformed_data,i) = A * cos(TWOPI * f * dt * i); 
    IMAG(transformed_data,i) = 0;
  }

  // Print initial `data` i.e. x(t)
  for (i = 0; i < n; i++)
  {
    printf ("%d %e\n", i,
      REAL(data,i)
    );
  }

  // Store H[x(t)] in `transformed_data`
  hilbert (transformed_data, 1, n);

  // Print `transformed_data` i.e. H[x(t)]
  for (i = 0; i < n; i++)
  {
    printf ("%d %e %e\n", i,
      REAL(transformed_data,i),
      IMAG(transformed_data,i)
    );
  }

  // Print calculated phase over time,  
  // * Mapped from (-pi,pi] to (0, 2pi]
  // * Shifted by -pi/2 (Hilbert shifts by +pi/2)
  for (i = 0; i < n; i++)
  {
    printf ("%d %e\n", i,
      angle(REAL(data,i), IMAG(transformed_data,i)) + (TWOPI / 2)
    );
  }

  // Print actual phase over time
  double phi_0 = TWOPI / 4; // pi / 2
  for (i = 0; i < n; i++)
  {
    double phi = (TWOPI * dt * i * f) + phi_0; 

    // shitty modulo
    while (phi > TWOPI) {
      phi -= TWOPI;
    }
    printf ("%d %e\n", i,
      phi 
    );
  }

  return 0;
}
