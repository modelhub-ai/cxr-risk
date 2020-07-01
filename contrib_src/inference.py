import json
from processing import ImageProcessor
from modelhublib.model import ModelBase
from fastai.vision import *
import pretrainedmodels
import os
from shutil import copyfile, rmtree

class Model(ModelBase):

    def __init__(self):
        # load config file
        config = json.load(open("model/config.json"))
        # get the image processor
        self._imageProcessor = ImageProcessor(config)
        #
        self._bs = 1
        path = pathlib.Path.cwd()
        self._path = path
        development_folder = path / 'development'
        self._development_folder = development_folder
        development_fn = development_folder / 'dummy_dataset'/ 'dummy_dataset.csv'
        self._development_fn = development_fn
        valid_fn = development_folder / 'dummy_dataset' / 'dummy_valid.csv'
        self._valid_fn = valid_fn


    def get_model(self, pretrained=True, model_name = 'inceptionv4', **kwargs ):
        if pretrained:
            arch = pretrainedmodels.__dict__[model_name](num_classes=1000, pretrained='imagenet')
        else:
            arch = pretrainedmodels.__dict__[model_name](num_classes=1000, pretrained=None)
        return arch

    def get_cadene_model(self, pretrained=True, **kwargs ):
        return self._fastai_inceptionv4

    def infer(self, input):

        no_working = False
        # if working is populated
        if len(os.listdir("/working")) != 0:
            test_folder = "/working"
        else:
            no_working = True
            os.mkdir("/temp")
            test_folder = "/temp"
            copyfile(input, "/temp/{}".format(input.split("/")[-1]))

        df = pd.read_csv(self._development_fn)
        src = (ImageList.from_csv(self._development_folder, self._development_fn, folder='', suffix='')
               .split_by_fname_file(self._valid_fn)
               .label_from_df())
        tfms = get_transforms(do_flip=False, flip_vert=False, max_lighting=0.3, max_zoom=1.2, max_warp=0., max_rotate=2.5)

        data = (src.transform(tfms, size=224)
            .add_test_folder(test_folder=test_folder)
            .databunch(bs=self._bs, no_check=True).normalize(imagenet_stats))

        custom_head = create_head(nf=2048*2, nc=37, ps=0.75, bn_final=False)
        self._fastai_inceptionv4 = nn.Sequential(*list(children( self.get_model(model_name = 'inceptionv4'))[:-2]),custom_head)
        #
        learn = cnn_learner(data , self.get_cadene_model, metrics=accuracy)
        learn.load(self._path / "model" / "cxr-risk_v1")
        learn.model.eval()

        # inference with test time augmentation (TTA)
        preds_tta,y_tta,losses_tta = learn.TTA(scale=1.05, ds_type=DatasetType.Test, with_loss=True)
        output = self._imageProcessor.computeOutput(preds_tta)

        if no_working:
            rmtree("/temp")

        return output
