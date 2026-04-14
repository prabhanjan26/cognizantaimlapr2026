"""
Application entry point for the day02 project.
"""
import random 
def generate_otp():
    """Generate a 6 digit OTP."""
    otp = random.randint(100000, 999999)
    return otp

if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
    
