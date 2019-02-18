//============================================================
// STUDENT NAME: <your name>
// MATRIC NO.  : <matric no.>
// NUS EMAIL   : <your NUS email address>
// COMMENTS TO GRADER:
// <comments to grader, if any>
//
// ============================================================
//
// FILE: Sphere.cpp



#include <cmath>
#include "Sphere.h"
#include <algorithm>
using namespace std;



bool Sphere::hit( const Ray &r, double tmin, double tmax, SurfaceHitRecord &rec ) const 
{
	//***********************************************
    //*********** WRITE YOUR CODE HERE **************
    //***********************************************

	Vector3d shifted_origin = r.origin() - center;

	double a = dot(r.direction(), r.direction());
	double b = 2 * dot(shifted_origin, r.direction());
	double c = dot(shifted_origin, shifted_origin) - radius * radius;
	double discriminant = b * b - 4 * a*c;

	double t = 0;

	if (discriminant < 0) {
		return false;
	}
	else if (discriminant == 0) {
		t = -b / 2 / a;
	}
	else {
		double t_big = (-b + pow(discriminant, 0.5)) / (2 * a);
		double t_small = (-b - pow(discriminant, 0.5)) / (2 * a);
		double t;

		// checking for the threshold, and to obtain the closest positive value of t
		if (t_big < tmin && t_small < tmin) {
			return false;
		}
		else if (t_big >= tmin && t_small <= tmin) {
			t = t_big;
		}
		else if (t_big <= tmin && t_small >= tmin) {
			t = t_small;
		}
		else {
			t = min(t_big, t_small);
		}

		//outside of threshold
		if (t < tmin || t > tmax) {
			return false;
		}

		rec.t = t;
		rec.p = r.pointAtParam(t);
		Vector3d temp = rec.p - center;
		rec.normal = temp / temp.length();
		rec.mat_ptr = matp;

		return true;
	}
		/*
		double t_small = (-b - sqrt(discriminant)) / 2 / a;
		double t_big = (-b + sqrt(discriminant)) / 2 / a;
		
		if (t_small <= tmin && t_big <= tmin) return false;

		double t = t_small >= 0 ? t_small : t_big;
		if (t_small >= tmin && t_big <= tmin) {
			t = t_small;
		}
		else if (t_small <= tmin && t_big >= tmin) {
			t = t_big;
		}
		else {
			t = min(t_small, t_big);
		}
	}
	if (tmax >= t && t >= tmin) {
		rec.t = t;
		rec.p = r.pointAtParam(t);
		rec.mat_ptr = matp;
		Vector3d normal = rec.p - center;
		rec.normal = normal / normal.length();
		return true;
	}
	else {
		return false;
	}
	*/
}




bool Sphere::shadowHit( const Ray &r, double tmin, double tmax ) const 
{

	//***********************************************
	//*********** WRITE YOUR CODE HERE **************
	//***********************************************
	Vector3d newRayOrigin = r.origin() - center;

	double a = 1;
	double b = 2 * dot(r.direction(), newRayOrigin);
	double c = dot(newRayOrigin, newRayOrigin) - radius * radius;

	double discriminant = b * b - 4 * a * c;

	if (discriminant < 0) {
		return false;
	}
	else {
		double t0 = (-b + pow(discriminant, 0.5)) / (2 * a);
		double t1 = (-b - pow(discriminant, 0.5)) / (2 * a);
		double t;
		if (t0 < tmin && t1 < tmin) {
			return false;
		}
		else if (t0 >= tmin && t1 <= tmin) {
			t = t0;
		}
		else if (t0 <= tmin && t1 >= tmin) {
			t = t1;
		}
		else {
			t = min(t0, t1);
		}

		return (t <= tmax);
	}
}

