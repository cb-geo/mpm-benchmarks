/*********************************************************************
 *
 *  Plate with a hole
 *
 *********************************************************************/

// Mesh size - characteristic length
lc = 0.1;
lf = 0.02;

// 4 corner points of a plate
Point(1) = {0.5, 0, 0, lf};
Point(2) = {4.0, 0, 0, lc};
Point(3) = {4.0, 2.5, 0, lc};
Point(4) = {0, 2.5, 0, lc};

// Circular hole
Point(5) = {0.0, 0.5, 0, lf};
Point(6) = {0.0, 0.0, 0, lc};

// Circle fine mesh
Point(7) = {1.5, 0.0, 0, lf};
Point(8) = {0.0, 1.5, 0, lf};

// Lines
Line(1) = {7,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,8};
Line(5) = {8,5};
Line(6) = {1,7};

Circle(7) = {5, 6, 1};
Circle(8) = {8, 6, 7};

Line Loop(1) = {1, 2, 3, 4, 8};
Line Loop(2) = {5, 7, 6, -8};

Plane Surface(1) = {1};
Plane Surface(2) = {2};

BottomBottomLine = 101;
Physical Line("BottomLine") = 1;
RightBottomLine = 102;
Physical Line("RightLine") = 2;
TopBottomLine = 103;
Physical Line("TopLine") = 3;
LeftBottomLine = 104;
Physical Line("LeftLine") = 4;
SideBottomLeftLine = 105;

// Transfinite Surface {1};
Recombine Surface{1, 2};

BottomSurface = 1001;
Physical Surface("Plate") = {1} ;

// 2D mesh algorithm (1=MeshAdapt, 2=Automatic, 5=Delaunay, 6=Frontal,
// 7=bamg, 8=delquad)
Mesh.Algorithm = 8;

// Apply recombination algorithm to all surfaces, ignoring per-surface
// spec Default value: '0'
Mesh.RecombineAll = 1;

// Mesh recombination algorithm (0=standard, 1=blossom)
Mesh.RecombinationAlgorithm = 1;

// Number of smoothing steps applied to the final mesh
Mesh.Smoothing = 50;

// Don't extend the elements sizes from the boundary inside the domain (0)
// Mesh.CharacteristicLengthExtendFromBoundary = 0;
