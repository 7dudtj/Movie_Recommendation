import numpy as np
from scipy import sparse
from tqdm import tqdm
import torch

class AdmmSlim():
    def __init__(self, args):
        self.lambda_1 = args.lambda_1
        self.lambda_2 = args.lambda_2
        self.rho = args.rho
        self.positive = args.positive
        self.n_iter = args.n_iter
        self.eps_rel = args.eps_rel
        self.eps_abs = args.eps_abs
        self.verbose = args.verbose
    
    def soft_thresholding(self, B, Gamma):
        if self.lambda_1 == 0:
            if self.positive:
                return np.abs(B)
            else:
                return B
        else:
            x = B + Gamma / self.rho
            threshold = self.lambda_1 / self.rho
            if self.positive:
                return np.where(threshold < x, x - threshold, 0)
            else:
                return np.where(threshold < x, x - threshold,
                                np.where(x < - threshold, x + threshold, 0))

    def is_converged(self, B, C, C_old, Gamma):
        B_norm = np.linalg.norm(B)
        C_norm = np.linalg.norm(C)
        Gamma_norm = np.linalg.norm(Gamma)

        eps_primal = self.eps_abs * B.shape[0] - self.eps_rel * np.max([B_norm, C_norm])
        eps_dual = self.eps_abs * B.shape[0] - self.eps_rel * Gamma_norm

        R_primal_norm = np.linalg.norm(B - C)
        R_dual_norm = np.linalg.norm(C  - C_old) * self.rho

        converged = R_primal_norm < eps_primal and R_dual_norm < eps_dual
        return converged

    def fit(self, X):
        XtX = X.T.dot(X)
        if sparse.issparse(XtX):
            XtX = XtX.todense().A

        if self.verbose:
            print(' --- init')
        identity_mat = np.identity(XtX.shape[0])
        diags = identity_mat * (self.lambda_2 + self.rho)
        P = np.linalg.inv(XtX + diags).astype(np.float32)
        B_aux = P.dot(XtX)

        Gamma = np.zeros_like(XtX, dtype=np.float32)
        C = np.zeros_like(XtX, dtype=np.float32)

        if self.verbose:
            print(' --- iteration start.')
        for iter in tqdm(range(self.n_iter)):
            if self.verbose:
                print(f' --- iteration {iter+1}/{self.n_iter}')
            C_old = C.copy()
            B_tilde = B_aux + P.dot(self.rho * C - Gamma)
            gamma = np.diag(B_tilde) / (np.diag(P) + 1e-8)
            B = B_tilde - P * gamma
            C = self.soft_thresholding(B, Gamma)
            Gamma = Gamma + self.rho * (B - C)
            if self.is_converged(B, C, C_old, Gamma):
                if self.verbose:
                    print(f' --- Converged. Stopped iteration.')
                break

        coef = C

        self.pred = torch.from_numpy(X.dot(coef))