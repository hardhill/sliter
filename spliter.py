import base64

from parameters import Parameters


class Application(object):
    def Start(self):
        print('====================================================================')
        print('=                     BaseEncoder ver. 1.0                         =')
        print('====================================================================')
        params = Parameters()
        file = params.Path()+"\picture.png"
        with open(file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        with open(params.Path()+"\picture.txt","wb") as txt_file:
            txt_file.write(encoded_string)

if __name__ == '__main__':
    app = Application()
    app.Start()