#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])
#define TWOPI 6.2831853

int main(void) {
  double f = 2.5;            // Hz
  double A = 5.0; 

  double period = 2.0;          // s
  int n = 2048; // # samples
  double dt = period / n;

  printf("%d\n", n);

  int i; 
  double data[2*n];
  double transformed_data[2*n];

  // Initialize data
  for (i = 0; i < n; i++)
    {
       REAL(data,i) = A * sin(TWOPI * f * dt * i); 
       IMAG(data,i) = 0;
       REAL(transformed_data,i) = A * sin(TWOPI * f * dt * i); 
       IMAG(transformed_data,i) = 0;
    }

  // Print initial data
  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
              REAL(data,i), IMAG(data,i));
    }


  
  { // Hilbert transform
    gsl_fft_complex_radix2_forward (transformed_data, 1, n);

    for (i = (n/2); i < n; i++) 
      {
        REAL(transformed_data, i) = 0;
      }

    gsl_fft_complex_radix2_inverse (transformed_data, 1, n);
  }

  // Print transformed data
  for (i = 0; i < n; i++)
    {
      printf ("%d %e %e\n", i,
              REAL(transformed_data,i),
              IMAG(transformed_data,i));
    }

  // Print phase 
  for (i = 0; i < n; i++)
    {
      printf ("%d %e\n", i,
          atan2(IMAG(transformed_data,i), REAL(transformed_data,i)));
    }

  return 0;
}
