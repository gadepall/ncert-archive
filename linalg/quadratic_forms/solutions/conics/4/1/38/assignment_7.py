import numpy as np            

def QR_decompose(V):
    a = np.array(([V[0,0]],[V[1,0]]))
    b = np.array(([V[0,1]],[V[1,1]]))
    u1 = a
    e1 = u1/np.sqrt(u1[0]**2 + u1[1]**2)
    u2 = b - np.dot(np.transpose(b),e1)*e1
    e2 = u2/np.sqrt(u2[0]**2 + u2[1]**2)
    q = np.array(([e1[0,0],e2[0,0]],[e1[1,0],e2[1,0]]))
    r = np.array(([np.dot(np.transpose(a),e1)[0],np.dot(np.transpose(b),e1)[0]],[0,np.dot(np.transpose(b),e2)[0]]))
    return q,r

V = np.array(([14,-2],[-2,11]))
print("The QR decomposition of Vector V is : ")
print("Q is :")
print(QR_decompose(V)[0])
print("R is :")
print(QR_decompose(V)[1])