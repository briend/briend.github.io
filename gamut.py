import numpy as np
import colorspacious as cs
import scipy.optimize as spo

def constrain_to_gamut(JMh, penalize_chroma, tols):

  def apply_constraint(inputs):
      #rgb must greater than 0 and less than 1
      rgb_ = cs.cspace_convert([inputs[0], inputs[1], JMh[2]], "JMh", "sRGB1")
      return min(min(rgb_), 1.0 - max(rgb_)) 

  my_constraints = {'type': 'ineq', "fun": apply_constraint }

  rgb = cs.cspace_convert(JMh, "JMh", "sRGB1")
  print("incoming rgb is", rgb)
  x = np.clip(rgb, 0, 1)
  if (rgb == x).all():
      return x

  def loss(JM_):
      #penalize colorfulness loss
      loss = abs(JMh[0] - JM_[0]) + abs(JMh[1] - JM_[1]) * penalize_chroma
      return loss

  #inital guess just cut them both in half
  guess = np.array([JMh[0] * .5 , JMh[1] * .5])
  #we shouldn't increase lightness or colorfulness, or go below zero
  lowerlimit=cs.cspace_convert([0, 0, 0], "sRGB1", "JMh")
  upperlimit=cs.cspace_convert([1, 1, 1], "sRGB1", "JMh")
  bounds = ((lowerlimit[0], upperlimit[0]), (lowerlimit[1], JMh[1]))
  opt = {'disp':True}

  x_opt = spo.minimize(loss,
                       guess,
                       method='SLSQP',
                       constraints=my_constraints,
                       bounds=bounds,
                       tol=tols,
                       options=opt
                      )

  answer = x_opt['x']
  print("final rgb is", cs.cspace_convert([answer[0], answer[1], JMh[2]], "JMh", "sRGB1"))  
  print(x_opt)                        
  return x_opt

#blue w/ yellow's attributes
constrain_to_gamut([95.67306142, 58.26474923, 257.9160105], 1.1, None)
#yellow w/ blue's attributes
constrain_to_gamut([21.074306 , 65.43521286, 106.14599451], 1.1, None)