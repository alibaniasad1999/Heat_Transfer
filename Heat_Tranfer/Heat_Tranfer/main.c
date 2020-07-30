//
//  main.c
//  Heat_Tranfer
//
//  Created by Ali Baniasad on 5/10/1399 AP.
//  Copyright © 1399 Ali Baniasad. All rights reserved.
//
#define PI 3.14159265358979323846
#include <stdio.h>
#include <math.h>
int r1 = 4/2;
int r = 4;
int l = 5;
int length = 1000;
int R = 200;
int k = 200;
//r function from x y z
int r_Up_get(int z){
    if (z == 50)
        return 200;
    return r1+z*r;
}
double A_side_get(int z){
    if (z == 0) {
         return PI*pow(r_Up_get(z),2)/2;
    }
    return PI*(pow(r_Up_get(z),2)/2-pow(r_Up_get(z-1),2)/2);
}
double A_Up(int z){
    return PI*r_Up_get(z)*l;
}
double A_Down(int z){
    if (z == 0) {
        return 2*r1*l;
    }
    return PI*r_Up_get(z-1)*l;
}
int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    return 0;
}
