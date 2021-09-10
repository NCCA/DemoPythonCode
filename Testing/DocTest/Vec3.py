
class Vec3 :
  x : float 
  y : float 
  z : float
  def __init__(self, x=0.0, y=0.0,z=0.0) :
    """Initialise the Vec3 class

    Default Initialiser
    >>> a=Vec3()

    >>> a.x
    0.0
    >>> a.y
    0.0
    >>> a.z
    0.0

    Let's try a user defined values
    >>> a=Vec3(0.5,0.2,8.0)

    >>> a.x
    0.5

    >>> a.y
    0.2

    >>> a.z
    8.0

   
    """
    try :
      self.x = float(x)
      self.y = float(y)
      self.z = float(z)
    except ValueError as e:
      raise ValueError("this class only accepts numeric values") from e


if __name__ == "__main__":
    import doctest
    doctest.testmod()