#import modules
import torch

def check():
    ret = True
    # Check available
    if torch.cuda.is_available() == True:
        print("GPU CUDA is available !")
        ret = True

        # Check number of devices
        if torch.cuda.device_count() != 0:
            print("Number of devices:",torch.cuda.device_count())

            # Check the number of current device
            num = torch.cuda.current_device()
            print("Value of current device:",num)

            # Check the device
            print("Current device object:",torch.cuda.device(num))

            # Check name of device
            print("Name of device:",torch.cuda.get_device_name(num))

        # End of function check number of devices
        else:
            ret = False

    # End of Check available
    else:
        ret = False

    if ret == False:
        print("GPU CUDA is not available !")

if __name__ == "__main__":
    check()







