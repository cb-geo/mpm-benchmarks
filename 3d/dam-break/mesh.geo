 /*********************************************************************
 *
 *  Background grid
 *
 *********************************************************************/

// Mesh size - characteristic length
lc = 0.005;

// Starting point of cube
Point(1) = {0,0,0,lc};

// Create line in the x direction with # of layer cells
numline[] = Extrude {0.456,0,0}{Point{1}; Layers{40};};

// Create plane surface in the xy direction
numsurf[] = Extrude {0,0.456,0}{Line{numline[1]}; Layers{40}; Recombine;};

// Create solid in the xyz direction with ...
numsolid[] = Extrude {0,0,0.228}{Surface{numsurf[1]}; Layers{20}; Recombine;};

// 3D mesh algorithm (1:Delaunay, 4:Frontal, 5:Frontal Delaunay,
// 6:Frontal Hex, 7:MMG3D, 9:R-tree, 10:HXT)
Mesh.Algorithm = 1;

// Apply recombination algorithm to all surfaces, ignoring per-surface
// spec Default value: '0'
Mesh.RecombineAll = 1;

// Mesh recombination algorithm (0=standard, 1=blossom)
Mesh.RecombinationAlgorithm = 1;

// Number of smoothing steps applied to the final mesh
Mesh.Smoothing = 50;

// Don't extend the elements sizes from the boundary inside the domain (0)
// Mesh.CharacteristicLengthExtendFromBoundary = 0;
