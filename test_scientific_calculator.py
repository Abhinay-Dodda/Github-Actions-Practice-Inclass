import unittest
import math
from scientific_calculator import sine,cosine,tan,sqrt,log,exp,asine,acosine,atan,sinh,cosh,tanh

class Test_Sine_Function(unittest.TestCase):
    
    def test_for_sine_positive(self):
        self.assertAlmostEqual(sine(90), 1.0)
    
    def test_for_sine_negative(self):
        self.assertAlmostEqual(sine(-90), -1.0)
    
    def test_for_sine_zero(self):
        self.assertAlmostEqual(sine(0), 0.0)
    
    def test_for_sine_non_numeric(self):
        with self.assertRaises(TypeError):
            sine("Hello")

class Test_Cosine_Function(unittest.TestCase):
    
    def test_for_cosine_positive(self):
        self.assertAlmostEqual(sine(90), 1.0)
    
    def test_for_cosine_negative(self):
        self.assertAlmostEqual(sine(-90), -1.0)
    
    def test_for_cosine_zero(self):
        self.assertAlmostEqual(sine(0), 0.0)
    
    def test_for_cosine_non_numeric(self):
        with self.assertRaises(TypeError):
            cosine("Hello")

class Test_Tan_Function(unittest.TestCase):
    
    def test_for_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1.0)
    
    def test_for_tan_negative(self):
        self.assertAlmostEqual(tan(-45), -1.0)
    
    def test_for_tan_zero(self):
        self.assertAlmostEqual(tan(0), 0.0)
    
    def test_for_tan_non_numeric(self):
        with self.assertRaises(TypeError):
            tan(None)
    
    def test_for_tan_undefined(self):   # tan(k*pi/2) is undefined.
        with self.assertRaises(ValueError):
            tan(90)  # tan90 is undefined, that is infinite.

class Test_Sqrt_Function(unittest.TestCase):
    
    def test_for_sqrt_positive(self):
        self.assertAlmostEqual(sqrt(16), 4.0)
    
    def test_for_sqrt_zero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)
    
    def test_for_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-25)
    
    def test_for_sqrt_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt([15, 10])

class Test_Log_Function(unittest.TestCase):
    
    def test_for_log_positive(self):
        self.assertAlmostEqual(log(math.e), 1.0)
    
    def test_for_log_one(self):
        self.assertAlmostEqual(log(1), 0.0)
    
    def test_for_log_negative(self):
        with self.assertRaises(ValueError):
            log(-5)
    
    def test_for_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_for_log_non_numeric(self):
        with self.assertRaises(TypeError):
            log("Something")

class Test_Exp_Function(unittest.TestCase):
    
    def test_for_exp_positive(self):
        self.assertAlmostEqual(exp(1), math.e)
    
    def test_for_exp_zero(self):
        self.assertAlmostEqual(exp(0), 1.0)
    
    def test_for_exp_negative(self):
        self.assertAlmostEqual(exp(-1), 1/math.e)
    
    def test_for_exp_non_numeric(self):
        with self.assertRaises(TypeError):
            exp({'dictionary': 10})
 #Testing for Inverse Functions
class Test_Asine_Function(unittest.TestCase):
    
    def test_for_asine_positive(self):
        self.assertAlmostEqual(asine(1.0), math.pi/2)
    
    def test_for_asin_negative(self):
        self.assertAlmostEqual(asine(-1.0), -math.pi/2)
    
    def test_for_asine_zero(self):
        self.assertAlmostEqual(asine(0.0), 0.0)
    
    def test_for_asine_out_of_domain(self):
        with self.assertRaises(ValueError):
            asine(2.0)
    
    def test_for_asine_non_numeric(self):
        with self.assertRaises(TypeError):
            asine("Example")

class Test_Acosine_Function(unittest.TestCase):
    
    def test_for_acosine_positive(self):
        self.assertAlmostEqual(acosine(1.0), 0.0)
    
    def test_for_acosine_negative(self):
        self.assertAlmostEqual(acosine(-1.0), math.pi)
    
    def test_for_acosine_zero(self):
        self.assertAlmostEqual(acosine(0.0), math.pi/2)
    
    def test_for_acosine_out_of_range(self):
        with self.assertRaises(ValueError):
            acosine(10.0)
    
    def test_for_acosine_non_numeric(self):
        with self.assertRaises(TypeError):
            acosine(None)

class Test_Atan_Function(unittest.TestCase):
    
    def test_for_atan_positive(self):
        self.assertAlmostEqual(atan(1.0), math.pi/4)
    
    def test_for_atan_negative(self):
        self.assertAlmostEqual(atan(-1.0), -math.pi/4)
    
    def test_for_atan_zero(self):
        self.assertAlmostEqual(atan(0.0), 0.0)
    
    def test_for_atan_non_numeric(self):
        with self.assertRaises(TypeError):
            atan("Something")

class Test_Sinh_Function(unittest.TestCase):
    
    def test_for_sinh_positive(self):
        self.assertAlmostEqual(sinh(1), math.sinh(1))
    
    def test_for_sinh_negative(self):
        self.assertAlmostEqual(sinh(-1), math.sinh(-1))
    
    def test_for_sinh_zero(self):
        self.assertAlmostEqual(sinh(0), 0.0)
    
    def test_for_sinh_non_numeric(self):
        with self.assertRaises(TypeError):
            sinh([1,'list'])

class Test_Cosh_Function(unittest.TestCase):
    
    def test_for_cosh_positive(self):
        self.assertAlmostEqual(cosh(1), math.cosh(1))
    
    def test_for_cosh_negative(self):
        self.assertAlmostEqual(cosh(-1), math.cosh(-1))
    
    def test_for_cosh_zero(self):
        self.assertAlmostEqual(cosh(0), 1.0)
    
    def test_for_cosh_non_numeric(self):
        with self.assertRaises(TypeError):
            cosh("hyperbolic cosine")

class Test_Tanh_Function(unittest.TestCase):
    
    def test_for_tanh_positive(self):
        self.assertAlmostEqual(tanh(1), math.tanh(1))
    
    def test_for_tanh_negative(self):
        self.assertAlmostEqual(tanh(-1), math.tanh(-1))
    
    def test_for_tanh_zero(self):
        self.assertAlmostEqual(tanh(0), 0.0)
    
    def test_for_tanh_non_numeric(self):
        with self.assertRaises(TypeError):
            tanh(None)

unittest.main()