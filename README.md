# ER-Pi-Pca
- Running 3 dc motors with Raspberry Pi via PCA9685 I2C module.
- Each motor picks up 3 pwm channels from PCA. We set one to HIGH, one to LOW, and the third controles the pwm of the motor.
- We need to give the PCA hexadecimal input, which we can map accordingly.
- We can map joystick input to [0,65535] and pass that as pwm inputs to the PCA. Hexadecimal is not neccesary.
- (TODO): Use 'cpython' to extend cpp libraries into python for holonomic drive
