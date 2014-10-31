from numpy import array, concatenate, r_, ix_, append
import numexpr as ne


class TotalVariationDenoising(object):
  """Total Variation Denoising class, based on Guy Gilboa"""
  # Input: I  - image (double array gray level 1-256),
  #    iter - num of iterations,
  #    dt   - time step [0.2],
  #    ep   - epsilon (of gradient regularization) [1],
  #    lam  - fidelity term lambda [0],
  #    I0   - input (noisy) image [I0=I]
  #     (default values are in [])
  def __init__(self, I, iter, ep=1.0, dt=None, lam=0.0, I0=None, C=0.0):
    super(TotalVariationDenoising, self).__init__()
    self.I = I
    self.iter = iter
    self.dt = ep / 5 if dt is None else dt
    self.ep = ep
    self.lam = lam
    self.I0 = self.I if I0 is None else I0
    self.C = C

  # Input: 3
  # Output: [0, 1, 2, 2]
  def left(self, n):
    # [2:nx nx]
    return append(r_[1:n], n - 1)

  # Input: 3
  # Output: [0, 0, 1, 2]
  def right(self, n):
    # [1 1:nx-1]
    return concatenate((array([0]), r_[0:n - 1]))

  def generate(self):
    ny, nx = self.I.shape
    ep2 = self.ep ** 2

    # Definitions
    I, I0, C, lam, dt = self.I, self.I0, self.C, self.lam, self.dt
    left, right = self.left, self.right

    lx = left(nx)
    rx = right(nx)
    ly = left(ny)
    ry = right(ny)
    ix_ly_lx = ix_(ly, lx)
    ix_ry_rx = ix_(ry, rx)
    ix_ry_lx = ix_(ry, lx)
    ix_ly_rx = ix_(ly, rx)

    I0_C = I0 + C

    for x in xrange(0, self.iter):
      I_rx = I[:, rx]
      I_ry = I[ry, :]
      I_lx = I[:, lx]
      I_ly = I[ly, :]

      I_x = ne.evaluate('(I_lx - I_rx) * 0.5')
      I_y = ne.evaluate('(I_ly - I_ry) * 0.5')
      I_xx = ne.evaluate('I_lx + I_rx - 2 * I')
      I_yy = ne.evaluate('I_ly + I_ry - 2 * I')

      Dp = I[ix_ly_lx] + I[ix_ry_rx]
      Dm = I[ix_ry_lx] + I[ix_ly_rx]

      I_xy = ne.evaluate('(Dp - Dm) * 0.25')
      Num = ne.evaluate('I_xx * (ep2 + I_y ** 2) - 2 * I_x * I_y * I_xy + I_yy * (ep2 + I_x ** 2)')
      Den = ne.evaluate('(ep2 + I_x ** 2 + I_y ** 2) ** 1.5')
      I_t = ne.evaluate('Num / Den + lam * (I0_C - I)')  # (I0 - I + C)')
      I = ne.evaluate('I + dt * I_t')
    return I
