#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])
#define TWOPI 6.2831853

int main(void) {
  int n = 256;
  double period = n / 2;
  double dt = 1 / period;
  double f = 1.0;
  double A = 1.0; 

  int i; 
  double data[2*n];

  for (i = 0; i < n; i++)
    {
       REAL(data,i) = A * sin(TWOPI * f * i * dt); IMAG(data,i) = 0.0;
    }

  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
              REAL(data,i), IMAG(data,i));
    }

  gsl_fft_complex_radix2_forward (data, 1, n);

  for (i = 0; i < n; i++) 
    {
      if (IMAG(data,i) * (1 / 1e-7) < 0) {
        IMAG(data,i) = 0;
      }
    }
  
  gsl_fft_complex_radix2_inverse (data, 1, n);

  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
              REAL(data,i),
              IMAG(data,i));
    }

  return 0;
}
