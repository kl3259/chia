from chia import components
from chia.components.datasets import (
    core50_dataset,
    cub2002011_dataset,
    icifar_dataset,
    icifar_dataset_v2,
    icubworld28_dataset,
    ilsvrc2012_dataset,
    inaturalist2018_dataset,
    json_dataset,
    lndw_dataset,
    nabirds_dataset,
)


class DatasetFactory(components.Factory.Factory):
    name_to_class_mapping = {
        "core50": core50_dataset.CORe50Dataset,
        "cub2002011": cub2002011_dataset.CUB2002011Dataset,
        "icifar": icifar_dataset.iCIFARDataset,
        "icifar_v2": icifar_dataset_v2.iCIFARDataset_v2,
        "icubworld28": icubworld28_dataset.iCubWorld28Dataset,
        "inaturalist2018": inaturalist2018_dataset.iNaturalist2018Dataset,
        "ilsvrc2012": ilsvrc2012_dataset.ILSVRC2012Dataset,
        "json": json_dataset.JSONDataset,
        "lndw": lndw_dataset.LNDWDataset,
        "nabirds": nabirds_dataset.NABirdsDataset,
    }
    default_section = "dataset"
