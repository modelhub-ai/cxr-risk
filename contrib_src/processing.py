from modelhublib.processor import ImageProcessorBase
import PIL
import SimpleITK
import numpy as np
import json


class ImageProcessor(ImageProcessorBase):

    # OPTIONAL: Use this method to preprocess images using the image objects
    #           they've been loaded into automatically.
    #           You can skip this and just perform the preprocessing after
    #           the input image has been convertet to a numpy array (see below).
    def _preprocessBeforeConversionToNumpy(self, image):
        if isinstance(image, PIL.Image.Image):
            # TODO: implement preprocessing of PIL image objects
            pass
        elif isinstance(image, SimpleITK.Image):
            # TODO: implement preprocessing of SimpleITK image objects
            pass
        else:
            raise IOError("Image Type not supported for preprocessing.")
        return image


    def _preprocessAfterConversionToNumpy(self, npArr):
        # TODO: implement preprocessing of image after it was converted to a numpy array
        return npArr


    def computeOutput(self, inferenceResults):
        # results are presented as [x, y] -- y is the risk probability.
        # items_test = data.test_ds.items
        preds_test_tta = inferenceResults.numpy()
        return inferenceResults


    def computeOutput(self, inferenceResults):
        inferenceResults = inferenceResults.numpy()[0]
        probs = np.squeeze(np.asarray(inferenceResults))
        with open("model/labels.json") as jsonFile:
            labels = json.load(jsonFile)
        result = []
        for i in range (len(probs)):
            obj = {'label': str(labels[str(i)]),
                    'probability': float(probs[i])}
            result.append(obj)
        print ('postprocessing done.')
        return result
