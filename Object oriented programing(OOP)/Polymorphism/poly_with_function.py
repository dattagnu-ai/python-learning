class Printer:
    def operate(self):
        print("Document printing")


class Scanner:
    def operate(self):
        print("Document Scanning")


class Camera:
    def operate(self):
        print("Taking photo")


def operate_device(device):
    device.operate()


printer = Printer()
scanner = Scanner()
camera = Camera()

operate_device(printer)
operate_device(scanner)
operate_device(camera)
