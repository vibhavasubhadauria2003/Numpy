from sympy import Matrix

def orthogonal_complement(vector):
    # Convert vector into a row matrix
    v = Matrix([vector])  
    
    # Nullspace gives a basis for all x such that v * x^T = 0
    nullspace_basis = v.nullspace()
    
    return nullspace_basis

def verify_orthogonality(vector, basis):
    v = Matrix(vector)
    for b in basis:
        print(f"Dot product with {b.T}: {v.dot(b)}")  # should be 0

# Test case 1
v1 = [2, 3]
basis1 = orthogonal_complement(v1)
print("Orthogonal complement basis for v1:", basis1)
verify_orthogonality(v1, basis1)

# Test case 2
v2 = [1, 2, 3]
basis2 = orthogonal_complement(v2)
print("\nOrthogonal complement basis for v2:", basis2)
verify_orthogonality(v2, basis2)