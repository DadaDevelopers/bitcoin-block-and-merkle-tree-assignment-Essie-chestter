import hashlib

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Transaction hashes
txA = "a3f1b9c4d2e7f8a91c0b3d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"
txB = "b7e4c2a1d9f8e6c5b4a3d2f1c0b9a8e7d6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1"
txC = "c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8"
txD = "d1c2b3a4f5e6d7c8b9a0e1f2d3c4b5a6f7e8d9c0b1a2c3d4e5f6a7b8c9d0e1f2"

# Step 1: Hash pairs
hashAB = sha256(txA + txB)
hashCD = sha256(txC + txD)

# Step 2: Calculate Merkle Root
merkle_root = sha256(hashAB + hashCD)

print("Transaction A:", txA)
print("Transaction B:", txB)
print("Transaction C:", txC)
print("Transaction D:", txD)

print("\nHash AB:", hashAB)
print("Hash CD:", hashCD)

print("\nMerkle Root:", merkle_root)
